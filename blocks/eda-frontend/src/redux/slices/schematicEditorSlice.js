import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import api from '../../utils/Api'

// Async Thunks
export const fetchLibraries = createAsyncThunk(
  'schematicEditor/fetchLibraries',
  async (_, { dispatch }) => {
    try {
      const res = await api.get('categories/')
      dispatch(schematicEditorSlice.actions.setLibraries(res.data))
    } catch (err) {
      console.error(err)
    }
  }
)

export const fetchComponents = createAsyncThunk(
  'schematicEditor/fetchComponents',
  async (libraryId, { dispatch }) => {
    try {
      const url = `newblocks/?categories=${parseInt(libraryId)}`
      const res = await api.get(url)
      dispatch(schematicEditorSlice.actions.setComponents({ components: res.data, id: libraryId }))
    } catch (err) {
      console.error(err)
    }
  }
)

export const fetchComponentImages = createAsyncThunk(
  'schematicEditor/fetchComponentImages',
  async (_, { dispatch }) => {
    try {
      const res = await api.get('block_images')
      dispatch(schematicEditorSlice.actions.setComponentImages(res.data))
    } catch (err) {
      console.error(err)
    }
  }
)

export const toggleCollapse = createAsyncThunk(
  'schematicEditor/toggleCollapse',
  (id, { dispatch }) => {
    dispatch(schematicEditorSlice.actions.toggleCollapse(id))
  }
)

export const toggleSimulate = createAsyncThunk(
  'schematicEditor/toggleSimulate',
  (_, { dispatch }) => {
    dispatch(schematicEditorSlice.actions.toggleSimulate())
  }
)

// Slice
const initialState = {
  isSimulate: false,
  libraries: [],
  collapse: {},
  components: {},
  component_images: []
}

const schematicEditorSlice = createSlice({
  name: 'schematicEditor',
  initialState,
  reducers: {
    setLibraries (state, action) {
      const collapse = {}
      const components = {}
      action.payload.forEach(element => {
        collapse[element.id] = false
        components[element.id] = []
      })
      state.libraries = action.payload
      state.collapse = collapse
      state.components = components
    },
    toggleCollapse (state, action) {
      // Extract the id of the dropdown to toggle from the action payload
      const id = action.payload
      // Check the current state of the dropdown with the extracted id
      const existingState = state.collapse[id]
      // Create a new object to hold the updated collapse state
      const newCollapse = {}
      // Loop through all dropdowns in the state and set them to false
      // This ensures that only the clicked dropdown will change state
      Object.keys(state.collapse).forEach(key => {
        newCollapse[key] = false
      })
      // Toggle the state of the clicked dropdown
      newCollapse[id] = !existingState
      // Update the state with the new collapse state
      state.collapse = { ...state.collapse, ...newCollapse }
    },
    setComponents (state, action) {
      state.components[action.payload.id] = action.payload.components
    },
    setComponentImages (state, action) {
      state.component_images = action.payload
    },
    toggleSimulate (state) {
      state.isSimulate = !state.isSimulate
    }
  }
})

export const schematicEditorActions = schematicEditorSlice.actions
export default schematicEditorSlice.reducer
