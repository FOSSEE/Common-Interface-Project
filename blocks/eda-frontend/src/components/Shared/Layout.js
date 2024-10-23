import React, { useState } from 'react'
import PropTypes from 'prop-types'

import { AppBar, IconButton, Toolbar } from '@mui/material'
import { makeStyles } from '@mui/styles'
import MenuIcon from '@mui/icons-material/Menu'

import LayoutSidebar from './LayoutSidebar'

const useStyles = makeStyles((theme) => ({
  appBar: {
    borderBottom: `1px solid ${theme.palette.divider}`,
    zIndex: theme.zIndex.drawer + 1
  },
  menuButton: {
    marginRight: theme.spacing(1),
    padding: theme.spacing(1),
    [theme.breakpoints.up('md')]: {
      display: 'none'
    }
  }
}))

// Common layout for Dashboard and Schematic Editor
function Layout ({ header, resToolbar, sidebar }) {
  const classes = useStyles()
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
        className={classes.appBar}
        style={{ zIndex: 2000 }}
      >
        {header}

        <Toolbar variant='dense' color='default'>
          <IconButton
            color='inherit'
            aria-label='open drawer'
            edge='start'
            size='small'
            onClick={handleDrawerToggle}
            className={classes.menuButton}
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
