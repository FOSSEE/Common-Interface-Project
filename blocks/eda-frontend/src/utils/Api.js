// Creating a new instance of axios for custom API config.
import axios from 'axios'

const getCookie = (name) => {
  const match = document.cookie?.split('; ').find(c => c.startsWith(name + '='))
  return match ? decodeURIComponent(match.split('=')[1]) : null
}

const csrftoken = getCookie('csrftoken')

const api = axios.create({
  baseURL: '/api/',
  responseType: 'json',
  xsrfCookieName: 'csrftoken',
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
    'X-CSRFToken': csrftoken
  },
  withCredentials: true
})

const isSessionExpired = () => {
  const expireAt = localStorage.getItem('expire_at')
  return !expireAt || new Date(expireAt) < new Date()
}

const deleteCookie = (name) => {
  document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;'
}

const refreshSession = async () => {
  try {
    const response = await api.get(`simulation/get_session?app_name=${process.env.REACT_APP_NAME}`)
    const sessionId = response.data.session_id
    const expireAt = response.data.expire_at
    localStorage.setItem('session_id', sessionId)
    localStorage.setItem('expire_at', expireAt)
    console.log('Refreshed sessionId', sessionId)
    return sessionId
  } catch (error) {
    console.error('Failed to refresh session', error)
    return null
  }
}

let refreshingSession = null

api.interceptors.request.use(async (config) => {
  // Avoid infinite loop by skipping the interceptor for session refresh requests
  if (config.url.includes('simulation/get_session')) {
    return config
  }

  let sessionId = localStorage.getItem('session_id')

  // Check if session is expired and refresh if necessary
  if (!sessionId || isSessionExpired()) {
    if (!refreshingSession) {
      console.log('Session expired, refreshing...')
      deleteCookie('sessionid')

      refreshingSession = refreshSession().finally(() => {
        refreshingSession = null
      })
    }

    // Refresh session but avoid triggering interceptor again
    sessionId = await refreshingSession
    if (!sessionId) {
      return Promise.reject(new Error('Failed to refresh session'))
    }
  }

  if (sessionId) {
    config.headers['Session-ID'] = sessionId // Custom header for session ID
    console.log('sessionId', sessionId)
  }
  return config
}, (error) => {
  return Promise.reject(error)
})

export default api
