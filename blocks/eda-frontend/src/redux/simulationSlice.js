import { createSlice } from "@reduxjs/toolkit";

const initialState = {
  title: "",
  isGraph: false,
  text: [],
  graph: {},
  isSimRes: false,
  taskId: "",
  scriptTaskId: "",
};

const simulationSlice = createSlice({
  name: "simulation",
  initialState,
  reducers: {
    setResultTitle: (state, action) => {
      state.title = action.payload;
    },
    setResultGraph: (state, action) => {
      state.isSimRes = true;
      state.isGraph = true;
      state.graph = action.payload;
    },
    setResultText: (state, action) => {
      state.isSimRes = true;
      state.isGraph = false;
      state.text = action.payload;
    },
    setResultTaskId: (state, action) => {
      state.taskId = action.payload;
    },
    setScriptTaskId: (state, action) => {
      state.scriptTaskId = action.payload;
    },
  },
});

export const {
  setResultTitle,
  setResultGraph,
  setResultText,
  setResultTaskId,
  setScriptTaskId,
} = simulationSlice.actions;

export default simulationSlice.reducer;
