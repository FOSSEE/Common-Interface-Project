import { combineReducers } from 'redux'
import schematicEditorReducer from './schematicEditorReducer'
import netlistReducer from './netlistReducer'
export default combineReducers({
  schematicEditorReducer,
  netlistReducer
})
