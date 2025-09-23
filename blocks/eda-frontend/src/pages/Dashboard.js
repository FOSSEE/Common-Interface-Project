// Main Layout for user dashboard.
import { useEffect } from 'react'
import { Route, Routes } from 'react-router-dom'

import Box from '@mui/material/Box'
import CssBaseline from '@mui/material/CssBaseline'

import DashboardHome from '../components/Dashboard/DashboardHome'
import DashboardSidebar from '../components/Dashboard/DashboardSidebar'
import SchematicsList from '../components/Dashboard/SchematicsList'
import Layout from '../components/Shared/Layout'
import LayoutMain from '../components/Shared/LayoutMain'
import { Header } from '../components/Shared/Navbar'

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
        <Routes>
          <Route index element={<DashboardHome />} />
          <Route path='schematics' element={<SchematicsList />} />
        </Routes>
      </LayoutMain>
    </Box>
  )
}
