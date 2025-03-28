import { configureStore } from '@reduxjs/toolkit'
import authReducer from './authSlice'
import dashboardReducer from './dashboardSlice'
import saveSchematicReducer from './saveSchematicSlice'
import simulationReducer from './simulationSlice'

const store = configureStore({
  reducer: {
    auth: authReducer,
    dashboard: dashboardReducer,
    saveSchematic: saveSchematicReducer,
    simulation: simulationReducer
  },
  middleware: (getDefaultMiddleware) => getDefaultMiddleware()
})

export default store
