import { createStore, applyMiddleware, combineReducers } from 'redux'
import reduxThunk from 'redux-thunk'
import reducer from './reducers/index'
import componentPropertiesReducer from './slices/componentPropertiesSlice' // Adjust the path as per your project structure

// Combine the existing reducers with the componentPropertiesReducer
const rootReducer = combineReducers({
  existingReducer: reducer, // Change `existingReducer` to the key under which you want to store your existing reducer
  componentProperties: componentPropertiesReducer
})

// Create store with combined reducers
const createStoreWithMiddleware = applyMiddleware(reduxThunk)(createStore)
const store = createStoreWithMiddleware(rootReducer)

export default store
