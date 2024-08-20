import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
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

export const loadUser = createAsyncThunk(
  'auth/loadUser',
  async (_, { getState, rejectWithValue }) => {
    const token = getState().auth.token
    if (!token) {
      return rejectWithValue('No token found')
    }

    const config = {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${token}`
      }
    }

    try {
      const res = await api.get('auth/users/me/', config)
      return res.data
    } catch (err) {
      return rejectWithValue(err.response.data || {})
    }
  }
)

export const login = createAsyncThunk(
  'auth/login',
  async ({ email, password, url }, { dispatch, rejectWithValue }) => {
    const body = { email, password }
    const allowedUrls = ['/editor']

    try {
      const res = await api.post('auth/token/login/', body)
      if (res.status === 200) {
        if (url === '') {
          dispatch(loadUser())
        } else if (!allowedUrls.includes(url)) {
          dispatch(loadUser())
        } else {
          window.open(url, '_self')
        }
        return res.data
      }
    } catch (err) {
      const res = err.response
      let errorMessage = 'Something went wrong! Login Failed'
      if (res && res.status >= 400 && res.status < 500) {
        const data = res.data
        if (data.email) {
          errorMessage = data.email[0]
        } else if (data.password) {
          errorMessage = data.password[0]
        } else if (data.non_field_errors) {
          errorMessage = data.non_field_errors[0]
        }
      }
      return rejectWithValue(errorMessage)
    }
  }
)

export const signUp = createAsyncThunk(
  'auth/signUp',
  async ({ email, password, reenterPassword }, { dispatch, rejectWithValue }) => {
    const body = {
      email,
      username: email,
      password,
      re_password: reenterPassword
    }
    const config = {
      headers: {
        'Content-Type': 'application/json'
      }
    }
    try {
      const res = await api.post('auth/users/', body, config)
      if (res.status === 200 || res.status === 201) {
        return 'Successfully Signed Up! A verification link has been sent to your email account.'
      }
    } catch (err) {
      const res = err.response
      let errorMessage = 'Something went wrong! Registration Failed'
      if (res && res.status >= 400 && res.status < 500) {
        const data = res.data
        if (data.email) {
          errorMessage = data.email[0]
        } else if (data.username) {
          errorMessage = data.username[0]
        } else if (data.password) {
          errorMessage = data.password[0]
        } else if (data.re_password) {
          errorMessage = data.re_password[0]
        } else if (data.non_field_errors) {
          errorMessage = data.non_field_errors[0]
        }
      }
      return rejectWithValue(errorMessage)
    }
  }
)

export const logout = createAsyncThunk(
  'auth/logout',
  async (_, { getState, rejectWithValue }) => {
    const token = getState().auth.token

    if (!token) {
      return rejectWithValue('No token found')
    }

    const config = {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${token}`
      }
    }

    try {
      await api.post('auth/token/logout/', {}, config)
      return true
    } catch (err) {
      return rejectWithValue(err.response.data || 'Logout failed')
    }
  }
)

const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    authDefault: (state) => {
      state.errors = ''
      state.regErrors = ''
    },
    setLoginError: (state, action) => {
      state.errors = action.payload
    },
    setSignUpError: (state, action) => {
      state.regErrors = action.payload
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(loadUser.pending, (state) => {
        state.isLoading = true
      })
      .addCase(loadUser.fulfilled, (state, action) => {
        state.isAuthenticated = true
        state.isLoading = false
        state.user = action.payload
      })
      .addCase(loadUser.rejected, (state, action) => {
        state.isLoading = false
        state.errors = action.payload
      })
      .addCase(login.pending, (state) => {
        state.isLoading = true
      })
      .addCase(login.fulfilled, (state, action) => {
        state.token = action.payload.auth_token
        state.errors = ''
        localStorage.setItem(token, action.payload.auth_token)
      })
      .addCase(login.rejected, (state, action) => {
        state.isLoading = false
        state.errors = action.payload
      })
      .addCase(signUp.pending, (state) => {
        state.isLoading = true
      })
      .addCase(signUp.fulfilled, (state, action) => {
        state.isRegistered = true
        state.regErrors = ''
        state.successMessage = action.payload
        state.isLoading = false
      })
      .addCase(signUp.rejected, (state, action) => {
        state.isLoading = false
        state.regErrors = action.payload
      })
      .addCase(logout.pending, (state) => {
        state.isLoading = true
      })
      .addCase(logout.fulfilled, (state) => {
        state.isAuthenticated = false
        state.token = null
        state.user = null
        localStorage.removeItem(token)
      })
      .addCase(logout.rejected, (state, action) => {
        state.isLoading = false
        state.errors = action.payload
      })
  }
})

export const googleLogin = (host, url) => {
  return function (dispatch) {
    api.get('auth/o/google-oauth2/?redirect_uri=' + host + '/api/auth/google-callback')
      .then((res) => {
        if (res.status === 200) {
          window.open(res.data.authorization_url, '_self')
        } else {
          dispatch(setLoginError({ data: 'Something went wrong! Login Failed' }))
        }
      })
      .catch((err) => {
        const res = err.response
        if (res.status === 400 || res.status === 403 || res.status === 401) {
          dispatch(setLoginError({ data: 'Incorrect Username or Password.' }))
        } else {
          dispatch(setLoginError({ data: 'Something went wrong! Login Failed' }))
        }
      })
  }
}

// Api call for GitHub OAuth login or sign up
export const githubLogin = (host, toUrl) => {
  return function (dispatch) {
    api.get('auth/o/github/?redirect_uri=' + host + '/api/auth/github-callback')
      .then((res) => {
        if (res.status === 200) {
          // Open GitHub login page
          window.open(res.data.authorization_url, '_self')
        } else {
          dispatch(setLoginError('Something went wrong! Login Failed'))
        }
      })
      .catch((err) => {
        const res = err.response
        if (res && (res.status === 400 || res.status === 403 || res.status === 401)) {
          dispatch(setLoginError('Incorrect Username or Password.'))
        } else {
          dispatch(setLoginError('Something went wrong! Login Failed'))
        }
      })
  }
}

export const { authDefault, setLoginError, setSignUpError } = authSlice.actions
export default authSlice.reducer
