from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
from game import ChessGame
from color import Color
from agents import StudentPlayer

# Small Flask app that starts a socket.io server for the game. Run with:
# > FLASK_APP=app.py python3.5 -m flask run

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('connect')
def start_game():
    # Create the game
    game = ChessGame()
    # Create the two players
    player1 = StudentPlayer(Color.WHITE, game)
    player2 = StudentPlayer(Color.BLACK, game)
    # For each move in the game we send the move to the frontend to be displayed
    # Note that play_game is a generator function and is thus iterable
    for move in game.play_game(player1, player2):
        print("MOVE: ", move)
        emit('move', move)

if __name__ == '__main__':
    socketio.run(app)
