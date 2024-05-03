// This is the JavaScript entry point of react application.
import React from 'react'
import ReactDOM from 'react-dom/client'
import * as serviceWorker from './serviceWorker'
import CssBaseline from '@mui/material/CssBaseline'
import { ThemeProvider } from '@mui/styles'
import theme from './theme'
import './index.css'
import App from './App'
import { Provider } from 'react-redux'
import store from './redux/store'

const root = ReactDOM.createRoot(document.getElementById('root'))

root.render(
  <ThemeProvider theme={theme}>
    {/* CssBaseline kickstart an elegant, consistent, and simple baseline to build upon. */}
    <CssBaseline />
    <Provider store={store}>
       <App />
    </Provider>
  </ThemeProvider>
)

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister()
