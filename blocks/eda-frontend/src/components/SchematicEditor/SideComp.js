import React, { createRef, useEffect, useState } from 'react'
import PropTypes from 'prop-types'

import { List, ListItemText, Tooltip, Popover } from '@mui/material'
import { makeStyles } from '@mui/styles'

import './Helper/SchematicEditor.css'
import { AddComponent } from './Helper/SideBar'

const useStyles = makeStyles((theme) => ({
  popupInfo: {
    margin: theme.spacing(1.5),
    padding: theme.spacing(1.5),
    border: '1px solid blue',
    borderRadius: '5px'
  }
}))

export default function SideComp ({ component }) {
  const classes = useStyles()
  const imageRef = createRef()

  const [anchorEl, setAnchorEl] = useState(null)

  const handleClick = (event) => {
    setAnchorEl(event.currentTarget)
  }
  const handleClose = () => {
    setAnchorEl(null)
  }

  const open = Boolean(anchorEl)
  const id = open ? 'simple-popover' : undefined

  useEffect(() => {
    // Function call to make components draggable
    AddComponent(component, imageRef.current)
  }, [component])

  const link1 = process.env.REACT_APP_BLOCK_NAME + ' Name'
  const link2 = process.env.REACT_APP_CATEGORY_NAME
  const link3 = process.env.REACT_APP_CATEGORIES_NAME
  return (
    <div>

      <Tooltip title={component.name} arrow>
        {/* Display Image thumbnail in left side pane */}
        <img ref={imageRef} className='compImage' src={'/django_static/' + component.block_image_path} alt={component.name} aria-describedby={id} onClick={handleClick} />
      </Tooltip>

      {/* Popover to display component information on single click */}
      <Popover
        id={id}
        open={open}
        className={classes.popup}
        anchorEl={anchorEl}
        onClose={handleClose}
        anchorOrigin={{
          vertical: 'bottom',
          horizontal: 'center'
        }}
        transformOrigin={{
          vertical: 'top',
          horizontal: 'center'
        }}
      >
        <List component='div' className={classes.popupInfo} disablePadding dense>
          <ListItemText>
            <b>{link1}:</b> {component.name}
          </ListItemText>

          {
            component.categories.length === 1 &&
              <ListItemText>
                <b>{link2}:</b> {component.categories[0].name}
              </ListItemText>
          }

          {
            component.categories.length > 1 &&
              <ListItemText>
                <b>{link3}:</b> {component.categories.map((c) => <li key={c.id}>{c.name}</li>)}
              </ListItemText>
          }

        </List>
      </Popover>

    </div>
  )
}

SideComp.propTypes = {
  component: PropTypes.object.isRequired
}
