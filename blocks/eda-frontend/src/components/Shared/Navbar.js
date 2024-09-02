import React, { useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { Link as RouterLink, useHistory } from 'react-router-dom'

import { AppBar, Avatar, Button, Fade, IconButton, Link, ListItemText, Menu, MenuItem, Toolbar, Typography } from '@mui/material'
import { deepPurple } from '@mui/material/colors'
import { makeStyles } from '@mui/styles'

import logo from '../../static/favicon.ico'

import store from '../../redux/store'
import { logout } from '../../redux/actions/index'

const useStyles = makeStyles((theme) => ({
  appBar: {
    borderBottom: `1px solid ${theme.palette.divider}`
  },
  toolbar: {
    flexWrap: 'wrap'
  },
  toolbarTitle: {
    flexGrow: 1
  },
  link: {
    margin: theme.spacing(1, 1.5)
  },
  button: {
    marginRight: theme.spacing(0.7)
  },
  small: {
    width: theme.spacing(3.7),
    height: theme.spacing(3.7)
  },
  purple: {
    width: theme.spacing(3.75),
    height: theme.spacing(3.75),
    color: theme.palette.getContrastText(deepPurple[500]),
    backgroundColor: deepPurple[500],
    fontSize: '17px'
  }
}))

// Common navbar for Dashboard, Home, Gallery, etc.
export function Header () {
  const history = useHistory()
  const classes = useStyles()
  const [anchorEl, setAnchorEl] = useState(null)
  const isAuthenticated = useSelector(state => state.authReducer.isAuthenticated)
  const user = useSelector(state => state.authReducer.user)

  const dispatch = useDispatch()

  const handleClick = (event) => {
    setAnchorEl(event.currentTarget)
  }

  const handleClose = () => {
    setAnchorEl(null)
  }

  const link = process.env.REACT_APP_NAME
  const altImage = process.env.REACT_APP_NAME + ' logo'
  const typography = 'My ' + process.env.REACT_APP_DIAGRAMS_NAME
  return (
    <>
      {/* Display logo */}
      <IconButton edge='start' className={classes.button} color='primary'>
        <Avatar alt={altImage} src={logo} className={classes.small} />
      </IconButton>
      <Typography
        variant='h6'
        color='inherit'
        noWrap
        className={classes.toolbarTitle}
      >
        <Link color='inherit' to='/' component={RouterLink}>
          {link}
        </Link>
      </Typography>

      {/* Display relative link to other pages */}
      <nav>
        {
          (isAuthenticated
            ? (<>
              <Link
                variant='button'
                color='textPrimary'
                to='/'
                component={RouterLink}
                className={classes.link}
              >
                Home
              </Link>

              <Link
                variant='button'
                color='textPrimary'
                to='/editor'
                component={RouterLink}
                className={classes.link}
              >
                Editor
              </Link>

              <Link
                variant='button'
                color='textPrimary'
                to='/gallery'
                component={RouterLink}
                className={classes.link}
              >
                Gallery
              </Link>

              <Link
                variant='button'
                color='textPrimary'
                to='/dashboard'
                component={RouterLink}
                className={classes.link}
              >
                Dashboard
              </Link>
            </>)
            : (<>
              <Link
                variant='button'
                color='textPrimary'
                to='/editor'
                component={RouterLink}
                style={{ marginRight: '20px' }}
              >
                Editor
              </Link>

              <Link
                variant='button'
                color='textPrimary'
                to='/gallery'
                component={RouterLink}
                style={{ marginRight: '20px' }}
              >
                Gallery
              </Link>
            </>
              )
          )
        }
      </nav>

      {/* Display login option or user menu as per authenticated status */}
      {
        (!isAuthenticated
          ? <Button
            size='small'
            component={RouterLink}
            to='/login'
            color='primary'
            variant='outlined'
          >
            Login
          </Button>
          : <>
            <IconButton
              edge='start'
              style={{ marginLeft: 'auto' }}
              color='primary'
              aria-controls='simple-menu'
              aria-haspopup='true'
              onClick={handleClick}
            >
              <Avatar className={classes.purple}>
                {user.username.charAt(0).toUpperCase()}
              </Avatar>
            </IconButton>
            <Menu
              id='simple-menu'
              anchorEl={anchorEl}
              keepMounted
              open={Boolean(anchorEl)}
              onClose={handleClose}
              TransitionComponent={Fade}
              style={{ marginTop: '25px' }}
            >
              <MenuItem
                component={RouterLink}
                to='/dashboard'
                onClick={handleClose}
              >
                <ListItemText primary={user.username} secondary={user.email} />
              </MenuItem>
              <MenuItem
                component={RouterLink}
                to='/dashboard/schematics'
                onClick={handleClose}
              >
                {typography}
              </MenuItem>
              <MenuItem onClick={() => {
                dispatch(logout(history))
              }}
              >
                Logout
              </MenuItem>
            </Menu>
          </>
        )
      }
    </>
  )
}

export default function Navbar () {
  const classes = useStyles()

  return (
    <AppBar
      position='static'
      color='default'
      elevation={0}
      className={classes.appBar}
    >
      <Toolbar variant='dense' color='default' className={classes.toolbar}>

        <Header />
      </Toolbar>
    </AppBar>
  )
}
