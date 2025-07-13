import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'

import api from '../utils/Api'

const tokenKey = process.env.REACT_APP_NAME + '_token'

const initialState = {
  token: localStorage.getItem(tokenKey),
  isAuthenticated: false,
  isLoggingOut: false,
  isRegistered: false,
  isLoading: false,
  user: null,
  errors: '',
  regErrors: ''
}

// Api call for maintaining user login state throughout the application
export const loadUser = createAsyncThunk(
  'auth/loadUser',
  async (tokenFromLogin, { getState, rejectWithValue }) => {
    // Get token from localstorage
    const token = tokenFromLogin || getState().auth.token
    if (!token) return rejectWithValue('No token found')

    // add headers
    const config = {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${token}`
      }
    }

    try {
      const res = await api.get('auth/users/me/', config)
      if ([200, 201, 204].includes(res.status)) {
        return res.data
      }
      return rejectWithValue(res.data || 'Failed to load user')
    } catch (err) {
      console.log(err)
      const res = err.response
      return rejectWithValue(res?.data || 'Failed to load user')
    }
  })

const loginError = (res, rejectWithValue) => {
  if ([400, 401, 403].includes(res.status)) {
    const data = res.data
    const error = data.email?.[0] ??
      data.password?.[0] ??
      data.non_field_errors?.[0] ??
      'Incorrect Username or Password.'
    return rejectWithValue(error)
  }

  console.error(res)
  return rejectWithValue('Something went wrong! Login Failed')
}

// Handle api call for user login
export const login = createAsyncThunk(
  'auth/login',
  async ({ email, password, toUrl }, { dispatch, rejectWithValue }) => {
    try {
      const allowedUrls = [
        '/editor'
      ]
      const res = await api.post('auth/token/login/', {
        email,
        password
      })
      if ([200, 201, 204].includes(res.status)) {
        const token = res.data.auth_token
        localStorage.setItem(tokenKey, token)
        if (toUrl === '') {
          dispatch(loadUser(token))
        } else if (!allowedUrls.includes(toUrl)) {
          console.log('Not redirecting to', toUrl)
          dispatch(loadUser(token))
        } else {
          window.open(toUrl, '_self')
        }
        return token
      }

      return loginError(res, rejectWithValue)
    } catch (err) {
      console.log(err)
      const res = err.response
      return loginError(res, rejectWithValue)
    }
  })

const signupError = (res, rejectWithValue) => {
  if ([400, 401, 403].includes(res.status)) {
    const data = res.data
    const error = data.email?.[0] ??
      data.username?.[0] ??
      data.password?.[0] ??
      data.re_password?.[0] ??
      data.non_field_errors?.[0] ??
      'Enter valid credentials.'
    return rejectWithValue(error)
  }

  console.error(res)
  return rejectWithValue('Something went wrong! Registration Failed')
}

// Handle api call for user sign up
export const signUp = createAsyncThunk(
  'auth/signUp',
  async ({ email, password, reenterPassword }, { rejectWithValue }) => {
    try {
      const res = await api.post('auth/users/', {
        email,
        username: email,
        password,
        re_password: reenterPassword
      })
      if ([200, 201, 204].includes(res.status)) {
        return 'Successfully Signed Up! A verification link has been sent to your email account.'
      }

      return signupError(res, rejectWithValue)
    } catch (err) {
      console.log(err)
      const res = err.response
      return signupError(res, rejectWithValue)
    }
  })

// Handle api call for user logout
export const logout = createAsyncThunk(
  'auth/logout',
  async (history, { getState }) => {
    try {
      // Get token from localstorage
      const token = getState().auth.token

      // add headers
      const config = {
        headers: {
          'Content-Type': 'application/json'
        }
      }

      // If token available add to headers
      if (token) {
        config.headers.Authorization = `Token ${token}`
      }

      await api.post('auth/token/logout/', {}, config)
      localStorage.removeItem(tokenKey)
      history.push('/login')
      return 'Logout successful'
    } catch (err) {
      console.log(err)
      return 'Logout successful'
    }
  })

// Api call for Google oAuth login or sign up
export const googleLogin = createAsyncThunk(
  'auth/googleLogin',
  async (host, { rejectWithValue }) => {
    try {
      const res = await api.get(`auth/o/google-oauth2/?redirect_uri=${host}/api/auth/google-callback`)
      if ([200, 201, 204].includes(res.status)) {
        // Open google login page
        window.open(res.data.authorization_url, '_self')
        return res.data.authorization_url
      }

      return loginError(res, rejectWithValue)
    } catch (err) {
      console.log(err)
      const res = err.response
      return loginError(res, rejectWithValue)
    }
  })

// Api call for GitHub OAuth login or sign up
export const githubLogin = createAsyncThunk(
  'auth/githubLogin',
  async (host, { rejectWithValue }) => {
    try {
      const res = await api.get(`auth/o/github/?redirect_uri=${host}/api/auth/github-callback`)
      if ([200, 201, 204].includes(res.status)) {
        // Open GitHub login page
        window.open(res.data.authorization_url, '_self')
        return res.data.authorization_url
      }

      return loginError(res, rejectWithValue)
    } catch (err) {
      console.log(err)
      const res = err.response
      return loginError(res, rejectWithValue)
    }
  })

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    authDefault: (state) => {
      state.errors = ''
      state.regErrors = ''
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(loadUser.pending, (state) => {
        state.isLoading = true
        state.isAuthenticated = false
      })
      .addCase(loadUser.fulfilled, (state, action) => {
        state.isLoading = false
        state.isAuthenticated = true
        state.user = action.payload
      })
      .addCase(loadUser.rejected, (state) => {
        state.isLoading = false
        state.isAuthenticated = false
      })
      .addCase(login.pending, (state) => {
        state.isLoading = true
        state.isAuthenticated = false
      })
      .addCase(login.fulfilled, (state, action) => {
        state.isLoading = false
        state.token = action.payload
        state.errors = ''
      })
      .addCase(login.rejected, (state, action) => {
        state.isLoading = false
        state.token = null
        state.user = null
        state.isAuthenticated = false
        state.errors = action.payload || 'Incorrect username or password.'
      })
      .addCase(googleLogin.pending, (state) => {
        state.isLoading = true
        state.isAuthenticated = false
      })
      .addCase(googleLogin.fulfilled, (state) => {
        state.isLoading = false
      })
      .addCase(googleLogin.rejected, (state, action) => {
        state.isLoading = false
        state.token = null
        state.user = null
        state.isAuthenticated = false
        state.errors = action.payload || 'Incorrect username or password.'
      })
      .addCase(githubLogin.pending, (state) => {
        state.isLoading = true
        state.isAuthenticated = false
      })
      .addCase(githubLogin.fulfilled, (state) => {
        state.isLoading = false
      })
      .addCase(githubLogin.rejected, (state, action) => {
        state.isLoading = false
        state.token = null
        state.user = null
        state.isAuthenticated = false
        state.errors = action.payload || 'Incorrect username or password.'
      })
      .addCase(signUp.pending, (state) => {
        state.isLoading = true
        state.isAuthenticated = false
      })
      .addCase(signUp.fulfilled, (state, action) => {
        state.isLoading = false
        state.isRegistered = true
        state.regErrors = action.payload
      })
      .addCase(signUp.rejected, (state, action) => {
        state.isLoading = false
        state.isRegistered = false
        state.regErrors = action.payload
      })
      .addCase(logout.pending, (state) => {
        state.isLoading = true
        state.isLoggingOut = true
      })
      .addCase(logout.fulfilled, (state) => {
        state.isLoading = false
        state.isLoggingOut = false
        state.token = null
        state.user = null
        state.isAuthenticated = false
        state.errors = ''
      })
  }
})

export const {
  authDefault
} = authSlice.actions

export default authSlice.reducer
