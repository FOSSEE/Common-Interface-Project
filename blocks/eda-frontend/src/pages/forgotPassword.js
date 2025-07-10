import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Link as RouterLink } from 'react-router-dom'

import {
  Avatar,
  Button,
  Card,
  Container,
  Grid,
  Link,
  TextField,
  Typography
} from '@material-ui/core'
import { makeStyles } from '@material-ui/core/styles'
import LockOutlinedIcon from '@material-ui/icons/LockOutlined'

import { resetPassword, authDefault } from '../redux/authSlice'

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
    width: '100%',
    marginTop: theme.spacing(1)
  },
  submit: {
    margin: theme.spacing(1.5, 0)
  }
}))

export default function ForgotPassword () {
  const classes = useStyles()
  const dispatch = useDispatch()
  const resetSuccess = useSelector(state => state.auth.resetSuccess)
  const regErrors = useSelector(state => state.auth.regErrors)

  const [email, setEmail] = useState('')

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
      <Card className={classes.paper}>
        <Avatar className={classes.avatar}>
          <LockOutlinedIcon />
        </Avatar>
        <Typography component='h1' variant='h5'>
          Forgot Password
        </Typography>

        <Typography variant='body1' align='center' style={{ marginTop: '10px' }} color={resetSuccess ? 'secondary' : 'error'}>
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
            autoComplete='email'
            value={email}
            onChange={e => setEmail(e.target.value)}
            autoFocus
          />
          <Button
            fullWidth
            variant='contained'
            color='primary'
            onClick={handleReset}
            className={classes.submit}
          >
            Send Reset Link
          </Button>
        </form>

        <Grid container>
          <Grid item xs>
            <Link component={RouterLink} to='/login' variant='body2'>
              Back to Login
            </Link>
          </Grid>
        </Grid>
      </Card>
    </Container>
  )
}
