// authSlice.js
import { createSlice } from '@reduxjs/toolkit'
import api from '../../utils/Api'

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
    authError (state, action) {
      localStorage.removeItem(token)
      state.errors = action.payload.data
      state.token = null
      state.user = null
      state.isAuthenticated = false
      state.isLoading = false
    }
  }
})

// Action creators
export const {
  userLoading,
  defaultStore,
  signUpSuccessful,
  signUpFailed,
  userLoaded,
  loginSuccessful,
  loadingFailed,
  authError
} = authSlice.actions

// Async action creators
export const loadUser = () => async (dispatch, getState) => {
  dispatch(userLoading())

  const token = getState().auth.token

  const config = {
    headers: {
      'Content-Type': 'application/json'
    }
  }

  if (token) {
    config.headers.Authorization = `Token ${token}`
  } else {
    dispatch(authError('Something went wrong! Login Failed'))
    return
  }

  try {
    const res = await api.get('auth/users/me/', config)
    if (res.status === 200) {
      dispatch(userLoaded({ user: res.data }))
    } else if (res.status >= 400 && res.status < 500) {
      dispatch(authError('Incorrect Username or Password.'))
    }
  } catch (err) {
    console.error(err)
    dispatch(authError('Something went wrong! Login Failed'))
  }
}

export const login = (username, password, toUrl) => async (dispatch) => {
  const body = {
    password,
    username
  }

  const allowedUrls = ['/editor']

  try {
    const res = await api.post('auth/token/login/', body)
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
      dispatch(authError('Incorrect Username or Password.'))
    } else {
      dispatch(authError('Something went wrong! Login Failed'))
    }
  } catch (err) {
    const res = err.response
    if (res.status === 400 || res.status === 403 || res.status === 401) {
      dispatch(authError('Incorrect Username or Password.'))
    } else {
      dispatch(authError('Something went wrong! Login Failed'))
    }
  }
}

export const signUp =
  (email, username, password, history) => async (dispatch) => {
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

    try {
      const res = await api.post('auth/users/', body, config)
      if (res.status === 200 || res.status === 201) {
        dispatch(signUpSuccessful({ data: 'Successfully Signed Up!' }))
        // history.push('/login')
      }
    } catch (err) {
      const res = err.response
      if (res.status === 400 || res.status === 403 || res.status === 401) {
        dispatch(signUpError(res.data.username[0]))
      } else {
        dispatch(signUpError('Something went wrong! Registeration Failed'))
      }
    }
  }

export const logout = (history) => async (dispatch, getState) => {
  const token = getState().auth.token

  const config = {
    headers: {
      'Content-Type': 'application/json'
    }
  }

  if (token) {
    config.headers.Authorization = `Token ${token}`
  }

  try {
    const res = await api.post('auth/token/logout/', {}, config)
    if (res.status === 200 || res.status === 204) {
      dispatch(authError({ data: null }))
      history.push('/login')
    }
  } catch (err) {
    console.error(err)
  }
}

// Redux slice for default auth store
export const authDefault = () => (dispatch) => {
  dispatch(defaultStore())
}

// Redux action for display login error
const loginError = (message) => (dispatch) => {
  dispatch(authError({ data: message }))
}

// Redux action for display sign up error
const signUpError = (message) => (dispatch) => {
  dispatch(signUpFailed({ data: message }))
}

// Api call for Google oAuth login or sign up
export const googleLogin = (host, toUrl) => async (dispatch) => {
  try {
    const res = await api.get(`auth/o/google-oauth2/?redirect_uri=${host}/api/auth/google-callback`)
    if (res.status === 200) {
      // Open google login page
      window.open(res.data.authorization_url, '_self')
    } else {
      dispatch(authError('Something went wrong! Login Failed'))
    }
  } catch (err) {
    const res = err.response
    if (res.status === 400 || res.status === 403 || res.status === 401) {
      dispatch(loginError('Incorrect Username or Password.'))
    } else {
      dispatch(loginError('Something went wrong! Login Failed'))
    }
  }
}

export default authSlice.reducer
