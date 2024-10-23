import { red } from '@mui/material/colors'
import { createTheme } from '@mui/material/styles'

// A custom Material UI theme for this application
const theme = createTheme({
  palette: {
    primary: {
      main: '#556cd6'
    },
    secondary: {
      main: '#19857b'
    },
    error: {
      main: red.A400
    },
    background: {
      default: '#fff'
    }
  }
})

export default theme
