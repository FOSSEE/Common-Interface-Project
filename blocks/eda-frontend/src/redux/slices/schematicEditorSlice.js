import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import api from '../../utils/Api'

// Async thunk action for fetching component library list
export const fetchLibraries = createAsyncThunk(
  'schematicEditor/fetchLibraries',
  async (_, { dispatch, rejectWithValue }) => {
    try {
      const response = await api.get('categories/')
      return response.data
    } catch (error) {
      return rejectWithValue(error.message)
    }
  }
)

// Async thunk action for fetching components under specified library id
export const fetchComponents = createAsyncThunk(
  'schematicEditor/fetchComponents',
  async (libraryId, { dispatch, rejectWithValue }) => {
    try {
      const url = `newblocks/?categories=${parseInt(libraryId)}`
      const response = await api.get(url)
      return { components: response.data, id: libraryId }
    } catch (error) {
      return rejectWithValue(error.message)
    }
  }
)

// Async thunk action for fetching component image names
export const fetchComponentImages = createAsyncThunk(
  'schematicEditor/fetchComponentImages',
  async (_, { dispatch, rejectWithValue }) => {
    try {
      const url = 'block_images'
      const response = await api.get(url)
      return response.data
    } catch (error) {
      return rejectWithValue(error.message)
    }
  }
)

const schematicEditorSlice = createSlice({
  name: 'schematicEditor',
  initialState: {
    isSimulate: false,
    libraries: [],
    collapse: {},
    components: {}
  },
  reducers: {
    toggleCollapse (state, action) {
      const existingState = state.collapse[action.payload.id]
      state.collapse = Object.keys(state.collapse).reduce((accObj, parseObj) => {
        accObj[parseObj] = false
        return accObj
      }, {})
      state.collapse[action.payload.id] = !existingState
    },
    toggleSimulate (state) {
      state.isSimulate = !state.isSimulate
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchLibraries.fulfilled, (state, action) => {
        const collapse = {}
        const components = {}
        action.payload.forEach((element) => {
          collapse[element.id] = false
          components[element.id] = []
        })
        state.libraries = action.payload
        state.collapse = collapse
        state.components = components
      })
      .addCase(fetchComponents.fulfilled, (state, action) => {
        state.components[action.payload.id] = action.payload.components
      })
      .addCase(fetchComponentImages.fulfilled, (state, action) => {
        state.component_images = action.payload
      })
  }
})

export const { toggleCollapse, toggleSimulate } = schematicEditorSlice.actions

export default schematicEditorSlice.reducer
