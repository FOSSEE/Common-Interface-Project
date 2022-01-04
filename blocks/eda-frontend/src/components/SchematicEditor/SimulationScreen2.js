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

import Graph2, { setStatusDone } from '../Shared/Graph2'
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
export default function SimulationScreen2 ({ open, close }) {
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

  // Keep track of block number for each graph(chart)
  const block_list = [];
  // Keep track of RANGE of each graph(chart)
  const RANGE = [];
  const name_values_colormap = new Map(); // for storing colormap values of cmatview and cmat3d block

  const streamSimulationResult = useCallback((streamingUrl) => {
    // define variables for block event
    // fig_id - figure_id  of blocks,
    // pnts - Points list of the blocks
    let fig_id
    const pnts = [];

    let block;
    // Initialise variable for entry condition of creating chart for BARXY and
    // AFFICH_m
    let block_entry_BARXY = 1;
    let cmatview_counter = 0; // counter to know how many line in log
    let loglines = 0;

    const printloglines = () => {
        if (loglines > 0) {
            console.log(loglines, 'log lines');
            loglines = 0;
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

    // Function to create a new chart
    const create_new_chart = (id, no_of_graph, ymin, ymax, xmin, xmax, type_chart, title_text) => {
        /*
         * id - container id for graph(chart),
         * no_of_graph - number of graphs in output of a block,
         * ymin - minimum y-axis value,
         * ymax - maximum y-axis value,
         * xmin - minimum x-axis value,
         * xmax - maximum x-axis value,
         * type_chart - type of chart to be drawn,
         * title_text - title to be given to the chart
         */

        // convert String values to desired datatype
        xmin = parseFloat(xmin);
        xmax = parseFloat(xmax);
        ymin = parseFloat(ymin);
        ymax = parseFloat(ymax);

        // default value of pointpadding added for ceventscope
        let pointWidth=0.1;
        let pointRange = null;

        let lineWidth = 2;
        if (title_text.substring(0, 5) === "BARXY") {
            lineWidth = no_of_graph;
            no_of_graph = 1;
        } else if (title_text.substring(0, 7) === "CSCOPXY") {
            // disable line by putting lineWidth as 0
            lineWidth = 0
        } else if (title_text.substring(0, 7) === "CANIMXY") {
            // disable line by putting lineWidth as 0
            lineWidth = 0
        } else if (title_text.substring(0, 7) === "CEVSCPE") {
            // To manipulate the graph width of ceventscope
            pointWidth = 2;
            pointRange = 0.05;
        }

        chartIdList.current[id] = chartIdCount.current
        const datapoint = {
          datapointId: id,
          datapointType: type_chart,
          datapointTitle: title_text,
          datapointXMin: xmin,
          datapointYMin: ymin,
          datapointXMax: xmax,
          datapointYMax: ymax,
          datapointPointRange: pointRange,
          datapointLineWidth: lineWidth,
          datapointPointWidth: pointWidth
        }
        datapointsRef.current[chartIdCount.current] = datapoint
        chartIdCount.current = chartIdCount.current + 1
        setNoOfGraphs(nog => nog + 1)
    }

    // Chart function for cmatview which has less than 10*10 matrix size
    const create_chart_for_cmatview = (id, m, n, title_text, color_axis) => {
        let xmin = 0;
        let xmax = m;
        let ymin = 0;
        let ymax = n;
        $('#charts').append("<div id='chart-"+id+"' style = 'height:100%;width:100%'></div>");
        let elem = $('#chart-'+id.toString());
        elem.highcharts({
            tooltip: {
                enabled: false
            },
            chart: {
                type: 'heatmap'
            },
            title: {
                text: title_text
            },
            xAxis: {
                min: xmin,
                max: xmax
            },
            yAxis: {
                min: ymin,
                max: ymax,
            },
            plotOptions: {
                marker: {
                    enabled: false
                },
                series: {
                    enableMouseTracking: false
                }
            },
            colorAxis: {
                dataClasses: color_axis
            },
            legend: {
                enabled: false
            },
            series: []
        });
    }

    // Chart function for cmatview large data ie matrix more than 10*10 size
    const create_chart_for_large_data_cmatview = (id, m, n, title_text, color_axis) => {
        let xmax = m;
        let ymax = n;
        $('#charts').append("<div id='chart-"+id+"' style = 'height:100%;width:100%'></div>");
        let elem = $('#chart-'+id.toString());
        elem.highcharts({
            tooltip: {
                enabled: false
            },
            chart: {
                type: 'heatmap'
            },
            boost: {
                useGPUTranslations: true,
                usePreallocated: true
            },
            title: {
                text: title_text
            },
            xAxis: {
                min: 0,
                max: xmax
            },
            yAxis: {
                min: 0,
                max: ymax
            },
            plotOptions: {
               series: {
                    animation:false,
                    boostThreshold : 400000,
                    turboThreshold : 0,
                    stickyTracking: false,
                    shadow: false
                },
                marker: {
                    enabled: false
                },
                 heatmap: {
                    shadow: false,
                    animation: false
                }
            },
            legend: {
                enabled: false
            },
            colorAxis: {
                dataClasses: color_axis
            },
            series: [{
                seriesThreshold: 2
            }]
        });
    }


    // Function to create a new 3d-chart
    const create_new_chart_3d = (id, no_of_graph, xmin, xmax, ymin, ymax, zmin, zmax, type_chart, title_text, alpha, theta) => {
        /*
         * id - container id for graph(chart),
         * no_of_graph - number of graphs in output of a block,
         * ymin - minimum y-axis value,
         * ymax - maximum y-axis value,
         * xmin - minimum x-axis value,
         * xmax - maximum x-axis value,
         * zmin - minimum z-axis value,
         * zmax - maximum z-axis value,
         * type_chart - type of chart to be drawn,
         * title_text - title to be given to the chart,
         * alpha - Angle of rotation for graph for 3D chart
         * theta - Angle of rotation for graph for 3D chart
         */

        // convert String values to desired datatype
        xmin = parseFloat(xmin);
        xmax = parseFloat(xmax);
        ymin = parseFloat(ymin);
        ymax = parseFloat(ymax);
        zmin = parseFloat(zmin);
        zmax = parseFloat(zmax);
        // Assigning angle theta of 3D block to beta angle of highchart ( Can be
        // modified later)
        let beta = theta;
        let lineWidth = 1;
        let radius = 1;
        if (title_text.substring(0, 9) === "CANIMXY3D") {
            lineWidth = 0;
            radius = 3;
        }
        $('#charts').append("<div id='chart-"+id.toString()+"' style = 'height:200px'></div>");

        let elem = $('#chart-'+id.toString());
        // change graph height if block has only 1 output graph
        if (no_of_graph === 1)
            elem.css('height', '400px');

        elem.highcharts({
            chart: {
                type: type_chart,
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
                text: title_text
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
        });
    }

    // To create coloraxis array which will be passed to cmatview chart for heatmap creation
    const get_color_axis_for_points = (block_uid) => {
        const color_axis_array = [];
        const get_hex_color_array = name_values_colormap.get(block_uid);
        for (let i = 0; i < get_hex_color_array.length; i++) {
            const color_values = {};
            const temp = i;
            color_values["from"] = temp + 1;
            color_values["to"] = temp + 2;
            color_values["color"] = get_hex_color_array[i];
            color_axis_array.push(color_values);
        }
        return color_axis_array;
    }

    const sse = new EventSource('/api/' + streamingUrl, { withCredentials: true })
    sse.addEventListener('log', e => {
      ++loglines;

      let data = e.data.split(' ');

      // store block info. from the data line
      block = parseInt(data[0]);

      // For BARXY
      if (block === 11) {
        let x1 = parseFloat(data[4]);
        let y1 = parseFloat(data[5]);
        let x2 = parseFloat(data[6]);
        let y2 = parseFloat(data[7]);

        if (block_entry_BARXY === 1) {
          fig_id = data[2];

          create_new_chart(fig_id, data[12], data[10], data[11], data[8], data[9], 'line', data[13]+'-'+fig_id);
          block_entry_BARXY = block_entry_BARXY + 1;
        }

        pnts.push([x1, y1]);
        pnts.push([x2, y2]);

        // Ending condition for blocks not having a dataline for 'Ending'
        if (pnts.length === (this.finalIntegrationTime*10-1)) {
          let xhr = new XMLHttpRequest();
          xhr.open("GET", "/endBlock/"+fig_id, true);
          xhr.send();
        }
      } else if (block === 21 || block === 22) {
        // handle writec_f and writeau_f
        // create a form and add the filename to it
        let form = new FormData()
        form.append('path', data[4]);
        let xhr = new XMLHttpRequest();
        xhr.responseType = 'blob';
        // sending form to get file for download
        xhr.open("POST", "/downloadfile", true);
        xhr.onload = function () {
          if (this.status === 200) {
            // blob data type to receive the file
            let blob = this.response;
            let url = window.URL.createObjectURL(blob);
            // popup for download option of the file
            let anchor = document.createElement("a");
            document.body.appendChild(anchor);
            anchor.style = "display: none";
            anchor.href = url;
            if (block === 21) {
              anchor.download = "writec-" + taskId + ".datas";
            } else {
              anchor.download = "audio-" + taskId + ".au";
            }
            anchor.click();
            document.body.removeChild(anchor);
            window.URL.revokeObjectURL(url);
          }
        };
        xhr.send(form);
        let xhr2 = new XMLHttpRequest();
        xhr2.open("POST", "/deletefile");
        xhr2.onload = function () {
        };
        xhr2.send(form);
      } else if (block < 5 ||block === 9 ||block === 23 ||block === 12) {
        // added new condition for ceventscope
        // process data for 2D-SCOPE blocks
        let figure_id = 0 ;
        if (block === 2) { // For cmscope block
          figure_id = data[4];
        } else {
          figure_id = data[2];
        }
        let line_id = parseInt(data[6]);
        let x = parseFloat(data[8]);
        let y = parseFloat(data[9]);
        if (chartIdList.current[figure_id] === undefined) {
          // set default chart type

          // if sink block is CSCOPXY or CANIMXY
          if (block === 4 || block === 9) {
            let chart_type = 'scatter';
            if (block === 4) {
              create_new_chart(figure_id, data[10], data[13], data[14], data[11], data[12], chart_type, data[15]+'-'+data[2]);
            } else {
              create_new_chart(figure_id, data[10], data[13], data[14], data[11], data[12], chart_type, data[16]+'-'+data[2]);
            }
            RANGE[chartIdList.current[figure_id]] = parseFloat(data[12]);
          } else {
            // Event Handling block is ceventscope
            if (block === 23) {
              let chart_type = 'column';
              create_new_chart(figure_id, data[10], 0, 1, 0, data[11], chart_type, data[12]+'-'+data[2]);
              RANGE[chartIdList.current[figure_id]] = parseFloat(data[11]);
            } else if (block === 12) {
              // process data for CMATVIEW blocks
              let m = data[8];
              let n = data[10];
              // let chart_type = 'heatmap';
              // let title_text = "CMATVIEW-" + figure_id;
              let color_axis = get_color_axis_for_points(figure_id);
              if (m*n <= 100) {
                create_chart_for_cmatview(figure_id, m, n, data[data.length-1]+'-'+figure_id, color_axis);
              } else {
                create_chart_for_large_data_cmatview(figure_id, m, n, data[data.length-1]+'-'+figure_id, color_axis);
              }
              RANGE[chartIdList.current[figure_id]] = parseFloat(30);
            } else {
              // sink block is not CSCOPXY
              let chart_type = 'line';
              create_new_chart(figure_id, data[10], data[11], data[12], 0, data[13], chart_type, data[14]+'-'+data[2]);
              RANGE[chartIdList.current[figure_id]] = parseFloat(data[13]);
            }
          }
        }
        let index = chartIdList.current[figure_id];
        // store 2d-data
        if (block !== 12) {
          addPointToGraph(figure_id, [line_id, x, y]);
        } else {
          let values = get_points_for_data(data, data[8], data[10]);
          cmatview_counter++; // to count lines from log
          if (cmatview_counter === 1) {
            // Only add points of line 1, so that no delay in chart appearance)
            addPointToGraph(figure_id, [line_id, values]);
          } else if (cmatview_counter < 16) {
            // Only add points of line which are multiple of 5, till 15 like 5 10 15 (this is to reduce load on browser)
            let count = cmatview_counter % 5;
            if (count === 0) {
              addPointToGraph(figure_id, [line_id, values]);
            }
          } else {
            // Only add points of line which are multiple of 10 but after 16 like 20 30 ... (this is to reduce load on browser)
            let count = cmatview_counter % 10;
            if (count === 0) {
              addPointToGraph(figure_id, [line_id, values]);
            }
          }
        }
        // store block number for chart creation
        block_list[index] = block;
      } else if (block === 5 || block === 10) {
        // process data for 3D-SCOPE blocks

        let figure_id = data[2];
        let line_id = parseInt(data[6]);
        let x = parseFloat(data[8]);
        let y = parseFloat(data[9]);
        let z = parseFloat(data[10]);
        if (chartIdList.current[figure_id] === undefined) {
          let chart_type = 'scatter';
          if (block === 10) {
            create_new_chart_3d(figure_id, data[11], data[12], data[13], data[14], data[15], data[16], data[17], chart_type, data[21]+'-'+data[2], data[18], data[19]);
          } else {
            create_new_chart_3d(figure_id, data[11], data[12], data[13], data[14], data[15], data[16], data[17], chart_type, data[20]+'-'+data[2], data[18], data[19]);
          }
        }
        let index = chartIdList.current[figure_id];
        // store 3d-data
        addPointToGraph(figure_id, [line_id, x, y, z]);
        // store block number for chart creation
        block_list[index] = block;
      } else if (block === 13) {
        // process data for CMAT3D blocks
        // let block_uid = data[2];
        // let m = data[8];
        // let n = data[10];
        // let xmin = data[12];
        // let xmax = data[14];
        // let ymin = data[16];
        // let ymax = data[18];
        // let zmin = data[20];
        // let zmax = data[22];
        // let alpha = data[24];
        // let theta = data[26];
        // Chart function need to be written
      } else if (block === 20) {
        // Process data for Affich_m block

        // store length of data for each line
        let length_of_data = data.length;
        let block_id = data[2]; // to store block id of affichm block
        let columns = data[5]; // gets column of matrix

        // below code creates a html code which is table with data in that
        // (To display it as matrix)
        let p = "<b>Value of Block : " + data[length_of_data-1] + "-" + block_id + "</b> (Refer to label on block)<br><br><table style='width:100%'><tr>";
        let count = 1;
        for (let k = 6; k < (length_of_data-1); k++) {
          if (data[k].length !== 0) {
            p += "<td>";
            p += data[k];
            if ((count % columns) === 0) {
              // to break into new column of table
              p += "</td></tr><tr>";
            } else {
              p += "</td>";
            }
            count++;
          }
        }
        p += "</table>";
        // to send data to display result
        create_affich_displaytext(p, block_id);
      }
    }, false)
    sse.addEventListener('duplicate', e => {
      printloglines();
      console.log('duplicate', e);
    }, false)
    sse.addEventListener('DONE', () => {
      printloglines();
      console.log('DONE');
      sse.close();
      setGraphStatusDone();
    }, false)
    sse.addEventListener('ERROR', e => {
      printloglines();
      console.log('ERROR', e);
      sse.close();
    }, false)
    sse.addEventListener('MESSAGE', e => {
      printloglines();
      console.log('MESSAGE', e);
      sse.close();
    }, false)
  }, [taskId, RANGE, block_list, chartIdList, name_values_colormap])

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

  const getSimulationResult = useCallback((task_id) => {
    if (task_id === '')
      return

    if (isResult)
      return

    const getUrl = 'simulation/status/' + task_id
    const getStreamingUrl = 'simulation/streaming/' + task_id

    simulationResult(getUrl, getStreamingUrl)
  }, [isResult, simulationResult])

  useEffect(() => getSimulationResult(taskId), [taskId, getSimulationResult])

/*
 * Function to display values of all affich blocks
 * displayParameter : Contains the data which is display as data of affich
 * block
 * blockId : is used to get needed div according to affichm id
 */
function create_affich_displaytext (displayParameter, blockId) {
    // updating html data of div html for each time change according to each
    // affich
    $('#affichdata-'+blockId).html(displayParameter);
};

// Gets data (array with x , y and coloraxis values) to be passed to chart points
function get_points_for_data (data, m, n) {
    const array_data = [];
    let i = 12;
    for (let x = (m-2) ; x >= 0; x--) {
        for (let y = 0 ; y < (n-1) ; y++) {
            const data_values = [];
            data_values[0] = x;
            data_values[1] = y;
            data_values[2] = parseInt(data[i]);
            array_data.push(data_values);
            i++;
        }
    }
    return array_data;
}

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
                          (noOfGraphs >= 1)
                            ? <Graph2
                              key={0}
                              ref={el => graphsRef.current[0] = el}
                              datapoint={datapointsRef.current[0]}
                            />
                            : <div />
                        }
                        {
                          (noOfGraphs >= 2)
                            ? <Graph2
                              key={1}
                              ref={el => graphsRef.current[1] = el}
                              datapoint={datapointsRef.current[1]}
                            />
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

SimulationScreen2.propTypes = {
  open: PropTypes.bool,
  close: PropTypes.func
}
