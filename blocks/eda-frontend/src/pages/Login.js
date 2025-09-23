// User Login / Sign In page.
import { useEffect, useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { Link as RouterLink, useLocation } from 'react-router-dom'

import PropTypes from 'prop-types'

import LockOutlinedIcon from '@mui/icons-material/LockOutlined'
import Visibility from '@mui/icons-material/Visibility'
import VisibilityOff from '@mui/icons-material/VisibilityOff'
import {
  Avatar,
  Box,
  Button,
  Card,
  Checkbox,
  Container,
  FormControlLabel,
  Grid,
  IconButton,
  InputAdornment,
  Link,
  TextField,
  Typography
} from '@mui/material'

import {
  authDefault,
  githubLogin,
  googleLogin,
  login,
  setAuthErrors
} from '../redux/authSlice'
import github from '../static/github-mark.png'
import google from '../static/google.png'

let url = ''

function useQuery () {
  return new URLSearchParams(useLocation().search)
}

export default function SignIn (props) {
  const authErrors = useSelector(state => state.auth.errors)
  const [errors, setErrors] = useState(authErrors || '')
  
  const dispatch = useDispatch()
  const query = useQuery()
  const homeURL = `${window.location.origin}/#/`

  useEffect(() => {
    const error = query.get('error')
    if (error) {
      const errorMessages = {
        'invalid_grant': 'Invalid username or password',
        'access_denied': 'Access denied. Please try again.'
      }

      const errorMessage = errorMessages[error] || 'An unexpected error occurred. Please try again later.'
      dispatch(setAuthErrors(errorMessage))
      window.history.replaceState({}, document.title, '/#/login')
    }
  }, [dispatch, query])

  useEffect(() => {
    setErrors(authErrors || '')
  }, [authErrors])

  useEffect(() => {
    document.title = 'Login - ' + process.env.REACT_APP_NAME
    if (props.location.search !== '') {
      const query = new URLSearchParams(props.location.search)
      url = query.get('url')
      localStorage.setItem('ard_redurl', url)
    } else {
      url = ''
    }

    return () => {
      dispatch(authDefault())
    }
  }, [dispatch, props.location.search])

  const rememberedUsername = localStorage.getItem('rememberedUsername') || ''
  const [username, setUsername] = useState(rememberedUsername)
  const [password, setPassword] = useState('')
  const [showPassword, setShowPassword] = useState(false)
  const [rememberMe, setRememberMe] = useState(!!rememberedUsername)
  const handleClickShowPassword = () => setShowPassword(!showPassword)
  const handleMouseDownPassword = () => setShowPassword(!showPassword)

  // Function call for normal user login.
  const handleLogin = () => {
    if (rememberMe) {
      localStorage.setItem('rememberedUsername', username)
    } else {
      localStorage.removeItem('rememberedUsername')
    }
    dispatch(login({ email: username, password, toUrl: url }))
  }

  // Function call for google oAuth login.
  const handleGoogleLogin = () => {
    const host = window.location.origin
    dispatch(googleLogin(host))
  }

  // Function call for github login.
  const handleGithubLogin = () => {
    const host = window.location.origin
    dispatch(githubLogin(host))
  }

  return (
    <Container component='main' maxWidth='xs'>
      <Card
        sx={{
          mt: 24,
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
          Login | Sign In
        </Typography>

        {/* Display's error messages while logging in */}
        {authErrors && (
          <Typography variant='body1' align='center' style={{ marginTop: '10px' }} color='error'>
            {errors}
          </Typography>
        )}

        <Box
          component='form'
          noValidate
          sx={{
            width: '100%', // Fix IE 11 issue.
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
            value={username}
            onChange={e => setUsername(e.target.value)}
            onFocus={() => setErrors('')}
          />
          <TextField
            variant='outlined'
            margin='normal'
            required
            fullWidth
            name='password'
            label='Password'
            InputProps={{
              endAdornment: (
                <InputAdornment position='end'>
                  <IconButton
                    size='small'
                    aria-label='toggle password visibility'
                    onClick={handleClickShowPassword}
                    onMouseDown={handleMouseDownPassword}
                  >
                    {showPassword ? <Visibility fontSize='small' /> : <VisibilityOff fontSize='small' />}
                  </IconButton>
                </InputAdornment>
              )
            }}
            type={showPassword ? 'text' : 'password'}
            id='password'
            value={password}
            onChange={e => setPassword(e.target.value)}
            onFocus={() => setErrors('')}
            autoComplete='current-password'
          />
          <FormControlLabel
            control={
              <Checkbox
                color='primary'
                checked={rememberMe}
                onChange={e => setRememberMe(e.target.checked)}
              />
            }
            label='Remember me'
          />
          <Button
            fullWidth
            variant='contained'
            color='primary'
            onClick={handleLogin}
            sx={{
              mx: 0,
              my: 2
            }}
          >
            Login
          </Button>
          <Grid container>
            <Grid size="grow" sx={{ m: 'auto' }}>
              <Link component={RouterLink} to='/forgotpwd' variant='body2'>
                Forgot password?
              </Link>
            </Grid>
            <Grid size="grow" sx={{ m: 'auto' }}>
              <Link component={RouterLink} to='/signup' variant='body2'>
                New User? Sign Up
              </Link>
            </Grid>
          </Grid>
        </Box>
        <Typography variant='body1' color='secondary' align='center'>Or</Typography>

        {/* Google oAuth Sign In option */}
        <Button
          fullWidth
          variant='outlined'
          color='primary'
          onClick={handleGoogleLogin}
          sx={{
            mx: 0,
            my: 2
          }}
        >
          <img alt='Google' src={google} height='20' />&emsp; Login With Google
        </Button>
        {/* Github Sign Up option */}
        <Button
          fullWidth
          variant='outlined'
          color='primary'
          onClick={handleGithubLogin}
          sx={{
            mx: 0,
            my: 2
          }}
        >
          <img alt='GitHub' src={github} height='20' />&emsp; Login With GitHub
        </Button>
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

SignIn.propTypes = {
  location: PropTypes.object
}
