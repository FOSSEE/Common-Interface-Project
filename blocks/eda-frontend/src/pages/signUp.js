// User Sign Up / Register page.
import { useEffect, useState } from 'react'
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
import { signUp, authDefault, googleLogin, githubLogin } from '../redux/authSlice'
import google from '../static/google.png'
import github from '../static/github-mark.png'

export default function SignUp () {
  const isRegistered = useSelector(state => state.auth.isRegistered)
  const regErrors = useSelector(state => state.auth.regErrors)

  const dispatch = useDispatch()
  const homeURL = `${window.location.origin}/#/`

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
        <Typography variant='body1' align='center' style={{ marginTop: '10px' }} color={isRegistered ? 'secondary' : 'error'}>
          {regErrors}
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
            onClick={() => dispatch(signUp({ email, password, reenterPassword }))}
            sx={{ my: 1.5 }}
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
            sx={{ my: 1.5 }}
          >
            <img alt='Google' src={google} height='20' />&emsp; Sign Up With Google
          </Button>
          {/* Github Sign Up option */}
          <Button
            fullWidth
            variant='outlined'
            color='primary'
            onClick={handleGithubSignup}
            sx={{ my: 1.5 }}
          >
            <img alt='GitHub' src={github} height='20' />&emsp; Sign Up With GitHub
          </Button>
        </form>

        <Grid container>
          <Grid item style={{ margin: 'auto' }}>
            <Link underline='hover' component={RouterLink} to='/login' variant='body2'>
              Already have account? Login
            </Link>
          </Grid>
        </Grid>
      </Card>
      <Button
        fullWidth
        onClick={() => { window.open(homeURL, '_self') }}
        color='default'
        sx={{ my: 1.5 }}
      >
        Back to home
      </Button>
    </Container>
  )
}
