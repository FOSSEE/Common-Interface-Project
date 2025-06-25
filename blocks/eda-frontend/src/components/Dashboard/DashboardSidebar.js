import { useEffect } from 'react'
import { Avatar, Box, Divider, InputBase, List, ListItem, ListItemAvatar, ListItemText, Typography } from '@mui/material'
import { Link as RouterLink } from 'react-router-dom'
import { deepPurple } from '@mui/material/colors'
import { useDispatch, useSelector } from 'react-redux'
import { fetchSchematics } from '../../redux/dashboardSlice'
import { getUppercaseInitial } from '../../utils/GalleryUtils'

// Vertical Navbar for user dashboard
export default function DashSidebar (_props) {
  const user = useSelector(state => state.auth.user)
  const schematics = useSelector(state => state.dashboard.schematics)

  const dispatch = useDispatch()

  // For Fetching Saved Schematics
  useEffect(() => {
    dispatch(fetchSchematics())
  }, [dispatch])

  const button = 'My ' + process.env.REACT_APP_DIAGRAMS_NAME
  const placeholder = 'Find your ' + process.env.REACT_APP_SMALL_DIAGRAM_NAME + '...'
  return (
    <>
      <Box
        component='div'
        sx={{
          minHeight: '45px',
          display: { xs: 'none', sm: 'block' }
        }}
      />
      <List>
        <ListItem
          alignItems='flex-start'
          component={RouterLink}
          to='/dashboard'
          style={{ marginTop: '15px' }}
          button
          divider
          sx={{
            px: 2,
            py: 1.5,
            width: 270
          }}
        >
          <ListItemAvatar>
            <Avatar
              sx={{
                color: theme => theme.palette.getContrastText(deepPurple[500]),
                bgcolor: deepPurple[500]
              }}
            >
              {getUppercaseInitial(user.username)}
            </Avatar>
          </ListItemAvatar>
          <ListItemText
            primary={user.username}
            secondary={
              <>
                <Typography
                  component='span'
                  variant='body2'
                  color='textSecondary'
                >
                  Contributor
                </Typography>
              </>
            }
          />
        </ListItem>
        <ListItem
          component={RouterLink}
          to='/dashboard/schematics'
          button
          sx={{
            px: 2,
            py: 1.5
          }}
        >
          <ListItemText primary={button} />
        </ListItem>

        {/* List name of saved schematics */}
        <List
          sx={{
            border: '1px solid #cccccc',
            mx: 2,
            my: 1,
            borderRadius: '5px'
          }}
        >
          <InputBase
            placeholder={placeholder}
            sx={{
              ml: 1,
              flex: 1
            }}
          />
        </List>
        <div
          sx={{
            pl: 2,
            overflow: 'auto',
            width: '100%',
            maxHeight: 200
          }}
        >
          {schematics.map((sch) => (
            <ListItem key={sch.save_id} button>
              <ListItemText primary={`${sch.name}`} />
            </ListItem>
          ))}
        </div>
        <Divider />
      </List>
    </>
  )
}
