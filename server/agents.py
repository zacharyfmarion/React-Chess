import random
import math
from game import ChessGame
from pieces import Piece
from color import Color

class GamePlayer(object):
    '''Represents the logic for an individual player in the game'''

    def __init__(self, color, game, horizon):
        '''"player_id" indicates which player is represented (int)
        "game" is a game object with a get_successors function'''
        self.color = color
        self.game = game
        self.horizon = horizon
        return

    def evaluate(self, state):
        '''Evaluates a given state for the specified agent
        "state" is a game state object'''
        pass

    def alpha_beta_move(self, state):
        '''Same as minimax_move with alpha-beta pruning'''
        pass

class StudentPlayer(GamePlayer):
    def __init__(self, color, game, horizon):
        GamePlayer.__init__(self, color, game, horizon)

    def evaluate(self, state):
        ''' 
        The evaluation function for the student player. For the moment it is just the
        sum of the values of the pieces that we have captured minus the values of the
        pieces that the opponent has captured
        '''
        # pieces that I have captured
        other_color = Color.WHITE if self.color == Color.BLACK else Color.BLACK
        my_captured = sum([int(piece) for piece in state.pieces[self.color]])
        their_captured = sum([int(piece) for piece in state.pieces[other_color]])
        captured_diff = my_captured - their_captured
        # Also check who has better control of the center of the board...for now just
        # the number of pieces that occupy the center
        return captured_diff # + (center_diff(state) / 3)

    def alpha_beta_move(self, state):
        assert state.color == self.color
        return alpha_beta(self.game, state, 0, self.horizon, self.evaluate, \
                float("-inf"), float("inf"))

def center_diff(state):
    ''' Get the difference in the number of pieces in the center of the board '''
    center_pieces = {Color.WHITE: 0, Color.BLACK: 0}
    for i in range(3, 5):
        for j in range(3, 5):
            piece = state.board[i][j]
            if isinstance(piece, Piece):
                center_pieces[piece.color] += 1
    other_color = Color.WHITE if state.color == Color.BLACK else Color.BLACK
    return center_pieces[state.color] - center_pieces[other_color]


# ======================================================================== #
# ============================ ALPHA BETA ================================ #
# ======================================================================== #

def alpha_beta(game, state, depth, horizon, eval_fn, alpha, beta):
    """ Return (value, action) tuple for minimax search up to the given depth,
    with alpha-beta pruning """
    successors, actions = game.get_successors(state)
    # IF THERE ARE NO MORE SUCCESSORS THE GAME IS OVER
    if len(successors) == 0: 
        print("No more successors") 
        return (((0, 0), (0, 0)), state)
    # add a new 
    options = [ab_min_value(game, new_state, depth + 1, horizon, eval_fn, alpha, beta) \
                  for new_state in successors]
    max_val = max(options)
    argmaxes = [i for i, x in enumerate(options) if x == max_val]
    index_choice = random.choice(argmaxes)
    print("Hueristic: ", options[index_choice])
    return (actions[index_choice], successors[index_choice])

def ab_max_value(game, state, depth, horizon, eval_fn, alpha, beta):
    if depth == horizon: return eval_fn(state) 
    successors, actions = game.get_successors(state)
    if len(successors) == 0: return eval_fn(state)
    v = float("-inf")
    for new_state in successors:
        min_val = ab_min_value(game, new_state, depth + 1, horizon, eval_fn, alpha, beta)
        v = max(min_val, v)
        if v >= beta: return v
        alpha = max(v, alpha)
    return v

def ab_min_value(game, state, depth, horizon, eval_fn, alpha, beta):
    if depth == horizon: return eval_fn(state)
    # get the sucessors
    successors, actions = game.get_successors(state)
    if len(successors) == 0: return eval_fn(state)
    v = float("inf")
    for new_state in successors:
        max_val = ab_max_value(game, new_state, depth + 1, horizon, eval_fn, alpha, beta)
        v = min(v, max_val)
        if v <= alpha: return v
        beta = min(v, beta)
    return v
