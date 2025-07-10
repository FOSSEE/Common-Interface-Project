import { useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { HashRouter, Switch, Route, Redirect } from 'react-router-dom'

import PropTypes from 'prop-types'

import CircularProgress from '@material-ui/core/CircularProgress'

import Navbar from './components/Shared/Navbar'
import Dashboard from './pages/Dashboard'
import ForgotPassword from './pages/forgotPassword'
import Gallery from './pages/Gallery'
import Home from './pages/Home'
import Login from './pages/Login'
import NotFound from './pages/NotFound'
import SchematicEditor from './pages/SchematicEditor'
import SignUp from './pages/signUp'
import { loadUser } from './redux/authSlice'
import api from './utils/Api'

// Controls Private routes, this are accessible for authenticated users.  [ e.g : dashboard ]
// and restricted routes disabled for authenticated users. [ e.g : login , signup ]
const PrivateRoute = ({ component: Component, ...rest }) => {
  const isAuthenticated = useSelector(state => state.auth.isAuthenticated)
  const isLoading = useSelector(state => state.auth.isLoading)

  return (
    <Route
      {...rest} render={props => {
        if (isLoading) {
          return <CircularProgress style={{ margin: '50vh 50vw' }} />
        } else if (!isAuthenticated) {
          return <Redirect to='/login' />
        } else {
          return <Component {...props} />
        }
      }}
    />
  )
}

PrivateRoute.propTypes = {
  component: PropTypes.func
}

// Public routes accessible to all users. [ e.g. editor, gallery ]
const PublicRoute = ({ component: Component, restricted, nav, ...rest }) => {
  const isAuthenticated = useSelector(state => state.auth.isAuthenticated)
  const isLoading = useSelector(state => state.auth.isLoading)

  return (
    <Route
      {...rest} render={props => {
        if (isLoading) {
          return <CircularProgress style={{ margin: '50vh 50vw' }} />
        } else if (isAuthenticated && restricted) {
          return <Redirect to='/dashboard' />
        } else if (nav) {
          return (<><Navbar /><Component {...props} /></>)
        } else {
          return <Component {...props} />
        }
      }}
    />
  )
}

PublicRoute.propTypes = {
  component: PropTypes.func,
  nav: PropTypes.bool,
  restricted: PropTypes.bool
}

const App = () => {
  const dispatch = useDispatch()

  useEffect(() => {
    const initializeCsrf = async () => {
      try {
        await api.get('init')
      } catch (err) {
        console.error('Failed to initialize csrf:', err)
      }
    }

    initializeCsrf()
  }, [])

  useEffect(() => {
    dispatch(loadUser())
  }, [dispatch])

  return (
    // Handles Routing for an application
    <HashRouter>
      <Switch>
        <PublicRoute exact path='/login' restricted nav={false} component={Login} />
        <PublicRoute exact path='/signup' restricted nav={false} component={SignUp} />
        <PublicRoute exact path='/forgotpwd' restricted nav={false} component={ForgotPassword} />
        <PublicRoute exact path='/' restricted={false} nav component={Home} />
        {localStorage.getItem(process.env.REACT_APP_NAME + '_token') !== null
          ? <PublicRoute exact path='/editor' restricted={false} nav={false} component={SchematicEditor} />
          : <Route path='/editor' component={SchematicEditor} />}
        <PublicRoute exact path='/gallery' restricted={false} nav component={Gallery} />
        <PrivateRoute path='/dashboard' component={Dashboard} />
        <PublicRoute restricted={false} nav component={NotFound} />
      </Switch>
    </HashRouter>
  )
}

export default App
