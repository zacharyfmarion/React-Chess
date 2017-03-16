# Simulation of a game of chess...
from pieces import *
from color import Color
from utils import find_king

class GameState:
    def __init__(self, board, color=Color.WHITE, pieces=None):
        self.board = board
        self.color = color
        self.pieces = pieces
        # Pieces is a dict representing which pieces has been captured
        if pieces == None:
            self.pieces = {
                Color.WHITE: [],
                Color.BLACK: []
            }

class ChessGame:

    def __init__(self, board=None):
        # chess board
        board = self.create_board() if board is None else board
        self.state = GameState(board, color=Color.WHITE)
        # A list of moves that have been made. They eventually should be in standard
        # chess notation so that the game can be exported and viewed in another
        # chess application
        self.moves = []

    def create_board(self):
        board = [[" " for i in range(8)] for i in range(8)]
        for i in range(8):
            color = Color.WHITE if i < 2 else Color.BLACK
            for j in range(8):
                if i == 0 or i == 7:
                    if j == 0 or j == 7:
                        board[i][j] = Rook(color)
                    elif j == 1 or j == 6:
                        board[i][j] = Knight(color)
                    elif j == 2 or j == 5:
                        board[i][j] = Bishop(color)
                    elif j == 3:
                        board[i][j] = King(color) if color == Color.WHITE else Queen(color)
                    elif j == 4:
                        board[i][j] = Queen(color) if color == Color.WHITE else King(color)
                elif i == 1 or i == 6:
                    board[i][j] = Pawn(color)
        return board

    def rotate_board(self):
        board = self.state.board
        for row in board:
            row.reverse()
        for i in range(4):
            temp = board[i]
            board[i] = board[7-i]
            board[7-i] = temp
        self.state.board = board

    def flip_coords(self, move):
        start, end = move
        start = (7 - start[0], 7 - start[1])
        end = (7 - end[0], 7 - end[1])
        return (start, end)

    def play_game(self, player1, player2):
        ''' Play a game with two minimax agents '''
        curr_player = player1 if player1.color == self.state.color else player2
        while True:
            print("{} Making their move:\n".format(curr_player.color))
            move, new_state = curr_player.alpha_beta_move(self.state)
            move = move if curr_player.color == Color.WHITE else self.flip_coords(move)
            start, end = move
            yield {
                'start': {'row': start[0], 'col': start[1]},
                'end': {'row': end[0], 'col': end[1]}
            }
            # If we are at the end of the game (no more moves) then break
            if move == -1: break
            self.state = new_state
            curr_player = player1 if curr_player == player2 else player2
            #  if curr_player.color == Color.WHITE: self.print_board()
            self.rotate_board()
            #  if curr_player.color == Color.BLACK: self.print_board()
            #  print("White: ", [str(piece) for piece in self.state.pieces[Color.WHITE]])
            #  print("Black: ", [str(piece) for piece in self.state.pieces[Color.BLACK]], "\n")
        print("\nGame ended")
    
    def get_successors(self, state):
        ''' 
        Get all of the sucessor moves given as valid position...this is quite the
        task given the number of valid moves in a given position in a chess game.
        I need to take some time and plan out exactly how everything will work.
        '''
        successors = []
        actions = []
        board = state.board
        for i, row in enumerate(board):
            for j, item in enumerate(row):
                if isinstance(item, Piece) and item.color == state.color:
                    # We need to add all the valid moves for the given piece to the 
                    # list of available moves
                    piece_successors, piece_actions = item.get_successors((i, j), state)
                    successors += piece_successors
                    actions += piece_actions
        return successors, actions

    def print_board(self):
        ''' Pretty print the board '''
        cols = "a  b  c  d  e  f  g  h" 
        print("    " + cols)
        print("  +------------------------+")
        for i, row in enumerate(self.state.board):
            print("{} |".format(i + 1), end="")
            for piece in row:
                if not isinstance(piece, Piece): print(" {} ".format(piece), end="")
                elif piece.color == Color.WHITE:
                    print("\033[37m {} \033[0m".format(piece), end="")
                else:
                    print("\033[34m {} \033[0m".format(piece), end="")
            print("|")
        print("  +------------------------+")
