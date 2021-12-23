import * as actions from './actions'

// Actions to update title for simulation result screen
export const setResultTitle = (title) => (dispatch) => {
  dispatch({
    type: actions.SET_RESULT_TITLE,
    payload: {
      title: title
    }
  })
}

// Action to update store with graphical result points
export const setResultGraph = (graph) => (dispatch) => {
  dispatch({
    type: actions.SET_RESULT_GRAPH,
    payload: {
      graph: graph
    }
  })
}

// Action to update store with simulation result text
export const setResultText = (text) => (dispatch) => {
  dispatch({
    type: actions.SET_RESULT_TEXT,
    payload: {
      text: text
    }
  })
}

// Actions to update task id for simulation result screen
export const setResultTaskId = (taskId) => (dispatch) => {
  dispatch({
    type: actions.SET_RESULT_TASK_ID,
    payload: {
      taskId: taskId
    }
  })
}
