// Creating a new instance of axios for custom API config.
import axios from 'axios'

const getCookie = (name) => {
  let cookieValue = null

  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';')
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim()

      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1))

        break
      }
    }
  }

  return cookieValue
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

api.interceptors.request.use((config) => {
  const sessionId = localStorage.getItem('session_id')
  if (sessionId) {
    config.headers['Session-ID'] = sessionId // Custom header for session ID
    console.log('sessionId', sessionId)
  }
  return config
}, (error) => {
  return Promise.reject(error)
})

export default api
