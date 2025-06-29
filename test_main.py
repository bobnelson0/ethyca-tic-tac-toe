"""Unit tests for TicTacToe"""
from main import TicTacToeGame

class TestTicTacToeGame:
    '''tic-tac-toe testing'''

    def test_checkwinner_3x3_no_winner(self):
        '''Testing no win permutations return (False, None)'''
        no_winner_1 = [
            [".",".","."],
            [".",".","."],
            [".",".","."],
        ]
        no_winner_2 = [
            [".",".","."],
            [".","X","."],
            [".","X","."],
        ]
        no_winner_3 = [
            ["O","X",".O"],
            ["X","O","X"],
            ["X","O","X"],
        ]

        assert TicTacToeGame.check_for_winner(no_winner_1) == (False, None)
        assert TicTacToeGame.check_for_winner(no_winner_2) == (False, None)
        assert TicTacToeGame.check_for_winner(no_winner_3) == (False, None)

    def test_checkwinner_3x3_vertical(self):
        '''Testing vertical wins on a 3x3 board'''
        winningboard_3x3_vertical_1 = [
            ["X",".","."],
            ["X",".","."],
            ["X",".","."],
        ]
        winningboard_3x3_vertical_2 = [
            [".","X","."],
            [".","X","."],
            [".","X","."],
        ]
        winningboard_3x3_vertical_3 = [
            [".",".","X"],
            [".",".","X"],
            [".",".","X"],
        ]

        assert TicTacToeGame.check_for_winner(winningboard_3x3_vertical_1) == (True, 'X')
        assert TicTacToeGame.check_for_winner(winningboard_3x3_vertical_2) == (True, 'X')
        assert TicTacToeGame.check_for_winner(winningboard_3x3_vertical_3) == (True, 'X')

    def test_checkwinner_3x3_horizontal(self):
        '''Testing horizontal wins on a 3x3 board'''
        winningboard_3x3_horizontal_1 = [
            ["X","X","X"],
            [".",".","."],
            [".",".","."],
        ]
        winningboard_3x3_horizontal_2 = [
            [".",".","."],
            ["X","X","X"],
            [".",".","."],
        ]
        winningboard_3x3_horizontal_3 = [
            [".",".","."],
            [".",".","."],
            ["X","X","X"],
        ]

        assert TicTacToeGame.check_for_winner(winningboard_3x3_horizontal_1) == (True, 'X')
        assert TicTacToeGame.check_for_winner(winningboard_3x3_horizontal_2) == (True, 'X')
        assert TicTacToeGame.check_for_winner(winningboard_3x3_horizontal_3) == (True, 'X')

    def test_checkwinner_3x3_diagonals(self):
        '''Testing diagonal wins on a 3x3 board'''
        winningboard_3x3_diagonal_1 = [
            ["X",".","."],
            [".","X","."],
            [".",".","X"],
        ]
        winningboard_3x3_diagonal_2 = [
            [".",".","X"],
            [".","X","."],
            ["X",".","."],
        ]

        assert TicTacToeGame.check_for_winner(winningboard_3x3_diagonal_1) == (True, 'X')
        assert TicTacToeGame.check_for_winner(winningboard_3x3_diagonal_2) == (True, 'X')

    def test_checkwinner_5x5_vertical(self):
        '''Testing vertical wins on a 5x5 board'''
        winningboard_5x5_vertical_1 = [
            ["X",".",".",".","."],
            ["X",".",".",".","."],
            ["X",".",".",".","."],
            ["X",".",".",".","."],
            ["X",".",".",".","."],
            ["X",".",".",".","."],
        ]
        winningboard_5x5_vertical_2 = [
            [".","X",".",".","."],
            [".","X",".",".","."],
            [".","X",".",".","."],
            [".","X",".",".","."],
            [".","X",".",".","."],
        ]
        winningboard_5x5_vertical_3 = [
            [".",".","X",".","."],
            [".",".","X",".","."],
            [".",".","X",".","."],
            [".",".","X",".","."],
            [".",".","X",".","."],
        ]
        winningboard_5x5_vertical_4 = [
            [".",".",".","X","."],
            [".",".",".","X","."],
            [".",".",".","X","."],
            [".",".",".","X","."],
            [".",".",".","X","."],
        ]
        winningboard_5x5_vertical_5 = [
            [".",".",".",".","X"],
            [".",".",".",".","X"],
            [".",".",".",".","X"],
            [".",".",".",".","X"],
            [".",".",".",".","X"],
        ]

        assert TicTacToeGame.check_for_winner(winningboard_5x5_vertical_1) == (True, 'X')
        assert TicTacToeGame.check_for_winner(winningboard_5x5_vertical_2) == (True, 'X')
        assert TicTacToeGame.check_for_winner(winningboard_5x5_vertical_3) == (True, 'X')
        assert TicTacToeGame.check_for_winner(winningboard_5x5_vertical_4) == (True, 'X')
        assert TicTacToeGame.check_for_winner(winningboard_5x5_vertical_5) == (True, 'X')

    def test_checkwinner_5x5_horizontal(self):
        '''Testing horizontal wins on a 5x5 board'''
        winningboard_5x5_horizontal_1 = [
            ["X","X","X","X","X"],
            [".",".",".",".","."],
            [".",".",".",".","."],
            [".",".",".",".","."],
            [".",".",".",".","."],
        ]
        winningboard_5x5_horizontal_2 = [
            [".",".",".",".","."],
            ["X","X","X","X","X"],
            [".",".",".",".","."],
            [".",".",".",".","."],
            [".",".",".",".","."],
        ]
        winningboard_5x5_horizontal_3 = [
            [".",".",".",".","."],
            [".",".",".",".","."],
            ["X","X","X","X","X"],
            [".",".",".",".","."],
            [".",".",".",".","."],
        ]
        winningboard_5x5_horizontal_4 = [
            [".",".",".",".","."],
            [".",".",".",".","."],
            [".",".",".",".","."],
            ["X","X","X","X","X"],
            [".",".",".",".","."],
        ]
        winningboard_5x5_horizontal_5 = [
            [".",".",".",".","."],
            [".",".",".",".","."],
            [".",".",".",".","."],
            [".",".",".",".","."],
            ["X","X","X","X","X"],
        ]


        assert TicTacToeGame.check_for_winner(winningboard_5x5_horizontal_1) == (True, 'X')
        assert TicTacToeGame.check_for_winner(winningboard_5x5_horizontal_2) == (True, 'X')
        assert TicTacToeGame.check_for_winner(winningboard_5x5_horizontal_3) == (True, 'X')
        assert TicTacToeGame.check_for_winner(winningboard_5x5_horizontal_4) == (True, 'X')
        assert TicTacToeGame.check_for_winner(winningboard_5x5_horizontal_5) == (True, 'X')

    def test_checkwinner_5x5_diagonal(self):
        '''Testing diagonal wins on a 5x5 board'''
        winningboard_5x5_diagonal_1 = [
            ["X",".",".",".","."],
            [".","X",".",".","."],
            [".",".","X",".","."],
            [".",".",".","X","."],
            [".",".",".",".","X"],
        ]
        winningboard_5x5_diagonal_2 = [
            [".",".",".",".","X"],
            [".",".",".","X","."],
            [".",".","X",".","."],
            [".","X",".",".","."],
            ["X",".",".",".","."],
        ]

        assert TicTacToeGame.check_for_winner(winningboard_5x5_diagonal_1) == (True, 'X')
        assert TicTacToeGame.check_for_winner(winningboard_5x5_diagonal_2) == (True, 'X')

    def test_checkwinner_for_funsiews(self):
        '''Testing various win permutations, because why not?'''
        fun_1 = [
            ["X","O","X"],
            ["O","X","X"],
            ["O","O","X"],
        ]
        fun_2 = [
            ["O","O","O","X"],
            ["X","O","O","X"],
            ["X","O","O","X"],
            ["X","X","X","O"],
        ]
        fun_3 = [
            [".",".","Z"],
            [".",".","Z"],
            [".",".","Z"],
        ]
        fun_4 = [
            ["T"]
        ]
        fun_5 = [
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","B"],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","B"],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","B"],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","B"],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","B"],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","B"],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","B"],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","B"],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","B"],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","B"],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","B"],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","B"],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","B"],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","B"],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","B"],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","B"],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","B"],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","B"],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","B"],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","B"],
        ]
        fun_6 = [
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",],
            [".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",],
            ["X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X",],
        ]

        assert TicTacToeGame.check_for_winner(fun_1) == (True, 'X')
        assert TicTacToeGame.check_for_winner(fun_2) == (True, 'O')
        assert TicTacToeGame.check_for_winner(fun_3) == (True, 'Z')
        assert TicTacToeGame.check_for_winner(fun_4) == (True, 'T')
        assert TicTacToeGame.check_for_winner(fun_5) == (True, 'B')
        assert TicTacToeGame.check_for_winner(fun_6) == (True, 'X')
