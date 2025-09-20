import { useSelector } from 'react-redux'
import { Link as RouterLink } from 'react-router-dom'

import {
  Button,
  Card,
  CardActions,
  CardContent,
  Grid,
  Typography
} from '@mui/material'

import SchematicCard from './SchematicCard'

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
      </CardActions>
    </Card>
  )
}

export default function SchematicsList () {
  const user = useSelector(state => state.auth.user)
  const schematics = useSelector(state => state.dashboard.schematics)

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
                px: 2,
                py: 1
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
