import { Button, Card, CardActions, CardContent, Grid, Typography } from '@mui/material'
import { Link as RouterLink } from 'react-router-dom'
import { useSelector } from 'react-redux'

import ProgressPanel from './ProgressPanel'

// Card displaying user dashboard home page header.
function MainCard () {
  const user = useSelector(state => state.auth.user)
  const dashboard = process.env.REACT_APP_NAME
  const button = 'My ' + process.env.REACT_APP_DIAGRAMS_NAME

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
          Welcome to your {dashboard} Dashboard
        </Typography>
        <Typography variant='h5' component='h2'>
          Welcome {user.username}...
        </Typography>
      </CardContent>
      <CardActions>
        <Button
          component={RouterLink}
          to='/dashboard/schematics'
          color='primary'
          size='small'
        >
          {button}
        </Button>
      </CardActions>
    </Card>
  )
}

export default function DashboardHome () {
  const user = useSelector(state => state.auth.user)
  const typography = 'Track your ' + process.env.REACT_APP_SMALL_DIAGRAMS_NAME + ' status here...'

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
        {/* User Dashboard Home Header */}
        <Grid size={12}>
          <MainCard />
        </Grid>

        <Grid size={12}>
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
              Hey {user.username} , {typography}
            </Typography>
          </Card>
        </Grid>

        {/* List recent schematics saved by user */}
        <Grid size={12}>
          <Card>
            <ProgressPanel />
          </Card>
        </Grid>
      </Grid>
    </>
  )
}
