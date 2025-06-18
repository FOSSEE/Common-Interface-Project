import { forwardRef, useCallback, useState, useEffect } from 'react'
import PropTypes from 'prop-types'
import {
  AppBar,
  Avatar,
  Button,
  Container,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
  Divider,
  Grid,
  IconButton,
  List,
  ListItem,
  ListItemAvatar,
  ListItemText,
  Paper,
  Slide,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  TextareaAutosize,
  Toolbar,
  Tooltip,
  Typography,
  Box,
  TextField
} from '@mui/material'

import CloseIcon from '@mui/icons-material/Close'
import { useSelector, useDispatch } from 'react-redux'
import store from '../../redux/store'
import { fetchSchematic, fetchDiagram, setSchScriptDump, setShowDot } from '../../redux/saveSchematicSlice'
import { fetchSchematics, fetchGallery } from '../../redux/dashboardSlice'
import { setScriptTaskId } from '../../redux/simulationSlice'
import { blue } from '@mui/material/colors'
import { getDateTime as getDate, getUppercaseInitial, saveToFile, sanitizeTitle } from '../../utils/GalleryUtils'
import { renderGalleryXML } from './Helper/ToolbarTools'
import api from '../../utils/Api'

const Transition = forwardRef(function Transition (props, ref) {
  return <Slide direction='up' ref={ref} {...props} />
})

// Dialog box to display generated netlist
export function NetlistModal ({ open, close, netlist }) {
  const title = useSelector(state => state.saveSchematic.title)
  const createNetlistFile = () => {
    const titleA = sanitizeTitle(title)
    const name = process.env.REACT_APP_NAME
    saveToFile(`${titleA}_${name}_on_Cloud.cir`, 'text/plain', netlist)
  }
  const typography2 = 'Current netlist for given ' + process.env.REACT_APP_SMALL_DIAGRAM_NAME + '...'
  return (
    <Dialog
      open={open}
      onClose={close}
      TransitionComponent={Transition}
      keepMounted
      aria-labelledby='generate-netlist'
      aria-describedby='generate-netlist-description'
    >
      <DialogTitle id='generate-netlist-title'>Netlist Generator</DialogTitle>
      <DialogContent dividers>
        <DialogContentText id='generate-netlist-description'>
          {typography2}<br /><br />
          <TextareaAutosize aria-label='empty textarea' minRows={20} maxRows={50} style={{ minWidth: '500px' }} value={netlist} />
        </DialogContentText>
      </DialogContent>
      <DialogActions>
        {/* Button to download the netlist */}
        <Button color='primary' onClick={createNetlistFile}>
          Download
        </Button>
        <Button onClick={close} color='primary' autoFocus>
          Close
        </Button>
      </DialogActions>
    </Dialog>
  )
}

NetlistModal.propTypes = {
  open: PropTypes.bool,
  close: PropTypes.func,
  netlist: PropTypes.string
}

//To get type of variable from map value type
const getType = (type) => {
  let type_name = ''
  switch (type) {
  case '1': type_name = 'Double'; break
  case '2': type_name = 'Polynomial'; break
  case '4': type_name = 'Boolean'; break
  case '10': type_name = 'String'; break
  default: type_name = 'N/A'; break
  }
  return type_name
}

// Screen to display information about as keyboard shortcuts, units table and simulation modes
export function HelpScreen ({ open, close }) {
  return (
    <div>
      <Dialog
        fullScreen open={open} onClose={close} TransitionComponent={Transition} PaperProps={{
          style: {
            backgroundColor: '#4d4d4d',
            boxShadow: 'none'
          }
        }}
      >
        <AppBar
          position='static'
          elevation={0}
          sx={{
            position: 'relative'
          }}
        >
          <Toolbar variant='dense' style={{ backgroundColor: '#404040' }}>
            <IconButton edge='start' color='inherit' onClick={close} aria-label='close'>
              <CloseIcon />
            </IconButton>
            <Typography
              variant='h6'
              sx={{
                ml: 2,
                flex: 1
              }}
            >
              Help
            </Typography>
            <Button autoFocus color='inherit' onClick={close}>
              close
            </Button>
          </Toolbar>
        </AppBar>
        <Container
          maxWidth='lg'
          sx={{
            pt: 5,
            pb: 6,
            color: '#fff'
          }}
        >
          <Grid
            container
            spacing={3}
            direction='row'
            justifyContent='center'
            alignItems='center'
          >

            <Grid item xs={12} sm={12}>
              <Paper
                sx={{
                  p: 2,
                  textAlign: 'center',
                  bgcolor: '#404040',
                  color: '#fff'
                }}
              >
                <fieldset style={{ padding: '20px 40px' }}>
                  <legend>
                    <Typography variant='h5' align='center' component='p' gutterBottom>
                      Keyboard Shorcuts
                    </Typography>
                  </legend>
                  <Typography variant='h6' align='left' gutterBottom>
                    UNDO
                  </Typography>
                  <Typography variant='subtitle1' align='left' style={{ color: '#b3b3b3' }} gutterBottom>
                    Ctrl + Z
                  </Typography>
                  <Divider />
                  <Typography variant='h6' align='left' gutterBottom>
                    REDO
                  </Typography>
                  <Typography variant='subtitle1' align='left' style={{ color: '#b3b3b3' }} gutterBottom>
                    Ctrl + A
                  </Typography>
                  <Divider />
                  <Typography variant='h6' align='left' gutterBottom>
                    ZOOM IN
                  </Typography>
                  <Typography variant='subtitle1' align='left' style={{ color: '#b3b3b3' }} gutterBottom>
                    Ctrl + I
                  </Typography>
                  <Divider />
                  <Typography variant='h6' align='left' gutterBottom>
                    ZOOM OUT
                  </Typography>
                  <Typography variant='subtitle1' align='left' style={{ color: '#b3b3b3' }} gutterBottom>
                    Ctrl + O
                  </Typography>
                  <Divider />
                  <Typography variant='h6' align='left' gutterBottom>
                    DEFAULT SIZE
                  </Typography>
                  <Typography variant='subtitle1' align='left' style={{ color: '#b3b3b3' }} gutterBottom>
                    Ctrl + Y
                  </Typography>
                </fieldset>
              </Paper>
            </Grid>

            <Grid item xs={12} sm={12}>
              <Paper
                sx={{
                  p: 2,
                  textAlign: 'center',
                  bgcolor: '#404040',
                  color: '#fff'
                }}
              >
                <fieldset style={{ padding: '20px 40px' }}>
                  <legend>
                    <Typography variant='h5' align='center' component='p' gutterBottom>
                      Units Table
                    </Typography>
                  </legend>
                  <Typography>

                    <TableContainer component={Paper}>
                      <Table
                        aria-label='simple table'
                      >
                        <caption>Ngspice scale factors naming conventions</caption>
                        <TableHead>
                          <TableRow>
                            <TableCell align='center'>SUFFIX</TableCell>
                            <TableCell align='center'>NAME</TableCell>
                            <TableCell align='center'>FACTOR</TableCell>
                          </TableRow>
                        </TableHead>
                        <TableBody>

                          <TableRow>
                            <TableCell align='center'>T</TableCell>
                            <TableCell align='center'>Tera</TableCell>
                            <TableCell align='center'>10<sup>12</sup></TableCell>
                          </TableRow>

                          <TableRow>
                            <TableCell align='center'>G</TableCell>
                            <TableCell align='center'>Giga</TableCell>
                            <TableCell align='center'>10<sup>9</sup></TableCell>
                          </TableRow>

                          <TableRow>
                            <TableCell align='center'>Meg</TableCell>
                            <TableCell align='center'>Mega</TableCell>
                            <TableCell align='center'>10<sup>6</sup></TableCell>
                          </TableRow>

                          <TableRow>
                            <TableCell align='center'>K</TableCell>
                            <TableCell align='center'>Kilo</TableCell>
                            <TableCell align='center'>10<sup>3</sup></TableCell>
                          </TableRow>

                          <TableRow>
                            <TableCell align='center'>mil</TableCell>
                            <TableCell align='center'>Mil</TableCell>
                            <TableCell align='center'>25.4 X 10<sup>-6</sup></TableCell>
                          </TableRow>

                          <TableRow>
                            <TableCell align='center'>m</TableCell>
                            <TableCell align='center'>milli</TableCell>
                            <TableCell align='center'>10<sup>-3</sup></TableCell>
                          </TableRow>

                          <TableRow>
                            <TableCell align='center'>u</TableCell>
                            <TableCell align='center'>micro</TableCell>
                            <TableCell align='center'>10<sup>-6</sup></TableCell>
                          </TableRow>

                          <TableRow>
                            <TableCell align='center'>n</TableCell>
                            <TableCell align='center'>nano</TableCell>
                            <TableCell align='center'>10<sup>-9</sup></TableCell>
                          </TableRow>
                          <TableRow>
                            <TableCell align='center'>p</TableCell>
                            <TableCell align='center'>pico</TableCell>
                            <TableCell align='center'>10<sup>-12</sup></TableCell>
                          </TableRow>

                          <TableRow>
                            <TableCell align='center'>f</TableCell>
                            <TableCell align='center'>femto</TableCell>
                            <TableCell align='center'>10<sup>-15</sup></TableCell>
                          </TableRow>

                        </TableBody>
                      </Table>
                    </TableContainer>
                  </Typography>
                </fieldset>
              </Paper>
            </Grid>
            <Grid item xs={12} sm={12}>
              <Paper
                sx={{
                  p: 2,
                  textAlign: 'center',
                  bgcolor: '#404040',
                  color: '#fff'
                }}
              >
                <fieldset style={{ padding: '20px 40px' }}>
                  <legend>
                    <Typography variant='h5' align='center' component='p' gutterBottom>
                      Simulation Modes
                    </Typography>
                  </legend>
                  <Typography variant='h6' align='left' gutterBottom>
                    DC Solver
                  </Typography>
                  <Typography variant='subtitle1' align='left' style={{ color: '#b3b3b3' }} gutterBottom>
                    A DC simulation attempts to find a stable DC solution of your circuit.
                  </Typography>
                  <Divider />
                  <Typography variant='h6' align='left' gutterBottom>
                    DC Sweep
                  </Typography>
                  <Typography variant='subtitle1' align='left' style={{ color: '#b3b3b3' }} gutterBottom>
                    A DC Sweep will plot the DC solution of your circuit across different values of a parameter of a circuit element.
                    You can sweep any numerical parameter of any circuit element in your circuit.
                  </Typography>
                  <Divider />
                  <Typography variant='h6' align='left' gutterBottom>
                    Transient Analysis
                  </Typography>
                  <Typography variant='subtitle1' align='left' style={{ color: '#b3b3b3' }} gutterBottom>
                    A Transient analysis does a Time-Domain Simulation of your circuit over a certain period of time.
                  </Typography>
                  <Divider />
                  <Typography variant='h6' align='left' gutterBottom>
                    AC Analysis
                  </Typography>
                  <Typography variant='subtitle1' align='left' style={{ color: '#b3b3b3' }} gutterBottom>
                    AC Analysis does a small signal analysis of your circuit. The input can be any voltage source or current source.
                  </Typography>
                </fieldset>
              </Paper>
            </Grid>
          </Grid>
        </Container>
      </Dialog>
    </div>
  )
}

HelpScreen.propTypes = {
  open: PropTypes.bool,
  close: PropTypes.func
}

export function ScriptScreen ({ isOpen, onClose }) {
  const scriptDump = useSelector(state => state.saveSchematic.scriptDump)
  const title = useSelector(state => state.saveSchematic.title)
  const showDot = useSelector(state => state.saveSchematic.showDot)
  const hasScript = useSelector(state => state.saveSchematic.hasScript)
  const dispatch = useDispatch()
  const [result, setResult] = useState('No output yet...')
  const [variables, setVariables] = useState([])
  const scriptHandler = (e) => {
    dispatch(setSchScriptDump(e.target.value))
    dispatch(setShowDot(true))
  }

  const sendScriptNetlist = useCallback((file, type) => {
    netlistConfig(file, type)
      .then((response) => {
        const data = response.data
        const taskId = data.task_id
        dispatch(setScriptTaskId(taskId))

        console.log('taskId2:', taskId)
        setResult(data.output || 'No output available.')
        setVariables(data.variables)
      })
      .catch(function (error) {
        console.error(error)
      })
  }, [dispatch])

  const prepareScriptNetlist = useCallback((scriptDump) => {
    const titleA = sanitizeTitle(title)
    const myblob = new Blob([scriptDump], {
      type: 'text/plain'
    })
    const file = new File([myblob], `${titleA}.sce`, { type: 'text/sce', lastModified: Date.now() })
    const type = 'SCRIPT'
    sendScriptNetlist(file, type)
  }, [sendScriptNetlist, title])

  const executeScript = useCallback(() => {
    const scriptDump = store.getState().saveSchematic.scriptDump
    if (!scriptDump) {
      return
    }

    dispatch(setScriptTaskId(''))
    prepareScriptNetlist(scriptDump)
    dispatch(setShowDot(false))
  }, [dispatch, prepareScriptNetlist])

  useEffect(() => {
    const isSelenium = typeof navigator !== 'undefined' && navigator.webdriver === true
    if (isSelenium || !hasScript) {
      return
    }

    const timer = setTimeout(() => {
      executeScript()
    }, 1000)

    return () => clearTimeout(timer)
  }, [executeScript, hasScript])

  async function netlistConfig (file, type) {
    const formData = new FormData()

    formData.append('app_name', process.env.REACT_APP_NAME)
    formData.append('file', file)
    formData.append('type', type)

    const config = {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    }
    return await api.post('simulation/upload', formData, config)
  }

  const resetCode = () => {
    dispatch(setSchScriptDump(''))
    dispatch(setShowDot(false))
    dispatch(setScriptTaskId(''))
    setResult('No output yet...')
    setVariables('')
  }

  return (
    <Dialog fullScreen open={isOpen} onClose={onClose}>
      {/* Top AppBar */}
      <AppBar position='static'>
        <Toolbar>
          <Typography variant='h6' sx={{ flexGrow: 1 }}>
            Script Editor
          </Typography>
          <IconButton edge='end' color='inherit' onClick={onClose}>
            <CloseIcon />
          </IconButton>
        </Toolbar>
      </AppBar>

      {/* Main Content */}
      <Box sx={{ p: 4 }}>

        {/* Code and Result Sections */}
        <Box
          sx={{
            display: 'grid',
            gridTemplateColumns: { xs: '1fr', md: '1fr 1fr' },
            gap: 4,
            alignItems: 'stretch'
          }}
        >
          <Box
            sx={{
              p: 2,
              boxShadow: 2,
              borderRadius: 2,
              display: 'flex',
              flexDirection: 'column',
              flexGrow: 1
            }}
          >
            <Typography variant="subtitle1" style={{ fontWeight: 'bold', mb: 1 }}>
              Scilab Code:
            </Typography>

            <Box
              sx={{
                height: '500px',
                overflowY: 'auto',
                border: '1px solid #ccc',
                borderRadius: 1
              }}
            >
              <TextField
                value={scriptDump}
                onChange={scriptHandler}
                multiline
                variant='outlined'
                fullWidth
                InputProps={{
                  style: {
                    fontFamily: '"Roboto Mono", monospace',
                    fontSize: '14px'
                  }
                }}
              />
            </Box>
            <Box sx={{ mt: 4, display: 'flex', gap: 4 }}>
              <Button onClick={executeScript} color='primary' variant='contained' disabled={!showDot}>
                Execute
              </Button>
              <Button onClick={resetCode} color='secondary' variant='contained'>
                Reset
              </Button>
            </Box>
          </Box>

          <Box
            sx={{
              p: 2,
              boxShadow: 2,
              borderRadius: 2,
              display: 'flex',
              flexDirection: 'column',
              height: '100%'
            }}
          >
            <Typography variant="subtitle1" style={{ fontWeight: 'bold', mb: 1 }}>
              Result:
            </Typography>
            <Box
              sx={{
                flexGrow: 1,
                width: '100%',
                p: 2,
                border: '1px solid gray',
                borderRadius: 1,
                overflowY: 'auto',
                display: 'flex',
                height: '500px',
                whiteSpace: 'pre-wrap', // Keep line breaks
                fontFamily: '"Roboto Mono", monospace'
              }}
            >
              {result}
            </Box>

            <Typography variant="subtitle1" style={{ fontWeight: 'bold', marginTop: 16 }}>
              Variable Browser :
            </Typography>
            <Box
              style={{
                flexGrow: 1,
                padding: 8,
                border: '1px solid gray',
                borderRadius: 4
              }}
            >
              <TableContainer
                component={Paper}
                elevation={0}
                style={{ maxHeight: 150 }}
              >
                <Table size="small" stickyHeader>
                  <TableHead>
                    <TableRow style={{ backgroundColor: '#e0e0e0' }}>
                      <TableCell
                        style={{
                          border: '1px solid gray',
                          fontWeight: 'bold',
                          padding: '4px 8px'
                        }}
                      >
                        Name
                      </TableCell>
                      <TableCell
                        style={{
                          border: '1px solid gray',
                          fontWeight: 'bold',
                          padding: '4px 8px'
                        }}
                      >
                        Value
                      </TableCell>
                      <TableCell
                        style={{
                          border: '1px solid gray',
                          fontWeight: 'bold',
                          padding: '4px 8px'
                        }}
                      >
                        Type
                      </TableCell>
                    </TableRow>
                  </TableHead>
                  <TableBody>
                    {variables?.length > 0
                      ? (
                        variables.map((variable, index) => (
                          <TableRow key={index}>
                            <TableCell style={{ border: '1px solid gray', padding: '4px 8px' }}>
                              {variable.name}
                            </TableCell>
                            <TableCell style={{ border: '1px solid gray', padding: '4px 8px', maxWidth: '300px', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                              <Tooltip title={<span style={{ whiteSpace: 'pre-wrap' }}>{variable.value}</span>} arrow>
                                <span style={{ cursor: 'pointer', display: 'inline-block', overflow: 'hidden', textOverflow: 'ellipsis', maxWidth: '100%' }}>
                                  {variable.value}
                                </span>
                              </Tooltip>
                            </TableCell>
                            <TableCell style={{ border: '1px solid gray', padding: '4px 8px' }}>
                              {getType(variable.type)}
                            </TableCell>
                          </TableRow>
                        ))
                      )
                      : (
                        <TableRow>
                          <TableCell colSpan={3} align="center">
                            No variables available.
                          </TableCell>
                        </TableRow>
                      )}
                  </TableBody>
                </Table>
              </TableContainer>
            </Box>
          </Box>

        </Box>

        {/* Action Buttons */}

      </Box>
    </Dialog>
  )
}

// PropTypes validation
ScriptScreen.propTypes = {
  isOpen: PropTypes.bool.isRequired,
  onClose: PropTypes.func.isRequired
}

// Image Export Dialog box
const ImgTypes = ['PNG', 'JPG', 'SVG']
export function ImageExportDialog (props) {
  const { onClose, open } = props

  const handleClose = () => {
    onClose('')
  }

  const handleListItemClick = (value) => {
    onClose(value)
  }

  return (
    <Dialog onClose={handleClose} aria-labelledby='image-export-dialog-title' open={open}>
      <DialogTitle id='image-export-dialog-title'>Select Image type</DialogTitle>
      <List>
        {ImgTypes.map((img) => (
          <ListItem button onClick={() => handleListItemClick(img)} key={img}>
            <ListItemAvatar>
              <Avatar
                sx={{
                  width: { xs: 28, sm: 32, md: 40 },
                  height: { xs: 28, sm: 32, md: 40 },
                  bgcolor: blue[100],
                  color: blue[600]
                }}
              >
                {getUppercaseInitial(img)}
              </Avatar>
            </ListItemAvatar>
            <ListItemText primary={img} />
          </ListItem>
        ))}
      </List>
      <DialogActions>
        <Button onClick={handleClose} color='primary' autoFocus>
          Close
        </Button>
      </DialogActions>
    </Dialog>
  )
}

ImageExportDialog.propTypes = {
  onClose: PropTypes.func.isRequired,
  open: PropTypes.bool.isRequired
}

// Dialog box to open saved Schematics
export function OpenSchDialog (props) {
  const { open, close, openLocal } = props
  const [isLocal, setisLocal] = useState(true)
  const [isGallery, setisGallery] = useState(false)
  const details = useSelector(state => state.saveSchematic.details)
  const isAuthenticated = useSelector(state => state.auth.isAuthenticated)
  const user = useSelector(state => state.auth.user)
  const schematics = useSelector(state => state.dashboard.schematics)
  const GallerySchSample = useSelector(state => state.dashboard.gallery)
  const xmlData = useSelector(state => state.saveSchematic.xmlData)

  const dispatch = useDispatch()

  useEffect(() => {
    dispatch(fetchGallery())
  }, [dispatch])

  useEffect(() => {
    if (xmlData) {
      renderGalleryXML(xmlData)
    }
  }, [xmlData])

  const title = 'Open ' + process.env.REACT_APP_DIAGRAM_NAME
  const typography1 = 'You don\'t have any saved ' + process.env.REACT_APP_SMALL_DIAGRAMS_NAME + '...'
  return (
    <Dialog
      open={open}
      onClose={close}
      maxWidth='md'
      TransitionComponent={Transition}
      keepMounted
      aria-labelledby='open-dialog-title'
      aria-describedby='open-dialog-description'
    >
      <DialogTitle id='open-dialog-title' onClose={close}>
        <Typography component='span' variant='h3'>{title}</Typography>
      </DialogTitle>
      <DialogContent dividers>
        <DialogContentText id='open-dialog-description'>
          {isLocal
            ? <Button variant='outlined' fullWidth size='large' onClick={() => { openLocal(); close() }} color='primary'>
              Upload File
            </Button>
            : isGallery
              ? <Grid item xs={12} sm={12}>
                {/* Listing Gallery Schematics */}
                <TableContainer component={Paper} style={{ maxHeight: '45vh' }}>
                  <Table stickyHeader size='small' aria-label='simple table'>
                    <TableHead>
                      <TableRow>
                        <TableCell align='center'>Name</TableCell>
                        <TableCell align='center'>Description</TableCell>
                        <TableCell align='center'>Launch</TableCell>
                      </TableRow>
                    </TableHead>
                    <TableBody>
                      <>
                        {GallerySchSample.map(
                          (sch) => {
                            return (
                              <TableRow key={sch.save_id}>
                                <TableCell align='center'>{sch.name}</TableCell>
                                <TableCell align='center'>
                                  <Tooltip title={sch.description !== null ? sch.description : 'No description'}>
                                    <span>
                                      {sch.description !== null ? sch.description.slice(0, 30) + (sch.description.length < 30 ? '' : '...') : '-'}
                                    </span>
                                  </Tooltip>
                                </TableCell>
                                <TableCell align='center'>
                                  <Button
                                    size='small'
                                    color='primary'
                                    onClick={() => { dispatch(fetchDiagram(sch.save_id)) }}
                                    variant={details.save_id === undefined ? 'outlined' : details.save_id !== sch.save_id ? 'outlined' : 'contained'}
                                  >
                                    Launch
                                  </Button>
                                </TableCell>
                              </TableRow>
                            )
                          }
                        )}
                      </>
                    </TableBody>
                  </Table>
                </TableContainer>
              </Grid>
              : <Grid item xs={12} sm={12}>
                {/* Listing Saved Schematics */}
                {schematics.length === 0
                  ? <Typography variant='subtitle1' gutterBottom>
                    Hey {user.username} , {typography1}
                  </Typography>
                  : <TableContainer component={Paper} style={{ maxHeight: '45vh' }}>
                    <Table stickyHeader size='small' aria-label='simple table'>
                      <TableHead>
                        <TableRow>
                          <TableCell align='center'>Name</TableCell>
                          <TableCell align='center'>Description</TableCell>
                          <TableCell align='center'>Created</TableCell>
                          <TableCell align='center'>Updated</TableCell>
                          <TableCell align='center'>Launch</TableCell>
                        </TableRow>
                      </TableHead>
                      <TableBody>
                        <>
                          {schematics.map(
                            (sch) => {
                              return (
                                <TableRow key={sch.save_id}>
                                  <TableCell align='center'>{sch.name}</TableCell>
                                  <TableCell align='center'>
                                    <Tooltip title={sch.description !== null ? sch.description : 'No description'}>
                                      <span>
                                        {sch.description !== null ? sch.description.slice(0, 30) + (sch.description.length < 30 ? '' : '...') : '-'}
                                      </span>
                                    </Tooltip>
                                  </TableCell>
                                  <TableCell align='center'>{getDate(sch.create_time)}</TableCell>
                                  <TableCell align='center'>{getDate(sch.save_time)}</TableCell>
                                  <TableCell align='center'>
                                    <Button
                                      size='small'
                                      color='primary'
                                      onClick={() => { dispatch(fetchSchematic(sch.save_id)) }}
                                      variant={details.save_id === undefined ? 'outlined' : details.save_id !== sch.save_id ? 'outlined' : 'contained'}
                                    >
                                      Launch
                                    </Button>
                                  </TableCell>
                                </TableRow>
                              )
                            }
                          )}
                        </>
                      </TableBody>
                    </Table>
                  </TableContainer>}
              </Grid>}
        </DialogContentText>
      </DialogContent>
      <DialogActions>
        <Button variant={isLocal ? 'outlined' : 'text'} onClick={() => { setisLocal(true); setisGallery(false) }} color='secondary'>
          Local
        </Button>
        <Button variant={isGallery ? 'outlined' : 'text'} onClick={() => { setisLocal(false); setisGallery(true) }} color='secondary'>
          Gallery
        </Button>
        {isAuthenticated !== true
          ? <></>
          : <Button variant={!isGallery & !isLocal ? 'outlined' : 'text'} onClick={() => { dispatch(fetchSchematics()); setisLocal(false); setisGallery(false) }} color='secondary'>
            on Cloud
          </Button>}
        <Button onClick={close} color='primary' autoFocus>
          Close
        </Button>
      </DialogActions>
    </Dialog>
  )
}

OpenSchDialog.propTypes = {
  close: PropTypes.func.isRequired,
  open: PropTypes.bool.isRequired,
  openLocal: PropTypes.func.isRequired
}
