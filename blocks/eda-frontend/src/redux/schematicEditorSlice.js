import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'

import api from '../utils/Api'

const initialState = {
  isLoading: false,
  isSimulate: false,
  libraries: [],
  collapse: {},
  components: {},
  component_images: []
}

// Api call for fetching component library list
export const fetchLibraries = createAsyncThunk(
  'schematicEditor/fetchLibraries',
  async (_, { rejectWithValue }) => {
    // SAMPLE Response from API
    // [
    //  {
    //   "id": 1
    //   "name": "Commonly Used Blocks",
    //   "sort_order": 1
    // },
    // ] -- Multiple dicts in array
    try {
      const res = await api.get('categories/')
      if (res.status === 200) {
        return res.data
      }
      return rejectWithValue(res.data || 'Failed to load libraries')
    } catch (err) {
      console.error(err)
      const res = err.response
      return rejectWithValue(res.data || 'Failed to load libraries')
    }
  })

// Api call for fetching components under specified library id
export const fetchComponents = createAsyncThunk(
  'schematicEditor/fetchComponents',
  async (libraryId, { rejectWithValue }) => {
    // SAMPLE Response from API
    //   [
    // {
    //   "id": 1,
    //   "blocktype": 1,
    //   "name": "LOGICAL_OP",
    //   "categories": [ 1 ],
    //   "initial_explicit_input_ports": 2,
    //   "initial_implicit_input_ports": 0,
    //   "initial_explicit_output_ports": 1,
    //   "initial_implicit_output_ports": 0,
    //   "initial_display_parameter": "AND",
    //   "p000_value_initial": "AND",
    //   "p001_value_initial": "AND",
    //   "p002_value_initial": "AND",
    //   "p003_value_initial": "AND",
    //   "p004_value_initial": null,
    //   ...
    //   "p039_value_initial": null,
    // },
    // ] -- Multiple dicts in array
    const url = 'newblocks/?categories=' + parseInt(libraryId)
    try {
      const res = await api.get(url)
      if (res.status === 200) {
        return { components: res.data, id: libraryId }
      }
      return rejectWithValue(res.data || 'Failed to load blocks')
    } catch (err) {
      console.error(err)
      const res = err.response
      return rejectWithValue(res.data || 'Failed to load blocks')
    }
  })

// Api call for fetching component image names
export const fetchComponentImages = createAsyncThunk(
  'schematicEditor/fetchComponentImages',
  async (_, { rejectWithValue }) => {
    // SAMPLE Response from API
    //   [
    //   "palettes/LOGICAL_OP.png",
    //   ...
    //   "palettes/SUPER_f.png"
    // ] -- Multiple strings in array
    const url = 'block_images'
    try {
      const res = await api.get(url)
      if (res.status === 200) {
        return res.data
      }
      return rejectWithValue(res.data || 'Failed to load block images')
    } catch (err) {
      console.error(err)
      const res = err.response
      return rejectWithValue(res.data || 'Failed to load block images')
    }
  })

const schematicEditorSlice = createSlice({
  name: 'schematicEditor',
  initialState,
  reducers: {
    toggleCollapse: (state, action) => {
      const existingState = state.collapse[action.payload.id]
      Object.keys(state.collapse).forEach((key) => {
        state.collapse[key] = false
      })
      state.collapse[action.payload.id] = !existingState
    },
    toggleSimulate: (state) => {
      state.isSimulate = !state.isSimulate
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchLibraries.pending, (state) => {
        state.isLoading = true
      })
      .addCase(fetchLibraries.fulfilled, (state, action) => {
        // Add 'open' parameter to track open/close state of collapse
        state.isLoading = false
        const collapse = {}
        const components = {}
        action.payload.forEach(element => {
          collapse[element.id] = false
          components[element.id] = []
        })
        state.libraries = action.payload
        state.collapse = collapse
        state.components = components
      })
      .addCase(fetchLibraries.rejected, (state) => {
        state.isLoading = false
        state.libraries = {}
        state.collapse = {}
        state.components = {}
      })
      .addCase(fetchComponents.pending, (state) => {
        state.isLoading = true
      })
      .addCase(fetchComponents.fulfilled, (state, action) => {
        state.isLoading = false
        state.components[action.payload.id] = action.payload.components
      })
      .addCase(fetchComponents.rejected, (state) => {
        state.isLoading = false
      })
      .addCase(fetchComponentImages.pending, (state) => {
        state.isLoading = true
      })
      .addCase(fetchComponentImages.fulfilled, (state, action) => {
        state.isLoading = false
        state.component_images = action.payload
      })
      .addCase(fetchComponentImages.rejected, (state) => {
        state.isLoading = false
      })
  }
})

export const {
  toggleCollapse,
  toggleSimulate
} = schematicEditorSlice.actions

export default schematicEditorSlice.reducer
