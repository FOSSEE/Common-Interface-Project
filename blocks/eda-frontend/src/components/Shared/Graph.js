import React from 'react'
import PropTypes from 'prop-types'
import Highcharts from 'highcharts'
import HighchartsReact from 'highcharts-react-official'
import { Queue } from '../../utils/Queue'

let statusDone = false

export function setStatusDone () {
  statusDone = true
}

class Graph extends React.Component {
  pointList = new Queue()

  addPointToQueue = (id, point) => {
    this.pointList.enqueue(point)
  }

  constructor (props) {
    super(props)
    const datapoint = props.datapoint
    const pointList = this.pointList
    let myInterval = null
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
                  const xmax = chart.xAxis[0].max
                  const xmin = chart.xAxis[0].min
                  const xshift = (xmax - xmin) * 0.2
                  const point = pointList.peek()
                  const x = parseFloat(point[1])
                  if (x > xmax) {
                    chart.xAxis[0].update({
                      max: xmax + xshift,
                      min: xmin + xshift
                    })
                    chart.redraw()
                  }
                  const timediff = starttime + x * 1000 - Date.now()
                  if (timediff > 0) {
                    chart.redraw()
                    return
                  }
                  const y = parseFloat(point[2])
                  series.addPoint([x, y])
                  pointList.dequeue()
                }
                chart.redraw()
                if (pointList.isEmpty() && statusDone) {
                  clearInterval(myInterval)
                }
              }
              myInterval = setInterval(addPoints, 450)
            }
          },
          type: datapoint.datapointType,
          showAxes: true,
          animation: false,
          zoomType: 'xy',
          options3d: {
            enabled: true,
            alpha: datapoint.datapointAlpha,
            beta: datapoint.datapointBeta,
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
        colorAxis: {
          dataClasses: datapoint.datapointDataClasses
        },
        lang: {
          noData: 'No data to display'
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
              radius: datapoint.datapointRadius,
              states: {
                hover: {
                  enabled: true,
                  lineColor: 'rgb(100,100,100)'
                }
              }
            }
          }
        },
        series: [
          {
            data: []
          }
        ],
        title: {
          text: datapoint.datapointTitle
        },
        tooltip: {
          enabled: false
        },
        xAxis: {
          title: {
            style: {
              fontWeight: 'bold',
              fontSize: '15px'
            },
            text: 'x'
          },
          gridLineWidth: 1,
          startOnTick: true,
          endOnTick: true,
          showLastLabel: true,
          min: parseFloat(datapoint.datapointXMin),
          max: parseFloat(datapoint.datapointXMax)
        },
        yAxis: {
          title: {
            rotation: 0,
            style: {
              fontWeight: 'bold',
              fontSize: '15px'
            },
            text: 'y'
          },
          gridLineWidth: 1,
          min: parseFloat(datapoint.datapointYMin),
          max: parseFloat(datapoint.datapointYMax),
          plotLines: [
            {
              width: 2,
              color: '#808080'
            }
          ]
        },
        zAxis: {
          title: {
            rotation: 300,
            margin: -30,
            style: {
              fontWeight: 'bold',
              fontSize: '15px'
            },
            text: 'z'
          },
          gridLineWidth: 1,
          min: parseFloat(datapoint.datapointZMin),
          max: parseFloat(datapoint.datapointZMax)
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

Graph.propTypes = {
  datapoint: PropTypes.object
}

export default Graph
