import React, { useState } from 'react'
import {
  List,
  ListItem,
  Button,
  TextField,
  InputAdornment,
  MenuItem,
  ExpansionPanel,
  ExpansionPanelSummary,
  ExpansionPanelDetails,
  Typography
} from '@material-ui/core'
import ExpandMoreIcon from '@material-ui/icons/ExpandMore'
import { makeStyles } from '@material-ui/core/styles'
import { useSelector, useDispatch } from 'react-redux'
import $ from 'jquery'

import { Queue } from '../../utils/Queue'
import { setResultTitle, setResultGraph, setResultText, addDatapointChart } from '../../redux/actions/index'
import { Save } from './Helper/ToolbarTools'
import SimulationScreen2 from './SimulationScreen2'
import { addPointToQueue, setStatusDone } from '../Shared/Graph2'
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

  const [simulateOpen, setSimulateOpen] = React.useState(false)
  const handleSimulateOpen = () => {
    setSimulateOpen(true)
  }

  const handleSimulateClose = () => {
    setSimulateOpen(false)
  }

  // Prepare Netlist to file
  const prepareNetlist = (netlist) => {
    const titleA = netfile.title.split(' ')[1]
    const myblob = new Blob([netlist], {
      type: 'text/plain'
    })
    const file = new File([myblob], `${titleA}.xml`, { type: 'text/xml', lastModified: Date.now() })
    sendNetlist(file)
  }

  function sendNetlist (file) {
    netlistConfig(file)
      .then((response) => {
        const res = response.data
        const getUrl = 'simulation/status/'.concat(res.details.task_id)
        const getStreamingUrl = 'simulation/streaming/'.concat(res.details.task_id)

        simulationResult(getUrl, getStreamingUrl)
      })
      .catch(function (error) {
        console.log(error)
      })
  }

  // Upload the nelist
  function netlistConfig (file) {
    const formData = new FormData()
    formData.append('app_name', process.env.REACT_APP_NAME)
    formData.append('file', file)
    for (const [key, value] of Object.entries(transientAnalysisControlLine)) {
      formData.append(key, value)
    }
    const config = {
      headers: {
        'content-type': 'multipart/form-data'
      }
    }
    return api.post('simulation/upload', formData, config)
  }

  const [isResult, setIsResult] = useState(false)

  var chart_id_list = [];
  var points_list = [];
  var series_list = [];
  // Keep track of block number for each graph(chart)
  var block_list = [];
  // Keep track of RANGE of each graph(chart)
  var RANGE = [];
  var clientID;
  // define variables for block event
  // fig_id - figure_id  of blocks,
  // pnts - Points list of the blocks
  var fig_id, pnts = [];
  var name_values_colormap = new Map(); //for storing colormap values of cmatview and cmat3d block

/*
 * Function to display values of all affich blocks
 * displayParameter : Contains the data which is display as data of affich
 * block
 * blockId : is used to get needed div according to affichm id
 */
var create_affich_displaytext = function(displayParameter, blockId) {
    $('#img_loader').html(""); // remove loading image once data is received
    // updating html data of div html for each time change according to each
    // affich
    $('#affichdata-'+blockId).html(displayParameter);
};

// Function to create a new chart
var create_new_chart = function(id, no_of_graph, ymin, ymax, xmin, xmax, type_chart, title_text) {
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

    var lineWidth = 2;
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

    dispatch(addDatapointChart(id, type_chart, title_text, xmin, ymin, xmax, ymax, pointRange, lineWidth, pointWidth));

    if (title_text.substring(0, 5) !== "BARXY") {
        chart_id_list.push(id);
        points_list.push(new Queue());
        series_list.push([]);
    }
};

//To create coloraxis array which will be passed to cmatview chart for heatmap creation
function get_color_axis_for_points(block_uid){
    var color_axis_array = [];
    var get_hex_color_array = name_values_colormap.get(block_uid);
    for(var i = 0; i < get_hex_color_array.length; i++){
        var color_values = {};
        var temp = i;
        color_values["from"] = temp + 1;
        color_values["to"] = temp + 2;
        color_values["color"] = get_hex_color_array[i];
        color_axis_array.push(color_values);
    }
    return color_axis_array;
}

//Gets data (array with x , y and coloraxis values) to be passed to chart points
function get_points_for_data(data, m, n){
    var array_data = [];
    var i = 12;
    for (var x = (m-2) ; x >= 0; x--){
        for (var y = 0 ; y < (n-1) ; y++){
            var data_values = [];
            data_values[0] = x;
            data_values[1] = y;
            data_values[2] = parseInt(data[i]);
            array_data.push(data_values);
            i++;
        }
    }
    return array_data;
}

//Chart function for cmatview which has less than 10*10 matrix size
var create_chart_for_cmatview = function(id, m, n, title_text, color_axis) {
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

    chart_id_list.push(id);
    points_list.push(new Queue());
    series_list.push([]);
};

//Chart function for cmatview large data ie matrix more than 10*10 size
var create_chart_for_large_data_cmatview = function(id, m, n, title_text, color_axis) {
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

    chart_id_list.push(id);
    points_list.push(new Queue());
    series_list.push([]);
};


// Function to create a new 3d-chart
var create_new_chart_3d = function(id, no_of_graph, xmin, xmax, ymin, ymax, zmin, zmax, type_chart, title_text, alpha, theta) {
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
    var lineWidth = 1;
    var radius = 1;
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

    chart_id_list.push(id);
    points_list.push(new Queue());
    series_list.push([]);
};

  function streamSimulationResult(streamingUrl) {
    var block;
    // Initialise variable for entry condition of creating chart for BARXY and
    // AFFICH_m
    var block_entry_BARXY = 1;
    var cmatview_counter = 0; // counter to know how many line in log
    let loglines = 0;

    function printloglines() {
        if (loglines > 0) {
            console.log(loglines, 'log lines');
            loglines = 0;
        }
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
          let chart = $('#chart-'+fig_id).highcharts();
          chart.addSeries({
            id: fig_id,
            data: []
          });
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
        xhr.onload = function() {
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
              anchor.download = "writec-" + clientID + ".datas";
            } else {
              anchor.download = "audio-" + clientID + ".au";
            }
            anchor.click();
            document.body.removeChild(anchor);
            window.URL.revokeObjectURL(url);
          }
        };
        xhr.send(form);
        let xhr2 = new XMLHttpRequest();
        xhr2.open("POST", "/deletefile");
        xhr2.onload = function() {
        };
        xhr2.send(form);
      } else if (block < 5 ||block === 9 ||block === 23 ||block === 12) {
        // added new condition for ceventscope
        // process data for 2D-SCOPE blocks
        let figure_id = 0 ;
        if (block === 2) { //For cmscope block
          figure_id = data[4];
        } else {
          figure_id = data[2];
        }
        let line_id = parseInt(data[6]);
        let x = parseFloat(data[8]);
        let y = parseFloat(data[9]);
        if (chart_id_list.indexOf(figure_id) < 0) {
          // set default chart type

          // if sink block is CSCOPXY or CANIMXY
          if (block === 4 || block === 9) {
            let chart_type = 'scatter';
            if (block === 4) {
              create_new_chart(figure_id, data[10], data[13], data[14], data[11], data[12], chart_type, data[15]+'-'+data[2]);
            } else {
              create_new_chart(figure_id, data[10], data[13], data[14], data[11], data[12], chart_type, data[16]+'-'+data[2]);
            }
            RANGE[chart_id_list.indexOf(figure_id)] = parseFloat(data[12]);
          } else {
            // Event Handling block is ceventscope
            if (block === 23) {
              let chart_type = 'column';
              create_new_chart(figure_id, data[10], 0, 1, 0, data[11], chart_type, data[12]+'-'+data[2]);
              RANGE[chart_id_list.indexOf(figure_id)] = parseFloat(data[11]);
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
              RANGE[chart_id_list.indexOf(figure_id)] = parseFloat(30);
            } else {
              // sink block is not CSCOPXY
              let chart_type = 'line';
              create_new_chart(figure_id, data[10], data[11], data[12], 0, data[13], chart_type, data[14]+'-'+data[2]);
              RANGE[chart_id_list.indexOf(figure_id)] = parseFloat(data[13]);
            }
          }
        }
        let index = chart_id_list.indexOf(figure_id);
        // store 2d-data
        if (block !== 12) {
          points_list[index].enqueue([line_id, x, y]);
          addPointToQueue(figure_id, [line_id, x, y]);
        } else {
          let values = get_points_for_data(data, data[8], data[10]);
          cmatview_counter++; // to count lines from log
          if (cmatview_counter === 1) {
            //Only add points of line 1, so that no delay in chart appearance)
            points_list[index].enqueue([line_id, values]);
          } else if (cmatview_counter < 16) {
            //Only add points of line which are multiple of 5, till 15 like 5 10 15 (this is to reduce load on browser)
            let count = cmatview_counter % 5;
            if (count === 0) {
              points_list[index].enqueue([line_id, values]);
            }
          } else {
            //Only add points of line which are multiple of 10 but after 16 like 20 30 ... (this is to reduce load on browser)
            let count = cmatview_counter % 10;
            if (count === 0) {
              points_list[index].enqueue([line_id, values]);
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
        if (chart_id_list.indexOf(figure_id) < 0) {
          let chart_type = 'scatter';
          if (block === 10) {
            create_new_chart_3d(figure_id, data[11], data[12], data[13], data[14], data[15], data[16], data[17], chart_type, data[21]+'-'+data[2], data[18], data[19]);
          } else {
            create_new_chart_3d(figure_id, data[11], data[12], data[13], data[14], data[15], data[16], data[17], chart_type, data[20]+'-'+data[2], data[18], data[19]);
          }
        }
        let index = chart_id_list.indexOf(figure_id);
        // store 3d-data
        points_list[index].enqueue([line_id, x, y, z]);
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
      setStatusDone();
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
  }

  // Get the simulation result with task_Id
  function simulationResult (url, streamingUrl) {
    api
      .get(url)
      .then((res) => {
        switch (res.data.state) {
          case 'PROGRESS':
          case 'PENDING':
          setTimeout(() => simulationResult(url, streamingUrl), 10000)
          break

          case 'STREAMING':
          streamSimulationResult(streamingUrl)
          setIsResult(true)
          dispatch(setResultGraph(null))
          break

          default:
          const result = res.data.details
          if (result === null) {
            setIsResult(false)
          } else {
            setIsResult(true)
            const temp = res.data.details.data
            const data = result.data
            if (res.data.details.graph === 'true') {
              const simResultGraph = { labels: [], x_points: [], y_points: [] }
              // populate the labels
              for (let i = 0; i < data.length; i++) {
                simResultGraph.labels[0] = data[i].labels[0]
                const lab = data[i].labels
                // lab is an array containeing labels names ['time','abc','def']
                simResultGraph.x_points = data[0].x

                // labels
                for (let x = 1; x < lab.length; x++) {
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
                for (let z = 0; z < data[i].y.length; z++) {
                  simResultGraph.y_points.push(data[i].y[z])
                }
              }

              simResultGraph.x_points = simResultGraph.x_points.map(d => parseFloat(d))

              for (let i1 = 0; i1 < simResultGraph.y_points.length; i1++) {
                simResultGraph.y_points[i1] = simResultGraph.y_points[i1].map(d => parseFloat(d))
              }

              dispatch(setResultGraph(simResultGraph))
            } else {
              const simResultText = []
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
      .then((res) => { handleSimulateOpen() })
      .catch(function (error) {
        console.log(error)
      })
  }

  const startSimulate = (type) => {
    const compNetlist = Save()
    switch (type) {
      case 'Transient':
        dispatch(setResultTitle('Transient Analysis Output'))
        break
      default:
        break
    }

    const netlist = compNetlist

    prepareNetlist(netlist)
  }

  // simulation properties add expression input box
  return (
    <>
      <div className={classes.SimulationOptions}>
      {
        simulateOpen
        ? <SimulationScreen2 open={simulateOpen} isResult={isResult} close={handleSimulateClose} />
        : <div />
      }

        {/* Simulation modes list */}
        <List>

          {/* Transient Analysis */}
          <ListItem className={classes.simulationOptions} divider>
            <ExpansionPanel>
              <ExpansionPanelSummary
                expandIcon={<ExpandMoreIcon />}
                aria-controls='panel1a-content'
                id='panel1a-header'
              >
                <Typography className={classes.heading}>Transient Analysis</Typography>
              </ExpansionPanelSummary>
              <ExpansionPanelDetails>
                <form className={classes.propertiesBox} noValidate autoComplete='off'>
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
                      <Button id='transientAnalysisSimulate' size='small' variant='contained' color='primary' onClick={(e) => { startSimulate('Transient') }}>
                        Simulate
                      </Button>
                    </ListItem>
                  </List>
                </form>
              </ExpansionPanelDetails>
            </ExpansionPanel>
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
