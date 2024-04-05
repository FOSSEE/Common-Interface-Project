import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import api from '../../utils/Api'

// Async thunk action for fetching schematics
export const fetchSchematics = createAsyncThunk(
  'dashboard/fetchSchematics',
  async (_, { getState, dispatch, rejectWithValue }) => {
    try {
      const token = getState().auth.token
      const config = {
        headers: {
          'Content-Type': 'application/json'
        }
      }

      if (token) {
        config.headers.Authorization = `Token ${token}`
      }

      const response = await api.get('save/list', config)
      return response.data
    } catch (error) {
      return rejectWithValue(error.message)
    }
  }
)

// Async thunk action for deleting a schematic
export const deleteSchematic = createAsyncThunk(
  'dashboard/deleteSchematic',
  async (saveId, { getState, dispatch, rejectWithValue }) => {
    try {
      const token = getState().auth.token
      const config = {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded'
        }
      }

      if (token) {
        config.headers.Authorization = `Token ${token}`
      }

      const response = await api.delete(`save/${saveId}`, config)
      if (response.status === 200) {
        dispatch(fetchSchematics())
      }
    } catch (error) {
      return rejectWithValue(error.message)
    }
  }
)

const dashboardSlice = createSlice({
  name: 'dashboard',
  initialState: {
    schematics: [],
    isLoading: false,
    error: null
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchSchematics.pending, (state) => {
        state.isLoading = true
        state.error = null
      })
      .addCase(fetchSchematics.fulfilled, (state, action) => {
        state.isLoading = false
        state.schematics = action.payload
      })
      .addCase(fetchSchematics.rejected, (state, action) => {
        state.isLoading = false
        state.error = action.payload
      })
  }
})

export default dashboardSlice.reducer
