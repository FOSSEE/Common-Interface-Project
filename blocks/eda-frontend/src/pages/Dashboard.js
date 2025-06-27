// Main Layout for user dashboard.
import { useEffect } from 'react'
import { Switch, Route } from 'react-router-dom'

import { CssBaseline } from '@material-ui/core'
import { makeStyles } from '@material-ui/core/styles'

import DashboardHome from '../components/Dashboard/DashboardHome'
import DashboardSidebar from '../components/Dashboard/DashboardSidebar'
import SchematicsList from '../components/Dashboard/SchematicsList'
import Layout from '../components/Shared/Layout'
import LayoutMain from '../components/Shared/LayoutMain'
import { Header } from '../components/Shared/Navbar'

const useStyles = makeStyles((_theme) => ({
  root: {
    display: 'flex',
    minHeight: '100vh'
  },
  toolbar: {
    minHeight: '40px'
  }
}))

export default function Dashboard () {
  const classes = useStyles()

  useEffect(() => {
    document.title = 'Dashboard - ' + process.env.REACT_APP_NAME
  }, [])

  return (
    <div className={classes.root}>
      <CssBaseline />

      {/* Schematic editor header and left side pane */}
      <Layout resToolbar={<Header />} sidebar={<DashboardSidebar />} />

      <LayoutMain>
        <div className={classes.toolbar} />

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
    </div>
  )
}
