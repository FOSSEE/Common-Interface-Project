import React, { useEffect, useState } from 'react'
import PropTypes from 'prop-types'
import api from '../../utils/Api'
import {
  Hidden,
  List,
  ListItem,
  Collapse,
  ListItemIcon,
  IconButton,
  Tooltip,
  TextField,
  InputAdornment

} from '@material-ui/core'
import Loader from 'react-loader-spinner'
import SearchIcon from '@material-ui/icons/Search'

import { makeStyles } from '@material-ui/core/styles'
import ExpandLess from '@material-ui/icons/ExpandLess'
import ExpandMore from '@material-ui/icons/ExpandMore'
import CloseIcon from '@material-ui/icons/Close'

import './Helper/SchematicEditor.css'
import { useDispatch, useSelector } from 'react-redux'
import { fetchLibraries, toggleCollapse, fetchComponents, toggleSimulate } from '../../redux/actions/index'
import SideComp from './SideComp.js'
import SimulationProperties from './SimulationProperties'
const COMPONENTS_PER_ROW = 3

const useStyles = makeStyles((theme) => ({
  toolbar: {
    minHeight: '90px'
  },
  nested: {
    paddingLeft: theme.spacing(2),
    width: '100%'
  },
  head: {
    marginRight: 'auto'
  }
}))

const searchOptions = {
  NAME: 'name__istartswith',
}

export default function ComponentSidebar ({ compRef }) {
  const classes = useStyles()
  const libraries = useSelector(state => state.schematicEditorReducer.libraries)
  const collapse = useSelector(state => state.schematicEditorReducer.collapse)
  const components = useSelector(state => state.schematicEditorReducer.components)
  const isSimulate = useSelector(state => state.schematicEditorReducer.isSimulate)

  const dispatch = useDispatch()
  const [isSearchedResultsEmpty, setIssearchedResultsEmpty] = useState(false)
  const [searchText, setSearchText] = useState('')
  const [loading, setLoading] = useState(false)

  const [searchedComponentList, setSearchedComponents] = useState([])
  const searchOption = 'NAME'

  const timeoutId = React.useRef()

  const handleSearchText = (evt) => {
    if (searchText.length === 0) {
      setSearchedComponents([])
    }
    setSearchText(evt.target.value.trim())
    setSearchedComponents([])
    // mimic the value so we can access the latest value in our API call.

    // call api from here. and set the result to searchedComponentList.
  }

  React.useEffect(() => {
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

      api.get(`blocks/?${searchOptions[searchOption]}=${searchText}`)
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
      <Hidden smDown>
        <div className={classes.toolbar} />
      </Hidden>

      <div style={isSimulate ? { display: 'none' } : {}}>
        {/* Display List of categorized components */}
        <List>
          <ListItem button>
            <h2 style={{ margin: '5px' }}>{link1}</h2>
          </ListItem>
          <ListItem>

            <TextField
              id="standard-number"
              placeholder={link2}
              variant="outlined"
              size="small"
              value={searchText}
              onChange={handleSearchText}
              InputProps={{
                startAdornment: (
                  <InputAdornment position="start">
                    <SearchIcon />
                  </InputAdornment>

                )

              }}
            />

          </ListItem>

          <div style={{ maxHeight: '70vh', overflowY: 'auto', overflowX: 'hidden' }} >
            {searchText.length !== 0 && searchedComponentList.length !== 0 &&

              searchedComponentList.map((component, i) => {
                return (<ListItemIcon key={i}>
                  <SideComp component={component} />
                </ListItemIcon>)
              }
              )

            }

            <ListItem>

              <Loader
                type="TailSpin"
                color="#F44336"
                height={100}
                width={100}
                visible={loading}
              />
            </ListItem>

            {!loading && searchText.length !== 0 && isSearchedResultsEmpty &&

              <span style={{ margin: '20px' }}>{link3}</span>

            }

            {/* Collapsing List Mapped by Libraries fetched by the API */}
            {searchText.length === 0 &&
              libraries.map(
                (library) => {
                  return (
                    <div key={library.id}>
                      <ListItem onClick={(e, id = library.id) => handleCollapse(id)} button divider>
                        <span className={classes.head}>{library.name}</span>
                        {collapse[library.id] ? <ExpandLess /> : <ExpandMore />}
                      </ListItem>
                      <Collapse in={collapse[library.id]} timeout={'auto'} unmountOnExit mountOnEnter exit={false}>
                        <List component="div" disablePadding dense >

                          {/* Chunked Blocks of Library */}
                          {
                            chunk(components[library.id], COMPONENTS_PER_ROW).map((componentChunk) => {
                              return (
                                <ListItem key={componentChunk[0].id} divider>
                                  {
                                    componentChunk.map((component) => {
                                      return (<ListItemIcon key={component.name}>
                                        <SideComp component={component} />
                                      </ListItemIcon>)
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
              )
            }
          </div>
        </List>
      </div>
      <div style={isSimulate ? {} : { display: 'none' }}>
        {/* Display simulation modes parameters on left side pane */}
        <List>
          <ListItem button divider>
            <h2 style={{ margin: '5px auto 5px 5px' }}>Simulation Modes</h2>
            <Tooltip title="close">
              <IconButton color="inherit" className={classes.tools} size="small" onClick={() => { dispatch(toggleSimulate()) }}>
                <CloseIcon fontSize="small" />
              </IconButton>
            </Tooltip>
          </ListItem>
          <SimulationProperties />
        </List>
      </div>
    </>
  )
}

ComponentSidebar.propTypes = {
  compRef: PropTypes.object.isRequired
}
