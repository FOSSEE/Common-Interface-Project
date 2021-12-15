import * as actions from './actions'

// Actions to update title for simulation result screen
export const addDatapointChart = (id, type, title, xMin, yMin, xMax, yMax, pointRange, lineWidth, pointWidth) => (dispatch) => {
  dispatch({
    type: actions.ADD_DATAPOINT_CHART,
    payload: {
      datapointId: id,
      datapointType: type,
      datapointTitle: title,
      datapointXMin: xMin,
      datapointYMin: yMin,
      datapointXMax: xMax,
      datapointYMax: yMax,
      datapointPointRange: pointRange,
      datapointLineWidth: lineWidth,
      datapointPointWidth: pointWidth
    }
  })
}

// Action to update store with graphical result points
export const addDatapointPoint = (id, point) => (dispatch) => {
  dispatch({
    type: actions.ADD_DATAPOINT_POINT,
    payload: {
      datapointId: id,
      datapointPoint: point
    }
  })
}
