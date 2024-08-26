import { createSlice, createAsyncThunk } from '@reduxjs/toolkit'
import queryString from 'query-string'
import api from '../../utils/Api'
import GallerySchSample from '../../utils/GallerySchSample'
import { renderGalleryXML } from '../../components/SchematicEditor/Helper/ToolbarTools'
import { setTitle } from './netlistSlice'
import { getXsltProcessor } from '../../utils/GalleryUtils'

const initialState = {
  title: 'Untitled',
  description: '',
  xmlData: null,
  details: {},
  isSaved: null,
  isShared: null
}

// Async Thunks
export const saveSchematic = createAsyncThunk(
  'saveSchematic/save',
  async ({ title, description, xml, base64 }, { getState, dispatch }) => {
    const body = {
      data_dump: xml,
      base64_image: base64,
      name: title,
      description
    }
    const token = getState().authReducer.token
    const schSave = getState().saveSchematic

    const config = {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    }

    if (token) {
      config.headers.Authorization = `Token ${token}`
    }

    if (schSave.isSaved) {
      const response = await api.post('save/diagram/' + schSave.details.save_id, queryString.stringify(body), config)
      return response.data
    } else {
      const response = await api.post('save/diagram', queryString.stringify(body), config)
      return response.data
    }
  }
)

export const fetchSchematic = createAsyncThunk(
  'saveSchematic/fetch',
  async (saveId, { getState, dispatch }) => {
    const token = getState().authReducer.token

    const config = {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded'
      }
    }

    if (token) {
      config.headers.Authorization = `Token ${token}`
    }

    const response = await api.get('save/diagram/' + saveId, config)
    const data = response.data

    dispatch(setSchTitle(data.name))
    dispatch(setSchDescription(data.description))
    dispatch(setSchXmlData(data.data_dump))
    renderGalleryXML(data.data_dump)

    return data
  }
)

export const setSchShared = createAsyncThunk(
  'saveSchematic/share',
  async (share, { getState }) => {
    const token = getState().authReducer.token
    const schSave = getState().saveSchematic

    const config = {
      headers: {
        'Content-Type': 'application/json'
      }
    }

    if (token) {
      config.headers.Authorization = `Token ${token}`
    }

    const isShared = share ? 'on' : 'off'
    const response = await api.post('save/' + schSave.details.save_id + '/sharing/' + isShared, {}, config)

    return response.data
  }
)

export const loadGallery = createAsyncThunk(
  'saveSchematic/loadGallery',
  async (saveId, { dispatch }) => {
    const data = GallerySchSample.find(sample => sample.save_id === saveId)

    if (!data) {
      throw new Error(`No gallery schematic found with save_id: ${saveId}`)
    }

    const parser = new DOMParser()
    let xmlDoc = parser.parseFromString(data.data_dump, 'application/xml')
    const isXcos = xmlDoc.getElementsByTagName('XcosDiagram').length > 0

    const handleGalleryLoad = (data, dataDump) => {
      dispatch({
        type: 'saveSchematic/loadGallery',
        payload: { ...data, data_dump: dataDump }
      })
      dispatch(setTitle('* ' + data.name))
      dispatch(setSchTitle(data.name))
      dispatch(setSchDescription(data.description))
      dispatch(setSchXmlData(dataDump))
      renderGalleryXML(dataDump)
    }

    if (isXcos) {
      const processor = await getXsltProcessor()
      xmlDoc = processor.transformToDocument(xmlDoc)
      const dataDump = new XMLSerializer().serializeToString(xmlDoc)
      handleGalleryLoad(data, dataDump)
    } else {
      handleGalleryLoad(data, data.dataDump)
    }
    window.loadGalleryComplete = true
  }
)

export const openLocalSch = createAsyncThunk(
  'saveSchematic/openLocal',
  async (data, { dispatch }) => {
    dispatch({ type: 'saveSchematic/clearDetails' })
    dispatch(setTitle('* ' + data.title))
    dispatch(setSchTitle(data.title))
    dispatch(setSchDescription(data.description))
    dispatch(setSchXmlData(data.data_dump))
    renderGalleryXML(data.data_dump)
  }
)

// Slice
const saveSchematicSlice = createSlice({
  name: 'saveSchematic',
  initialState,
  reducers: {
    setSchTitle (state, action) {
      state.title = action.payload.title
    },
    setSchDescription (state, action) {
      state.description = action.payload.description
    },
    setSchXmlData (state, action) {
      state.xmlData = action.payload.xmlData
    },
    clearDetails (state) {
      state.isSaved = null
      state.isShared = null
      state.details = {}
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(saveSchematic.fulfilled, (state, action) => {
        state.isSaved = true
        state.isShared = action.payload.shared
        state.details = action.payload
      })
      .addCase(fetchSchematic.fulfilled, (state, action) => {
        state.isSaved = true
        state.isShared = action.payload.shared
        state.details = action.payload
      })
      .addCase(setSchShared.fulfilled, (state, action) => {
        state.isShared = true
        state.details = action.payload
      })
      .addCase(loadGallery.fulfilled, (state, action) => {
        state.details = action.payload
      })
  }
})

// Export actions and reducer
export const { setSchTitle, setSchDescription, setSchXmlData, clearDetails } = saveSchematicSlice.actions
export default saveSchematicSlice.reducer
