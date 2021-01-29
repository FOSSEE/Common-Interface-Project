import * as actions from './actions'

// Action to update netlist with component nodes and parameters
export const setNetlist = (netlist) => (dispatch) => {
  dispatch({
    type: actions.SET_NETLIST,
    payload: {
      netlist: netlist
    }
  })
}

// Action to update netlist title
export const setTitle = (title) => (dispatch) => {
  dispatch({
    type: actions.SET_TITLE,
    payload: {
      title: title
    }
  })
}

// Action to update netlist model section
export const setModel = (model) => (dispatch) => {
  dispatch({
    type: actions.SET_MODEL,
    payload: {
      model: model
    }
  })
}
