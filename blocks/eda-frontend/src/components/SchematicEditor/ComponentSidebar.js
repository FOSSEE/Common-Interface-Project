import { useEffect, useRef, useState } from 'react'
import { TailSpin } from 'react-loader-spinner'
import { useDispatch, useSelector } from 'react-redux'

import PropTypes from 'prop-types'

import CloseIcon from '@mui/icons-material/Close'
import ExpandLess from '@mui/icons-material/ExpandLess'
import ExpandMore from '@mui/icons-material/ExpandMore'
import SearchIcon from '@mui/icons-material/Search'
import Box from '@mui/material/Box'
import Collapse from '@mui/material/Collapse'
import IconButton from '@mui/material/IconButton'
import InputAdornment from '@mui/material/InputAdornment'
import List from '@mui/material/List'
import ListItem from '@mui/material/ListItem'
import ListItemButton from '@mui/material/ListItemButton'
import ListItemIcon from '@mui/material/ListItemIcon'
import TextField from '@mui/material/TextField'
import Tooltip from '@mui/material/Tooltip'

import {
  fetchComponents,
  fetchComponentImages,
  fetchLibraries,
  toggleCollapse,
  toggleSimulate
} from '../../redux/schematicEditorSlice'
import api from '../../utils/Api'

import './Helper/SchematicEditor.css'
import SideComp from './SideComp'
import SimulationProperties from './SimulationProperties'

const COMPONENTS_PER_ROW = 3

const searchOptions = {
  NAME: 'name__istartswith'
}

export default function ComponentSidebar ({ _compRef }) {
  const libraries = useSelector(state => state.schematicEditor.libraries)
  const collapse = useSelector(state => state.schematicEditor.collapse)
  const components = useSelector(state => state.schematicEditor.components)
  const isSimulate = useSelector(state => state.schematicEditor.isSimulate)

  const dispatch = useDispatch()
  const [searchText, setSearchText] = useState('')
  const [loading, setLoading] = useState(false)

  const [searchedComponentList, setSearchedComponents] = useState([])
  const searchOption = 'NAME'

  const handleSearchText = (evt) => {
    if (searchText.length === 0) {
      setSearchedComponents([])
    }
    setSearchText(evt.target.value.trim())
    setSearchedComponents([])
    // mimic the value so we can access the latest value in our API call.

    // call api from here. and set the result to searchedComponentList.
  }

  useEffect(() => {
    // if the user keeps typing, stop the API call!
    setLoading(searchText.length !== 0)
    setSearchedComponents([])
    // don't make an API call with no data
    if (searchText.length === 0) return
    // capture the timeoutId so we can
    // stop the call if the user keeps typing
    const timeoutId = setTimeout(() => {
      // call api here
      api.get(`newblocks/?${searchOptions[searchOption]}=${searchText}`)
        .then(
          (res) => {
            if (res.data.length !== 0) {
              setSearchedComponents([...res.data])
            }
          }
        )
        .catch((err) => { console.error(err) })
      setLoading(false)
    }, 600)

    return () => {
      clearTimeout(timeoutId)
    }
  }, [searchText, searchOption])

  const handleCollapse = (id) => {
    // Fetches Components for given library if not already fetched
    if (collapse[id] === false && components[id].length === 0) {
      dispatch(fetchComponents(id))
    }

    // Updates state of collapse to show/hide dropdown
    dispatch(toggleCollapse(id))
  }

  // For Fetching Libraries
  useEffect(() => {
    dispatch(fetchLibraries())
  }, [dispatch])

  // Used to chunk array
  const chunk = (array, size) => {
    return array.reduce((chunks, item, i) => {
      if (i % size === 0) {
        chunks.push([item])
      } else {
        chunks[chunks.length - 1].push(item)
      }
      return chunks
    }, [])
  }

  const link1 = process.env.REACT_APP_BLOCKS_NAME + ' List'
  const link2 = 'Search ' + process.env.REACT_APP_BLOCK_NAME
  const link3 = 'No ' + process.env.REACT_APP_BLOCKS_NAME + ' Found'
  return (
    <>
      <Box
        sx={{
          minHeight: '90px',
          display: { xs: 'none', sm: 'block' }
        }}
      />

      {!isSimulate ? (
        <>
          <Box>
            <ListItemButton>
              <h2 style={{ margin: '5px' }}>{link1}</h2>
            </ListItemButton>
            <ListItem>
              <TextField
                id='standard-number'
                placeholder={link2}
                variant='outlined'
                size='small'
                value={searchText}
                onChange={handleSearchText}
                InputProps={{
                  startAdornment: (
                    <InputAdornment position='start'>
                      <SearchIcon />
                    </InputAdornment>
                  )
                }}
              />
            </ListItem>
            <ListItem>
              <TailSpin
                color='#F44336'
                height={100}
                width={100}
                visible={loading}
              />
            </ListItem>
          </Box>

          <Box
            sx={{
              flex: 1,
              overflowY: 'auto',
              pr: 1
            }}
          >
            <List disablePadding>
              {searchText.length === 0 && libraries.map(library => (
                <div key={library.id}>
                  <ListItemButton onClick={() => handleCollapse(library.id)} divider>
                    <Box
                      component='span'
                      sx={{
                        mr: 'auto'
                      }}
                    >
                      {library.name}
                    </Box>
                    {collapse[library.id] ? <ExpandLess /> : <ExpandMore />}
                  </ListItemButton>
                  <Collapse in={collapse[library.id]} timeout='auto' unmountOnExit mountOnEnter exit={false}>
                    <List component='div' disablePadding dense>
                      {chunk(components[library.id], COMPONENTS_PER_ROW).map((componentChunk) => (
                        <ListItem key={componentChunk[0].id} divider>
                          {componentChunk.map((component) => (
                            <ListItemIcon key={component.name}>
                              <SideComp component={component} />
                            </ListItemIcon>
                          ))}
                        </ListItem>
                      ))}
                    </List>
                  </Collapse>
                </div>
              ))}

              {!loading && searchText.length !== 0 && (
                searchedComponentList.length === 0 ? (
                  <Box component='span' sx={{ m: 2 }}>{link3}</Box>
                ) : (
                  searchedComponentList.map((component, i) => (
                    <ListItemIcon key={i}>
                      <SideComp component={component} />
                    </ListItemIcon>
                  ))
                )
              )}
            </List>
          </Box>
        </>
      ) : (
        <List>
          <ListItemButton divider>
            <h2 style={{ margin: '5px auto 5px 5px' }}>Simulation Modes</h2>
            <Tooltip title='close'>
              <IconButton
                color='inherit'
                size='small'
                onClick={() => { dispatch(toggleSimulate()) }}
              >
                <CloseIcon fontSize='small' />
              </IconButton>
            </Tooltip>
          </ListItemButton>
          <SimulationProperties />
        </List>
      )}
    </>
  )
}

export function ComponentImages () {
  const componentImages = useSelector(state => state.schematicEditor.component_images)

  const dispatch = useDispatch()

  // For Fetching Image Paths
  useEffect(() => {
    dispatch(fetchComponentImages())
  }, [dispatch])

  return (
    <div>
      {(componentImages !== undefined) && componentImages.forEach((image) => { new Image().src = '/django_static/' + image })}
    </div>
  )
}

ComponentSidebar.propTypes = {
  compRef: PropTypes.object.isRequired
}
