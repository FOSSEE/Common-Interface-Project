import { createSlice } from '@reduxjs/toolkit'
import api from '../../utils/Api'
import queryString from 'query-string'
import GallerySchSample from '../../utils/GallerySchSample'
import { renderGalleryXML } from '../../components/SchematicEditor/Helper/ToolbarTools'
import { setTitle } from './netlistSlice'
import * as actions from '../actions/actions'

const initialState = {
  title: 'Untitled',
  description: '',
  xmlData: null,
  details: {},
  isSaved: null,
  isShared: null
}

const saveSchematicSlice = createSlice({
  name: 'saveSchematic',
  initialState,
  reducers: {
    setSchTitle (state, action) {
      state.title = action.payload
    },
    setSchDescription (state, action) {
      state.description = action.payload
    },
    setSchXmlData (state, action) {
      state.xmlData = action.payload
    },
    setSchSaved (state, action) {
      const payload = action.payload
      state.isSaved = true
      state.isShared = payload.shared
      state.details = payload
    },
    setSchShared (state, action) {
      const payload = action.payload
      state.isShared = true
      state.details = payload
    },
    clearSchematicDetails (state) {
      return initialState
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(actions.LOAD_GALLERY, (state, action) => {
        const data = action.payload
        state = { ...initialState, details: data }
      })
  }
})

export const {
  setSchTitle,
  setSchDescription,
  setSchXmlData,
  setSchSaved,
  setSchShared,
  clearSchematicDetails
} = saveSchematicSlice.actions

export default saveSchematicSlice.reducer

export const saveSchematic = (title, description, xml, base64) => (dispatch, getState) => {
  const body = {
    data_dump: xml,
    base64_image: base64,
    name: title,
    description
  }

  const token = getState().authReducer.token
  const schSave = getState().schematic

  const config = {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  }

  if (token) {
    config.headers.Authorization = `Token ${token}`
  }

  const endpoint = schSave.isSaved ? `save/${schSave.details.save_id}` : 'save'

  api.post(endpoint, queryString.stringify(body), config)
    .then((res) => {
      dispatch(setSchSaved(res.data))
    })
    .catch((err) => {
      console.error(err)
    })
}

export const fetchSchematic = (saveId) => (dispatch, getState) => {
  const token = getState().authReducer.token
  const config = {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  }

  if (token) {
    config.headers.Authorization = `Token ${token}`
  }

  api.get(`save/${saveId}`, config)
    .then((res) => {
      dispatch(setSchSaved(res.data))
      dispatch(setSchTitle(res.data.name))
      dispatch(setSchDescription(res.data.description))
      dispatch(setSchXmlData(res.data.data_dump))
      renderGalleryXML(res.data.data_dump)
    })
    .catch((err) => {
      console.error(err)
    })
}

export const setShared = (share) => (dispatch, getState) => {
  const token = getState().authReducer.token
  const schSave = getState().schematic

  const config = {
    headers: {
      'Content-Type': 'application/json'
    }
  }

  if (token) {
    config.headers.Authorization = `Token ${token}`
  }

  let isShared
  if (share === true) {
    isShared = 'on'
  } else {
    isShared = 'off'
  }

  api.post(`save/${schSave.details.save_id}/sharing/${isShared}`, {}, config)
    .then((res) => {
      dispatch(setSchShared(res.data))
    })
    .catch((err) => {
      console.error(err)
    })
}

export const loadGallery = (Id) => (dispatch) => {
  const data = GallerySchSample[Id]

  dispatch({
    type: 'schematic/loadGallery',
    payload: data
  })
  dispatch(setTitle('* ' + data.name))
  dispatch(setSchTitle(data.name))
  dispatch(setSchDescription(data.description))
  dispatch(setSchXmlData(data.data_dump))
  renderGalleryXML(data.data_dump)
}

export const openLocalSch = (obj) => (dispatch) => {
  const data = obj

  dispatch(clearSchematicDetails())
  dispatch(setTitle('* ' + data.title))
  dispatch(setSchTitle(data.title))
  dispatch(setSchDescription(data.description))
  dispatch(setSchXmlData(data.data_dump))
  renderGalleryXML(data.data_dump)
}
