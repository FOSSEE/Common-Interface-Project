import { combineReducers } from 'redux'
import schematicEditorReducer from './schematicEditorReducer'
import componentPropertiesReducer from './componentPropertiesReducer'
import netlistReducer from './netlistReducer'
import saveSchematicReducer from './saveSchematicReducer'
import dashboardReducer from './dashboardReducer'
export default combineReducers({
  schematicEditorReducer,
  componentPropertiesReducer,
  netlistReducer,
  saveSchematicReducer,
  dashboardReducer
})
