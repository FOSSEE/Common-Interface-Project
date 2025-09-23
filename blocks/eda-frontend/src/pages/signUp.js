// User Sign Up / Register page.
import { useEffect, useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { Link as RouterLink } from 'react-router-dom'

import LockOutlinedIcon from '@mui/icons-material/LockOutlined'
import Visibility from '@mui/icons-material/Visibility'
import VisibilityOff from '@mui/icons-material/VisibilityOff'
import Avatar from '@mui/material/Avatar'
import Box from '@mui/material/Box'
import Button from '@mui/material/Button'
import Card from '@mui/material/Card'
import Checkbox from '@mui/material/Checkbox'
import Container from '@mui/material/Container'
import FormControlLabel from '@mui/material/FormControlLabel'
import Grid from '@mui/material/Grid'
import IconButton from '@mui/material/IconButton'
import InputAdornment from '@mui/material/InputAdornment'
import Link from '@mui/material/Link'
import TextField from '@mui/material/TextField'
import Typography from '@mui/material/Typography'

import {
  authDefault,
  githubLogin,
  googleLogin,
  signUp
} from '../redux/authSlice'
import github from '../static/github-mark.png'
import google from '../static/google.png'

export default function SignUp () {
  const isRegistered = useSelector(state => state.auth.isRegistered)
  const regErrors = useSelector(state => state.auth.regErrors)
  const [errors, setErrors] = useState(regErrors || '')
  const [isSignupSuccess, setIsSignupSuccess] = useState(false)

  useEffect(() => {
    if (isRegistered) {
      setIsSignupSuccess(true)
    }
  }, [isRegistered])

  const dispatch = useDispatch()
  const homeURL = `${window.location.origin}/#/`

  useEffect(() => {
    setErrors(regErrors || '')
  }, [regErrors])

  useEffect(() => {
    document.title = 'Sign Up - ' + process.env.REACT_APP_NAME

    return () => {
      dispatch(authDefault())
    }
  }, [dispatch])

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
    const host = window.location.origin
    dispatch(googleLogin(host))
  }

  // Function call for github sign up.
  const handleGithubSignup = () => {
    const host = window.location.origin
    dispatch(githubLogin(host))
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
          Register | Sign Up
        </Typography>

        {/* Display's error messages while signing in */}
        {regErrors && (
          <Typography variant='body1' align='center' style={{ marginTop: '10px' }} color={isRegistered ? 'secondary' : 'error'}>
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
            type='email'
            autoComplete='email'
            value={email}
            onChange={e => setEmail(e.target.value)}
            onFocus={() => setErrors('')}
            disabled={isSignupSuccess}
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
            onFocus={() => setErrors('')}
            autoComplete='current-password'
            disabled={isSignupSuccess}
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
            onFocus={() => setErrors('')}
            autoComplete='current-password'
            disabled={isSignupSuccess}
          />
          <FormControlLabel
            control={<Checkbox checked={accept} onChange={e => setAccept(e.target.checked)} color='primary' disabled={isSignupSuccess} />}
            label='I accept the Terms of Use & Privacy Policy'
          />
          <Button
            fullWidth
            variant='contained'
            color='primary'
            onClick={() => dispatch(signUp({ email, password, reenterPassword }))}
            disabled={!accept}
            sx={{
              mx: 0,
              my: 2
            }}
          >
            Sign Up
          </Button>
          <Grid container justifyContent='space-between'>
            <Grid size="6">
              <Link component={RouterLink} to='/login' underline='hover' variant='body2'>
                Back to Login
              </Link>
            </Grid>
            <Grid size="6">
              <Link component={RouterLink} to='/forgotpwd' underline='hover' variant='body2'>
                Forgot password?
              </Link>
            </Grid>
          </Grid>
          <Typography variant='body1' color='secondary' align='center'>Or</Typography>

          {/* Google oAuth Sign Up option */}
          <Button
            fullWidth
            variant='outlined'
            color='primary'
            onClick={handleGoogleSignup}
            sx={{
              mx: 0,
              my: 1.5
            }}
          >
            <img alt='Google' src={google} height='20' />&emsp; Sign Up With Google
          </Button>
          {/* Github Sign Up option */}
          <Button
            fullWidth
            variant='outlined'
            color='primary'
            onClick={handleGithubSignup}
            sx={{
              mx: 0,
              my: 1.5
            }}
          >
            <img alt='GitHub' src={github} height='20' />&emsp; Sign Up With GitHub
          </Button>
        </Box>

      </Card>
      <Button
        fullWidth
        onClick={() => { window.open(homeURL, '_self') }}
        color='default'
        sx={{
          mx: 0,
          my: 1.5
        }}
      >
        Back to home
      </Button>
    </Container>
  )
}
