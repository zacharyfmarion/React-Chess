from pieces import *

def valid_position(position):
    ''' Return whether the new position is valid '''
    row, col = position
    return not (col < 0 or col > 7 or row < 0 or row > 7)

def check_instance(obj, classes):
    ''' Check whether an object is an instance of a given set of classes '''
    return any([isinstance(obj, c) for c in classes])

def check_attacking(location, state, row_dir, col_dir):
    ''' Check whether the pieces in a given direction are checking the king '''
    # QUEEN OR ROOK
    dirs = (row_dir, col_dir)
    attacking = []
    if dirs in [(1,0), (0, 1), (-1, 0), (0, -1)]: 
        attacking = [Queen, Rook]
    # QUEEN OR BISHOP
    elif dirs in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
        attacking = [Queen, Bishop]
    for i in range(1, 8):
        new_row = location[0] + (row_dir * i)
        new_col = location[1] + (col_dir * i)
        if not valid_position((new_row, new_col)): break
        piece = state.board[new_row][new_col]
        if isinstance(piece, Piece):
            if piece.color == state.color: break
            if check_instance(piece, attacking): return True
    return False

def check_attacking_from_dirs(location, state, dirs, correct_piece):
    ''' Check whether an opposing team's piece is attacking given the directions
    (offsets) from the king'''
    for _dir in dirs:
        new_row = location[0] + _dir[0]
        new_col = location[1] + _dir[1]
        if not valid_position((new_row, new_col)): continue
        # Get the location of the piece
        piece = state.board[new_row][new_col]
        if isinstance(piece, correct_piece) and piece.color != state.color:
            return True
    return False

def in_check(state):
    ''' Return whether a given state is currently in check. The easiest way to do this is to
    just look in all the places where an attacking place could be...if an attacking piece is
    there then we are in check...if not then we are not'''
    color = state.color
    board = state.board
    king_loc = find_king(state, state.color)
    # Check whether the queen, bishop, and rook are attacking
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0: continue
            if check_attacking(king_loc, state, i, j): return True
    # Check whether a pawn is attacking
    pawn_dirs = [(-1, -1), (-1, 1)]
    if check_attacking_from_dirs(king_loc, state, pawn_dirs, Pawn): return True
    # Check whether a knight
    knight_dirs = [(2, -1), (2, 1), (1, -2), (1, 2), (-1, -2), (-1, 2), (-2, -1), (-2, 1)]
    if check_attacking_from_dirs(king_loc, state, knight_dirs, Knight): return True
    # Finally return false if nothing is attacking
    return False

def find_king(state, color):
    ''' Find a certain colors king '''
    for i, row in enumerate(state.board):
        for j, piece in enumerate(row):
            if isinstance(piece, King) and piece.color == color:
                return (i, j)
    print("[ERROR] No king found")
    return (0, 0)

