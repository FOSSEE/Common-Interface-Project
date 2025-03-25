import { configureStore } from '@reduxjs/toolkit'
import simulationReducer from './simulationSlice'

const store = configureStore({
  reducer: {
    simulation: simulationReducer
  },
  middleware: (getDefaultMiddleware) => getDefaultMiddleware()
})

export default store
