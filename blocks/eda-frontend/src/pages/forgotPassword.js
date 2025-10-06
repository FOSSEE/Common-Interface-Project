import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Link as RouterLink } from 'react-router-dom'

import LockOutlinedIcon from '@mui/icons-material/LockOutlined'
import Avatar from '@mui/material/Avatar'
import Box from '@mui/material/Box'
import Button from '@mui/material/Button'
import Card from '@mui/material/Card'
import Container from '@mui/material/Container'
import Grid from '@mui/material/Grid'
import Link from '@mui/material/Link'
import TextField from '@mui/material/TextField'
import Typography from '@mui/material/Typography'

import { resetPassword, authDefault } from '../redux/authSlice'

export default function ForgotPassword () {
  const dispatch = useDispatch()
  const homeURL = `${window.location.origin}/#/`
  const resetSuccess = useSelector(state => state.auth.resetSuccess)
  const regErrors = useSelector(state => state.auth.regErrors)
  const [isResetSuccess, setIsResetSuccess] = useState(false)

  const [email, setEmail] = useState('')

  useEffect(() => {
    if (resetSuccess) {
      setIsResetSuccess(true)
    }
  }, [resetSuccess])

  useEffect(() => {
    document.title = 'Forgot Password - ' + process.env.REACT_APP_NAME

    return () => {
      dispatch(authDefault())
    }
  }, [dispatch])

  const handleReset = () => {
    if (email) {
      dispatch(resetPassword({ email }))
    }
  }

  return (
    <Container component='main' maxWidth='xs'>
      <Card
        sx={{
          mt: 20,
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          px: 5,
          py: 3
        }}
      >
        <Avatar
          sx={{
            m: 1,
            bgcolor: 'primary.main'
          }}
        >
          <LockOutlinedIcon />
        </Avatar>
        <Typography component='h1' variant='h5'>
          Forgot Password
        </Typography>

        <Typography variant='body1' align='center' style={{ marginTop: '10px' }} color={resetSuccess ? 'secondary' : 'error'}>
          {regErrors}
        </Typography>

        <Box
          component='form'
          noValidate
          sx={{
            width: '100%',
            mt: 1
          }}
        >
          <TextField
            variant='outlined'
            margin='normal'
            required
            fullWidth
            id='email'
            label='Email'
            name='email'
            autoComplete='email'
            value={email}
            onChange={e => setEmail(e.target.value)}
            autoFocus
            disabled={isResetSuccess}
          />
          <Button
            fullWidth
            variant='contained'
            color='primary'
            onClick={handleReset}
            disabled={isResetSuccess}
            sx={{
              mx: 0,
              my: 1.5
            }}
          >
            Send Reset Link
          </Button>

          <Grid container justifyContent='space-between'>
            <Grid size="6">
              <Link component={RouterLink} to='/login' underline='hover' variant='body2'>
                Back to Login
              </Link>
            </Grid>
            <Grid size="6">
              <Link component={RouterLink} to='/signup' underline='hover' variant='body2'>
                New User? Sign Up
              </Link>
            </Grid>
          </Grid>
        </Box>

      </Card>
      <Button
        onClick={() => { window.open(homeURL, '_self') }}
        fullWidth
        color='default'
        sx={{
          mx: 0,
          my: 2
        }}
      >
        Back to home
      </Button>
    </Container>
  )
}
