import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import api from '../../utils/Api'

// Thunk action creator for fetching schematics
export const fetchSchematics = createAsyncThunk(
  'dashboard/fetchSchematics',
  async (_, { getState }) => {
    const token = getState().authReducer.token

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
  }
)

// Thunk action creator for deleting schematic
export const deleteSchematic = createAsyncThunk(
  'dashboard/deleteSchematic',
  async (saveId, { dispatch, getState }) => {
    const token = getState().authReducer.token

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
      // Dispatch fetchSchematics to update schematics after deletion
      dispatch(fetchSchematics())
    }
  }
)

const dashboardSlice = createSlice({
  name: 'dashboard',
  initialState: {
    schematics: [],
    status: 'idle',
    error: null
  },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchSchematics.pending, (state) => {
        state.status = 'loading'
      })
      .addCase(fetchSchematics.fulfilled, (state, action) => {
        state.status = 'succeeded'
        state.schematics = action.payload
      })
      .addCase(fetchSchematics.rejected, (state, action) => {
        state.status = 'failed'
        state.error = action.error.message
      })
  }
})

export const selectSchematics = (state) => state.dashboard.schematics

export default dashboardSlice.reducer
