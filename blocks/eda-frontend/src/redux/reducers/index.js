import { combineReducers } from 'redux'
import authReducer from './authReducer'
import saveSchematicReducer from './saveSchematicReducer'
export default combineReducers({
  authReducer,
  saveSchematicReducer
})
