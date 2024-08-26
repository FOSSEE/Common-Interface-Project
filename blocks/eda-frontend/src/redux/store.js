import { configureStore } from '@reduxjs/toolkit'
import componentPropertiesReducer from './slices/componentPropertiesSlice'
import schematicEditorReducer from './slices/schematicEditorSlice'
import dashboardReducer from './slices/dashboardSlice'
import netlistReducer from './slices/netlistSlice'
import simulationReducer from './slices/simulationSlice'
import saveSchematicReducer from './slices/saveSchematicSlice'
import authReducer from './slices/authSlice'

const store = configureStore({
  reducer: {
    componentProperties: componentPropertiesReducer,
    schematicEditor: schematicEditorReducer,
    dashboard: dashboardReducer,
    netlist: netlistReducer,
    simulation: simulationReducer,
    saveSchematic: saveSchematicReducer,
    auth: authReducer
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        ignoredActions: ['componentProperties/getCompProperties'],
        ignoredPaths: ['componentProperties.block']
      }
    })
})

export default store
