// User Login / Sign In page.
import { useEffect, useState } from 'react'
import PropTypes from 'prop-types'

import {
  Avatar,
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
import LockOutlinedIcon from '@mui/icons-material/LockOutlined'
import Visibility from '@mui/icons-material/Visibility'
import VisibilityOff from '@mui/icons-material/VisibilityOff'
import { Link as RouterLink } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'
import { login, authDefault, googleLogin, githubLogin } from '../redux/authSlice'
import google from '../static/google.png'
import github from '../static/github-mark.png'

let url = ''

export default function SignIn (props) {
  const errors = useSelector(state => state.auth.errors)

  const dispatch = useDispatch()
  const homeURL = `${window.location.origin}/#/`

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

  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [showPassword, setShowPassword] = useState(false)
  const handleClickShowPassword = () => setShowPassword(!showPassword)
  const handleMouseDownPassword = () => setShowPassword(!showPassword)

  // Function call for normal user login.
  const handleLogin = () => {
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
            bgcolor: theme => theme.palette.primary.main
          }}
        >
          <LockOutlinedIcon />
        </Avatar>

        <Typography component='h1' variant='h5'>
          Login | Sign In
        </Typography>

        {/* Display's error messages while logging in */}
        <Typography variant='body1' align='center' style={{ marginTop: '10px' }} color='error'>
          {errors}
        </Typography>

        <form
          noValidate
          sx={{
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
            autoFocus
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
                    {showPassword ? <Visibility fontSize='small' /> : <VisibilityOff fontSize='small' />} {/* Handle password visibility */}
                  </IconButton>
                </InputAdornment>
              )
            }}
            type={showPassword ? 'text' : 'password'}
            id='password'
            value={password}
            onChange={e => setPassword(e.target.value)}
            autoComplete='current-password'
          />
          <FormControlLabel
            control={<Checkbox value='remember' color='primary' />}
            label='Remember me'
          />
          <Button
            fullWidth
            variant='contained'
            color='primary'
            onClick={handleLogin}
            sx={{
              my: 2
            }}
          >
            Login
          </Button>
          <Grid container>
            <Grid item xs>
              <Link underline='hover' component={RouterLink} to='#' variant='body2'>
                Forgot password?
              </Link>
            </Grid>
            <Grid item>
              <Link underline='hover' component={RouterLink} to='/signup' variant='body2'>
                New User? Sign Up
              </Link>
            </Grid>
          </Grid>
        </form>
        <Typography variant='body1' color='secondary' align='center'>Or</Typography>

        {/* Google oAuth Sign In option */}
        <Button
          fullWidth
          variant='outlined'
          color='primary'
          onClick={handleGoogleLogin}
          sx={{
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
