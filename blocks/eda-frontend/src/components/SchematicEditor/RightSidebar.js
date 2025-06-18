import PropTypes from 'prop-types'
import { Box, Drawer, IconButton } from '@mui/material'
import HighlightOffIcon from '@mui/icons-material/HighlightOff'

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
          ModalProps={{
            keepMounted: true // Better open performance on mobile.
          }}
          sx={{
            '& .MuiDrawer-paper': {
              width: drawerWidth
            },
            display: { xl: 'none' }
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
          anchor='right'
          variant='permanent'
          open
          sx={{
            '& .MuiDrawer-paper': {
              width: drawerWidth
            },
            display: { xs: 'none', md: 'block' }
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
