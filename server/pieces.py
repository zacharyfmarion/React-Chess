""" Each piece is a class bc OOP why not """
from copy import deepcopy
from color import Color

class Piece(object):

    def __init__(self, color):
        ''' Set the color of the piece '''
        self.color = color

    def valid_moves(location, board):
        ''' Return all the valid moves for a piece given a location '''
        pass

    def get_successors(self, location, state):
        ''' 
        Location is an (i, j) tuple representing where the player
        is on the board. Note that we need to be careful, as the white players
        indices will be different front the black players.

        We return (successors, actions) where successors are just state objects,
        and actions is a tuple of tuples, being the location of the piece to move,
        and where that piece will be going
        '''
        successors = []
        actions = []
        board = state.board
        for move in self.valid_moves(location, state):
            new_state = deepcopy(state)
            # We check whether a piece exists to capture
            dest = board[move[0]][move[1]]
            if isinstance(dest, Piece):
                if isinstance(dest, King): continue
                new_state.pieces[self.color].append(dest)
            # Moving the piece to the given location
            # We might need to actually copy the object if it is just a reference!
            new_state.board[move[0]][move[1]] = new_state.board[location[0]][location[1]]
            new_state.board[location[0]][location[1]] = " "
            # Change the color of the state to point to the other player...their turn
            other_color = Color.WHITE if state.color == Color.BLACK else Color.BLACK
            new_state.color = other_color
            # We CANNOT move into check. This means that we stop the game when there are
            # no more moves that are available to us
            if in_check(new_state): continue 
            successors.append(new_state)
            actions.append((location, move))
        return (successors, actions)

    def __int__(self):
        ''' Convert to integer (based on the value of the piece) '''
        pass
    
    def __str__(self):
        ''' Convert to string '''
        pass

class Pawn(Piece):

    def __init__(self, color):
        Piece.__init__(self, color)
        self.name = 'pawn'

    def valid_moves(self, location, state):
        moves = []
        # if we are on the first row, we can move forward if we are not blocked by
        # another piece
        if location[0] == 1 and not isinstance(state.board[2][location[1]], Piece) and \
                                not isinstance(state.board[3][location[1]], Piece):
            moves.append((3, location[1]))
        for i in [-1, 0, 1]:
            new_row = location[0] + 1
            new_col = location[1] + i
            if not valid_position((new_row, new_col)): continue
            attacking = state.board[new_row][new_col]
            attacking_piece = isinstance(attacking, Piece)
            # we need to be attacking an opponents piece to move diagonally
            if i != 0 and not attacking_piece: continue
            if attacking_piece and attacking.color == self.color: continue
            if i == 0 and attacking_piece: continue
            moves.append((new_row, new_col))
        return moves

    def __int__(self): return 1
    def __str__(self): return "♙"


class Knight(Piece):

    def __init__(self, color):
        Piece.__init__(self, color)
        self.name = 'knight'

    def valid_moves(self, location, state):
        moves = []
        dirs = [(2, -1), (2, 1), (1, -2), (1, 2), 
                (-1, -2), (-1, 2), (-2, -1), (-2, 1)]
        for _dir in dirs:
            new_row = location[0] + _dir[0]
            new_col = location[1] + _dir[1]
            if not valid_position((new_row, new_col)): continue
            attacking = state.board[new_row][new_col]
            if isinstance(attacking, Piece) and attacking.color == self.color:
                continue
            moves.append((new_row, new_col))
        return moves

    def __int__(self): return 3
    def __str__(self): return "♘"

class Bishop(Piece):

    def __init__(self, color):
        Piece.__init__(self, color)
        self.name = 'bishop'

    def moves_helper(self, location, state, row_dir, col_dir):
        ''' Helper function to compute the valid moves in a given direction '''
        moves = []
        for i in range(1, 8):
            new_row = location[0] + (row_dir * i)
            new_col = location[1] + (col_dir * i)
            if not valid_position((new_row, new_col)): break
            attacking = state.board[new_row][new_col]
            if isinstance(attacking, Piece):
                if attacking.color == self.color: break
                else: 
                    # We still add this state as a valid move, but we break out of
                    # the loop afterwards
                    moves.append((new_row, new_col))
                    break
            moves.append((new_row, new_col))
        return moves
        
    def valid_moves(self, location, state):
        ''' Bishops can move diagonally, but cannot move past any squares occupied
        by another piece. '''
        moves = []
        moves += self.moves_helper(location, state, 1, 1)
        moves += self.moves_helper(location, state, 1, -1)
        moves += self.moves_helper(location, state, -1, 1)
        moves += self.moves_helper(location, state, -1, -1)
        return moves

    def __int__(self): return 3
    def __str__(self): return "♗"


class Rook(Piece):

    def __init__(self, color):
        Piece.__init__(self, color)
        self.name = 'rook'

    def moves_helper(self, location, state, row_dir, col_dir):
        ''' Helper function to compute the valid moves in a given direction '''
        moves = []
        for i in range(1, 8):
            new_row = location[0] + (row_dir * i)
            new_col = location[1] + (col_dir * i)
            if not valid_position((new_row, new_col)): break
            attacking = state.board[new_row][new_col]
            if isinstance(attacking, Piece):
                if attacking.color == self.color: break
                else: 
                    # We still add this state as a valid move, but we break out of
                    # the loop afterwards
                    moves.append((new_row, new_col))
                    break
            moves.append((new_row, new_col))
        return moves
        
    def valid_moves(self, location, state):
        ''' Rooks can move left or right or up or down'''
        moves = []
        moves += self.moves_helper(location, state, 1, 0)
        moves += self.moves_helper(location, state, -1, 0)
        moves += self.moves_helper(location, state, 0, 1)
        moves += self.moves_helper(location, state, 0, -1)
        return moves

    def __int__(self): return 5
    def __str__(self): return "♖"

class Queen(Piece):

    def __init__(self, color):
        Piece.__init__(self, color)
        self.name = 'queen'

    def moves_helper(self, location, state, row_dir, col_dir):
        ''' Helper function to compute the valid moves in a given direction '''
        moves = []
        for i in range(1, 8):
            new_row = location[0] + (row_dir * i)
            new_col = location[1] + (col_dir * i)
            if not valid_position((new_row, new_col)): break
            attacking = state.board[new_row][new_col]
            if isinstance(attacking, Piece):
                if attacking.color == self.color: break
                else: 
                    # We still add this state as a valid move, but we break out of
                    # the loop afterwards
                    moves.append((new_row, new_col))
                    break
            moves.append((new_row, new_col))
        return moves

    def valid_moves(self, location, state):
        ''' Queens can essentially move in the same direction as a rook or a bishop '''
        moves = []
        # Bishop moves
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0: continue
                moves += self.moves_helper(location, state, i, j)
        return moves

    def __int__(self): return 9
    def __str__(self): return "♕"

class King(Piece):

    def __init__(self, color):
        Piece.__init__(self, color)
        self.name = 'king'

    def valid_moves(self, location, state):
        moves = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                new_row = location[0] + i
                new_col = location[1] + j
                if (i == 0 and j == 0) or not valid_position((new_row, new_col)): 
                    continue
                attacking = state.board[new_row][new_col]
                if isinstance(attacking, Piece) and attacking.color == self.color: continue
                moves.append((new_row, new_col))
        return moves
        pass

    def __int__(self): return 200
    def __str__(self): return "♔"

# Need to avoid circular dependencies
from utils import in_check, valid_position
