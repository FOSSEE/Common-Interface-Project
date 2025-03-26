import { configureStore } from '@reduxjs/toolkit'
import authReducer from './authSlice'
import simulationReducer from './simulationSlice'

const store = configureStore({
  reducer: {
    auth: authReducer,
    simulation: simulationReducer
  },
  middleware: (getDefaultMiddleware) => getDefaultMiddleware()
})

export default store
