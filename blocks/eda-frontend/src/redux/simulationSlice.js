import { createSlice } from '@reduxjs/toolkit'

const initialState = {
  isSimulating: false,
  title: '',
  isGraph: false,
  text: [],
  errorMessage: '',
  graph: {},
  isSimRes: false,
  taskId: '',
  scriptTaskId: ''
}

const simulationSlice = createSlice({
  name: 'simulation',
  initialState,
  reducers: {
    resetResult: (state) => {
      state.isSimulating = false
      state.title = ''
      state.isGraph = false
      state.text = []
      state.errorMessage = ''
      state.graph = {}
      state.isSimRes = false
      state.taskId = ''
    },
    setSimulating: (state, action) => {
      state.isSimulating = action.payload
    },
    setResultTitle: (state, action) => {
      state.title = action.payload
    },
    setResultGraph: (state, action) => {
      state.isSimRes = true
      state.isGraph = true
      state.graph = action.payload
    },
    setResultText: (state, action) => {
      state.isSimRes = true
      state.isGraph = false
      state.text = action.payload
    },
    setErrorMessage: (state, action) => {
      state.isSimulating = false
      state.isGraph = false
      state.errorMessage = action.payload
    },
    setResultTaskId: (state, action) => {
      state.taskId = action.payload
    },
    setScriptTaskId: (state, action) => {
      state.scriptTaskId = action.payload
    }
  }
})

export const {
  resetResult,
  setSimulating,
  setResultTitle,
  setResultGraph,
  setResultText,
  setErrorMessage,
  setResultTaskId,
  setScriptTaskId
} = simulationSlice.actions

export default simulationSlice.reducer
