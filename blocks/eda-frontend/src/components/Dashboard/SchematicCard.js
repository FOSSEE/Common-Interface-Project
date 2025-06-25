import { useState } from 'react'
import PropTypes from 'prop-types'
import { Button, Card, CardActionArea, CardActions, CardContent, CardHeader, CardMedia, Snackbar, Tooltip, Typography } from '@mui/material'
import ShareIcon from '@mui/icons-material/Share'
import { Link as RouterLink } from 'react-router-dom'
import DeleteIcon from '@mui/icons-material/Delete'
import { useDispatch } from 'react-redux'
import { deleteSchematic } from '../../redux/dashboardSlice'
import MuiAlert from '@mui/material/Alert'
import { getDate } from '../../utils/GalleryUtils'
import { Grid } from '@mui/material'
import { useSelector } from 'react-redux'

function Alert (props) {
  return <MuiAlert elevation={6} variant='filled' {...props} />
}

// Schematic delete snackbar
function SimpleSnackbar ({ open, close, sch }) {
  const dispatch = useDispatch()

  return (
    <Snackbar
      anchorOrigin={{
        vertical: 'bottom',
        horizontal: 'center'
      }}
      open={open}
      autoHideDuration={6000}
      onClose={close}
    >
      <Alert
        icon={false} severity='warning' color='error' style={{ width: '100%' }} action={
          <>
            <Button size='small' aria-label='close' color='inherit' onClick={() => { dispatch(deleteSchematic(sch.save_id)) }}>
              Yes
            </Button>
            <Button size='small' aria-label='close' color='inherit' onClick={close}>
              NO
            </Button>
          </>
        }
      >
        {'Delete ' + sch.name + ' ?'}
      </Alert>
    </Snackbar>
  )
}

SimpleSnackbar.propTypes = {
  open: PropTypes.bool,
  close: PropTypes.func,
  sch: PropTypes.object
}

// Display schematic updated status (e.g : updated 2 hours ago...)
function timeSince (jsonDate) {
  const json = jsonDate

  const date = new Date(json)

  const seconds = Math.floor((new Date() - date) / 1000)

  let interval = Math.floor(seconds / 31536000)

  if (interval > 1) {
    return interval + ' years'
  }
  interval = Math.floor(seconds / 2592000)
  if (interval > 1) {
    return interval + ' months'
  }
  interval = Math.floor(seconds / 86400)
  if (interval > 1) {
    return interval + ' days'
  }
  interval = Math.floor(seconds / 3600)
  if (interval > 1) {
    return interval + ' hours'
  }
  interval = Math.floor(seconds / 60)
  if (interval > 1) {
    return interval + ' minutes'
  }
  return Math.floor(seconds) + ' seconds'
}

// Card displaying overview of onCloud saved schematic.
export default function SchematicCard () {
  const schematics = useSelector(state => state.dashboard.schematics)
  // To handle delete schematic snackbar
  const [snacOpen, setSnacOpen] = useState(false)

  const handleSnacClick = () => {
    setSnacOpen(true)
  }

  const handleSnacClose = (event, reason) => {
    if (reason === 'clickaway') {
      return
    }
    setSnacOpen(false)
  }

  return (
    <>
      {/* User saved Schematic Overview Card */}

      <Grid container spacing={3}>
        {schematics.map((sch) => (
          <Grid size={4}>
            < Card sx={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
              <CardActionArea component={RouterLink} to={`/editor?id=${sch.save_id}`}>
                <CardHeader
                  title={sch.name}
                  subheader={`Created On ${getDate(sch.create_time)}`}
                  sx={{ pt: 2, pb: 0 }}
                />
                <CardMedia
                  component='img'
                  image={sch.base64_image}
                  alt={sch.name}
                  sx={{
                    width: '100%',
                    height: 240,
                    objectFit: 'contain',
                    mt: 1
                  }}
                />
                <CardContent sx={{ pt: 1, pb: 0 }}>
                  <Typography variant='body2' color='text.primary'>
                    {sch.description}
                  </Typography>
                  <Typography variant='body2' color='text.secondary' sx={{ mt: 1 }}>
                    Updated {timeSince(sch.save_time)} ago...
                  </Typography>
                </CardContent>
              </CardActionArea>
              <CardActions sx={{ justifyContent: 'space-between', px: 1 }}>
                <Button
                  size='small'
                  color='primary'
                  component={RouterLink}
                  to={`/editor?id=${sch.save_id}`}
                >
                  Launch in Editor
                </Button>

                {/* Display delete option */}
                <Tooltip title='Delete' placement='bottom' arrow>
                  <DeleteIcon
                    color='secondary'
                    fontSize='small'
                    style={{ marginLeft: 'auto' }}
                    onClick={() => { handleSnacClick() }}
                  />
                </Tooltip>
                <SimpleSnackbar open={snacOpen} close={handleSnacClose} sch={sch} />

                {/* Display share status */}
                <Tooltip title={!sch.shared ? 'SHARE OFF' : 'SHARE ON'} placement='bottom' arrow>
                  <ShareIcon
                    color={!sch.shared ? 'disabled' : 'primary'}
                    fontSize='small'
                    style={{ marginRight: '10px' }}
                  />
                </Tooltip>
              </CardActions>
            </Card >
          </Grid>
        ))
        }
      </Grid >
    </>



  )
}

SchematicCard.propTypes = {
  sch: PropTypes.object
}
