import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'

import api from '../utils/Api'

import { logout } from './authSlice'

const initialState = {
  isLoading: false,
  schematics: [],
  gallery: []
}

// Api call for listing saved schematic to display on dashboard
export const fetchSchematics = createAsyncThunk(
  'dashboard/fetchSchematics',
  async (_, { getState, rejectWithValue }) => {
    const token = getState().auth.token
    if (!token) return rejectWithValue('No token found')

    const config = {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${token}`
      }
    }

    try {
      const res = await api.get('save/list', config)
      if (res.status === 200) {
        return res.data
      }

      return rejectWithValue('No data found')
    } catch (err) {
      console.error(err)
      return rejectWithValue('No data found')
    }
  })

export const fetchGallery = createAsyncThunk(
  'dashboard/fetchGallery',
  async (_, { rejectWithValue }) => {
    try {
      const res = await api.get('save/gallery')
      if (res.status === 200) {
        return res.data
      }

      return rejectWithValue('No data found')
    } catch (err) {
      console.error(err)
      return rejectWithValue('No data found')
    }
  })

// Api call for deleting saved schematic
export const deleteSchematic = createAsyncThunk(
  'dashboard/deleteSchematic',
  async (saveId, { getState, rejectWithValue, dispatch }) => {
    const token = getState().auth.token
    if (!token) return rejectWithValue('No token found')

    const config = {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${token}`
      }
    }

    try {
      const res = await api.delete(`save/diagram/${saveId}`, config)
      if (res.status === 200) {
        await dispatch(fetchSchematics())
        return saveId
      }

      return rejectWithValue('No data found')
    } catch (err) {
      console.error(err)
      return rejectWithValue('No data found')
    }
  })

const dashboardSlice = createSlice({
  name: 'dashboard',
  initialState,
  extraReducers: (builder) => {
    builder
      .addCase(fetchSchematics.pending, (state) => {
        state.isLoading = true
      })
      .addCase(fetchSchematics.fulfilled, (state, action) => {
        state.isLoading = false
        state.schematics = action.payload
      })
      .addCase(fetchSchematics.rejected, (state) => {
        state.isLoading = false
        state.schematics = []
      })
      .addCase(fetchGallery.pending, (state) => {
        state.isLoading = true
      })
      .addCase(fetchGallery.fulfilled, (state, action) => {
        state.isLoading = false
        state.gallery = action.payload
      })
      .addCase(fetchGallery.rejected, (state) => {
        state.isLoading = false
        state.gallery = []
      })
      .addCase(logout.fulfilled, (state) => {
        state.schematics = []
      })
  }
})

export default dashboardSlice.reducer
