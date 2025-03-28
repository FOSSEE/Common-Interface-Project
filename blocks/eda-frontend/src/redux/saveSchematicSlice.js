import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'

import api from '../utils/Api'
import { transformXcos } from '../utils/GalleryUtils'

const initialState = {
  title: 'Untitled',
  description: '',
  xmlData: null,
  scriptDump: '',
  details: {},
  isLoading: false,
  isSaved: null,
  isShared: null
}

// Api call to save new schematic or updating saved schematic.
export const saveSchematic = createAsyncThunk(
  'saveSchematic/saveSchematic',
  async ({ title, description, xml, base64, scriptDump }, { getState, rejectWithValue }) => {
    // Get token from localstorage
    const token = getState().auth.token
    if (!token) return rejectWithValue('No token found')
    const isSaved = getState().saveSchematic.isSaved
    const details = getState().saveSchematic.details

    // add headers
    const config = {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${token}`
      }
    }

    const body = {
      data_dump: xml,
      base64_image: base64,
      name: title,
      description,
      script_dump: scriptDump
    }

    try {
      const url = `save/diagram${isSaved ? `/${details.save_id}` : ''}`
      const res = await api.post(url, body, config)
      if (res.status === 200) {
        return res.data
      }

      return rejectWithValue(res.data || 'Failed to save schematic')
    } catch (err) {
      console.log(err)
      const res = err.response
      return rejectWithValue(res?.data || 'Failed to save schematic')
    }
  })

// Action for Loading on-cloud saved schematics
export const fetchSchematic = createAsyncThunk(
  'saveSchematic/fetchSchematic',
  async (saveId, { getState, rejectWithValue }) => {
    // Get token from localstorage
    const token = getState().auth.token
    if (!token) return rejectWithValue('No token found')

    // add headers
    const config = {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${token}`
      }
    }

    try {
      const res = await api.get(`save/diagram/${saveId}`, config)
      if (res.status === 200) {
        return res.data
      }

      return rejectWithValue(res.data || 'Failed to load schematic')
    } catch (err) {
      console.log(err)
      const res = err.response
      return rejectWithValue(res?.data || 'Failed to load schematic')
    }
  })

// Action for Loading on-cloud saved schematics
export const fetchDiagram = createAsyncThunk(
  'saveSchematic/fetchDiagram',
  async (saveId, { rejectWithValue }) => {
    try {
      const res = await api.get(`save/gallery/${saveId}`)
      if (res.status === 200) {
        res.data.data_dump = await loadGallery(res.data)()
        return res.data
      }

      return rejectWithValue(res.data || 'Failed to load diagram')
    } catch (err) {
      console.log(err)
      const res = err.response
      return rejectWithValue(res?.data || 'Failed to load diagram')
    }
  })

export const setSchShared = createAsyncThunk(
  'saveSchematic/setSchShared',
  async (share, { getState, rejectWithValue }) => {
    // Get token from localstorage
    const token = getState().auth.token
    if (!token) return rejectWithValue('No token found')

    const details = getState().saveSchematic.details

    // add headers
    const config = {
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${token}`
      }
    }

    const isShared = share ? 'on' : 'off'

    try {
      const res = await api.get(`save/${details.save_id}/sharing/${isShared}`, config)
      if (res.status === 200) {
        return res.data
      }

      return rejectWithValue(res.data || 'Failed to share schematic')
    } catch (err) {
      console.log(err)
      const res = err.response
      return rejectWithValue(res?.data || 'Failed to share schematic')
    }
  })

// Action for Loading local exported schematics
export const openLocalSch = createAsyncThunk(
  'saveSchematic/openLocalSch',
  async (data) => {
    return data
  })

// Action for Loading Gallery diagrams
const loadGallery = (data) => async () => {
  if (!data) {
    console.error('No diagram found')
    return
  }

  try {
    // Check if the data is xcos or xml
    const parser = new DOMParser()
    let dataDump = data.data_dump
    const xmlDoc = parser.parseFromString(dataDump, 'application/xml')
    const isXcos = xmlDoc.getElementsByTagName('XcosDiagram').length > 0
    if (isXcos) {
      dataDump = new XMLSerializer().serializeToString(await transformXcos(xmlDoc))
    }
    return dataDump
  } catch (error) {
    console.error('Error loading gallery:', error)
  } finally {
    window.loadGalleryComplete = true
  }
}

const saveSchematicSlice = createSlice({
  name: 'saveSchematic',
  initialState,
  reducers: {
    setLoadingDiagram: (state, action) => {
      state.isLoading = action.payload
    },
    setSchTitle: (state, action) => {
      state.title = action.payload
    },
    setSchDescription: (state, action) => {
      state.description = action.payload
    },
    setSchXmlData: (state, action) => {
      state.xmlData = action.payload
    },
    setSchScriptDump: (state, action) => {
      state.scriptDump = action.payload
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(saveSchematic.pending, (state) => {
        state.isLoading = true
      })
      .addCase(saveSchematic.fulfilled, (state, action) => {
        state.isLoading = false
        state.details = action.payload
        state.isSaved = true
        state.isShared = action.payload.shared
      })
      .addCase(saveSchematic.rejected, (state) => {
        state.isLoading = false
      })
      .addCase(fetchSchematic.pending, (state) => {
        state.isLoading = true
      })
      .addCase(fetchSchematic.fulfilled, (state, action) => {
        state.isLoading = false
        state.details = action.payload
        state.description = action.payload.description
        state.isSaved = true
        state.isShared = action.payload.shared
        state.title = action.payload.name
        state.xmlData = action.payload.data_dump
        state.scriptDump = action.payload.script_dump
      })
      .addCase(fetchSchematic.rejected, (state) => {
        state.isLoading = false
      })
      .addCase(fetchDiagram.pending, (state) => {
        state.isLoading = true
      })
      .addCase(fetchDiagram.fulfilled, (state, action) => {
        state.isLoading = false
        state.details = action.payload
        state.description = action.payload.description
        state.isSaved = false
        state.isShared = false
        state.title = action.payload.name
        state.xmlData = action.payload.data_dump
        state.scriptDump = action.payload.script_dump
      })
      .addCase(fetchDiagram.rejected, (state) => {
        state.isLoading = false
      })
      .addCase(setSchShared.pending, (state) => {
        state.isLoading = true
      })
      .addCase(setSchShared.fulfilled, (state, action) => {
        state.isLoading = false
        state.details = action.payload
        state.isShared = action.payload.shared
      })
      .addCase(setSchShared.rejected, (state) => {
        state.isLoading = false
      })
      .addCase(openLocalSch.pending, (state) => {
        state.isLoading = true
      })
      .addCase(openLocalSch.fulfilled, (state, action) => {
        state.isLoading = false
        state.details = action.payload
        state.description = action.payload.description
        state.isSaved = true
        state.isShared = action.payload.shared
        state.title = action.payload.name
        state.xmlData = action.payload.data_dump
        state.scriptDump = action.payload.script_dump
      })
      .addCase(openLocalSch.rejected, (state) => {
        state.isLoading = false
      })
  }
})

export const {
  setLoadingDiagram,
  setSchTitle,
  setSchDescription,
  setSchXmlData,
  setSchScriptDump
} = saveSchematicSlice.actions

export default saveSchematicSlice.reducer
