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

# Create the chess game
game = ChessGame()
# Create the two players
player1 = StudentPlayer(Color.WHITE, game)
player2 = StudentPlayer(Color.BLACK, game)

# Create a simulation of the game
sim = game.play_game(player1, player2)

@socketio.on('connect')
def on_connect():
    # For each move in the game we send the move to the frontend to be displayed
    # Note that play_game is a generator function and is thus iterable
    emit('server-ready')

@socketio.on('request-move')
def on_request_move():
    print("Move requested")
    move = next(sim)
    emit('move', (move['start'], move['end']))

@socketio.on('reset-game')
def on_reset_game():
    game = ChessGame()
    sim = game.play_game(player1, player2)

if __name__ == '__main__':
    socketio.run(app)
