import { useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'

import PropTypes from 'prop-types'

import Box from '@mui/material/Box'
import List from '@mui/material/List'
import ListItem from '@mui/material/ListItem'
import ListItemButton from '@mui/material/ListItemButton'
import ListItemText from '@mui/material/ListItemText'
import MenuItem from '@mui/material/MenuItem'
import TextareaAutosize from '@mui/material/TextareaAutosize'
import TextField from '@mui/material/TextField'

import { setSchDescription } from '../../redux/saveSchematicSlice'

import ComponentProperties from './ComponentProperties'

import './Helper/SchematicEditor.css'

const pageSize = [
  {
    value: 'A1',
    label: 'A1'
  },
  {
    value: 'A2',
    label: 'A2'
  },
  {
    value: 'A3',
    label: 'A3'
  },
  {
    value: 'A4',
    label: 'A4'
  },
  {
    value: 'A5',
    label: 'A5'
  }
]

const pageLayout = [
  {
    value: 'P',
    label: 'Portrait'
  },
  {
    value: 'L',
    label: 'Landscape'
  }
]

// Display grid size and orientation
function GridProperties ({ gridRef }) {
  const [gridSize, setGridSize] = useState('A4')
  const [gridLayout, setGridLayout] = useState('L')

  const handleSizeChange = (event) => {
    setGridSize(event.target.value)
    gridRef.current.className = 'grid-container ' + event.target.value + '-' + gridLayout
  }

  const handleLayoutChange = (event) => {
    setGridLayout(event.target.value)
    gridRef.current.className = 'grid-container ' + gridSize + '-' + event.target.value
  }

  return (
    <>
      <ListItem>
        <ListItemText primary='Grid Properties' />
      </ListItem>
      <ListItem style={{ padding: '10px 5px 15px 5px' }} divider>
        <TextField
          id='filled-select-currency'
          select
          size='small'
          value={gridSize}
          onChange={handleSizeChange}
          helperText='Grid size'
          variant='outlined'
          sx={{
            mx: 0.7,
            my: 0
          }}
        >
          {pageSize.map((option) => (
            <MenuItem key={option.value} value={option.value}>
              {option.label}
            </MenuItem>
          ))}
        </TextField>
        <TextField
          id='grid-layout'
          select
          size='small'
          value={gridLayout}
          onChange={handleLayoutChange}
          helperText='Grid Layout'
          variant='outlined'
          sx={{
            mx: 0.7,
            my: 0
          }}
        >
          {pageLayout.map((option) => (
            <MenuItem key={option.value} value={option.value}>
              {option.label}
            </MenuItem>
          ))}
        </TextField>
      </ListItem>

    </>
  )
}
GridProperties.propTypes = {
  gridRef: PropTypes.object.isRequired
}

export default function PropertiesSidebar ({ gridRef, outlineRef }) {
  const isOpen = useSelector(state => state.componentProperties.isPropertiesWindowOpen)
  const description1 = useSelector(state => state.saveSchematic.description)

  const [description, setDescription] = useState(description1)

  const dispatch = useDispatch()

  const getInputValues = (evt) => {
    setDescription(`${evt.target.value}`)
    dispatch(setSchDescription(evt.target.value))
  }

  const typography1 = process.env.REACT_APP_DIAGRAM_NAME + ' Description'
  const typography2 = 'Add ' + process.env.REACT_APP_DIAGRAM_NAME + ' Description'
  const typography3 = process.env.REACT_APP_BLOCKS_NAME + ' Position'
  return (
    <>
      <Box
        sx={{
          minHeight: '90px',
          display: { xs: 'none', md: 'block' }
        }}
      />

      <List>
        <ListItemButton divider>
          <h2 style={{ margin: '5px' }}>Properties</h2>
        </ListItemButton>
        <div style={isOpen ? { display: 'none' } : {}}>
          <GridProperties gridRef={gridRef} />

          {/* Display component position box */}
          <ListItem>
            <ListItemText primary={typography3} />
          </ListItem>
          <ListItem style={{ padding: '0px' }} divider>
            <div className='outline-container' ref={outlineRef} id='outlineContainer' />
          </ListItem>

          {/* Input form field for schematic description */}
          <ListItem>
            <ListItemText primary={typography1} />
          </ListItem>
          <ListItem style={{ padding: '0px 7px 7px 7px' }} divider>
            <TextareaAutosize id='Description' label='Description' value={description1 === '' ? description || '' : description1} onChange={getInputValues} minRows={6} aria-label='Description' placeholder={typography2} style={{ width: '100%', minWidth: '234px', maxHeight: '250px' }} />
          </ListItem>
        </div>
      </List>

      <ComponentProperties />
    </>
  )
}

PropertiesSidebar.propTypes = {
  gridRef: PropTypes.object.isRequired,
  outlineRef: PropTypes.object.isRequired
}
