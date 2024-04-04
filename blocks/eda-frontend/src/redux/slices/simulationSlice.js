import { createSlice } from '@reduxjs/toolkit'

const simulationSlice = createSlice({
  name: 'simulation',
  initialState: {
    title: '',
    isGraph: false,
    text: [],
    graph: {},
    isSimRes: false,
    taskId: ''
  },
  reducers: {
    setResultTitle(state, action) {
      state.title = action.payload.title
    },
    setResultGraph(state, action) {
      state.isSimRes = true
      state.isGraph = true
      state.graph = action.payload.graph
    },
    setResultText(state, action) {
      state.isSimRes = true
      state.isGraph = false
      state.text = action.payload.text
    },
    setResultTaskId(state, action) {
      state.taskId = action.payload.taskId
    }
  }
})

export const { setResultTitle, setResultGraph, setResultText, setResultTaskId } = simulationSlice.actions

export default simulationSlice.reducer
