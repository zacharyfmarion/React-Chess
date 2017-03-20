import * as game from '../actionTypes/gameTypes'
import { initializeBoard } from '../../helpers/chess'

/*
 *  Initial state of the game. 
 */
const initialState = {
  playing: false,
  /*
   * A 2d array of the locations of all of the pieces on the board.
   */
  pieces: initializeBoard(),
  /*
   * The list of captured pieces associated with each player. Each piece is 
   * formatted as an object { color, type }
   */
  captured: {
    'white': [],
    'black': [],
  },
  /*
   * A list of the moves made in the game. Formatted as { start: {row, col},
   * end: {row, col} }
   */
  moves: [],
}

export default function gameReducer(state=initialState, action) {
  switch (action.type) {
    case game.UPDATE_PIECES:
      return {...state, pieces: action.payload}
    case game.UPDATE_CAPTURED:
      return {...state, captured: action.payload}
    case game.ADD_MOVE: {
      const moves = state.moves.slice() 
      moves.push(action.payload)
      return {...state, moves}
    }
    case game.CHANGE_GAME_STATE:
      return {...state, playing: action.payload}
    default: return {...state}
  }
}
