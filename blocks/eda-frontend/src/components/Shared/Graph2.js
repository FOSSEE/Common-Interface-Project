import React, { Component } from 'react'
import Highcharts from 'highcharts';
import HighchartsReact from 'highcharts-react-official';
import Chart from 'chart.js'
import 'chartjs-plugin-colorschemes'
import { Queue } from '../../utils/Queue'

// Chart Style Options
Chart.defaults.global.defaultFontColor = '#e6e6e6'

let pointList = new Queue();
let statusDone = false;

export function addPointToQueue(id, point) {
  pointList.enqueue(point);
}

export function setStatusDone() {
  statusDone = true;
}

class Graph2 extends Component {
  constructor(props) {
    super(props)
    const datapoint = props.datapoint;
    this.state = {
      options: {
        chart: {
          events: {
            load: function () {
              // set up the updating of the chart each second
              let chart = this;
              let series = this.series[0];
              let starttime = Date.now();
              function addPoints() {
                while (!pointList.isEmpty()) {
                  let point = pointList.peek();
                  let x = parseFloat(point[1]);
                  let timediff = (starttime + x * 1000) - Date.now();
                  if (timediff > 0) {
                    setInterval(addPoints, timediff);
                    return;
                  }
                  let y = parseFloat(point[2]);
                  series.addPoint([x, y]);
                  pointList.dequeue();
                }
                chart.redraw();
                if (!pointList.isEmpty() || !statusDone) {
                  setInterval(addPoints, 1000);
                }
              }
              addPoints();
            }
          },
          type: datapoint.datapointType,
          animation: false,
          zoomType: 'xy'
        },
        title: {
          text: datapoint.datapointTitle
        },
        xAxis: {
          title: {
            text: 'x'
          },
          tickInterval: 2,
          startOnTick: true,
          endOnTick: true,
          showLastLabel: true,
          min: parseFloat(datapoint.datapointXMin),
          max: parseFloat(datapoint.datapointXMax)
        },
        yAxis: {
          title: {
            text: 'y'
          },
          min: parseFloat(datapoint.datapointYMin),
          max: parseFloat(datapoint.datapointYMax),
          plotLines: [{
            width: 2,
            color: '#808080'
          }]
        },
        plotOptions: {
          marker: {
            enabled: false
          },
          column: {
            pointPlacement: 0,
            pointRange: datapoint.datapointPointRange
          },
          series: {
            lineWidth: datapoint.datapointLineWidth,
            pointWidth: datapoint.datapointPointWidth,
            enableMouseTracking: false,
            states: {
              hover: {
                lineWidth: datapoint.datapointLineWidth
              }
            }
          },
          scatter: {
            marker: {
              radius: 1,
              states: {
                hover: {
                  enabled: true,
                  lineColor: 'rgb(100,100,100)'
                }
              }
            }
          }
        },
        legend: {
          enabled: false
        },
        tooltip: {
          enabled: false
        },
        series: [
          {
            data: []
          }
        ]
      }
    }
  }

  render () {
    return (
      <div>
        <HighchartsReact highcharts={Highcharts} options={this.state.options} />
      </div>
    )
  }
}

export default Graph2
