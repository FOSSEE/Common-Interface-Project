import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import api from '../../utils/Api'

// Define the initial state
const initialState = {
  block: null,
  name: '',
  parameter_values: {},
  errorFields: {},
  isPropertiesWindowOpen: false,
  compProperties: {},
  displayProperties: {},
  isLoading: false
}

// Create a new RTK slice
export const componentPropertiesSlice = createSlice({
  name: 'componentProperties',
  initialState,
  reducers: {
    loadingGetCompProperties: (state, action) => {
      state.name = action.payload.name
      state.isPropertiesWindowOpen = true
      state.compProperties = undefined
      state.isLoading = action.payload.isLoading
    },
    getCompProperties: (state, action) => {
      state.block = action.payload.block
      state.name = action.payload.name
      state.parameter_values = action.payload.parameter_values
      state.errorFields = action.payload.errorFields
      state.isPropertiesWindowOpen = true
      state.displayProperties = action.payload.displayProperties
      state.compProperties = action.payload.compProperties
      state.isLoading = false
    },
    loadingSetCompProperties: (state, action) => {
      state.isPropertiesWindowOpen = true
      state.isLoading = action.payload.isLoading
    },
    setCompProperties: (state, action) => {
      state.block = action.payload.block
      state.parameter_values = action.payload.parameter_values
      state.errorFields = action.payload.errorFields
      state.isPropertiesWindowOpen = false
      state.displayProperties = action.payload.displayProperties
      state.isLoading = false
    },
    closeCompProperties: (state) => {
      state.isPropertiesWindowOpen = false
    }
  }
})

// Export the actions
export const { loadingGetCompProperties, getCompProperties, loadingSetCompProperties, setCompProperties, closeCompProperties } = componentPropertiesSlice.actions

// Create an async thunk for fetching component properties
export const fetchCompProperties = createAsyncThunk(
  'componentProperties/fetchCompProperties',
  async (block, { dispatch }) => {
    dispatch(loadingGetCompProperties({ name: block.style, isLoading: true }))
    try {
      const url = 'block_parameters/?block__name=' + block.style
      const res = await api.get(url)
      return {
        block,
        name: block.style,
        parameterValues: block.parameter_values,
        errorFields: block.errorFields,
        displayProperties: block.displayProperties,
        compProperties: res.data[0]
      }
    } catch (err) {
      console.error(err)
      dispatch(loadingGetCompProperties({ name: block.style, isLoading: false }))
    }
  }
)

// Create an async thunk for setting component properties
export const setBlockParameter = createAsyncThunk(
  'componentProperties/setBlockParameter',
  async (block, parameterValues, errorFields, { dispatch }) => {
    dispatch(loadingSetCompProperties({ isLoading: true }))
    try {
      const url = 'setblockparameter'
      const filteredParameterValues = Object.fromEntries(Object.entries(parameterValues).filter(([k, v]) => v != null))
      const data = { block: block.style, ...filteredParameterValues }
      const res = await api.post(url, data)
      block.parameter_values = filteredParameterValues
      block.errorFields = errorFields
      return {
        block,
        parameterValues,
        errorFields,
        displayProperties: res.data
      }
    } catch (err) {
      console.error(err)
      dispatch(loadingSetCompProperties({ isLoading: false }))
    }
  }
)

// Export the reducer
export default componentPropertiesSlice.reducer
