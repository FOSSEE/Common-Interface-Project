// Initialize Redux store which holds the whole state tree of application.
import reducer from './reducers/index'
import { createStore, applyMiddleware } from 'redux'
import { thunk } from 'redux-thunk'
const createStoreWithMiddleware = applyMiddleware(thunk)(createStore)
const store = createStoreWithMiddleware(reducer)

export default store
