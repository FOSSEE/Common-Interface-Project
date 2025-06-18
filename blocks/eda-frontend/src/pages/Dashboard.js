// Main Layout for user dashboard.
import { useEffect } from 'react'
import { Switch, Route } from 'react-router-dom'
import { Box, CssBaseline } from '@mui/material'

import { Header } from '../components/Shared/Navbar'
import Layout from '../components/Shared/Layout'
import LayoutMain from '../components/Shared/LayoutMain'
import DashboardSidebar from '../components/Dashboard/DashboardSidebar'
import DashboardHome from '../components/Dashboard/DashboardHome'
import SchematicsList from '../components/Dashboard/SchematicsList'

export default function Dashboard () {
  useEffect(() => {
    document.title = 'Dashboard - ' + process.env.REACT_APP_NAME
  }, [])

  return (
    <Box
      component='div'
      sx={{
        display: 'flex',
        minHeight: '100vh'
      }}
    >
      <CssBaseline />

      {/* Schematic editor header and left side pane */}
      <Layout resToolbar={<Header />} sidebar={<DashboardSidebar />} />

      <LayoutMain>
        <Box
          component='div'
          sx={{
            minHeight: '40px'
          }}
        />

        {/* Subroutes under dashboard section */}
        <Switch>
          <Route exact path='/dashboard' component={DashboardHome} />
          <Route exact path='/dashboard/profile' />
          <Route
            exact
            path='/dashboard/schematics'
            component={SchematicsList}
          />
        </Switch>
      </LayoutMain>
    </Box>
  )
}
