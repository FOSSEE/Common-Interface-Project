import { useEffect } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import {
  HashRouter,
  Navigate,
  Route,
  Routes
} from 'react-router-dom'

import PropTypes from 'prop-types'

import CircularProgress from '@mui/material/CircularProgress'

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
const PrivateRoute = ({ element: Element }) => {
  const isAuthenticated = useSelector(state => state.auth.isAuthenticated)
  const isLoading = useSelector(state => state.auth.isLoading)

  if (isLoading) {
    return <CircularProgress style={{ margin: '50vh 50vw' }} />
  } else if (!isAuthenticated) {
    return <Navigate to='/login' replace />
  } else {
    return Element
  }
}

PrivateRoute.propTypes = {
  element: PropTypes.node
}

// Public routes accessible to all users. [ e.g. editor, gallery ]
const PublicRoute = ({ element: Element, restricted, nav }) => {
  const isAuthenticated = useSelector(state => state.auth.isAuthenticated)
  const isLoading = useSelector(state => state.auth.isLoading)

  if (isLoading) {
    return <CircularProgress style={{ margin: '50vh 50vw' }} />
  } else if (isAuthenticated && restricted) {
    return <Navigate to='/dashboard' replace />
  } else if (nav) {
    return (
      <>
        <Navbar />
        {Element}
      </>
    )
  } else {
    return Element
  }
}

PublicRoute.propTypes = {
  element: PropTypes.node,
  restricted: PropTypes.bool,
  nav: PropTypes.bool
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
      <Routes>
        <Route path='/login' element={
          <PublicRoute restricted nav={false} element={<Login />} />
        } />
        <Route path='/signup' element={
          <PublicRoute restricted nav={false} element={<SignUp />} />
        } />
        <Route path='/forgotpwd' element={
          <PublicRoute restricted nav={false} element={<ForgotPassword />} />
        } />
        <Route path='/' element={
          <PublicRoute restricted={false} nav element={<Home />} />
        } />
        <Route path='/editor' element={
          localStorage.getItem(process.env.REACT_APP_NAME + '_token') !== null
            ? <PublicRoute restricted={false} nav={false} element={<SchematicEditor />} />
            : <SchematicEditor />
        } />
        <Route path='/gallery' element={
          <PublicRoute restricted={false} nav element={<Gallery />} />
        } />
        <Route path='/dashboard/*' element={
          <PrivateRoute element={<Dashboard />} />
        } />
        <Route path='*' element={
          <PublicRoute restricted={false} nav element={<NotFound />} />
        } />
      </Routes>
    </HashRouter>
  )
}

export default App
