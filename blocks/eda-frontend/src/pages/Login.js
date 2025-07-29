// User Login / Sign In page.
import { useEffect, useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { Link as RouterLink, useLocation } from 'react-router-dom'

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
} from '@material-ui/core'
import { makeStyles } from '@material-ui/core/styles'
import LockOutlinedIcon from '@material-ui/icons/LockOutlined'
import Visibility from '@material-ui/icons/Visibility'
import VisibilityOff from '@material-ui/icons/VisibilityOff'

import { login, authDefault, setAuthErrors, googleLogin, githubLogin } from '../redux/authSlice'
import github from '../static/github-mark.png'
import google from '../static/google.png'

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

function useQuery () {
  return new URLSearchParams(useLocation().search)
}

export default function SignIn (props) {
  const classes = useStyles()
  const authErrors = useSelector(state => state.auth.errors)
  const [errors, setErrors] = useState(authErrors || '')
  
  const dispatch = useDispatch()
  const query = useQuery()
  const homeURL = `${window.location.origin}/#/`

  useEffect(() => {
    const error_description = query.get('error_description')
    if (error_description) {
      dispatch(setAuthErrors(error_description))
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
      <Card className={classes.paper}>
        <Avatar className={classes.avatar}>
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
            className={classes.submit}
          >
            Login
          </Button>
          <Grid container>
            <Grid item xs>
              <Link component={RouterLink} to='/forgotpwd' variant='body2'>
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
