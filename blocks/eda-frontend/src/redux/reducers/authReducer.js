import * as actions from '../actions/actions'

const token = process.env.REACT_APP_NAME + '_token';
const initialState = {
  token: localStorage.getItem(token),
  isAuthenticated: null,
  isRegistered: null,
  isLoading: false,
  user: null,
  errors: '',
  regErrors: ''
}

export default function (state = initialState, action) {
  switch (action.type) {
    case actions.USER_LOADING: {
      return {
        ...state,
        isLoading: true
      }
    }

    case actions.DEFAULT_STORE: {
      return {
        ...state,
        errors: '',
        regErrors: ''
      }
    }

    case actions.SIGNUP_SUCCESSFUL: {
      return {
        ...state,
        isRegistered: true,
        regErrors: action.payload.data
      }
    }

    case actions.SIGNUP_FAILED: {
      return {
        ...state,
        isRegistered: false,
        regErrors: action.payload.data
      }
    }

    case actions.USER_LOADED: {
      return {
        ...state,
        isAuthenticated: true,
        isLoading: false,
        user: action.payload.user
      }
    }

    case actions.LOGIN_SUCCESSFUL: {
      localStorage.setItem(token, action.payload.data.auth_token)
      return {
        ...state,
        token: action.payload.data.auth_token,
        // ...action.payload.data,
        // isAuthenticated: true,
        // isLoading: false,
        errors: ''
      }
    }

    case actions.LOADING_FAILED: {
      return {
        ...state,
        isLoading: false
      }
    }

    case actions.AUTHENTICATION_ERROR:
    case actions.LOGIN_FAILED:
    case actions.LOGOUT_SUCCESSFUL: {
      localStorage.removeItem(token)
      return {
        ...state,
        errors: action.payload.data,
        token: null,
        user: null,
        isAuthenticated: false,
        isLoading: false
      }
    }

    default:
      return state
  }
}
