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
    dashboardReducer: dashboardReducer,
    netlistReducer: netlistReducer,
    simulationReducer: simulationReducer,
    saveSchematicReducer: saveSchematicReducer,
    authReducer: authReducer
  }
})

export default store
