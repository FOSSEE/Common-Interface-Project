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
  const [isSearchedResultsEmpty, setIssearchedResultsEmpty] = useState(false)
  const [searchText, setSearchText] = useState('')
  const [loading, setLoading] = useState(false)

  const [searchedComponentList, setSearchedComponents] = useState([])
  const searchOption = 'NAME'

  const timeoutId = useRef()

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
    clearTimeout(timeoutId.current)
    setSearchedComponents([])
    // don't make an API call with no data
    if (searchText.length === 0) return
    // capture the timeoutId so we can
    // stop the call if the user keeps typing
    timeoutId.current = setTimeout(() => {
      // call api here
      setLoading(true)

      api.get(`newblocks/?${searchOptions[searchOption]}=${searchText}`)
        .then(
          (res) => {
            if (res.data.length === 0) {
              setIssearchedResultsEmpty(true)
            } else {
              setIssearchedResultsEmpty(false)
              setSearchedComponents([...res.data])
            }
          }
        )
        .catch((err) => { console.error(err) })
      setLoading(false)
    }, 800)
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

      <div style={isSimulate ? { display: 'none' } : {}}>
        {/* Display List of categorized components */}
        <List>
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

          <div style={{ maxHeight: '70vh', overflowY: 'auto', overflowX: 'hidden' }}>
            {searchText.length !== 0 && searchedComponentList.length !== 0 &&

              searchedComponentList.map((component, i) => {
                return (
                  <ListItemIcon key={i}>
                    <SideComp component={component} />
                  </ListItemIcon>
                )
              }
              )}

            <ListItem>

              <TailSpin
                color='#F44336'
                height={100}
                width={100}
                visible={loading}
              />
            </ListItem>

            {!loading && searchText.length !== 0 && isSearchedResultsEmpty &&

              <span style={{ margin: '20px' }}>{link3}</span>}

            {/* Collapsing List Mapped by Libraries fetched by the API */}
            {searchText.length === 0 &&
              libraries.map(
                (library) => {
                  return (
                    <div key={library.id}>
                      <ListItemButton onClick={(e, id = library.id) => handleCollapse(id)} divider>
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

                          {/* Chunked Blocks of Library */}
                          {
                            chunk(components[library.id], COMPONENTS_PER_ROW).map((componentChunk) => {
                              return (
                                <ListItem key={componentChunk[0].id} divider>
                                  {
                                    componentChunk.map((component) => {
                                      return (
                                        <ListItemIcon key={component.name}>
                                          <SideComp component={component} />
                                        </ListItemIcon>
                                      )
                                    }
                                    )
                                  }
                                </ListItem>
                              )
                            })
                          }

                        </List>
                      </Collapse>
                    </div>
                  )
                }
              )}
          </div>
        </List>
      </div>
      <div style={isSimulate ? {} : { display: 'none' }}>
        {/* Display simulation modes parameters on left side pane */}
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
      </div>
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
