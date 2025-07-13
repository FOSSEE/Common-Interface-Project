import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'

import PropTypes from 'prop-types'

import { Tab, Box, Tabs, AppBar, Typography, Grid } from '@material-ui/core'
import { makeStyles } from '@material-ui/core/styles'

import { fetchSchematics } from '../../redux/dashboardSlice'

import SchematicCard from './SchematicCard'

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    width: '100%',
    backgroundColor: theme.palette.background.paper
  }
}))

function TabPanel (props) {
  const { children, value, index, ...other } = props

  return (
    <div
      role='tabpanel'
      hidden={value !== index}
      id={`scrollable-auto-tabpanel-${index}`}
      aria-labelledby={`scrollable-auto-tab-${index}`}
      {...other}
    >
      {value === index && (
        <Box p={3}>
          <Typography>{children}</Typography>
        </Box>
      )}
    </div>
  )
}

TabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.any.isRequired,
  value: PropTypes.any.isRequired
}

function a11yProps (index) {
  return {
    id: `scrollable-auto-tab-${index}`,
    'aria-controls': `scrollable-auto-tabpanel-${index}`
  }
}

export default function ProgressPanel () {
  const classes = useStyles()
  const [value, setValue] = useState(0)
  const isLoggingOut = useSelector(state => state.auth.isLoggingOut)
  const schematics = useSelector(state => state.dashboard.schematics)

  const dispatch = useDispatch()

  const handleChange = (event, newValue) => {
    setValue(newValue)
  }

  // For Fetching Saved Schematics
  useEffect(() => {
    if (isLoggingOut) return

    dispatch(fetchSchematics())
  }, [dispatch, isLoggingOut])

  const tab = 'Recent ' + process.env.REACT_APP_DIAGRAMS_NAME
  const typography = 'You have not created any ' + process.env.REACT_APP_SMALL_DIAGRAM_NAME
  return (
    <div className={classes.root}>
      <AppBar position='static'>
        <Tabs
          value={value}
          onChange={handleChange}
          variant='scrollable'
          scrollButtons='auto'
          aria-label='scrollable auto tabs example'
        >
          <Tab label={tab} {...a11yProps(0)} />
        </Tabs>
      </AppBar>

      {/* Display overview of recently 4 saved schematics */}
      <TabPanel value={value} index={0}>
        {schematics.length !== 0
          ? <Grid
            container
            direction='row'
            justifyContent='flex-start'
            alignItems='flex-start'
            alignContent='center'
            spacing={3}
          >
            {schematics.slice(0, 4).map(
              (sch) => {
                return (
                  <Grid item xs={12} sm={6} lg={3} key={sch.save_id}>
                    <SchematicCard sch={sch} />
                  </Grid>
                )
              }
            )}
          </Grid>
          : <Typography variant='button' display='block' gutterBottom>
            {typography} , Create your first one now...
          </Typography>}
      </TabPanel>
    </div>
  )
}
