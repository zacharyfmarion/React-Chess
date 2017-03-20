/*
 * Actions for the application
 */

import * as game from '../actionTypes/gameTypes'

export function changeGameState(playing) {
  return {
    type: game.CHANGE_GAME_STATE,
    payload: playing,
  } 
}

export function updatePieces(pieces) {
  return {
    type: game.UPDATE_PIECES,
    payload: pieces,
  }
}

/*
 * Add a move to the moves list
 */
export function addMove(move) {
  return {
    type: game.ADD_MOVE,
    payload: move,
  }
}

/*
 * Update the captured pieces state
 */
export function updateCaptured(captured) {
  return {
    type: game.UPDATE_CAPTURED,
    payload: captured,
  }
}

/*
 * Step backward in the moves array
 */
export function moveBackward() {
  return {
    type: game.MOVE_BACKWARD,
    payload: {},
  }
}

/*
 * Step forward in the moves array
 */
export function moveForward() {
  return {
    type: game.MOVE_FORWARD,
    payload: {},
  }
}
