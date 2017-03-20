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
player1 = StudentPlayer(Color.WHITE, game, 3)
player2 = StudentPlayer(Color.BLACK, game, 3)

# Create a simulation of the game
sim = game.play_game(player1, player2)

@socketio.on('connect')
def on_connect():
    # For each move in the game we send the move to the frontend to be displayed
    # Note that play_game is a generator function and is thus iterable
    emit('server-ready')

@socketio.on('request-move')
def on_request_move():
    global sim
    move = next(sim)
    emit('move', (move['start'], move['end'], move['captured']))

@socketio.on('valid-moves')
def on_valid_moves(coords):
    ''' Return to the frontend the valid moves available for a particular piece '''
    global game
    row, col = coords['row'], coords['col']
    # The value we return is passed into the callback on the fronted
    return game.valid_moves(row, col)

@socketio.on('reset-game')
def on_reset_game():
    global game
    global sim
    game = ChessGame()
    sim = game.play_game(player1, player2)

if __name__ == '__main__':
    socketio.run(app)
