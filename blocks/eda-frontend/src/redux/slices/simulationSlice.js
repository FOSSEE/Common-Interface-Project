import { createSlice } from '@reduxjs/toolkit'

export const simulationSlice = createSlice({
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
    setResultTitle: (state, action) => {
      state.title = action.payload.title
    },
    setResultGraph: (state, action) => {
      state.isSimRes = true
      state.isGraph = true
      state.graph = action.payload.graph
    },
    setResultText: (state, action) => {
      state.isSimRes = true
      state.isGraph = false
      state.text = action.payload.text
    },
    setResultTaskId: (state, action) => {
      state.taskId = action.payload.taskId
    }
  }
})

export const { setResultTitle, setResultGraph, setResultText, setResultTaskId } = simulationSlice.actions

export const selectTitle = (state) => state.simulation.title
export const selectIsGraph = (state) => state.simulation.isGraph
export const selectText = (state) => state.simulation.text
export const selectGraph = (state) => state.simulation.graph
export const selectIsSimRes = (state) => state.simulation.isSimRes
export const selectTaskId = (state) => state.simulation.taskId

export default simulationSlice.reducer
