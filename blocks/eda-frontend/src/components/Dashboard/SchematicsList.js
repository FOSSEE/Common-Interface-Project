import { useEffect } from 'react'
import { Button, Card, CardActions, CardContent, Grid, Typography } from '@mui/material'
import { Link as RouterLink } from 'react-router-dom'

import SchematicCard from './SchematicCard'
import { useDispatch, useSelector } from 'react-redux'
import { fetchSchematics } from '../../redux/dashboardSlice'

// Card displaying user my schematics page header.
function MainCard () {
  const typography1 = 'All ' + process.env.REACT_APP_SMALL_DIAGRAMS_NAME + ' are listed below'
  const typography2 = 'My ' + process.env.REACT_APP_DIAGRAMS_NAME

  return (
    <Card
      sx={{
        width: '100%',
        bgcolor: '#404040',
        color: '#fff'
      }}
    >
      <CardContent>
        <Typography
          gutterBottom
          sx={{
            fontSize: 14,
            color: '#80ff80'
          }}
        >
          {typography1}
        </Typography>
        <Typography variant='h5' component='h2'>
          {typography2}
        </Typography>
      </CardContent>
      <CardActions>
        <Button
          target='_blank'
          component={RouterLink}
          to='/editor'
          size='small'
          color='primary'
        >
          Create New
        </Button>
        <Button size='small' color='secondary'>
          Load More
        </Button>
      </CardActions>
    </Card>
  )
}

export default function SchematicsList () {
  const user = useSelector(state => state.auth.user)
  const schematics = useSelector(state => state.dashboard.schematics)

  const dispatch = useDispatch()

  // For Fetching Saved Schematics
  useEffect(() => {
    dispatch(fetchSchematics())
  }, [dispatch])

  const typography1 = 'You don\'t have any saved ' + process.env.REACT_APP_SMALL_DIAGRAMS_NAME + '...'
  return (
    <>
      <Grid
        container
        direction='row'
        justifyContent='flex-start'
        alignItems='flex-start'
        alignContent='center'
        spacing={3}
      >
        {/* User Dashboard My Schematic Header */}
        <Grid item xs={12}>
          <MainCard />
        </Grid>

        {/* List all schematics saved by user */}
        {schematics.length !== 0
          ? <>
            {schematics.map(
              (sch) => {
                return (
                  <Grid item xs={12} sm={6} lg={3} key={sch.save_id}>
                    <SchematicCard sch={sch} />
                  </Grid>
                )
              }
            )}
          </>
          : <Grid item xs={12}>
            <Card
              sx={{
                width: '100%',
                bgcolor: '#404040',
                color: '#fff',
                px: '15px',
                py: '7px'
              }}
            >
              <Typography variant='subtitle1' gutterBottom>
                Hey {user.username} , {typography1}
              </Typography>
            </Card>
          </Grid>}
      </Grid>
    </>
  )
}
