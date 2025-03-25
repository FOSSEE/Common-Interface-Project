import { configureStore } from '@reduxjs/toolkit'
import simulationReducer from './simulationSlice'
import thunk from 'redux-thunk'

const store = configureStore({
    reducer: {
        simulation: simulationReducer
    },
    middleware: (getDefaultMiddleware) => getDefaultMiddleware().concat(thunk)
})

export default store
