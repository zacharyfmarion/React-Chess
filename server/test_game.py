""" Testing that we can come up with a correct move """
from game import ChessGame
from color import Color
from pieces import *
from agents import StudentPlayer

def play_game():
    # Create the game
    game = ChessGame()
    # Create the two players
    player1 = StudentPlayer(Color.WHITE, game, 4)
    player2 = StudentPlayer(Color.BLACK, game, 4)
    move_list = []
    for move in game.play_game(player1, player2, verbose=True):
        move_list.append(move)

def main():
    play_game()

if __name__ == "__main__":
    main()
