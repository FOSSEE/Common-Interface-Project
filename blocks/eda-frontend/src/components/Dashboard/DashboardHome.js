import React from 'react'
import { Link as RouterLink } from 'react-router-dom'
import { useSelector } from 'react-redux'

import { Button, Card, CardActions, CardContent, Grid, Typography } from '@mui/material'
import { makeStyles } from '@mui/styles'

import ProgressPanel from './ProgressPanel'

const useStyles = makeStyles((theme) => ({
  mainHead: {
    width: '100%',
    backgroundColor: '#404040',
    color: '#fff'
  },
  title: {
    fontSize: 14,
    color: '#80ff80'
  }
}))

// Card displaying user dashboard home page header.
function MainCard () {
  const classes = useStyles()
  const user = useSelector(state => state.authReducer.user)
  const dashboard = process.env.REACT_APP_NAME
  const button = 'My ' + process.env.REACT_APP_DIAGRAMS_NAME

  return (
    <Card className={classes.mainHead}>
      <CardContent>
        <Typography className={classes.title} gutterBottom>
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
  const classes = useStyles()
  const user = useSelector(state => state.authReducer.user)
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
        <Grid item xs={12}>
          <MainCard />
        </Grid>

        <Grid item xs={12}>
          <Card style={{ padding: '7px 15px' }} className={classes.mainHead}>
            <Typography variant='subtitle1' gutterBottom>
              Hey {user.username} , {typography}
            </Typography>
          </Card>
        </Grid>

        {/* List recent schematics saved by user */}
        <Grid item xs={12}>
          <Card>
            <ProgressPanel />
          </Card>
        </Grid>
      </Grid>
    </>
  )
}
