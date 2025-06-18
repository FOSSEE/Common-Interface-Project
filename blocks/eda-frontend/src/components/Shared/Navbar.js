import { useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'

import { AppBar, Avatar, Button, Fade, IconButton, Link, ListItemText, Menu, MenuItem, Toolbar, Typography } from '@mui/material'
import { deepPurple } from '@mui/material/colors'
import { Link as RouterLink, useHistory } from 'react-router-dom'
import logo from '../../static/favicon.ico'
import { logout } from '../../redux/authSlice'
import { getUppercaseInitial } from '../../utils/GalleryUtils'

// Common navbar for Dashboard, Home, Gallery, etc.
export function Header () {
  const history = useHistory()
  const [anchorEl, setAnchorEl] = useState(null)
  const isAuthenticated = useSelector(state => state.auth.isAuthenticated)
  const user = useSelector(state => state.auth.user)

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
      <IconButton
        edge='start'
        color='primary'
        sx={{
          mr: 0.7
        }}
      >
        <Avatar
          alt={altImage}
          src={logo}
          sx={{
            width: { xs: 28, sm: 32, md: 40 },
            height: { xs: 28, sm: 32, md: 40 }
          }}
        />
      </IconButton>
      <Typography
        variant='h6'
        color='inherit'
        noWrap
        sx={{
          flexGrow: 1
        }}
      >
        <Link underline='hover' color='inherit' to='/' component={RouterLink}>
          {link}
        </Link>
      </Typography>

      {/* Display relative link to other pages */}
      <nav>
        {
          (isAuthenticated
            ? (<>
              <Link
                underline='hover'
                variant='button'
                color='textPrimary'
                to='/'
                component={RouterLink}
                sx={{
                  mx: 1.5,
                  my: 1
                }}
              >
                Home
              </Link>

              <Link
                underline='hover'
                variant='button'
                color='textPrimary'
                to='/editor'
                component={RouterLink}
                sx={{
                  mx: 1.5,
                  my: 1
                }}
              >
                Editor
              </Link>

              <Link
                underline='hover'
                variant='button'
                color='textPrimary'
                to='/gallery'
                component={RouterLink}
                sx={{
                  mx: 1.5,
                  my: 1
                }}
              >
                Gallery
              </Link>

              <Link
                underline='hover'
                variant='button'
                color='textPrimary'
                to='/dashboard'
                component={RouterLink}
                sx={{
                  mx: 1.5,
                  my: 1
                }}
              >
                Dashboard
              </Link>
            </>)
            : (<>
              <Link
                underline='hover'
                variant='button'
                color='textPrimary'
                to='/editor'
                component={RouterLink}
                style={{ marginRight: '20px' }}
              >
                Editor
              </Link>

              <Link
                underline='hover'
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
              <Avatar
                sx={{
                  width: { xs: 28, sm: 32, md: 40 },
                  height: { xs: 28, sm: 32, md: 40 },
                  color: theme => theme.palette.getContrastText(deepPurple[500]),
                  bgcolor: deepPurple[500],
                  fontSize: '17px'
                }}
              >
                {getUppercaseInitial(user.username)}
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
  return (
    <AppBar
      position='static'
      color='default'
      elevation={0}
      sx={{
        borderBottom: theme => `1px solid ${theme.palette.divider}`
      }}
    >
      <Toolbar
        variant='dense'
        color='default'
        sx={{
          flexWrap: 'wrap'
        }}
      >

        <Header />
      </Toolbar>
    </AppBar>
  )
}
