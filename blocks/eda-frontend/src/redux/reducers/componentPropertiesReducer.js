import * as actions from '../actions/actions'
import { ZoomAct } from '../../components/SchematicEditor/Helper/ToolbarTools.js'

const InitialState = {
  block_id: 0,
  name: '',
  parameter_values: {},
  isPropertiesWindowOpen: false,
  compProperties: {},
  displayProperties: {}
}

export default function (state = InitialState, action) {
  switch (action.type) {
    case actions.GET_COMP_PROPERTIES: {
      return {
        ...state,
        block_id: action.payload.block_id,
        name: action.payload.name,
        parameter_values: action.payload.parameter_values,
        isPropertiesWindowOpen: true,
        compProperties: action.payload.compProperties
      }
    }

    case actions.SET_COMP_PROPERTIES: {
      return {
        ...state,
        block_id: action.payload.block_id,
        parameter_values: action.payload.parameter_values,
        isPropertiesWindowOpen: false,
        displayProperties: action.payload.displayProperties
      }
    }

    case actions.CLOSE_COMP_PROPERTIES: {
      ZoomAct()
      return {
        ...state,
        isPropertiesWindowOpen: false
      }
    }

    default:
      return state
  }
}
