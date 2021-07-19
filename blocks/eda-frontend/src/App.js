import React, { useEffect } from 'react'
import { HashRouter, Switch, Route, Redirect } from 'react-router-dom'
import CircularProgress from '@material-ui/core/CircularProgress'

import Navbar from './components/Shared/Navbar'
import Home from './pages/Home'
import Login from './pages/Login'
import NotFound from './pages/NotFound'
import SchematicEditor from './pages/SchematicEditor'

import Simulator from './pages/Simulator'
import Gallery from './pages/Gallery'
import Dashboard from './pages/Dashboard'
import SignUp from './pages/signUp'

import { useSelector, useDispatch } from 'react-redux'
import { loadUser } from './redux/actions/index'

// Controls Private routes, this are accessible for authenticated users.  [ e.g : dashboard ]
// and restricted routes disabled for authenticated users. [ e.g : login , signup ]
function PrivateRoute ({ component: Component, ...rest }) {
  const auth = useSelector(state => state.authReducer)
  const dispatch = useDispatch()

  useEffect(() => dispatch(loadUser()), [dispatch])

  return <Route {...rest} render={props => {
    if (auth.isLoading) {
      return <CircularProgress style={{ margin: '50vh 50vw' }} />
    } else if (!auth.isAuthenticated) {
      return <Redirect to="/login" />
    } else {
      return <Component {...props} />
    }
  }} />
}

// Public routes accessible to all users. [ e.g. editor, gallery ]
function PublicRoute ({ component: Component, restricted, nav, ...rest }) {
  const auth = useSelector(state => state.authReducer)
  const dispatch = useDispatch()

  useEffect(() => dispatch(loadUser()), [dispatch])

  return <Route {...rest} render={props => {
    if (auth.isLoading) {
      return <CircularProgress style={{ margin: '50vh 50vw' }} />
    } else if (auth.isAuthenticated && restricted) {
      return <Redirect to="/dashboard" />
    } else if (nav) {
      return (<><Navbar /><Component {...props} /></>)
    } else {
      return <Component {...props} />
    }
  }} />
}

function App () {
  return (
    // Handles Routing for an application
    <HashRouter>
      <Switch>
        <PublicRoute exact path="/login" restricted={true} nav={false} component={Login} />
        <PublicRoute exact path="/signup" restricted={true} nav={false} component={SignUp} />
        <PublicRoute exact path="/" restricted={false} nav={true} component={Home} />
        {localStorage.getItem(process.env.REACT_APP_NAME + '_token') !== null
          ? <PublicRoute exact path="/editor" restricted={false} nav={false} component={SchematicEditor} />
          : <Route path="/editor" component={SchematicEditor} />
        }
        <PublicRoute exact path="/simulator/ngspice" restricted={false} nav={true} component={Simulator} />
        <PublicRoute exact path="/gallery" restricted={false} nav={true} component={Gallery} />
        <PrivateRoute path="/dashboard" component={Dashboard} />
        <PublicRoute restricted={false} nav={true} component={NotFound} />
      </Switch>
    </HashRouter>
  )
}

export default App
