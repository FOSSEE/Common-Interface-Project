import { configureStore } from '@reduxjs/toolkit'
import authReducer from './authSlice'
import dashboardReducer from './dashboardSlice'
import simulationReducer from './simulationSlice'

const store = configureStore({
  reducer: {
    auth: authReducer,
    dashboard: dashboardReducer,
    simulation: simulationReducer
  },
  middleware: (getDefaultMiddleware) => getDefaultMiddleware()
})

export default store
