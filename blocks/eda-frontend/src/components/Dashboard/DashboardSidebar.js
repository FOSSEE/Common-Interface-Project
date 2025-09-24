import { useSelector } from 'react-redux'
import { Link as RouterLink } from 'react-router-dom'

import Avatar from '@mui/material/Avatar'
import Box from '@mui/material/Box'
import { deepPurple } from '@mui/material/colors'
import Divider from '@mui/material/Divider'
import InputBase from '@mui/material/InputBase'
import List from '@mui/material/List'
import ListItemAvatar from '@mui/material/ListItemAvatar'
import ListItemButton from '@mui/material/ListItemButton'
import ListItemText from '@mui/material/ListItemText'
import Typography from '@mui/material/Typography'

import { getUppercaseInitial } from '../../utils/GalleryUtils'

// Vertical Navbar for user dashboard
export default function DashSidebar (_props) {
  const user = useSelector(state => state.auth.user)
  const schematics = useSelector(state => state.dashboard.schematics)

  const button = 'My ' + process.env.REACT_APP_DIAGRAMS_NAME
  const placeholder = 'Find your ' + process.env.REACT_APP_SMALL_DIAGRAM_NAME + '...'
  return (
    <>
      <Box
        sx={{
          minHeight: '45px',
          display: { xs: 'none', sm: 'block' }
        }}
      />
      <List>
        <ListItemButton
          alignItems='flex-start'
          component={RouterLink}
          to='/dashboard'
          divider
          sx={{
            px: 2,
            py: 1.5,
            mt: '15px'
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
        </ListItemButton>
        <ListItemButton
          component={RouterLink}
          to='/dashboard/schematics'
          sx={{
            px: 2,
            py: 1.5
          }}
        >
          <ListItemText primary={button} />
        </ListItemButton>

        {/* List name of saved schematics */}
        <List
          sx={{
            p: 0,
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
        <Box
          component='div'
          sx={{
            pl: 2,
            overflow: 'auto',
            width: '100%',
            maxHeight: 200
          }}
        >
          {schematics.map((sch) => (
            <ListItemButton key={sch.save_id}>
              <ListItemText primary={`${sch.name}`} />
            </ListItemButton>
          ))}
        </Box>
        <Divider />
      </List>
    </>
  )
}
