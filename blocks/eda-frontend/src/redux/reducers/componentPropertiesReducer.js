import * as actions from '../actions/actions'
import { editorZoomAct } from '../../components/SchematicEditor/Helper/ToolbarTools'

const InitialState = {
  block: null,
  name: '',
  parameter_values: {},
  errorFields: {},
  isPropertiesWindowOpen: false,
  compProperties: [],
  displayProperties: {},
  isLoading: false
}

export default function componentPropertiesReducer (state = InitialState, action) {
  switch (action.type) {
    case actions.LOADING_GET_COMP_PROPERTIES: {
      return {
        ...state,
        name: action.payload.name,
        isPropertiesWindowOpen: true,
        compProperties: undefined,
        isLoading: action.payload.isLoading
      }
    }

    case actions.GET_COMP_PROPERTIES: {
      return {
        ...state,
        block: action.payload.block,
        name: action.payload.name,
        parameter_values: action.payload.parameter_values,
        errorFields: action.payload.errorFields,
        isPropertiesWindowOpen: true,
        displayProperties: action.payload.displayProperties,
        compProperties: action.payload.compProperties,
        isLoading: false
      }
    }

    case actions.LOADING_SET_COMP_PROPERTIES: {
      return {
        ...state,
        isPropertiesWindowOpen: true,
        isLoading: action.payload.isLoading
      }
    }

    case actions.SET_COMP_PROPERTIES: {
      return {
        ...state,
        block: action.payload.block,
        parameter_values: action.payload.parameter_values,
        errorFields: action.payload.errorFields,
        isPropertiesWindowOpen: false,
        displayProperties: action.payload.displayProperties,
        isLoading: false
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
