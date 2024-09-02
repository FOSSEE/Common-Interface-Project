// User Sign Up / Register page.
import React, { useEffect, useState } from 'react'
import { Link as RouterLink, useHistory } from 'react-router-dom'
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

import { signUp, authDefault, googleLogin, githubLogin } from '../redux/actions/index'

const useStyles = makeStyles((theme) => ({
  paper: {
    marginTop: theme.spacing(20),
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
    margin: theme.spacing(1.5, 0)
  }
}))

export default function SignUp () {
  const classes = useStyles()

  const isRegistered = useSelector(state => state.authReducer.isRegistered)
  const regErrors = useSelector(state => state.authReducer.regErrors)

  const dispatch = useDispatch()
  const homeURL = `${window.location.protocol}\\\\${window.location.host}/`

  useEffect(() => {
    dispatch(authDefault())
    document.title = 'Sign Up - ' + process.env.REACT_APP_NAME
  }, [])

  const history = useHistory()

  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [reenterPassword, setReenterPassword] = useState('')
  const [accept, setAccept] = useState(true)
  const [showPassword, setShowPassword] = useState(false)
  const handleClickShowPassword = () => setShowPassword(!showPassword)
  const handleMouseDownPassword = () => setShowPassword(!showPassword)
  const [showReenterPassword, setShowReenterPassword] = useState(false)
  const handleClickShowReenterPassword = () => setShowReenterPassword(!showReenterPassword)
  const handleMouseDownReenterPassword = () => setShowReenterPassword(!showReenterPassword)

  // Function call for google oAuth sign up.
  const handleGoogleSignup = () => {
    const host = window.location.protocol + '//' + window.location.host
    dispatch(googleLogin(host))
  }

  // Function call for github sign up.
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
          Register | Sign Up
        </Typography>

        {/* Display's error messages while signing in */}
        <Typography variant='body1' align='center' style={{ marginTop: '10px' }} color={isRegistered ? 'secondary' : 'error'}>
          {regErrors}
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
            type='email'
            autoComplete='email'
            value={email}
            onChange={e => setEmail(e.target.value)}
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
          <TextField
            variant='outlined'
            margin='normal'
            required
            fullWidth
            name='reenterPassword'
            label='Reenter Password'
            InputProps={{
              endAdornment: (
                <InputAdornment position='end'>
                  <IconButton
                    size='small'
                    aria-label='toggle password visibility'
                    onClick={handleClickShowReenterPassword}
                    onMouseDown={handleMouseDownReenterPassword}
                  >
                    {showReenterPassword ? <Visibility fontSize='small' /> : <VisibilityOff fontSize='small' />} {/* Handle password visibility */}
                  </IconButton>
                </InputAdornment>
              )
            }}
            type={showReenterPassword ? 'text' : 'password'}
            id='reenterPassword'
            value={reenterPassword}
            onChange={e => setReenterPassword(e.target.value)}
            autoComplete='current-password'
          />
          <FormControlLabel
            control={<Checkbox checked={accept} onChange={e => setAccept(e.target.checked)} color='primary' />}
            label='I accept the Terms of Use & Privacy Policy'
          />
          <Button
            fullWidth
            variant='contained'
            color='primary'
            onClick={() => dispatch(signUp(email, password, reenterPassword, history))}
            className={classes.submit}
            disabled={!accept}
          >
            Sign Up
          </Button>
          <Typography variant='body2' color='secondary' align='center'>Or</Typography>

          {/* Google oAuth Sign Up option */}
          <Button
            fullWidth
            variant='outlined'
            color='primary'
            onClick={handleGoogleSignup}
            className={classes.submit}
          >
            <img alt='Google' src={google} height='20' />&emsp; Sign Up With Google
          </Button>
          {/* Github Sign Up option */}
          <Button
            fullWidth
            variant='outlined'
            color='primary'
            onClick={handleGithubLogin}
            className={classes.submit}
          >
            <img alt='GitHub' src={github} height='20' />&emsp; Sign Up With GitHub
          </Button>
        </form>

        <Grid container>
          <Grid item style={{ margin: 'auto' }}>
            <Link component={RouterLink} to='/login' variant='body2'>
              Already have account? Login
            </Link>
          </Grid>
        </Grid>
      </Card>
      <Button
        fullWidth
        onClick={() => { window.open(homeURL, '_self') }}
        color='default'
        className={classes.submit}
      >
        Back to home
      </Button>
    </Container>
  )
}
