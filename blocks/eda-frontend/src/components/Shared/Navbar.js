import { useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { Link as RouterLink, useNavigate } from 'react-router-dom'

import AppBar from '@mui/material/AppBar'
import Avatar from '@mui/material/Avatar'
import Button from '@mui/material/Button'
import { deepPurple } from '@mui/material/colors'
import Fade from '@mui/material/Fade'
import IconButton from '@mui/material/IconButton'
import Link from '@mui/material/Link'
import ListItemText from '@mui/material/ListItemText'
import Menu from '@mui/material/Menu'
import MenuItem from '@mui/material/MenuItem'
import Toolbar from '@mui/material/Toolbar'
import Typography from '@mui/material/Typography'

import { logout } from '../../redux/authSlice'
import logo from '../../static/favicon.ico'
import { getUppercaseInitial } from '../../utils/GalleryUtils'

// Common navbar for Dashboard, Home, Gallery, etc.
export function Header () {
  const navigate = useNavigate()
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
            width: theme => theme.spacing(3.7),
            height: theme => theme.spacing(3.7),
            borderRadius: '10%'
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
        <Link color='inherit' to='/' component={RouterLink} underline='hover'>
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
                underline='hover'
                sx={{
                  mx: 1.5,
                  my: 1
                }}
              >
                Home
              </Link>

              <Link
                variant='button'
                color='textPrimary'
                to='/editor'
                component={RouterLink}
                underline='hover'
                sx={{
                  mx: 1.5,
                  my: 1
                }}
              >
                Editor
              </Link>

              <Link
                variant='button'
                color='textPrimary'
                to='/gallery'
                component={RouterLink}
                underline='hover'
                sx={{
                  mx: 1.5,
                  my: 1
                }}
              >
                Gallery
              </Link>

              <Link
                variant='button'
                color='textPrimary'
                to='/dashboard'
                component={RouterLink}
                underline='hover'
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
                variant='button'
                color='textPrimary'
                to='/editor'
                component={RouterLink}
                underline='hover'
                style={{ marginRight: '20px' }}
              >
                Editor
              </Link>

              <Link
                variant='button'
                color='textPrimary'
                to='/gallery'
                component={RouterLink}
                underline='hover'
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
                  width: theme => theme.spacing(3.75),
                  height: theme => theme.spacing(3.75),
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
                dispatch(logout(navigate))
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
        borderBottom: 1,
        borderColor: 'divider'
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
