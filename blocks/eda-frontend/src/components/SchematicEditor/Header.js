import { useEffect, useRef, useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'
import { useNavigate, Link as RouterLink } from 'react-router-dom'

import PropTypes from 'prop-types'

import CloseIcon from '@mui/icons-material/Close'
import ShareIcon from '@mui/icons-material/Share'
import {
  Avatar,
  Box,
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
  Fade,
  FormControlLabel,
  IconButton,
  Input,
  Link,
  ListItemText,
  Menu,
  MenuItem,
  Snackbar,
  Switch,
  Toolbar,
  Typography
} from '@mui/material'
import { deepPurple } from '@mui/material/colors'

import { logout } from '../../redux/authSlice'
import { setSchTitle, setSchShared } from '../../redux/saveSchematicSlice'
import logo from '../../static/favicon.ico'
import { getDateTime as getDate, getUppercaseInitial } from '../../utils/GalleryUtils'

// Notification snackbar to give alert messages
function SimpleSnackbar ({ open, close, message }) {
  return (
    <div>
      <Snackbar
        anchorOrigin={{
          vertical: 'bottom',
          horizontal: 'left'
        }}
        open={open}
        autoHideDuration={6000}
        onClose={close}
        message={message}
        action={
          <>
            <IconButton size='small' aria-label='close' color='inherit' onClick={close}>
              <CloseIcon fontSize='small' />
            </IconButton>
          </>
        }
      />
    </div>
  )
}

SimpleSnackbar.propTypes = {
  open: PropTypes.bool,
  close: PropTypes.func,
  message: PropTypes.string
}

function Header () {
  const navigate = useNavigate()
  const isAuthenticated = useSelector(state => state.auth.isAuthenticated)
  const user = useSelector(state => state.auth.user)
  const details = useSelector(state => state.saveSchematic.details)
  const isSaved = useSelector(state => state.saveSchematic.isSaved)
  const isShared = useSelector(state => state.saveSchematic.isShared)
  const title = useSelector(state => state.saveSchematic.title)
  const [anchorEl, setAnchorEl] = useState(null)

  const dispatch = useDispatch()

  const handleClick = (event) => {
    setAnchorEl(event.currentTarget)
  }

  const handleClose = () => {
    setAnchorEl(null)
  }

  const titleHandler = (e) => {
    dispatch(setSchTitle(`${e.target.value}`))
  }

  // handle notification snackbar open and close with message
  const [snacOpen, setSnacOpen] = useState(false)
  const [message, setMessage] = useState('')

  const handleSnacClick = () => {
    setSnacOpen(true)
  }

  const handleSnacClose = (event, reason) => {
    if (reason === 'clickaway') {
      return
    }
    setSnacOpen(false)
  }

  // handle schematic Share Dialog box
  const [openShare, setShareOpen] = useState(false)

  const handleShareOpen = () => {
    setShareOpen(true)
  }

  const handleShareClose = () => {
    setShareOpen(false)
  }

  // change saved schematic share status
  const [shared, setShared] = useState(isShared)

  useEffect(() => {
    setShared(isShared)
  }, [isShared])

  const handleShareChange = (event) => {
    setShared(event.target.checked)
    dispatch(setSchShared(event.target.checked))
  }

  const handleShare = () => {
    if (isAuthenticated !== true) {
      setMessage('You are not Logged In')
      handleSnacClick()
    } else if (isSaved !== true) {
      setMessage('You have not saved the ' + process.env.REACT_APP_DIAGRAM_NAME + ' yet')
      handleSnacClick()
    } else {
      handleShareOpen()
    }
  }

  // handle Copy Share Url
  const textAreaRef = useRef(null)

  function copyToClipboard (e) {
    textAreaRef.current.select()
    document.execCommand('copy')
    e.target.focus()
    setMessage('Copied Successfully!')
    handleSnacClick()
  }

  const link = process.env.REACT_APP_NAME
  const altImage = process.env.REACT_APP_NAME + ' logo'
  const typography1 = 'Share Your ' + process.env.REACT_APP_DIAGRAM_NAME
  const typography2 = 'My ' + process.env.REACT_APP_DIAGRAMS_NAME
  return (
    <Toolbar variant='dense' color='default'>
      <SimpleSnackbar open={snacOpen} close={handleSnacClose} message={message} />

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
          mr: 2
        }}
      >
        <Link color='inherit' target='_blank' component={RouterLink} to='/' underline='hover'>
          {link}
        </Link>
      </Typography>

      {/* Input field for schematic title */}
      <Input
        color='secondary'
        value={title === 'Untitled' ? 'Untitled' : title}
        onChange={titleHandler}
        inputProps={{ 'aria-label': 'Title' }}
        sx={{
          ml: 1,
          width: '200px',
          color: '#595959'
        }}
      />

      {/* Display last saved and shared option for saved schematics */}
      {isAuthenticated === true
        ? <>
          {(isSaved === true && details.save_time !== undefined)
            ? <Typography
              variant='body2'
              style={{ margin: '0px 15px 0px auto', paddingTop: '5px', color: '#8c8c8c' }}
            >
              Last Saved : {getDate(details.save_time)} {/* Display last saved status for saved schematics */}
            </Typography>
            : <></>}
          <Button
            size='small'
            variant={shared !== true ? 'outlined' : 'contained'}
            color='primary'
            sx={isSaved === true && details.save_time !== undefined
              ? {
                mr: 0.7
              }
              : {
                ml: 'auto',
                mr: 2
              }
            }
            startIcon={<ShareIcon />}
            onClick={handleShare}
          >
            <Box
              sx={{
                display: { xs: 'block', sm: 'none' }
              }}
            >
              Share
            </Box>
          </Button>
        </>
        : <></>}

      {/* Share dialog box to get share url */}
      <Dialog
        open={openShare}
        onClose={handleShareClose}
        aria-labelledby='share-dialog-title'
        aria-describedby='share-dialog-description'
      >
        <DialogTitle id='share-dialog-title'>{typography1}</DialogTitle>
        <DialogContent>
          <DialogContentText id='share-dialog-description'>
            <FormControlLabel
              control={<Switch checked={shared} onChange={handleShareChange} name='shared' />}
              label=': Sharing On'
            />
          </DialogContentText>
          <DialogContentText id='share-dialog-description'>
            {shared === true
              ? <input
                ref={textAreaRef}
                value={`${window.location.origin}/#/editor?id=${details.save_id}`}
                readOnly
              />
              : <> Turn On sharing </>}
          </DialogContentText>

        </DialogContent>
        <DialogActions>
          {shared === true && document.queryCommandSupported('copy')
            ? <Button onClick={copyToClipboard} color='primary' autoFocus>
              Copy url
            </Button>
            : <></>}
          <Button onClick={handleShareClose} color='primary' autoFocus>
            close
          </Button>
        </DialogActions>
      </Dialog>

      {/* Display login option or user menu as per authenticated status */}
      {
        (!isAuthenticated
          ? <Button
            size='small'
            component={RouterLink}
            to='/login'
            style={{ marginLeft: 'auto' }}
            color='primary'
            variant='outlined'
          >
            Login
          </Button>
          : <>
            <IconButton
              edge='start'
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
              style={{ marginTop: '25px' }}
            >
              <MenuItem
                target='_blank'
                component={RouterLink}
                to='/dashboard'
                onClick={handleClose}
              >
                <ListItemText primary={user.username} secondary={user.email} />
              </MenuItem>
              <MenuItem
                target='_blank'
                component={RouterLink}
                to='/dashboard/schematics'
                onClick={handleClose}
              >
                {typography2}
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
    </Toolbar>
  )
}

export default Header
