import { applyMiddleware, createStore } from 'redux'
import createLogger from 'redux-logger'
import reducers from './reducers'

export default createStore(
  reducers,
  applyMiddleware(createLogger()),
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
)
