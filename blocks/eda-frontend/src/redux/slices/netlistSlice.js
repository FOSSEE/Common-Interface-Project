import { createSlice } from '@reduxjs/toolkit'

export const netlistSlice = createSlice({
  name: 'netlist',
  initialState: {
    title: '* Untitled',
    model: '',
    netlist: '',
    controlLine: '',
    controlBlock: ''
  },
  reducers: {
    setNetlist: (state, action) => {
      state.netlist = action.payload.netlist
    },
    setTitle: (state, action) => {
      state.title = action.payload.title
    },
    setModel: (state, action) => {
      state.model = action.payload.model
    }
  }
})

export const { setNetlist, setTitle, setModel } = netlistSlice.actions

export const selectTitle = (state) => state.netlist.title
export const selectModel = (state) => state.netlist.model
export const selectNetlist = (state) => state.netlist.netlist

export default netlistSlice.reducer
