import * as actions from '../actions/actions'

const initialState = {
  title: '* Untitled',
  model: '',
  netlist: '',
  controlLine: '',
  controlBlock: ''
}

export default function (state = initialState, action) {
  switch (action.type) {
    case actions.SET_NETLIST: {
      return {
        ...state,
        netlist: action.payload.netlist
      }
    }
    case actions.SET_TITLE: {
      return {
        ...state,
        title: action.payload.title
      }
    }

    case actions.SET_MODEL: {
      return {
        ...state,
        model: action.payload.model
      }
    }
    default:
      return state
  }
}
