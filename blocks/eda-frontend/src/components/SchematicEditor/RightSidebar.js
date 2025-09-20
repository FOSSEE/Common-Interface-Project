import PropTypes from 'prop-types'

import HighlightOffIcon from '@mui/icons-material/HighlightOff'
import { Box, Drawer, IconButton } from '@mui/material'

const drawerWidth = 250

// Editor right side pane to display grid and compProperties.
export default function RightSidebar ({ window, mobileOpen, mobileClose, children }) {
  const container =
    window !== undefined ? () => window().document.body : undefined

  return (
    <>
      <Box
        component='nav'
        aria-label='mailbox folders'
        sx={{
          width: { lg: drawerWidth },
          flexShrink: { lg: 0 }
        }}
      >
        <Drawer
          container={container}
          variant='temporary'
          open={mobileOpen}
          anchor='right'
          onClose={mobileClose}
          sx={{ display: { xl: 'none' } }}
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
            style={{ marginRight: '190px' }}
          >
            <HighlightOffIcon />
          </IconButton>
          {children}
        </Drawer>

        <Drawer
          sx={{ display: { xs: 'none', md: 'block' } }}
          anchor='right'
          variant='permanent'
          open
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

RightSidebar.propTypes = {
  window: PropTypes.object,
  mobileOpen: PropTypes.bool.isRequired,
  mobileClose: PropTypes.func.isRequired,
  children: PropTypes.element
}
