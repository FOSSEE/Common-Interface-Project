import * as actions from './actions'
import api from '../../utils/Api'

// Api call for maintaining user login state throughout the application
export const loadUser = () => (dispatch, getState) => {
  // User Loading
  dispatch({ type: actions.USER_LOADING })

  // Get token from localstorage
  const token = getState().authReducer.token

  // add headers
  const config = {
    headers: {
      'Content-Type': 'application/json'
    }
  }

  // If token available add to headers
  if (token) {
    config.headers.Authorization = `Token ${token}`
  } else {
    dispatch({ type: actions.LOADING_FAILED })
    return
  }

  api.get('auth/users/me/', config)
    .then(
      (res) => {
        if (res.status === 200) {
          dispatch({
            type: actions.USER_LOADED,
            payload: {
              user: res.data
            }
          })
        } else if (res.status >= 400 && res.status < 500) {
          dispatch({
            type: actions.LOGIN_FAILED,
            payload: {
              data: res.data
            }
          })
        }
      }
    )
    .catch((err) => {
      console.error(err)
      dispatch({
        type: actions.LOGIN_FAILED,
        payload: {
          data: {}
        }
      })
    })
}

// Handle api call for user login
export const login = (email, password, toUrl) => {
  const body = {
    password,
    email
  }

  return function (dispatch) {
    const allowedUrls = [
      '/editor'
    ]
    api.post('auth/token/login/', body)
      .then((res) => {
        if (res.status === 200) {
          dispatch({
            type: actions.LOGIN_SUCCESSFUL,
            payload: {
              data: res.data
            }
          })
          if (toUrl === '') {
            dispatch(loadUser())
          } else if (!allowedUrls.includes(toUrl)) {
            console.log('Not redirecting to', toUrl)
            dispatch(loadUser())
          } else {
            window.open(toUrl, '_self')
          }
        } else if (res.status === 400 || res.status === 403 || res.status === 401) {
          const data = res.data
          if (data.email !== undefined) {
            dispatch(loginError(data.email[0]))
          } else if (data.password !== undefined) {
            dispatch(loginError(data.password[0]))
          } else if (data.re_password !== undefined) {
            dispatch(loginError(data.re_password[0]))
          } else if (data.non_field_errors !== undefined) {
            dispatch(loginError(data.non_field_errors[0]))
          } else {
            dispatch(loginError('Enter valid credentials.'))
          }
        } else {
          dispatch({
            type: actions.LOGIN_FAILED,
            payload: {
              data: 'Something went wrong! Login Failed'
            }
          })
        }
      })
      .catch((err) => {
        const res = err.response
        if (res.status === 400 || res.status === 403 || res.status === 401) {
          const data = res.data
          if (data.email !== undefined) {
            dispatch(loginError(data.email[0]))
          } else if (data.password !== undefined) {
            dispatch(loginError(data.password[0]))
          } else if (data.re_password !== undefined) {
            dispatch(loginError(data.re_password[0]))
          } else if (data.non_field_errors !== undefined) {
            dispatch(loginError(data.non_field_errors[0]))
          } else {
            dispatch(loginError('Incorrect Username or Password.'))
          }
        } else {
          dispatch(loginError('Something went wrong! Login Failed'))
        }
      })
  }
}

// Handle api call for user sign up
export const signUp = (email, password, reenterPassword, history) => (dispatch) => {
  const body = {
    email,
    username: email,
    password,
    re_password: reenterPassword
  }

  // add headers
  const config = {
    headers: {
      'Content-Type': 'application/json'
    }
  }

  api.post('auth/users/', body, config)
    .then((res) => {
      if (res.status === 200 || res.status === 201) {
        dispatch({
          type: actions.SIGNUP_SUCCESSFUL,
          payload: {
            data: 'Successfully Signed Up! A verification link has been sent to your email account.'
          }
        })
        // history.push('/login')
      }
    })
    .catch((err) => {
      const res = err.response
      if (res.status === 400 || res.status === 403 || res.status === 401) {
        const data = res.data
        if (data.email !== undefined) {
          dispatch(signUpError(data.email[0]))
        } else if (data.password !== undefined) {
          dispatch(signUpError(data.password[0]))
        } else if (data.re_password !== undefined) {
          dispatch(signUpError(data.re_password[0]))
        } else if (data.non_field_errors !== undefined) {
          dispatch(signUpError(data.non_field_errors[0]))
        } else {
          dispatch(signUpError('Enter valid credentials.'))
        }
      } else {
        dispatch(signUpError('Something went wrong! Registration Failed'))
      }
    })
}

// Handle api call for user logout
export const logout = (history) => (dispatch, getState) => {
  // Get token from localstorage
  const token = getState().authReducer.token

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

  api.post('auth/token/logout/', {}, config)
    .then(
      (res) => {
        if (res.status === 200 || res.status === 204) {
          dispatch({
            type: actions.LOGOUT_SUCCESSFUL,
            payload: {
              user: res.data
            }
          })
          history.push('/login')
        }
      }
    )
    .catch((err) => { console.error(err) })
}

// Redux action for default auth store
export const authDefault = () => (dispatch) => {
  dispatch({ type: actions.DEFAULT_STORE })
}

// Redux action for display login error
const loginError = (message) => (dispatch) => {
  dispatch({
    type: actions.AUTHENTICATION_ERROR,
    payload: {
      data: message
    }
  })
}

// Redux action for display sign up error
const signUpError = (message) => (dispatch) => {
  dispatch({
    type: actions.SIGNUP_FAILED,
    payload: {
      data: message
    }
  })
}

// Api call for Google oAuth login or sign up
export const googleLogin = (host, toUrl) => {
  return function (dispatch) {
    api.get('auth/o/google-oauth2/?redirect_uri=' + host + '/api/auth/google-callback')
      .then((res) => {
        if (res.status === 200) {
          // Open google login page
          window.open(res.data.authorization_url, '_self')
        } else {
          dispatch({
            type: actions.LOGIN_FAILED,
            payload: {
              data: 'Something went wrong! Login Failed'
            }
          })
        }
      })
      .then((res) => { console.log(res) })
      .catch((err) => {
        const res = err.response
        if (res.status === 400 || res.status === 403 || res.status === 401) {
          dispatch(loginError('Incorrect Username or Password.'))
        } else {
          dispatch(loginError('Something went wrong! Login Failed'))
        }
      })
  }
}
