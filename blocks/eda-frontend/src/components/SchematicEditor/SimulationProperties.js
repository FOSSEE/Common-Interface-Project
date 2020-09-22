import React, { useState } from 'react'
import {
  List,
  ListItem,
  Button,
  TextField,
  ExpansionPanel,
  ExpansionPanelSummary,
  ExpansionPanelDetails,
  Typography
} from '@material-ui/core'
import ExpandMoreIcon from '@material-ui/icons/ExpandMore'
import { makeStyles } from '@material-ui/core/styles'
import { useSelector, useDispatch } from 'react-redux'

import { setResultTitle, setResultGraph, setResultText } from '../../redux/actions/index'
import { Save } from './Helper/ToolbarTools'
import SimulationScreen from './SimulationScreen'
import api from '../../utils/Api'

const useStyles = makeStyles((theme) => ({
  toolbar: {
    minHeight: '90px'
  },
  pages: {
    margin: theme.spacing(0, 1)
  },
  propertiesBox: {
    width: '100%'
  },
  simulationOptions: {
    margin: '0px',
    padding: '0px',
    width: '100%'
  },
  heading: {
    fontSize: theme.typography.pxToRem(15),
    fontWeight: theme.typography.fontWeightRegular
  }
}))

export default function SimulationProperties () {
  const netfile = useSelector(state => state.netlistReducer)
  const isSimRes = useSelector(state => state.simulationReducer.isSimRes)
  const dispatch = useDispatch()
  const classes = useStyles()
  const [transientAnalysisControlLine, setTransientAnalysisControlLine] = useState({
    stop: '30',
    step: '0.1'
  })

  const handleTransientAnalysisControlLine = (evt) => {
    const value = evt.target.value

    setTransientAnalysisControlLine({
      ...transientAnalysisControlLine,
      [evt.target.id]: value
    })
  }

  const [simulateOpen, setSimulateOpen] = React.useState(false)
  const handlesimulateOpen = () => {
    setSimulateOpen(true)
  }

  const handleSimulateClose = () => {
    setSimulateOpen(false)
  }

  // Prepare Netlist to file
  const prepareNetlist = (netlist) => {
    var titleA = netfile.title.split(' ')[1]
    var myblob = new Blob([netlist], {
      type: 'text/plain'
    })
    var file = new File([myblob], `${titleA}.xml`, { type: 'text/xml', lastModified: Date.now() })
    // console.log(file)
    sendNetlist(file)
  }

  function sendNetlist (file) {
    netlistConfig(file)
      .then((response) => {
        const res = response.data
        const getUrl = 'simulation/status/'.concat(res.details.task_id)

        simulationResult(getUrl)
      })
      .catch(function (error) {
        console.log(error)
      })
  }

  // Upload the nelist
  function netlistConfig (file) {
    const formData = new FormData()
    formData.append('file', file)
    formData.append('stop', transientAnalysisControlLine.stop)
    formData.append('step', transientAnalysisControlLine.step)
    const config = {
      headers: {
        'content-type': 'multipart/form-data'
      }
    }
    return api.post('simulation/upload', formData, config)
  }

  const [isResult, setIsResult] = useState(false)

  // Get the simulation result with task_Id
  function simulationResult (url) {
    api
      .get(url)
      .then((res) => {
        if (res.data.state === 'PROGRESS' || res.data.state === 'PENDING') {
          setTimeout(simulationResult(url), 1000)
        } else {
          var result = res.data.details
          if (result === null) {
            setIsResult(false)
          } else {
            setIsResult(true)
            var temp = res.data.details.data
            var data = result.data
            // console.log('DATA SIm', data)
            if (res.data.details.graph === 'true') {
              var simResultGraph = { labels: [], x_points: [], y_points: [] }
              // populate the labels
              for (var i = 0; i < data.length; i++) {
                simResultGraph.labels[0] = data[i].labels[0]
                var lab = data[i].labels
                // lab is an array containeing labels names ['time','abc','def']
                simResultGraph.x_points = data[0].x

                // labels
                for (var x = 1; x < lab.length; x++) {
                  if (lab[x].includes('#branch')) {
                    lab[x] = `I (${lab[x].replace('#branch', '')})`
                  }
                  //  uncomment below if you want label like V(r1.1) but it will break the graph showing time as well
                  //  else {
                  // lab[x] = `V (${lab[x]})`

                  // }
                  simResultGraph.labels.push(lab[x])
                }
                // populate y_points
                for (var z = 0; z < data[i].y.length; z++) {
                  simResultGraph.y_points.push(data[i].y[z])
                }
              }

              simResultGraph.x_points = simResultGraph.x_points.map(d => parseFloat(d))

              for (let i1 = 0; i1 < simResultGraph.y_points.length; i1++) {
                simResultGraph.y_points[i1] = simResultGraph.y_points[i1].map(d => parseFloat(d))
              }

              dispatch(setResultGraph(simResultGraph))
            } else {
              var simResultText = []
              for (let i = 0; i < temp.length; i++) {
                let postfixUnit = ''
                if (temp[i][0].includes('#branch')) {
                  temp[i][0] = `I(${temp[i][0].replace('#branch', '')})`
                  postfixUnit = 'A'
                } else {
                  temp[i][0] = `V(${temp[i][0]})`
                  postfixUnit = 'V'
                }

                simResultText.push(temp[i][0] + ' ' + temp[i][1] + ' ' + parseFloat(temp[i][2]) + ' ' + postfixUnit + '\n')
              }

              dispatch(setResultText(simResultText))
            }
          }
        }
      })
      .then((res) => { handlesimulateOpen() })
      .catch(function (error) {
        console.log(error)
      })
  }

  const startSimulate = (type) => {
    var compNetlist = Save()
    switch (type) {
      case 'Transient':
        dispatch(setResultTitle('Transient Analysis Output'))
        break
      default:
        break
    }

    var netlist = compNetlist

    prepareNetlist(netlist)
  }

  // simulation properties add expression input box
  return (
    <>
      <div className={classes.SimulationOptions}>
        <SimulationScreen open={simulateOpen} isResult={isResult} close={handleSimulateClose} />

        {/* Simulation modes list */}
        <List>

          {/* Transient Analysis */}
          <ListItem className={classes.simulationOptions} divider>
            <ExpansionPanel>
              <ExpansionPanelSummary
                expandIcon={<ExpandMoreIcon />}
                aria-controls="panel1a-content"
                id="panel1a-header"
              >
                <Typography className={classes.heading}>Transient Analysis</Typography>
              </ExpansionPanelSummary>
              <ExpansionPanelDetails>
                <form className={classes.propertiesBox} noValidate autoComplete="off">
                  <List>
                    <ListItem>
                      <TextField id="stop" label="Stop Time" size='small' variant="outlined"
                        value={transientAnalysisControlLine.stop}
                        onChange={handleTransientAnalysisControlLine}
                      />
                      <span style={{ marginLeft: '10px' }}>S</span>
                    </ListItem>
                    <ListItem>
                      <TextField id="step" label="Time Step" size='small' variant="outlined"
                        value={transientAnalysisControlLine.step}
                        onChange={handleTransientAnalysisControlLine}
                      />
                      <span style={{ marginLeft: '10px' }}>S</span>
                    </ListItem>

                    <ListItem>
                      <Button id="transientAnalysisSimulate" size='small' variant="contained" color="primary" onClick={(e) => { startSimulate('Transient') }}>
                        Simulate
                      </Button>
                    </ListItem>
                  </List>
                </form>
              </ExpansionPanelDetails>
            </ExpansionPanel>
          </ListItem>

          <ListItem style={isSimRes ? {} : { display: 'none' }} onClick={handlesimulateOpen} >
            <Button size='small' variant="contained" color="primary" style={{ margin: '10px auto' }} onClick={handlesimulateOpen}>
              Simulation Result
            </Button>
          </ListItem>
        </List>
      </div>
    </>
  )
}
