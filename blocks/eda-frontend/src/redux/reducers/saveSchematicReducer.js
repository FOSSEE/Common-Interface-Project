import * as actions from '../actions/actions'

const initialState = {
  title: 'Untitled',
  description: '',
  xmlData: null,
  details: {},
  isLoading: false,
  isSaved: null,
  isShared: null
}

export default function saveSchematicReducer (state = initialState, action) {
  switch (action.type) {
    case actions.LOADING_DIAGRAM: {
      return {
        ...state,
        isLoading: action.payload.isLoading
      }
    }

    case actions.SET_SCH_SAVED: {
      return {
        ...state,
        isSaved: true,
        isShared: action.payload.shared,
        details: action.payload
      }
    }

    case actions.SET_SCH_SHARED: {
      return {
        ...state,
        isShared: true,
        details: action.payload
      }
    }

    case actions.CLEAR_DETAILS: {
      return {
        ...state,
        isSaved: null,
        isShared: null,
        details: {}
      }
    }

    case actions.LOAD_GALLERY: {
      return {
        ...state,
        isSaved: null,
        isShared: null,
        details: action.payload
      }
    }

    case actions.SET_SCH_TITLE: {
      return {
        ...state,
        title: action.payload.title
      }
    }

    case actions.SET_SCH_DESCRIPTION: {
      return {
        ...state,
        description: action.payload.description
      }
    }

    case actions.SET_SCH_XML_DATA: {
      return {
        ...state,
        xmlData: action.payload.xmlData
      }
    }

    default:
      return state
  }
}
