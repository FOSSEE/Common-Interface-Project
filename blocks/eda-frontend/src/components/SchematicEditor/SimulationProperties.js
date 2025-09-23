import { useState } from 'react'
import { useSelector, useDispatch } from 'react-redux'

import ExpandMoreIcon from '@mui/icons-material/ExpandMore'
import Accordion from '@mui/material/Accordion'
import AccordionDetails from '@mui/material/AccordionDetails'
import AccordionSummary from '@mui/material/AccordionSummary'
import Box from '@mui/material/Box'
import Button from '@mui/material/Button'
import InputAdornment from '@mui/material/InputAdornment'
import List from '@mui/material/List'
import ListItem from '@mui/material/ListItem'
import MenuItem from '@mui/material/MenuItem'
import TextField from '@mui/material/TextField'
import Typography from '@mui/material/Typography'

import { setResultTitle, setResultTaskId, resetResult } from '../../redux/simulationSlice'
import store from '../../redux/store'
import api from '../../utils/Api'
import { sanitizeTitle } from '../../utils/GalleryUtils'
import { isStatusDone } from '../Shared/Graph'

import { saveXml } from './Helper/ToolbarTools'
import SimulationScreen, { setGraphStatusClosed } from './SimulationScreen'

export default function SimulationProperties () {
  const title = useSelector(state => state.saveSchematic.title)
  const isSimRes = useSelector(state => state.simulation.isSimRes)
  const dispatch = useDispatch()
  const [transientAnalysisControlLine, setTransientAnalysisControlLine] = useState({
    final_integration_time: '30',
    real_time_scaling: '0',
    integrator_absolute_tolerance: '1E-6',
    integrator_relative_tolerance: '1E-6',
    tolerance_on_time: '1E-10',
    max_integration_time_interval: '100001',
    solver_kind: '1',
    maximum_step_size: '0'
  })

  const handleTransientAnalysisControlLine = (evt) => {
    const value = evt.target.value

    setTransientAnalysisControlLine({
      ...transientAnalysisControlLine,
      [evt.target.id]: value
    })
  }

  const [simulateOpen, setSimulateOpen] = useState(false)

  const handleSimulateOpen = () => {
    setSimulateOpen(true)
  }

  const handleSimulateClose = (taskId) => {
    if (taskId && !isStatusDone()) {
      const getUrl = 'simulation/cancel/' + taskId
      api.get(getUrl)
    }
    setGraphStatusClosed()
    setSimulateOpen(false)
  }

  // Prepare Netlist to file
  const prepareNetlist = (netlist) => {
    const titleA = sanitizeTitle(title)
    const myblob = new Blob([netlist], {
      type: 'text/plain'
    })
    const file = new File([myblob], `${titleA}.xml`, { type: 'text/xml', lastModified: Date.now() })
    const type = 'XCOS'
    sendNetlist(file, type)
  }

  function sendNetlist (file, type) {
    netlistConfig(file, type)
      .then((response) => {
        const res = response.data
        const taskId = res.task_id
        dispatch(setResultTaskId(taskId))
      })
      .catch(function (error) {
        console.error(error)
      })
  }

  // Upload the nelist
  async function netlistConfig (file, type) {
    const scriptTaskId = store.getState().simulation.scriptTaskId
    const formData = new FormData()
    formData.append('app_name', process.env.REACT_APP_NAME)
    formData.append('file', file)
    formData.append('type', type)
    if (scriptTaskId) {
      formData.append('script_task_id', scriptTaskId)
    }

    for (const [key, value] of Object.entries(transientAnalysisControlLine)) {
      formData.append(key, value)
    }
    const config = {
      headers: {
        'Content-Type': 'multipart/form-data'
      }
    }
    return await api.post('simulation/upload', formData, config)
  }

  const startSimulate = (type) => {
    dispatch(resetResult())

    const compNetlist = saveXml()
    switch (type) {
    case 'Transient':
      dispatch(setResultTitle('Transient Analysis Output'))
      break
    default:
      break
    }

    const netlist = compNetlist

    prepareNetlist(netlist)

    handleSimulateOpen()
  }

  // simulation properties add expression input box
  return (
    <>
      <div>
        {
          simulateOpen
            ? <SimulationScreen open={simulateOpen} close={handleSimulateClose} />
            : <div />
        }

        {/* Simulation modes list */}
        <List>

          {/* Transient Analysis */}
          <ListItem
            divider
            sx={{
              m: 0,
              p: 0,
              width: '100%'
            }}
          >
            <Accordion>
              <AccordionSummary
                expandIcon={<ExpandMoreIcon />}
                aria-controls='panel1a-content'
                id='panel1a-header'
              >
                <Typography
                  sx={{
                    fontSize: '15px',
                    fontWeight: 400
                  }}
                >
                  Transient Analysis
                </Typography>
              </AccordionSummary>
              <AccordionDetails>
                <Box
                  component='form'
                  noValidate
                  autoComplete='off'
                  sx={{
                    width: '100%'
                  }}
                >
                  <List>
                    <ListItem>
                      <TextField
                        id='final_integration_time' label='Final integration time' size='small' variant='outlined'
                        InputProps={{ endAdornment: <InputAdornment position='end'>S</InputAdornment> }}
                        value={transientAnalysisControlLine.final_integration_time}
                        onChange={handleTransientAnalysisControlLine}
                      />
                    </ListItem>
                    <ListItem>
                      <TextField
                        id='real_time_scaling' label='Real time scaling' size='small' variant='outlined'
                        value={transientAnalysisControlLine.real_time_scaling}
                        onChange={handleTransientAnalysisControlLine}
                      />
                    </ListItem>
                    <ListItem>
                      <TextField
                        id='integrator_absolute_tolerance' label='Integrator absolute tolerance' size='small' variant='outlined'
                        value={transientAnalysisControlLine.integrator_absolute_tolerance}
                        onChange={handleTransientAnalysisControlLine}
                      />
                    </ListItem>
                    <ListItem>
                      <TextField
                        id='integrator_relative_tolerance' label='Integrator relative tolerance' size='small' variant='outlined'
                        value={transientAnalysisControlLine.integrator_relative_tolerance}
                        onChange={handleTransientAnalysisControlLine}
                      />
                    </ListItem>
                    <ListItem>
                      <TextField
                        id='tolerance_on_time' label='Tolerance on time' size='small' variant='outlined'
                        InputProps={{ endAdornment: <InputAdornment position='end'>S</InputAdornment> }}
                        value={transientAnalysisControlLine.tolerance_on_time}
                        onChange={handleTransientAnalysisControlLine}
                      />
                    </ListItem>
                    <ListItem>
                      <TextField
                        id='max_integration_time_interval' label='Max integration time interval' size='small' variant='outlined'
                        InputProps={{ endAdornment: <InputAdornment position='end'>S</InputAdornment> }}
                        value={transientAnalysisControlLine.max_integration_time_interval}
                        onChange={handleTransientAnalysisControlLine}
                      />
                    </ListItem>
                    <ListItem>
                      <TextField
                        id='solver_kind' select label='Solver kind' size='small' variant='outlined'
                        value={transientAnalysisControlLine.solver_kind}
                        onChange={handleTransientAnalysisControlLine}
                      >
                        <MenuItem value='0'>LSodar</MenuItem>
                        <MenuItem value='1'>Sundials/CVODE - BDF - NEWTON</MenuItem>
                        <MenuItem value='2'>Sundials/CVODE - BDF - FUNCTIONAL</MenuItem>
                        <MenuItem value='3'>Sundials/CVODE - ADAMS - NEWTON</MenuItem>
                        <MenuItem value='4'>Sundials/CVODE - ADAMS - FUNCTIONAL</MenuItem>
                        <MenuItem value='5'>DOPRI5 - Dormand-Prince 4(5)</MenuItem>
                        <MenuItem value='6'>RK45 - Runge-Kutta 4(5)</MenuItem>
                        <MenuItem value='7'>Implicit RK45 - Implicit Runge-Kutta 4(5) - FIXED-POINT</MenuItem>
                        <MenuItem value='8'>CRANI - Crank-Nicolson 2(3) - FIXED-POINT</MenuItem>
                        <MenuItem value='100'>Sundials/IDA</MenuItem>
                        <MenuItem value='101'>DDaskr - BDF</MenuItem>
                      </TextField>
                    </ListItem>
                    <ListItem>
                      <TextField
                        id='maximum_step_size' label='Maximum step size' size='small' variant='outlined'
                        value={transientAnalysisControlLine.maximum_step_size}
                        onChange={handleTransientAnalysisControlLine}
                      />
                    </ListItem>

                    <ListItem>
                      <Button id='transientAnalysisSimulate' size='small' variant='contained' color='primary' onClick={() => { startSimulate('Transient') }}>
                        Simulate
                      </Button>
                    </ListItem>
                  </List>
                </Box>
              </AccordionDetails>
            </Accordion>
          </ListItem>

          <ListItem style={isSimRes ? {} : { display: 'none' }} onClick={handleSimulateOpen}>
            <Button size='small' variant='contained' color='primary' style={{ margin: '10px auto' }} onClick={handleSimulateOpen}>
              Simulation Result
            </Button>
          </ListItem>
        </List>
      </div>
    </>
  )
}
