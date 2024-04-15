import { combineReducers } from 'redux'
import netlistReducer from './netlistReducer'
import simulationReducer from './simulationReducer'
import authReducer from './authReducer'
import saveSchematicReducer from './saveSchematicReducer'
export default combineReducers({
  netlistReducer,
  simulationReducer,
  authReducer,
  saveSchematicReducer
})
