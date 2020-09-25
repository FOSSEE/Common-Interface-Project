import * as actions from '../actions/actions'
import { ZoomAct } from '../../components/SchematicEditor/Helper/ToolbarTools.js'

const InitialState = {
  id: 0,
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
        id: action.payload.id,
        parameter_values: action.payload.parameter_values,
        isPropertiesWindowOpen: true,
        compProperties: action.payload.compProperties
      }
    }

    case actions.SET_COMP_PROPERTIES: {
      return {
        ...state,
        id: action.payload.id,
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
