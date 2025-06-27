import { configureStore } from '@reduxjs/toolkit'

import authReducer from './authSlice'
import componentPropertiesReducer from './componentPropertiesSlice'
import dashboardReducer from './dashboardSlice'
import saveSchematicReducer from './saveSchematicSlice'
import schematicEditorReducer from './schematicEditorSlice'
import simulationReducer from './simulationSlice'

const store = configureStore({
  reducer: {
    auth: authReducer,
    componentProperties: componentPropertiesReducer,
    dashboard: dashboardReducer,
    saveSchematic: saveSchematicReducer,
    schematicEditor: schematicEditorReducer,
    simulation: simulationReducer
  },
  middleware: (getDefaultMiddleware) => getDefaultMiddleware()
})

export default store
