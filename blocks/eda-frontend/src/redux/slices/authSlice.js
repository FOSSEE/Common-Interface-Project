import { createSlice } from '@reduxjs/toolkit'
import api from '../../utils/Api'
import * as actions from '../actions/actions'

const token = process.env.REACT_APP_NAME + '_token'
const initialState = {
  token: localStorage.getItem(token),
  isAuthenticated: null,
  isRegistered: null,
  isLoading: false,
  user: null,
  errors: '',
  regErrors: ''
}

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    userLoading (state) {
      state.isLoading = true
    },
    defaultStore (state) {
      state.errors = ''
      state.regErrors = ''
    },
    signUpSuccessful (state, action) {
      state.isRegistered = true
      state.regErrors = action.payload.data
    },
    signUpFailed (state, action) {
      state.isRegistered = false
      state.regErrors = action.payload.data
    },
    userLoaded (state, action) {
      state.isAuthenticated = true
      state.isLoading = false
      state.user = action.payload.user
    },
    loginSuccessful (state, action) {
      localStorage.setItem(token, action.payload.data.auth_token)
      state.token = action.payload.data.auth_token
      state.errors = ''
    },
    loadingFailed (state) {
      state.isLoading = false
    },
    authenticationError (state, action) {
      localStorage.removeItem(token)
      state.errors = action.payload.data
      state.token = null
      state.user = null
      state.isAuthenticated = false
      state.isLoading = false
    },
    logoutSuccessful (state) {
      localStorage.removeItem(token)
      state.token = null
      state.user = null
      state.isAuthenticated = false
      state.isLoading = false
    }
  }
})

export const {
  userLoading,
  defaultStore,
  signUpSuccessful,
  signUpFailed,
  userLoaded,
  loginSuccessful,
  loadingFailed,
  authenticationError,
  logoutSuccessful
} = authSlice.actions

export default authSlice.reducer

export const loadUser = () => (dispatch, getState) => {
  dispatch(userLoading())

  const token = getState().auth?.token

  const config = {
    headers: {
      'Content-Type': 'application/json'
    }
  }

  if (token) {
    config.headers.Authorization = `Token ${token}`
  } else {
    dispatch(loadingFailed())
    return
  }

  api.get('auth/users/me/', config)
    .then((res) => {
      if (res.status === 200) {
        dispatch(userLoaded(res.data))
      } else if (res.status >= 400 && res.status < 500) {
        dispatch(authenticationError({ data: res.data }))
      }
    })
    .catch((err) => {
      console.error(err)
      dispatch(authenticationError({ data: {} }))
    })
}

export const login = (username, password, toUrl) => {
  const body = {
    password,
    username
  }

  return function (dispatch) {
    const allowedUrls = [
      '/editor'
    ]

    api.post('auth/token/login/', body)
      .then((res) => {
        if (res.status === 200) {
          dispatch(loginSuccessful({ data: res.data }))
          if (toUrl === '') {
            dispatch(loadUser())
          } else if (!allowedUrls.includes(toUrl)) {
            console.log('Not redirecting to', toUrl)
            dispatch(loadUser())
          } else {
            window.open(toUrl, '_self')
          }
        } else if (res.status === 400 || res.status === 403 || res.status === 401) {
          dispatch(authenticationError({ data: 'Incorrect Username or Password.' }))
        } else {
          dispatch(authenticationError({ data: 'Something went wrong! Login Failed' }))
        }
      })
      .catch((err) => {
        const res = err.response
        if (res.status === 400 || res.status === 403 || res.status === 401) {
          dispatch(authenticationError({ data: 'Incorrect Username or Password.' }))
        } else {
          dispatch(authenticationError({ data: 'Something went wrong! Login Failed' }))
        }
      })
  }
}

export const signUp = (email, username, password, history) => (dispatch) => {
  const body = {
    email,
    username,
    password
  }

  const config = {
    headers: {
      'Content-Type': 'application/json'
    }
  }

  api.post('auth/users/', body, config)
    .then((res) => {
      if (res.status === 200 || res.status === 201) {
        dispatch(signUpSuccessful({ data: 'Successfully Signed Up! A verification link has been sent to your email account.' }))
      }
    })
    .catch((err) => {
      const res = err.response
      if (res.status === 400 || res.status === 403 || res.status === 401) {
        if (res.data.username !== undefined) {
          if (res.data.username[0].search('already') !== -1 && res.data.username[0].search('exists') !== -1) {
            dispatch(signUpFailed({ data: 'Username Already Taken.' }))
          }
        } else {
          dispatch(signUpFailed({ data: 'Enter Valid Credentials.' }))
        }
      } else {
        dispatch(signUpFailed({ data: 'Something went wrong! Registeration Failed' }))
      }
    })
}

export const logout = (history) => (dispatch, getState) => {
  const token = getState().auth.token

  const config = {
    headers: {
      'Content-Type': 'application/json'
    }
  }

  if (token) {
    config.headers.Authorization = `Token ${token}`
  }

  api.post('auth/token/logout/', {}, config)
    .then((res) => {
      if (res.status === 200 || res.status === 204) {
        dispatch(logoutSuccessful())
        history.push('/login')
      }
    })
    .catch((err) => {
      console.error(err)
    })
}

export const authDefault = () => (dispatch) => {
  dispatch(defaultStore())
}

export const loginError = (message) => (dispatch) => {
  dispatch({
    type: actions.AUTHENTICATION_ERROR,
    payload: {
      data: message
    }
  })
}

export const signupError = (message) => (dispatch) => {
  dispatch({
    type: actions.SIGNUP_FAILED,
    payload: {
      data: message
    }
  })
}

export const googleLogin = (host, toUrl) => {
  return function (dispatch) {
    api.get('auth/o/google-oauth2/?redirect_uri=' + host + '/api/auth/google-callback')
      .then((res) => {
        if (res.status === 200) {
          window.open(res.data.authorization_url, '_self')
        } else {
          dispatch(authenticationError({ data: 'Something went wrong! Login Failed' }))
        }
      })
      .then((res) => { console.log(res) })
      .catch((err) => {
        const res = err.response
        if (res.status === 400 || res.status === 403 || res.status === 401) {
          dispatch(authenticationError({ data: 'Incorrect Username or Password.' }))
        } else {
          dispatch(authenticationError({ data: 'Something went wrong! Login Failed' }))
        }
      })
  }
}
