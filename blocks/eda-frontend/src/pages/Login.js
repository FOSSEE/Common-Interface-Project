// User Login / Sign In page.
import React, { useEffect, useState } from 'react'
import PropTypes from 'prop-types'
import { Link as RouterLink } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'

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
import { makeStyles } from '@mui/styles'

import google from '../static/google.png'
import github from '../static/github-mark.png'

import { login, authDefault, googleLogin, githubLogin } from '../redux/actions/index'

const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(24),
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    padding: theme.spacing(3, 5)
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.primary.main
  },
  form: {
    width: '100%', // Fix IE 11 issue.
    marginTop: theme.spacing(1)
  },
  submit: {
    margin: theme.spacing(2, 0)
  }
}))

let url = ''

export default function SignIn (props) {
  const classes = useStyles()
  const errors = useSelector(state => state.authReducer.errors)

  const dispatch = useDispatch()
  const homeURL = `${window.location.protocol}\\\\${window.location.host}/`

  useEffect(() => {
    dispatch(authDefault())
    document.title = 'Login - ' + process.env.REACT_APP_NAME
    if (props.location.search !== '') {
      const query = new URLSearchParams(props.location.search)
      url = query.get('url')
      localStorage.setItem('ard_redurl', url)
    } else {
      url = ''
    }
  }, [props.location.search])

  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [showPassword, setShowPassword] = useState(false)
  const handleClickShowPassword = () => setShowPassword(!showPassword)
  const handleMouseDownPassword = () => setShowPassword(!showPassword)

  // Function call for normal user login.
  const handleLogin = () => {
    dispatch(login(username, password, url))
  }

  // Function call for google oAuth login.
  const handleGoogleLogin = () => {
    const host = window.location.protocol + '//' + window.location.host
    dispatch(googleLogin(host))
  }

  // Function call for github login.
  const handleGithubLogin = () => {
    const host = window.location.origin
    const toUrl = '' // Add any redirect URL logic if needed
    dispatch(githubLogin(host, toUrl))
  }

  return (
    <Container component='main' maxWidth='xs'>
      <Card className={classes.paper}>
        <Avatar className={classes.avatar}>
          <LockOutlinedIcon />
        </Avatar>

        <Typography component='h1' variant='h5'>
          Login | Sign In
        </Typography>

        {/* Display's error messages while logging in */}
        <Typography variant='body1' align='center' style={{ marginTop: '10px' }} color='error'>
          {errors}
        </Typography>

        <form className={classes.form} noValidate>
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
            className={classes.submit}
          >
            Login
          </Button>
          <Grid container>
            <Grid item xs>
              <Link component={RouterLink} to='#' variant='body2'>
                Forgot password?
              </Link>
            </Grid>
            <Grid item>
              <Link component={RouterLink} to='/signup' variant='body2'>
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
          className={classes.submit}
        >
          <img alt='Google' src={google} height='20' />&emsp; Login With Google
        </Button>
        {/* Github Sign Up option */}
        <Button
          fullWidth
          variant='outlined'
          color='primary'
          onClick={handleGithubLogin}
          className={classes.submit}
        >
          <img alt='GitHub' src={github} height='20' />&emsp; Login With GitHub
        </Button>
      </Card>
      <Button
        onClick={() => { window.open(homeURL, '_self') }}
        fullWidth
        color='default'
        className={classes.submit}
      >
        Back to home
      </Button>
    </Container>
  )
}

SignIn.propTypes = {
  location: PropTypes.object
}
