import { configureStore } from '@reduxjs/toolkit'
import reducer from './reducers/index'
import componentPropertiesReducer from './slices/componentPropertiesSlice'
import schematicEditorReducer from './slices/schematicEditorSlice'
import dashboardReducer from './slices/dashboardSlice'
import netlistReducer from './slices/netlistSlice'
import simulationReducer from './slices/simulationSlice'
import saveSchematicReducer from './slices/saveSchematicSlice'

const store = configureStore({
  reducer: {
    oldReducers: reducer,
    componentProperties: componentPropertiesReducer,
    schematicEditor: schematicEditorReducer,
    dashboardReducer: dashboardReducer,
    netlistReducer: netlistReducer,
    simulationReducer: simulationReducer,
    saveSchematicReducer: saveSchematicReducer
  }
})

// store.dispatch(fetchCompProperties())
// store.dispatch(setBlockParameter())

export default store
