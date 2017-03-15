""" Test the implementation of each chess piece """
from pieces import *
from game import *

def test_piece(piece):
    for i in range(8):
        for j in range(8):
            board = [[" " for x in range(8)] for y in range(8)]
            board[i][j] = piece(Color.WHITE)
            new_game = ChessGame(board)
            for coord in board[i][j].valid_moves((i, j), new_game.state):
                board[coord[0]][coord[1]] = "x"
            new_game.print_board()

def main():
    for piece in [Pawn, Knight, Bishop, Rook, Queen, King]:
        print("Testing: {}".format(str(piece)))
        test_piece(piece)

if __name__ == "__main__":
    main()
