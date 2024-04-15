import { combineReducers } from 'redux'
// import schematicEditorReducer from './schematicEditorReducer'
import netlistReducer from './netlistReducer'
import simulationReducer from './simulationReducer'
import authReducer from './authReducer'
import saveSchematicReducer from './saveSchematicReducer'
import dashboardReducer from './dashboardReducer'
export default combineReducers({
  // schematicEditorReducer,
  netlistReducer,
  simulationReducer,
  authReducer,
  saveSchematicReducer,
  dashboardReducer
})
