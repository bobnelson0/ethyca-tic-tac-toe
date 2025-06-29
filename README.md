# Ethyca Tic Tac Toe API
 
This exercise is authored by Bobby Nelson and is based on the take-home exercise documented here: https://github.com/ethyca/python-takehome-2

# Installation
There are two options available for running this. Follow the instructions below.

## via Docker
I've provided a `Dockerfile` to provide a quickstart to avoid any environment specific issues. To use the `Dockerfile`, be sure you have docker available and then follow these steps:

1. First, build the image
`docker build --no-cache=true -t ethyca-tic-tac-toe .`
2. Run the docker image on port 80
`docker run -p 80:80 ethyca-tic-tac-toe`
3. You'll see console output stating that the API server has started. This application uses [FastAPI](https://fastapi.tiangolo.com/) to start an API server and serve a usable OpenAPI inteface at http://0.0.0.0:80/docs . The output you see should look something like this:
```
FastAPI   Starting production server 🚀

             Searching for package file structure from directories with
             __init__.py files
             Importing from /

    module   🐍 main.py

      code   Importing the FastAPI app object from the module with the following
             code:

             from main import app

       app   Using import string: main:app

    server   Server started at http://0.0.0.0:80
    server   Documentation at http://0.0.0.0:80/docs
```

## via Python
This will allow you to run the application and play with the settings, run `pytest` etc. This will basically put you in dev mode for this project. These steps should ensure that you don't encounter any issues, but it's always possible that local machine configurations could cause problems. These steps were all tested on a Mac running OSX.
From the root of the application directory, follow these steps:

1. `pip3 install virtualenv` (if you don't have it already)
2. `python3 -m venv venv`
3. `source venv/bin/activate`
4. `pip install -r requirements.txt` 
5. `pytest` (optional)
6. `fastapi dev main.py`

You'll see console output stating that the API server has started in dev mode. The application will have a usable OpenAPI inteface at http://0.0.0.0:80/docs . The output you see should look something like this:
```
   FastAPI   Starting development server 🚀
 
             Searching for package file structure from directories with __init__.py files
             Importing from /Users/bnelson/Workspace/Ethyca/ethyca-tic-tac-toe
 
    module   🐍 main.py
 
      code   Importing the FastAPI app object from the module with the following code:
 
             from main import app
 
       app   Using import string: main:app
 
    server   Server started at http://127.0.0.1:8000
    server   Documentation at http://127.0.0.1:8000/docs
 
       tip   Running in development mode, for production use: fastapi run
```

# Did I check all the boxes?
The following items were give has part of the overall exercise. How did I solve these? More info below:

__Use Python (any flavour) to develop a REST API that__
This uses Python 3.11 and FastAPI to build a quick API and usable OpenAPI intervace

__Allows me to create a new game of Noughts and Crosses, and returns the game ID.__
The IDs generated use a fun package called `names_generator` which generates unique names which are also human readable. Examples `flamboyant_bartik`, `angry_sanderson`

__Allows me to make the next move by specifying the co-ordinates I wish to move on. e.g. {"x": 1, "y": 1} would denote a move to the middle square by the requesting player, and returns the new state of the board after the computer has made its move in turn. Note: There is no need to create an AI opponent, random moves are fine__
The `POST` endpoint `/make-a-move` takes a request body of `{"row": X, "col": Y}` where `X` and `Y` are integers. This move is also recorded in the history file.
There is also a `GET` endpoint (`/get-game-status`) which shows the current game status without requiring another move to be made.

__Allows me to view all moves in a game, chronologically ordered.__
All "history" is stored in a single `.ndjson` file. Each line of history has a tag that can be filtered on. There is a `GET` endpoint (`/get-move-history`) which returns all move data, for all games, starting with earliest and ending with most recent.
There is also a `GET` endpoint (`/get-all-history`) which returns all events.


__Allows me to view all games I have played, chronologically ordered.__
All "history" is stored in a single `.ndjson` file. Each line of history has a tag that can be filtered on. There is a `GET` endpoint (`/get-game-history`) which returns all game data, for all games, starting with earliest and ending with most recent.
There is also a `GET` endpoint (`/get-all-history`) which returns all events.

__Surprise us! Use your inherent style and panache to sprinkle that extra bit of gee-whizz atop your solution.__
First, I decided to make the board size configurable. Now you aren't limited to only a 3x3 board. The `CONST_BOARD_SIZE` constant can be modified to change the size of the board. You'll need to restart the application for it to take effect. I've tested this for up to 20x20 boards. The unit tests in `test_main.py` cover some of these more unique cases.
I also decided to use an `.ndjson` format for the history. I was initially going to include a sqlite database, but I chose this option because it is much easier to setup quickly, make schema changes, test with, etc. I've even included some data so that the endpoint returns valid data from the start.
Format info:
* https://en.wikipedia.org/wiki/JSON_streaming#Newline-delimited_JSON
* https://github.com/ndjson/ndjson-spec