import { combineReducers } from 'redux'
import undoable from 'redux-undo'
import gameReducer from './gameReducer'

export default combineReducers({
  game: undoable(gameReducer),
})
