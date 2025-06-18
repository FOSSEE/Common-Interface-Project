import { useState } from 'react'
import PropTypes from 'prop-types'
import { AppBar, IconButton, Toolbar } from '@mui/material'
import MenuIcon from '@mui/icons-material/Menu'

import LayoutSidebar from './LayoutSidebar'

// Common layout for Dashboard and Schematic Editor
function Layout ({ header, resToolbar, sidebar }) {
  const [mobileOpen, setMobileOpen] = useState(false)

  const handleDrawerToggle = () => {
    setMobileOpen(!mobileOpen)
  }

  return (
    <>
      {/* Header and Toolbar of layout */}
      <AppBar
        position='fixed'
        color='default'
        elevation={0}
        sx={{
          borderBottom: theme => `1px solid ${theme.palette.divider}`,
          zIndex: theme => theme.zIndex.drawer + 1
        }}
      >
        {header}

        <Toolbar variant='dense' color='default'>
          <IconButton
            color='inherit'
            aria-label='open drawer'
            edge='start'
            size='small'
            onClick={handleDrawerToggle}
            sx={{
              mr: 1,
              p: 1,
              display: {
                xs: 'inline-flex',
                md: 'none'
              }
            }}
          >
            <MenuIcon fontSize='small' />
          </IconButton>

          {resToolbar}
        </Toolbar>
      </AppBar>

      {/* Left Sidebar for Layout */}
      <LayoutSidebar mobileOpen={mobileOpen} mobileClose={handleDrawerToggle}>
        {sidebar}
      </LayoutSidebar>
    </>
  )
}

Layout.propTypes = {
  header: PropTypes.element,
  resToolbar: PropTypes.element,
  sidebar: PropTypes.element
}

export default Layout
