// Main layout for home page.
import { useEffect } from 'react'

import Button from '@mui/material/Button'
import Typography from '@mui/material/Typography'
import Container from '@mui/material/Container'
import { Link as RouterLink } from 'react-router-dom'
import logo from '../static/favicon.ico'

export default function Home () {
  useEffect(() => {
    document.title = process.env.REACT_APP_NAME
  }, [])

  const typography1 = process.env.REACT_APP_NAME + ' on Cloud'
  const typography2 = 'Online ' + process.env.REACT_APP_NAME + ' Simulator'
  const typography3 = process.env.REACT_APP_DIAGRAM_NAME + ' Editor'
  return (
    <Container
      maxWidth='sm'
      component='main'
      sx={{
        pt: 23,
        pb: 6
      }}
    >
      <center>
        <img src={logo} width='120' height='120' alt='Logo' />
      </center>
      <Typography
        component='h1'
        variant='h2'
        align='center'
        color='textPrimary'
        gutterBottom
      >
        {typography1}
      </Typography>
      <Typography
        variant='h5'
        align='center'
        color='textSecondary'
        component='p'
      >
        {typography2}
        <br />
        <br />
        <Button
          component={RouterLink}
          to='/editor'
          variant='contained'
          size='large'
          color='primary'
        >
          {typography3}
        </Button>
      </Typography>
    </Container>
  )
}
