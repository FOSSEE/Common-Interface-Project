import PropTypes from 'prop-types'

import HighlightOffIcon from '@mui/icons-material/HighlightOff'
import Box from '@mui/material/Box'
import Drawer from '@mui/material/Drawer'
import IconButton from '@mui/material/IconButton'

const drawerWidth = 250

// Common layout left side pane for Dashboard and Schematic Editor
export default function LayoutSidebar ({ window, mobileOpen, mobileClose, children }) {
  const container =
    window !== undefined ? () => window().document.body : undefined

  return (
    <>
      <Box
        component='nav'
        aria-label='mailbox folders'
        sx={{
          width: { md: drawerWidth },
          flexShrink: { md: 0 }
        }}
      >
        <Drawer
          container={container}
          variant='temporary'
          open={mobileOpen}
          onClose={mobileClose}
          sx={{
            display: { lg: 'none' }
          }}
          PaperProps={{
            sx: { width: drawerWidth }
          }}
          ModalProps={{
            keepMounted: true // Better open performance on mobile.
          }}
        >
          <IconButton
            onClick={mobileClose}
            color='inherit'
            style={{ marginLeft: '190px' }}
          >
            <HighlightOffIcon />
          </IconButton>
          {children}
        </Drawer>

        <Drawer
          variant='permanent'
          open
          sx={{
            display: { xs: 'none', sm: 'block' }
          }}
          PaperProps={{
            sx: { width: drawerWidth }
          }}
        >
          {children}
        </Drawer>
      </Box>
    </>
  )
}

LayoutSidebar.propTypes = {
  window: PropTypes.object,
  mobileOpen: PropTypes.bool.isRequired,
  mobileClose: PropTypes.func.isRequired,
  children: PropTypes.element
}
