import * as actions from '../actions/actions'
import { editorZoomAct } from '../../components/SchematicEditor/Helper/ToolbarTools.js'

const InitialState = {
  block: null,
  name: '',
  parameter_values: {},
  isPropertiesWindowOpen: false,
  compProperties: {},
  displayProperties: {}
}

export default function componentPropertiesReducer (state = InitialState, action) {
  switch (action.type) {
    case actions.GET_COMP_PROPERTIES: {
      return {
        ...state,
        block: action.payload.block,
        name: action.payload.name,
        parameter_values: action.payload.parameter_values,
        isPropertiesWindowOpen: true,
        displayProperties: action.payload.displayProperties,
        compProperties: action.payload.compProperties
      }
    }

    case actions.SET_COMP_PROPERTIES: {
      return {
        ...state,
        block: action.payload.block,
        parameter_values: action.payload.parameter_values,
        isPropertiesWindowOpen: false,
        displayProperties: action.payload.displayProperties
      }
    }

    case actions.CLOSE_COMP_PROPERTIES: {
      editorZoomAct()
      return {
        ...state,
        isPropertiesWindowOpen: false
      }
    }

    default:
      return state
  }
}
