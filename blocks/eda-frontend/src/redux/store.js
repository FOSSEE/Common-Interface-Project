// // Initialize Redux store which holds the whole state tree of application.
// import reducer from './reducers/index'
// import { createStore, applyMiddleware } from 'redux'
// import reduxThunk from 'redux-thunk'
// const createStoreWithMiddleware = applyMiddleware(reduxThunk)(createStore)
// const store = createStoreWithMiddleware(reducer)

// export default store

import { configureStore } from '@reduxjs/toolkit'
import reducer from './reducers/index' // Your existing reducers
import componentPropertiesReducer, { fetchCompProperties, setBlockParameter } from './slices/componentPropertiesSlice'
// import thunk from 'redux-thunk'

// Middleware setup if needed
// const middleware = [thunk]

// Add any middleware you need here

// Create store with Redux Toolkit's configureStore
const store = configureStore({
  reducer: {
    // Include your existing reducers
    oldReducers: reducer,

    // Include your new RTK slice reducer
    componentProperties: componentPropertiesReducer
  }
  // middleware
})

// If you have any async thunk actions in your new RTK slice, you can add them as extraReducers to the store
store.dispatch(fetchCompProperties())
store.dispatch(setBlockParameter())

export default store
