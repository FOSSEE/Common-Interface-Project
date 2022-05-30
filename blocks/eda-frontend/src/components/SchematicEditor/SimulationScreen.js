/* eslint-disable */
import React, { useState, useEffect, useRef, useCallback } from 'react'
import PropTypes from 'prop-types'
import {
  AppBar,
  Button,
  Container,
  Dialog,
  Grid,
  IconButton,
  Paper,
  Slide,
  Toolbar,
  Typography
} from '@material-ui/core'
import { makeStyles } from '@material-ui/core/styles'
import CloseIcon from '@material-ui/icons/Close'
import { useSelector, useDispatch } from 'react-redux'
import $ from 'jquery'

import Graph, { setStatusDone } from '../Shared/Graph'
import { setResultGraph } from '../../redux/actions/index'
import api from '../../utils/Api'

const Transition = React.forwardRef(function Transition (props, ref) {
  return <Slide direction='up' ref={ref} {...props} />
})

const useStyles = makeStyles((theme) => ({
  appBar: {
    position: 'relative'
  },
  title: {
    marginLeft: theme.spacing(2),
    flex: 1
  },
  header: {
    padding: theme.spacing(5, 0, 6),
    color: '#fff'
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    backgroundColor: '#404040',
    color: '#fff'
  }
}))

export function setGraphStatusDone () {
  setStatusDone()
}

// Screen to display simulation result in graph or text format
export default function SimulationScreen ({ open, close }) {
  const classes = useStyles()
  const dispatch = useDispatch()
  const result = useSelector(state => state.simulationReducer)
  const stitle = useSelector(state => state.netlistReducer.title)
  const taskId = useSelector(state => state.simulationReducer.taskId)
  const [isResult, setIsResult] = useState(false)
  const graphsRef = useRef([])
  const datapointsRef = useRef([])
  const timeoutRef = useRef(null)
  const [noOfGraphs, setNoOfGraphs] = useState(0)
  const chartIdCount = useRef(0)
  const chartIdList = useRef({})
  const [count,setcount]=useState(0);
  const [cp,setcp]=useState(1);

  // Keep track of RANGE of each graph(chart)
  const range = useRef([])
  const nameValuesColormap = useRef(new Map()) // for storing colormap values of cmatview and cmat3d block

  const streamSimulationResult = useCallback((streamingUrl) => {
    // define variables for block event
    // pnts - Points list of the blocks
    const pnts = []

    // Initialise variable for entry condition of creating chart for BARXY and
    // AFFICH_m
    let cmatviewCounter = 0 // counter to know how many line in log
    let loglines = 0

    const printloglines = () => {
      if (loglines > 0) {
        console.log(loglines, 'log lines')
        loglines = 0
      }
    }

    const addPointToGraph = (id, point) => {
      const refId = chartIdList.current[id]
      if (graphsRef.current[refId] !== undefined) {
        graphsRef.current[refId].addPointToQueue(id, point)
      } else {
        console.log('cannot add point', id, point, chartIdList)
      }
    }
    const newchart =(figureId, noOfGraph, xmin, xmax, ymin, ymax, typeChart, titleText, colorAxis)=>{
    const temp = [];
    temp.push(chartIdList.current[figureId])
    console.log(chartIdList.current[figureId])
    const found= temp.find(element => element == chartIdList.current[figureId] );
    if(found == undefined)
    {
      ()=>{setcount(count + 1);}
      ()=>{setcp(cp+1);}
      createNewChart(figureId, noOfGraph, xmin, xmax, ymin, ymax, typeChart, titleText, colorAxis)
    }
    else
    {
      addPointToGraph(id,point)
    }
    }
    // Function to create a new chart
    const createNewChart = (id, noOfGraph, xmin, xmax, ymin, ymax, typeChart, titleText, colorAxis = null) => {
      /*
       * id - container id for graph(chart),
       * noOfGraph - number of graphs in output of a block,
       * xmin - minimum x-axis value,
       * xmax - maximum x-axis value,
       * ymin - minimum y-axis value,
       * ymax - maximum y-axis value,
       * typeChart - type of chart to be drawn,
       * titleText - title to be given to the chart
       */

      // convert String values to desired datatype
      xmin = parseFloat(xmin)
      xmax = parseFloat(xmax)
      ymin = parseFloat(ymin)
      ymax = parseFloat(ymax)

      // default value of pointpadding added for ceventscope
      let pointWidth = 0.1
      let pointRange = null

      let lineWidth = 2
      if (titleText.substring(0, 5) === 'BARXY') {
        lineWidth = noOfGraph
        noOfGraph = 1
      } else if (titleText.substring(0, 7) === 'CSCOPXY') {
        // disable line by putting lineWidth as 0
        lineWidth = 0
      } else if (titleText.substring(0, 7) === 'CANIMXY') {
        // disable line by putting lineWidth as 0
        lineWidth = 0
      } else if (titleText.substring(0, 7) === 'CEVSCPE') {
        // To manipulate the graph width of ceventscope
        pointWidth = 2
        pointRange = 0.05
      }

      chartIdList.current[id] = chartIdCount.current
      const datapoint = {
        datapointId: id,
        datapointType: typeChart,
        datapointTitle: titleText,
        datapointXMin: xmin,
        datapointYMin: ymin,
        datapointXMax: xmax,
        datapointYMax: ymax,
        datapointPointRange: pointRange,
        datapointLineWidth: lineWidth,
        datapointPointWidth: pointWidth,
        datapointDataClasses: colorAxis
      }
      datapointsRef.current[chartIdCount.current] = datapoint
      chartIdCount.current = chartIdCount.current + 1
      setNoOfGraphs(nog => nog + 1)
    }

    // Function to create a new 3d-chart
    const createNewChart3d = (id, noOfGraph, xmin, xmax, ymin, ymax, zmin, zmax, typeChart, titleText, alpha, theta) => {
      /*
       * id - container id for graph(chart),
       * noOfGraph - number of graphs in output of a block,
       * ymin - minimum y-axis value,
       * ymax - maximum y-axis value,
       * xmin - minimum x-axis value,
       * xmax - maximum x-axis value,
       * zmin - minimum z-axis value,
       * zmax - maximum z-axis value,
       * typeChart - type of chart to be drawn,
       * titleText - title to be given to the chart,
       * alpha - Angle of rotation for graph for 3D chart
       * theta - Angle of rotation for graph for 3D chart
       */

      // convert String values to desired datatype
      xmin = parseFloat(xmin)
      xmax = parseFloat(xmax)
      ymin = parseFloat(ymin)
      ymax = parseFloat(ymax)
      zmin = parseFloat(zmin)
      zmax = parseFloat(zmax)
      // Assigning angle theta of 3D block to beta angle of highchart ( Can be
      // modified later)
      const beta = theta
      let lineWidth = 1
      let radius = 1
      if (titleText.substring(0, 9) === 'CANIMXY3D') {
        lineWidth = 0
        radius = 3
      }
      $('#charts').append("<div id='chart-" + id.toString() + "' style = 'height:200px'></div>")

      const elem = $('#chart-' + id.toString())
      // change graph height if block has only 1 output graph
      if (noOfGraph === 1) {
        elem.css('height', '400px')
      }

      elem.highcharts({
        chart: {
          type: typeChart,
          zoomtype: 'xy',
          options3d: {
            enabled: true,
            alpha: alpha,
            beta: beta,
            depth: 100,
            viewDistance: 100,
            frame: {
              bottom: {
                size: 0,
                color: '#FFFFFF'
              },
              back: {
                size: 0,
                color: '#FFFFFF'
              },
              side: {
                size: 0,
                color: '#FFFFFF'
              }
            }
          }
        },
        title: {
          text: titleText
        },
        tooltip: {
          enabled: false
        },
        yAxis: {
          // Manipulation for showing z axis vertically instead of Y axis
          // (only for 3D graph).
          min: zmin,
          max: zmax,
          gridLineWidth: 1,
          tickInterval: 1,
          title: {
            rotation: 0,
            style: {
              fontWeight: 'bold',
              fontSize: '15px'
            },
            text: 'z'
          }
        },
        xAxis: {
          min: xmin,
          max: xmax,
          tickInterval: 1,
          gridLineWidth: 1,
          title: {
            style: {
              fontWeight: 'bold',
              fontSize: '15px'
            },
            text: 'x' // title for X for differentiating axis
          }
        },
        zAxis: {
          // Manipulation for showing y axis values in place of z axis (only
          // for 3D graph).
          min: ymin,
          max: ymax,
          tickInterval: 1,
          gridLineWidth: 1,
          title: {
            rotation: 300,
            margin: -30,
            style: {
              fontWeight: 'bold',
              fontSize: '15px'
            },
            text: 'y'
          }
        },
        plotOptions: {
          marker: {
            enabled: false
          },
          series: {
            lineWidth: lineWidth,
            states: {
              hover: {
                lineWidth: lineWidth
              }
            }
          },
          scatter: {
            marker: {
              radius: radius,
              states: {
                hover: {
                  enabled: true,
                  lineColor: 'rgb(100,100,100)'
                }
              }
            }
          }
        },
        series: []
      })
    }

    // To create coloraxis array which will be passed to cmatview chart for heatmap creation
    const getColorAxisForPoints = (blockUid) => {
      const colorAxisArray = []
      const getHexColorArray = nameValuesColormap.current.get(blockUid)
      for (let i = 0; i < getHexColorArray.length; i++) {
        const colorValues = {}
        const temp = i
        colorValues.from = temp + 1
        colorValues.to = temp + 2
        colorValues.color = getHexColorArray[i]
        colorAxisArray.push(colorValues)
      }
      return colorAxisArray
    }

    const sse = new EventSource('/api/' + streamingUrl, { withCredentials: true })
    sse.addEventListener('log', e => {
      ++loglines

      const data = e.data.split(' ')

      // store block info. from the data line
      const block = parseInt(data[0])
      const figureId = (block === 2) ? data[4] : data[2] // For CMSCOPE
      let noOfGraph
      if (block === 5 || block === 10) { // For 3D-SCOPE blocks
        noOfGraph = data[11]
      } else if (block === 11) { // For BARXY
        noOfGraph = data[12]
      } else {
        noOfGraph = data[10]
      }
      let xmin
      let xmax
      let ymin
      let ymax
      let zmin = null
      let zmax = null
      if (block === 4 || block === 9) { // For CSCOPXY or CANIMXY
        xmin = data[11]
        xmax = data[12]
        ymin = data[13]
        ymax = data[14]
      } else if (block === 5 || block === 10) { // For 3D-SCOPE blocks
        xmin = data[12]
        xmax = data[13]
        ymin = data[14]
        ymax = data[15]
        zmin = data[16]
        zmax = data[17]
      } else if (block === 11) { // For BARXY
        xmin = data[8]
        xmax = data[9]
        ymin = data[10]
        ymax = data[11]
      } else if (block === 12) { // For CMATVIEW
        xmin = 0
        xmax = data[8]
        ymin = 0
        ymax = data[10]
      } else if (block === 23) { // For CEVENTSCOPE
        xmin = 0
        xmax = data[11]
        ymin = 0
        ymax = 1
      } else {
        xmin = 0
        xmax = data[13]
        ymin = data[11]
        ymax = data[12]
      }
      let alpha = null
      let theta = null
      if (block === 5 || block === 10) { // For 3D-SCOPE blocks
        alpha = data[18]
        theta = data[19]
      }
      let colorAxis = null
      if (block === 12) { // For CMATVIEW
        colorAxis = getColorAxisForPoints(figureId)
      }
      // set default chart type
      let typeChart
      if (block === 4 || block === 5 || block === 9 || block === 10) { // For CSCOPXY or CANIMXY
        typeChart = 'scatter'
      } else if (block === 12) { // For CMATVIEW
        typeChart = 'heatmap'
      } else if (block === 23) { // For CEVENTSCOPE
        typeChart = 'column'
      } else {
        typeChart = 'line'
      }
      let titleText
      if (block === 4) { // For CSCOPXY
        titleText = data[15] + '-' + data[2]
      } else if (block === 5) { // For 3D-SCOPE block
        titleText = data[20] + '-' + data[2]
      } else if (block === 9) { // For CANIMXY
        titleText = data[16] + '-' + data[2]
      } else if (block === 10) { // For 3D-SCOPE block
        titleText = data[21] + '-' + data[2]
      } else if (block === 11) { // For BARXY
        titleText = data[13] + '-' + figureId
      } else if (block === 12) { // For CMATVIEW
        titleText = data[data.length - 1] + '-' + figureId
      } else if (block === 23) { // For CEVENTSCOPE
        titleText = data[12] + '-' + data[2]
      } else {
        titleText = data[14] + '-' + data[2]
      }

      if (chartIdList.current[figureId] === undefined) {
        if (block === 5 || block === 10) {
          // process data for 3D-SCOPE blocks
          createNewChart3d(figureId, noOfGraph, xmin, xmax, ymin, ymax, zmin, zmax, typeChart, titleText, alpha, theta)
        } else if (block < 5 || block === 9 || block === 11 || block === 12 || block === 23) {
          // sink block is not CSCOPXY
          newchart(figureId, noOfGraph, xmin, xmax, ymin, ymax, typeChart, titleText, colorAxis)
          range.current[chartIdList.current[figureId]] = parseFloat(xmax)
        }
      }

      // For BARXY
      if (block === 11) {
        const x1 = parseFloat(data[4])
        const y1 = parseFloat(data[5])
        const x2 = parseFloat(data[6])
        const y2 = parseFloat(data[7])

        pnts.push([x1, y1])
        pnts.push([x2, y2])

        // Ending condition for blocks not having a dataline for 'Ending'
        if (pnts.length === this.finalIntegrationTime * 10 - 1) {
          const xhr = new XMLHttpRequest()
          xhr.open('GET', '/endBlock/' + figureId, true)
          xhr.send()
        }
      } else if (block === 21 || block === 22) {
        // handle writec_f and writeau_f
        // create a form and add the filename to it
        const form = new FormData()
        form.append('path', data[4])
        const xhr = new XMLHttpRequest()
        xhr.responseType = 'blob'
        // sending form to get file for download
        xhr.open('POST', '/downloadfile', true)
        xhr.onload = function () {
          if (this.status === 200) {
            // blob data type to receive the file
            const blob = this.response
            const url = window.URL.createObjectURL(blob)
            // popup for download option of the file
            const anchor = document.createElement('a')
            document.body.appendChild(anchor)
            anchor.style = 'display: none'
            anchor.href = url
            if (block === 21) {
              anchor.download = 'writec-' + taskId + '.datas'
            } else {
              anchor.download = 'audio-' + taskId + '.au'
            }
            anchor.click()
            document.body.removeChild(anchor)
            window.URL.revokeObjectURL(url)
          }
        }
        xhr.send(form)
        const xhr2 = new XMLHttpRequest()
        xhr2.open('POST', '/deletefile')
        xhr2.onload = function () {
        }
        xhr2.send(form)
      } else if (block < 5 || block === 9 || block === 23 || block === 12) {
        // added new condition for ceventscope
        // process data for 2D-SCOPE blocks
        const lineId = parseInt(data[6])
        const x = parseFloat(data[8])
        const y = parseFloat(data[9])
        // store 2d-data
        if (block !== 12) {
          addPointToGraph(figureId, [lineId, x, y])
        } else {
          const values = getPointsForData(data, data[8], data[10])
          cmatviewCounter++ // to count lines from log
          if (cmatviewCounter === 1) {
            // Only add points of line 1, so that no delay in chart appearance)
            addPointToGraph(figureId, [lineId, values])
          } else if (cmatviewCounter < 16) {
            // Only add points of line which are multiple of 5, till 15 like 5 10 15 (this is to reduce load on browser)
            const count = cmatviewCounter % 5
            if (count === 0) {
              addPointToGraph(figureId, [lineId, values])
            }
          } else {
            // Only add points of line which are multiple of 10 but after 16 like 20 30 ... (this is to reduce load on browser)
            const count = cmatviewCounter % 10
            if (count === 0) {
              addPointToGraph(figureId, [lineId, values])
            }
          }
        }
        // store block number for chart creation
      } else if (block === 5 || block === 10) {
        // process data for 3D-SCOPE blocks
        const lineId = parseInt(data[6])
        const x = parseFloat(data[8])
        const y = parseFloat(data[9])
        const z = parseFloat(data[10])
        // store 3d-data
        addPointToGraph(figureId, [lineId, x, y, z])
        // store block number for chart creation
      } else if (block === 13) {
        // process data for CMAT3D blocks
        // const blockUid = data[2]
        // const m = data[8]
        // const n = data[10]
        // const xmin = data[12]
        // const xmax = data[14]
        // const ymin = data[16]
        // const ymax = data[18]
        // const zmin = data[20]
        // const zmax = data[22]
        // const alpha = data[24]
        // const theta = data[26]
        // Chart function need to be written
      } else if (block === 20) {
        // Process data for Affich_m block

        // store length of data for each line
        const lengthOfData = data.length
        const blockId = data[2] // to store block id of affichm block
        const columns = data[5] // gets column of matrix

        // below code creates a html code which is table with data in that
        // (To display it as matrix)
        let p = '<b>Value of Block : ' + data[lengthOfData - 1] + '-' + blockId + "</b> (Refer to label on block)<br><br><table style='width:100%'><tr>"
        let count = 1
        for (let k = 6; k < lengthOfData - 1; k++) {
          if (data[k].length !== 0) {
            p += '<td>'
            p += data[k]
            if (count % columns === 0) {
              // to break into new column of table
              p += '</td></tr><tr>'
            } else {
              p += '</td>'
            }
            count++
          }
        }
        p += '</table>'
        // to send data to display result
        createAffichDisplaytext(p, blockId)
      }
    }, false)
    sse.addEventListener('duplicate', e => {
      printloglines()
      console.log('duplicate', e)
    }, false)
    sse.addEventListener('DONE', () => {
      printloglines()
      console.log('DONE')
      sse.close()
      setGraphStatusDone()
    }, false)
    sse.addEventListener('ERROR', e => {
      printloglines()
      console.log('ERROR', e)
      sse.close()
    }, false)
    sse.addEventListener('MESSAGE', e => {
      printloglines()
      console.log('MESSAGE', e)
      sse.close()
    }, false)
  }, [taskId, chartIdList])

  // Get the simulation result with task_Id
  const simulationResult = useCallback((url, streamingUrl) => {
    api
      .get(url)
      .then((res) => {
        switch (res.data.state) {
          case 'PROGRESS':
          case 'PENDING':
            setIsResult(false)
            timeoutRef.current = setTimeout(() => simulationResult(url, streamingUrl), 10000)
            break

          case 'STREAMING':
          case 'SUCCESS':
            streamSimulationResult(streamingUrl)
            setIsResult(true)
            dispatch(setResultGraph(null))
            if (timeoutRef.current !== null) {
              clearTimeout(timeoutRef.current)
              timeoutRef.current = null
            }
            break

          default:
            console.log('unhandled case', res)
            if (timeoutRef.current !== null) {
              clearTimeout(timeoutRef.current)
              timeoutRef.current = null
            }
            break
        }
      })
      .catch(function (error) {
        console.log(error)
      })
  }, [dispatch, streamSimulationResult])

  const getSimulationResult = useCallback((taskId) => {
    if (taskId === '') {
      return
    }

    if (isResult) {
      return
    }

    const getUrl = 'simulation/status/' + taskId
    const getStreamingUrl = 'simulation/streaming/' + taskId

    simulationResult(getUrl, getStreamingUrl)
  }, [isResult, simulationResult])

  useEffect(() => getSimulationResult(taskId), [taskId, getSimulationResult])

  /*
   * Function to display values of all affich blocks
   * displayParameter : Contains the data which is display as data of affich
   * block
   * blockId : is used to get needed div according to affichm id
   */
  function createAffichDisplaytext (displayParameter, blockId) {
    // updating html data of div html for each time change according to each
    // affich
    $('#affichdata-' + blockId).html(displayParameter)
  }

  // Gets data (array with x , y and coloraxis values) to be passed to chart points
  function getPointsForData (data, m, n) {
    const arrayData = []
    let i = 12
    for (let x = m - 2; x >= 0; x--) {
      for (let y = 0; y < n - 1; y++) {
        const dataValues = []
        dataValues[0] = x
        dataValues[1] = y
        dataValues[2] = parseInt(data[i])
        arrayData.push(dataValues)
        i++
      }
    }
    return arrayData
  }
  useEffect(() => {
    for(var i=0;i<noOfGraphs;i++)
    {
      if(chartIdList.current[figureId] !== undefined)
      {
        chartIdList.current[figureId].reflow();
      }
    }
  },[datapointsRef.current])

  const typography1 = 'SOMETHING WENT WRONG. Please Check The Simulation Parameters.'
  const typography2 = 'SOMETHING WENT WRONG. Please Check The Simulation Parameters And ' + process.env.REACT_APP_DIAGRAM_NAME + '.'
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
        <AppBar position='static' elevation={0} className={classes.appBar}>
          <Toolbar variant='dense' style={{ backgroundColor: '#404040' }}>
            <IconButton edge='start' color='inherit' onClick={close} aria-label='close'>
              <CloseIcon />
            </IconButton>
            <Typography variant='h6' className={classes.title}>
              Simulation Result
            </Typography>
            <Button autoFocus color='inherit' onClick={close}>
              close
            </Button>
          </Toolbar>
        </AppBar>
        <Container maxWidth='lg' className={classes.header}>
          <Grid
            container
            spacing={3}
            direction='row'
            justify='center'
            alignItems='center'
          >
            {/* Card to display simulation result screen header */}
            <Grid item xs={12} sm={12}>
              <Paper className={classes.paper}>
                <Typography variant='h2' align='center' gutterBottom>
                  {result.title}
                </Typography>
                <Typography variant='h5' align='center' component='p' gutterBottom>
                  Simulation Result for {stitle} *
                </Typography>
              </Paper>
            </Grid>

            {/* Display graph result */}
            {isResult === true
              ? <>
                {
                  (result.isGraph === 'true')
                    ? <Grid item xs={12} sm={12}>
                      <Paper className={classes.paper}>
                        <Typography variant='h4' align='center' gutterBottom>
                          GRAPH OUTPUT
                        </Typography>
                        {
                          (noOfGraphs!=0)?
                            datapointsRef.current.map((element,i)=>(
                              <Graph
                              key={i}
                              ref={el => { graphsRef.current[i] = el }}
                              datapoint={datapointsRef.current[i]}
                            />
                            ))
                            : <div />
                          }
                      </Paper>
                    </Grid>
                    : (result.isGraph === 'true') ? <span>{typography1}</span> : <span />
                }

                {/* Display text result */}
                {
                  (result.isGraph === 'false')
                    ? <Grid item xs={12} sm={12}>
                      <Paper className={classes.paper}>
                        <Typography variant='h4' align='center' gutterBottom>
                          OUTPUT
                        </Typography>
                      </Paper>
                    </Grid>
                    : <span />
                }
              </>
              : <Grid item xs={12} sm={12}>
                <Paper className={classes.paper}>
                  <Typography variant='h6' align='center' gutterBottom>
                    {typography2} {/* Error handling message in case of null result */}
                  </Typography>
                </Paper>
              </Grid>
            }
          </Grid>
        </Container>
      </Dialog>
    </div>
  )
}

SimulationScreen.propTypes = {
  open: PropTypes.bool,
  close: PropTypes.func
}
