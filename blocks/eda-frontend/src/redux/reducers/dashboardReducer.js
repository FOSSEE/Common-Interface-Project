import * as actions from '../actions/actions'

const InitialState = {
  schematics: [],
  gallery: []
}

export default function dashboardReducer (state = InitialState, action) {
  switch (action.type) {
    case actions.FETCH_SCHEMATICS: {
      return {
        ...state,
        schematics: action.payload
      }
    }

    case actions.FETCH_GALLERY: {
      return {
        ...state,
        gallery: action.payload
      }
    }

    default:
      return state
  }
}
