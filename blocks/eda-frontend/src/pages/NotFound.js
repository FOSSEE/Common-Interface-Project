// Page to display Page Not Found (i.e. 404) error.
import { useEffect } from 'react'

import { Container, Typography } from '@mui/material'

export default function NotFound () {
  const name = process.env.REACT_APP_NAME

  useEffect(() => {
    document.title = 'Not Found - ' + name
  }, [name])

  return (
    <Container
      maxWidth='lg'
      sx={{
        px: 0,
        pt: 8,
        pb: 6
      }}
    >
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
