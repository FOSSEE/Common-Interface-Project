import { createSlice } from '@reduxjs/toolkit'
import queryString from 'query-string'
import api from '../../utils/Api'
import GallerySchSample from '../../utils/GallerySchSample'
import { setTitle } from './index'

// Define clearDetails function separately
export const clearDetails = () => ({
  type: 'saveSchematic/clearDetails'
})

const saveSchematicSlice = createSlice({
  name: 'saveSchematic',
  initialState: {
    title: 'Untitled',
    description: '',
    xmlData: null,
    details: {},
    isSaved: null,
    isShared: null
  },
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
    setSchSaved (state, action) {
      state.isSaved = true
      state.isShared = action.payload.shared
      state.details = action.payload
    },
    setSchShared (state, action) {
      state.isShared = true
      state.details = action.payload
    },
    // clearDetails reducer remains unchanged
    loadGallery (state, action) {
      state.isSaved = null
      state.isShared = null
      state.details = action.payload
    }
  }
})

export const {
  setSchTitle,
  setSchDescription,
  setSchXmlData,
  setSchSaved,
  setSchShared,
  loadGallery
} = saveSchematicSlice.actions

// Api call to save new schematic or updating saved schematic.
export const saveSchematic = (title, description, xml, base64) => async (dispatch, getState) => {
  const body = {
    data_dump: xml,
    base64_image: base64,
    name: title,
    description
  }

  const token = getState().authReducer.token
  const config = {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  }

  if (token) {
    config.headers.Authorization = `Token ${token}`
  }

  const schSave = getState().saveSchematicSlice

  if (schSave.isSaved) {
    api.post(`save/${schSave.details.save_id}`, queryString.stringify(body), config)
      .then((res) => {
        dispatch(setSchSaved(res.data))
      })
      .catch((err) => { console.error(err) })
  } else {
    api.post('save', queryString.stringify(body), config)
      .then((res) => {
        dispatch(setSchSaved(res.data))
      })
      .catch((err) => { console.error(err) })
  }
}

// Action for Loading on-cloud saved schematics
export const fetchSchematic = (saveId) => async (dispatch, getState) => {
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
    })
    .catch((err) => { console.error(err) })
}

export const setSchSharedAsync = (share) => async (dispatch, getState) => {
  const token = getState().authReducer.token
  const schSave = getState().saveSchematicSlice
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
    .catch((err) => { console.error(err) })
}

// Action for Loading Gallery schematics
export const loadGalleryAsync = (Id) => (dispatch) => {
  const data = GallerySchSample[Id]

  dispatch(loadGallery(data))
  dispatch(setTitle('* ' + data.name))
  dispatch(setSchTitle(data.name))
  dispatch(setSchDescription(data.description))
  dispatch(setSchXmlData(data.data_dump))
}

// Action for Loading local exported schematics
export const openLocalSch = (obj) => (dispatch) => {
  const data = obj

  dispatch(clearDetails())
  dispatch(setTitle('* ' + data.title))
  dispatch(setSchTitle(data.title))
  dispatch(setSchDescription(data.description))
  dispatch(setSchXmlData(data.data_dump))
}

export default saveSchematicSlice.reducer
