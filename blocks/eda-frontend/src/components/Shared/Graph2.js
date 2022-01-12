import React from 'react'
import Highcharts from 'highcharts'
import HighchartsReact from 'highcharts-react-official'
import 'chartjs-plugin-colorschemes'
import { Queue } from '../../utils/Queue'

let statusDone = false

export function setStatusDone () {
  statusDone = true
}

class Graph2 extends React.Component {
  pointList = new Queue();

  addPointToQueue = (id, point) => {
    this.pointList.enqueue(point)
  }

  constructor (props) {
    super(props)
    const datapoint = props.datapoint
    const pointList = this.pointList
    this.state = {
      options: {
        chart: {
          events: {
            load: function () {
              // set up the updating of the chart each second
              const chart = this
              const series = this.series[0]
              const starttime = Date.now()
              function addPoints () {
                while (!pointList.isEmpty()) {
                  const point = pointList.peek()
                  const x = parseFloat(point[1])
                  let timediff = (starttime + x * 1000) - Date.now()
                  if (timediff > 0) {
                    if (timediff < 1000) {
                      timediff *= 5
                      if (timediff > 1000) {
                        timediff = 1000
                      }
                    }
                    setTimeout(addPoints, timediff)
                    return
                  }
                  const y = parseFloat(point[2])
                  series.addPoint([x, y])
                  pointList.dequeue()
                }
                chart.redraw()
                if (!pointList.isEmpty() || !statusDone) {
                  setTimeout(addPoints, 1000)
                }
              }
              addPoints()
            }
          },
          type: datapoint.datapointType,
          animation: false,
          zoomType: 'xy'
        },
        colorAxis: {
          dataClasses: datapoint.datapointDataClasses
        },
        legend: {
          enabled: false
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
        series: [{
          data: []
        }],
        title: {
          text: datapoint.datapointTitle
        },
        tooltip: {
          enabled: false
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
        }
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
