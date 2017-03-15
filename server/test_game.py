""" Testing that we can come up with a correct move """
from game import ChessGame
from color import Color
from pieces import *
from agents import StudentPlayer

def play_game():
    # Create the game
    game = ChessGame()
    # Create the two players
    player1 = StudentPlayer(Color.WHITE, game)
    player2 = StudentPlayer(Color.BLACK, game)
    game.play_game(player1, player2)

def main():
    play_game()

if __name__ == "__main__":
    main()
