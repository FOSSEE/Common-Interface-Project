// Page to display Page Not Found (i.e. 404) error.
import React, { useEffect } from 'react'

import { Container, Typography } from '@mui/material'
import { makeStyles } from '@mui/styles'

const useStyles = makeStyles((theme) => ({
  header: {
    padding: theme.spacing(8, 0, 6)
  }
}))

export default function NotFound () {
  const classes = useStyles()
  const name = process.env.REACT_APP_NAME

  useEffect(() => {
    document.title = 'Not Found - ' + name
  }, [])

  return (
    <Container maxWidth='lg' className={classes.header}>
      <Typography variant='h1' align='center' gutterBottom>
        404 Not Found
      </Typography>
      <Typography
        variant='h4'
        align='center'
        color='textSecondary'
        gutterBottom
      >
        Sorry, Requested page not found
      </Typography>
    </Container>
  )
}
