import * as actions from '../actions/actions'

const initialState = {
  datapointId: 0,
  datapointType: '',
  datapointTitle: '',
  datapointXMin: 0,
  datapointYMin: 0,
  datapointXMax: 0,
  datapointYMax: 0,
  datapointPointRange: null,
  datapointLineWidth: 2,
  datapointPointWidth: 2
}

export default function (state = initialState, action) {
  switch (action.type) {
    case actions.ADD_DATAPOINT_CHART: {
      return {
        ...state,
        datapointId: action.payload.datapointId,
        datapointType: action.payload.datapointType,
        datapointTitle: action.payload.datapointTitle,
        datapointXMin: action.payload.datapointXMin,
        datapointYMin: action.payload.datapointYMin,
        datapointXMax: action.payload.datapointXMax,
        datapointYMax: action.payload.datapointYMax,
        datapointPointRange: action.payload.datapointPointRange,
        datapointLineWidth: action.payload.datapointLineWidth,
        datapointPointWidth: action.payload.datapointPointWidth
      }
    }

    default:
      return state
  }
}
