import React from 'react'
import PropTypes from 'prop-types'

import { Drawer, Hidden, IconButton } from '@mui/material'
import HighlightOffIcon from '@mui/icons-material/HighlightOff'
import { makeStyles } from '@mui/styles'

const drawerWidth = 250

const useStyles = makeStyles((theme) => ({
  drawer: {
    [theme.breakpoints.up('lg')]: {
      width: drawerWidth,
      flexShrink: 0
    }
  },
  drawerPaper: {
    width: drawerWidth
  }
}))

// Editor right side pane to display grid and compProperties.
export default function RightSidebar ({ window, mobileOpen, mobileClose, children }) {
  const classes = useStyles()

  const container =
    window !== undefined ? () => window().document.body : undefined

  return (
    <>
      <nav className={classes.drawer} aria-label='mailbox folders'>
        <Hidden xlUp implementation='css'>
          <Drawer
            container={container}
            variant='temporary'
            open={mobileOpen}
            anchor='right'
            onClose={mobileClose}
            classes={{
              paper: classes.drawerPaper
            }}
            ModalProps={{
              keepMounted: true // Better open performance on mobile.
            }}
          >
            <IconButton
              onClick={mobileClose}
              color='inherit'
              style={{ marginRight: '190px' }}
            >
              <HighlightOffIcon />
            </IconButton>
            {children}
          </Drawer>
        </Hidden>

        <Hidden mdDown implementation='css'>
          <Drawer
            classes={{
              paper: classes.drawerPaper
            }}
            anchor='right'
            variant='permanent'
            open
          >
            {children}
          </Drawer>
        </Hidden>
      </nav>
    </>
  )
}

RightSidebar.propTypes = {
  window: PropTypes.object,
  mobileOpen: PropTypes.bool.isRequired,
  mobileClose: PropTypes.func.isRequired,
  children: PropTypes.element
}
