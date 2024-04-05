import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import api from '../../utils/Api'

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

export const getCompProperties = createAsyncThunk(
  'compProperties/getCompProperties',
  async (block, { dispatch }) => {
    dispatch(loadingGetCompProperties(true))
    const url = 'block_parameters/?block__name=' + block.style
    try {
      const response = await api.get(url)
      const compProperties = response.data[0]
      dispatch(loadingGetCompProperties(false))
      return { block, compProperties }
    } catch (error) {
      console.error(error)
      dispatch(loadingGetCompProperties(false))
      throw error
    }
  }
)

export const setCompProperties = createAsyncThunk(
  'compProperties/setCompProperties',
  async ({ block, parameterValues, errorFields }, { dispatch }) => {
    dispatch(loadingSetCompProperties(true))
    const url = 'setblockparameter'
    const filteredParameterValues = Object.fromEntries(Object.entries(parameterValues).filter(([k, v]) => v != null))
    const data = { block: block.style, ...filteredParameterValues }
    try {
      const response = await api.post(url, data)
      const displayProperties = response.data
      dispatch(loadingSetCompProperties(false))
      return { block, parameterValues, errorFields, displayProperties }
    } catch (error) {
      console.error(error)
      dispatch(loadingSetCompProperties(false))
      throw error
    }
  }
)

const compPropertiesSlice = createSlice({
  name: 'compProperties',
  initialState,
  reducers: {
    loadingGetCompProperties (state, action) {
      state.isLoading = action.payload
    },
    loadingSetCompProperties (state, action) {
      state.isLoading = action.payload
    },
    closeCompProperties (state) {
      state.isPropertiesWindowOpen = false
      // You may want to add other state updates here as well
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(getCompProperties.fulfilled, (state, action) => {
        const { block, compProperties } = action.payload
        state.block = block
        state.compProperties = compProperties
        state.isLoading = false
        state.isPropertiesWindowOpen = true
      })
      .addCase(setCompProperties.fulfilled, (state, action) => {
        const { block, parameterValues, errorFields, displayProperties } = action.payload
        state.block = block
        state.parameter_values = parameterValues
        state.errorFields = errorFields
        state.displayProperties = displayProperties
        state.isPropertiesWindowOpen = false
        state.isLoading = false
      })
  }
})

export const { loadingGetCompProperties, loadingSetCompProperties, closeCompProperties } = compPropertiesSlice.actions

export default compPropertiesSlice.reducer
