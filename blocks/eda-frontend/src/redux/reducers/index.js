import { combineReducers } from 'redux'
import schematicEditorReducer from './schematicEditorReducer'
import componentPropertiesReducer from './componentPropertiesReducer'
import netlistReducer from './netlistReducer'
import simulationReducer from './simulationReducer'
import datapointReducer from './datapointReducer'
import authReducer from './authReducer'
import saveSchematicReducer from './saveSchematicReducer'
import dashboardReducer from './dashboardReducer'
export default combineReducers({
  schematicEditorReducer,
  componentPropertiesReducer,
  netlistReducer,
  simulationReducer,
  datapointReducer,
  authReducer,
  saveSchematicReducer,
  dashboardReducer
})
