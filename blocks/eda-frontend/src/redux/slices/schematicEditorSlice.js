import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import api from '../../utils/Api'

const initialState = {
  isSimulate: false,
  libraries: [],
  collapse: {},
  components: {},
  componentImages: []
}

// Async thunk action creators
export const fetchLibraries = createAsyncThunk(
  'schematicEditor/fetchLibraries',
  async () => {
    const response = await api.get('categories/')
    return response.data
  }
)

export const fetchComponents = createAsyncThunk(
  'schematicEditor/fetchComponents',
  async (libraryId) => {
    const response = await api.get(`newblocks/?categories=${libraryId}`)
    return { components: response.data, id: libraryId }
  }
)

export const fetchComponentImages = createAsyncThunk(
  'schematicEditor/fetchComponentImages',
  async () => {
    const response = await api.get('block_images')
    return response.data
  }
)

const schematicEditorSlice = createSlice({
  name: 'schematicEditor',
  initialState,
  reducers: {
    toggleCollapse (state, action) {
      const { id } = action.payload
      state.collapse = { ...state.collapse, [id]: !state.collapse[id] }
    },
    toggleSimulate (state) {
      state.isSimulate = !state.isSimulate
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchLibraries.fulfilled, (state, action) => {
        state.libraries = action.payload
        state.collapse = action.payload.reduce((acc, cur) => {
          acc[cur.id] = false
          return acc
        }, {})
        state.components = action.payload.reduce((acc, cur) => {
          acc[cur.id] = []
          return acc
        }, {})
      })
      .addCase(fetchComponents.fulfilled, (state, action) => {
        const { components, id } = action.payload
        state.components[id] = components
      })
      .addCase(fetchComponentImages.fulfilled, (state, action) => {
        state.componentImages = action.payload
      })
  }
})

export const { toggleCollapse, toggleSimulate } = schematicEditorSlice.actions

export default schematicEditorSlice.reducer
