import React, { useEffect } from 'react'
import PropTypes from 'prop-types'
import { HashRouter, Switch, Route, Redirect } from 'react-router-dom'
import { useSelector, useDispatch } from 'react-redux'

import CircularProgress from '@mui/material/CircularProgress'

import Navbar from './components/Shared/Navbar'
import Home from './pages/Home'
import Login from './pages/Login'
import NotFound from './pages/NotFound'
import SchematicEditor from './pages/SchematicEditor'
import Gallery from './pages/Gallery'
import Dashboard from './pages/Dashboard'
import SignUp from './pages/signUp'

import { loadUser } from './redux/actions/index'

// Controls Private routes, this are accessible for authenticated users.  [ e.g : dashboard ]
// and restricted routes disabled for authenticated users. [ e.g : login , signup ]
function PrivateRoute ({ component: Component, ...rest }) {
  const isAuthenticated = useSelector(state => state.authReducer.isAuthenticated)
  const isLoading = useSelector(state => state.authReducer.isLoading)
  const dispatch = useDispatch()

  useEffect(() => dispatch(loadUser()), [])

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
function PublicRoute ({ component: Component, restricted, nav, ...rest }) {
  const isAuthenticated = useSelector(state => state.authReducer.isAuthenticated)
  const isLoading = useSelector(state => state.authReducer.isLoading)
  const dispatch = useDispatch()

  useEffect(() => dispatch(loadUser()), [])

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

function App () {
  return (
    // Handles Routing for an application
    <HashRouter>
      <Switch>
        <PublicRoute exact path='/login' restricted nav={false} component={Login} />
        <PublicRoute exact path='/signup' restricted nav={false} component={SignUp} />
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
