'''Fastapi API for tic-tac-toe'''
import json
import random
import os
from datetime import datetime
from typing import Optional

from fastapi import FastAPI, HTTPException
from names_generator import generate_name
from pydantic import BaseModel

# CONST_BOARD_SIZE: My panache and gee-whizz to add to this exercise. 
# This tic-tac-toe handles any X*X board. Try it!
CONST_BOARD_SIZE = 3
CONST_PLAYER = "X"
CONST_CPU = "O"
CONST_BLANK = "."
CONST_HISTORY_TYPE_GAME = 'game'
CONST_HISTORY_TYPE_MOVE = 'move'
CONST_HISTORY_TYPE_ALL = 'all'
CONST_HISTORY_FILE = "history.ndjson"

class Move(BaseModel):
    '''This represents the x, y coordinates a user will submit via API'''
    row: int
    col: int

class TicTacToeGame:
    '''TicTacToeGame object and methods'''
    def __init__(self):
        '''Init the game params'''
        if not os.path.exists(CONST_HISTORY_FILE):
            open(CONST_HISTORY_FILE, 'a', encoding="utf-8").close()
        self.id = None 
        self.board = None
        self.current_player = None
        self.winner: Optional[str] = None

    # GET based methods
    def get_status(self):
        '''Get the status (ie. board) of the current active game'''
        return {
            "game_id": game.id,
            "status": "No active games" if not game.id else "Game complete" if self.winner else "In progress",
            "board": self.board,
            "current_player": self.current_player,
            "winner": self.winner
        }

    def get_move_history(self):
        '''Get the history of all move events'''
        return self.read_history(CONST_HISTORY_TYPE_MOVE)

    def get_game_history(self):
        '''Get the history of all game events'''
        return self.read_history(CONST_HISTORY_TYPE_GAME)

    def get_all_history(self):
        '''Get all history'''
        return self.read_history()

    def clear_game_history(self):
        '''Clear the file that stores all the game history'''
        return self.clear_history()
    
    # POST based methods
    def new_game(self):
        '''Start a new game'''
        self.id = generate_name() # Fun and readable name as an ID
        self.board = [[CONST_BLANK for _ in range(CONST_BOARD_SIZE)] 
                      for _ in range(CONST_BOARD_SIZE)]
        self.current_player = CONST_PLAYER
        self.winner: Optional[str] = None
        self.write_history(CONST_HISTORY_TYPE_GAME, 
                           f'New game started with a {CONST_BOARD_SIZE}x{CONST_BOARD_SIZE} board')

    def make_a_move(self, move: Move):
        '''Make a move on the board with the provided `move` object'''
        if not self.id:
            raise ValueError("No games in progress.")
        # Only an API player will use the endpoint
        self.current_player = CONST_PLAYER

        # Check for any non-starter conditions
        if move.col > CONST_BOARD_SIZE-1 or move.row > CONST_BOARD_SIZE-1:
            raise ValueError("Invalid cell coordinates.")
        if self.board[move.row][move.col] != CONST_BLANK:
            raise ValueError("This cell is already occupied.")
        if self.winner:
            raise ValueError("Game is already over.")

        # Save the move to the board and check if win conditions are met
        self.board[move.row][move.col] = CONST_PLAYER
        we_have_a_winner, self.winner = TicTacToeGame.check_for_winner(self.board)

        # Log move history for the player, log win event if conditions met
        self.write_history(CONST_HISTORY_TYPE_MOVE, 
                           f'Player {self.current_player} chose row {move.row}, column {move.col}')
        if we_have_a_winner:
            self.winner = self.current_player
            self.write_history(CONST_HISTORY_TYPE_GAME, f'Game won by player {self.current_player}')

        # If player won, don't let the computer take a turn
        if self.winner:
            return

        # Computer's turn to make a move, find an empty spot randomly
        self.current_player = CONST_CPU
        while True:
            cpu_x = random.randint(0, CONST_BOARD_SIZE-1)
            cpu_y = random.randint(0, CONST_BOARD_SIZE-1)

            if self.board[cpu_x][cpu_y] != CONST_BLANK:
                continue
            else:
                self.board[cpu_x][cpu_y] = CONST_CPU
                break

        # Check if the computer won, log move history, log win event if conditions are met
        we_have_a_winner, self.winner = TicTacToeGame.check_for_winner(self.board)
        self.write_history(CONST_HISTORY_TYPE_MOVE, 
                           f'Player {self.current_player} chose row {cpu_x}, column {cpu_y}')
        if we_have_a_winner:
            self.winner = self.current_player
            self.write_history(CONST_HISTORY_TYPE_GAME, f'Game won by player {self.current_player}')

    def write_history(self, history_type, message):
        '''Write an event to the history log (stored as .ndjson)'''
        file = open(CONST_HISTORY_FILE, 'a', encoding="utf-8")
        line = json.dumps({
            "datetime": datetime.now().isoformat(),
            "type": history_type,
            "game_id": self.id,
            "message": message
        })
        file.write(f'{line}\n')
        file.close()

    def read_history(self, history_type = CONST_HISTORY_TYPE_ALL):
        '''Reads history events from file. Can filter based on `type` property'''
        data = []
        with open(CONST_HISTORY_FILE, 'r', encoding="utf-8") as file:
            for line in file:
                try:
                    json_object = json.loads(line)
                    if(history_type == CONST_HISTORY_TYPE_ALL 
                       or json_object['type'] == history_type):
                        data.append(json_object)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}, in line: {line.strip()}")
        return data

    def clear_history(self):
        '''Wipes out the history file'''
        open(CONST_HISTORY_FILE, 'w', encoding="utf-8").close()
        return {"message": "All history cleared"}

    @staticmethod
    def check_for_winner(board):
        '''
        Checks the game board for winning conditions, assigns winner if conditions met
        I started out with a 3x3 working example. I wanted to add something unique to
        this, so I made the board size configurable. A set board size makes checking for
        a winner much easier and straight forward. But when you check against a board of 
        varied size, the check becomes less efficient. But it still works!'''
        we_have_a_winner = False
        winner = None
        size=len(board[0])

        # Diagonal checks first, there are fewer of them for all boards configurations
        # Start first with the upper-left, lower-right diagonal, if no win is found
        # Move onto the upper-right, lower-left diagonal
        if board[0][0] != CONST_BLANK:
            for i in range(size):
                if board[i][i] != board[0][0]:
                    we_have_a_winner = False
                    break
                we_have_a_winner = True

            if we_have_a_winner:
                winner = board[0][0]

        if not we_have_a_winner and board[0][size-1] != CONST_BLANK:
            for i in range(size):
                if board[i][size-1-i] != board[0][size-1]:
                    we_have_a_winner = False
                    break
                we_have_a_winner = True

            if we_have_a_winner:
                winner = board[0][size-1]

        # Veritcal checks if no winnner has been found
        # Check all verticals and attempt to break out of loops early
        if not we_have_a_winner:
            for i in range(size):
                if board[0][i] != CONST_BLANK:
                    for j in range(size):
                        if board[0][i] == board[j][i]:
                            we_have_a_winner = True
                            continue
                        we_have_a_winner = False
                        break
                    if we_have_a_winner:
                        winner = board[0][i]

        # Horizonal checks if no winnner has been found
        # Check all horizontals and attempt to break out of loops early
        if not we_have_a_winner:
            for i in range(size):
                if board[i][0] != CONST_BLANK:
                    for j in range(size):
                        if board[i][0] == board[i][j]:
                            we_have_a_winner = True
                            continue
                        we_have_a_winner = False
                        break
                    if we_have_a_winner:
                        winner = board[i][0]

        return we_have_a_winner, winner



# Setup, init, and API definitions
game = TicTacToeGame()
app = FastAPI(title="Tic-Tac-Toe API")

@app.get("/get-game-status")
def get_status():
    '''Get the status of the game board'''
    return game.get_status()

@app.get("/get-move-history")
def get_move_history():
    '''Get all history events of type `move`'''
    return game.get_move_history()

@app.get("/get-game-history")
def get_game_history():
    '''Get all history events of type `game`'''
    return game.get_game_history()

@app.get("/get-all-history")
def get_all_history():
    '''Get all history events regardless of type'''
    return game.get_all_history()

@app.get("/clear-game-history")
def clear_game_history():
    '''Clear all history'''
    return game.clear_game_history()

@app.post("/create-new-game")
def new_game():
    '''Create a new game'''
    global game
    game = TicTacToeGame()
    game.new_game()
    return {"game_id": game.id, "message": "New game started", "board_size": CONST_BOARD_SIZE}

@app.post("/make-a-move")
def make_move(move: Move):
    '''Make a move on the game using a row+column coordinate'''
    try:
        game.make_a_move(move)
        return game.get_status()
    except ValueError as e:
        exception_detail = {"message": str(e), "game_details": game.get_status()}
        raise HTTPException(status_code=400, detail=exception_detail) from e
