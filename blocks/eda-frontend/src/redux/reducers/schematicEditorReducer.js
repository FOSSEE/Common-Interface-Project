import * as actions from '../actions/actions'

const InitialState = {
  isSimulate: false,
  libraries: [],
  collapse: {},
  components: {}
}

export default function schematicEditorReducer (state = InitialState, action) {
  switch (action.type) {
    case actions.FETCH_LIBRARIES: {
    // Add 'open' parameter to track open/close state of collapse
      const collapse = {}
      const components = {}
      action.payload.forEach(element => {
        collapse[element.id] = false
        components[element.id] = []
      })
      return { ...state, libraries: action.payload, collapse, components }
    }

    case actions.TOGGLE_COLLAPSE: {
      const existingState = state.collapse[action.payload.id]
      const newCollapse = Object.keys(state.collapse).reduce(function (accObj, parseObj) {
        accObj[parseObj] = false
        return accObj
      }, {})
      newCollapse[action.payload.id] = !existingState
      Object.assign(state.collapse, newCollapse)
      return { ...state, collapse: { ...state.collapse, newCollapse } }
    }

    case actions.FETCH_COMPONENTS: {
      const newComponents = state.components
      newComponents[action.payload.id] = action.payload.components
      Object.assign(state.components, newComponents)
      return { ...state, components: { ...state.components, newComponents } }
    }

    case actions.COMPONENT_IMAGES: {
      const componentImages = action.payload.component_images
      return { ...state, component_images: componentImages }
    }

    case actions.TOGGLE_SIMULATE: {
      return { ...state, isSimulate: !state.isSimulate }
    }

    default:
      return state
  }
}
