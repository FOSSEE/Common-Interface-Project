import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'

import api from '../utils/Api'
import { styleToObject } from '../utils/GalleryUtils'

const initialState = {
  block: null,
  name: '',
  id: '',
  parameter_values: {},
  errorFields: {},
  isPropertiesWindowOpen: false,
  compProperties: [],
  displayProperties: {},
  isLoading: false
}

// Actions for listing stored component properites on double click on component
export const getCompProperties = createAsyncThunk(
  'componentProperties/getCompProperties',
  async (block, { rejectWithValue }) => {
    const style = styleToObject(block.style).default
    const url = 'newblockparameters/?block__name=' + style
    try {
      const res = await api.get(url)
      if (res.status === 200) {
        return res.data
      }
      return rejectWithValue(res.data || 'Failed to get component properties')
    } catch (err) {
      console.error(err)
      const res = err.response
      return rejectWithValue(res.data || 'Failed to get component properties')
    }
  })

// Actions for updating entered component properites on clicking set parameters
export const setCompProperties = createAsyncThunk(
  'componentProperties/setCompProperties',
  async ({ block, parameterValues, errorFields }, { rejectWithValue }) => {
    const style = styleToObject(block.style).default
    const url = 'setblockparameter'
    const parameters = Object.values(parameterValues)
    const data = { block: style, parameters }
    try {
      const res = await api.post(url, data)
      if (res.status === 200) {
        block.parameter_values = parameterValues
        block.errorFields = errorFields
        return {
          id: block.id,
          parameter_values: parameterValues,
          errorFields,
          displayProperties: res.data
        }
      }
      return rejectWithValue(res.data || 'Failed to set component properties')
    } catch (err) {
      console.error(err)
      const res = err.response
      return rejectWithValue(res.data || 'Failed to set component properties')
    }
  })

const componentPropertiesSlice = createSlice({
  name: 'componentProperties',
  initialState,
  reducers: {
    closeCompProperties: (state) => {
      state.isPropertiesWindowOpen = false
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(getCompProperties.pending, (state, action) => {
        state.isLoading = true
        state.isPropertiesWindowOpen = true
        state.compProperties = []
        const block = action.meta.arg
        state.name = styleToObject(block.style).default
        state.id = block.id
        state.parameter_values = block.parameter_values
        state.errorFields = block.errorFields
        state.displayProperties = block.displayProperties       
      })
      .addCase(getCompProperties.fulfilled, (state, action) => {
        state.isLoading = false
        state.isPropertiesWindowOpen = true
        state.compProperties = action.payload
      })
      .addCase(getCompProperties.rejected, (state) => {
        state.isLoading = false
        state.isPropertiesWindowOpen = false
      })
      .addCase(setCompProperties.pending, (state) => {
        state.isLoading = true
        state.isPropertiesWindowOpen = true
      })
      .addCase(setCompProperties.fulfilled, (state, action) => {
        state.isLoading = false
        state.isPropertiesWindowOpen = false
        state.id = action.payload.id
        state.parameter_values = action.payload.parameter_values
        state.errorFields = action.payload.errorFields
        state.displayProperties = action.payload.displayProperties
      })
      .addCase(setCompProperties.rejected, (state) => {
        state.isLoading = false
        state.isPropertiesWindowOpen = true
      })
  }
})

export const {
  closeCompProperties
} = componentPropertiesSlice.actions

export default componentPropertiesSlice.reducer
