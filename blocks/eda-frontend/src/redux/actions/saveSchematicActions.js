import * as actions from './actions'
import queryString from 'query-string'
import api from '../../utils/Api'
import GallerySchSample from '../../utils/GallerySchSample'
import { renderGalleryXML } from '../../components/SchematicEditor/Helper/ToolbarTools'
import { setTitle } from './index'
import { transformXcos } from '../../utils/GalleryUtils'

export const loadingDiagram = (isLoading) => (dispatch) => {
  dispatch({
    type: actions.LOADING_DIAGRAM,
    payload: {
      isLoading
    }
  })
}

export const setSchTitle = (title) => (dispatch) => {
  dispatch({
    type: actions.SET_SCH_TITLE,
    payload: {
      title
    }
  })
}

export const setSchDescription = (description) => (dispatch) => {
  dispatch({
    type: actions.SET_SCH_DESCRIPTION,
    payload: {
      description
    }
  })
}

export const setSchXmlData = (xmlData) => (dispatch) => {
  dispatch({
    type: actions.SET_SCH_XML_DATA,
    payload: {
      xmlData
    }
  })
}

// Api call to save new schematic or updating saved schematic.
export const saveSchematic = (title, description, xml, base64) => (dispatch, getState) => {
  const body = {
    data_dump: xml,
    base64_image: base64,
    name: title,
    description
  }

  // Get token from localstorage
  const token = getState().authReducer.token
  const schSave = getState().saveSchematicReducer

  // add headers
  const config = {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  }

  // If token available add to headers
  if (token) {
    config.headers.Authorization = `Token ${token}`
  }

  if (schSave.isSaved) {
    //  Updating saved schemaic
    api.post('save/diagram/' + schSave.details.save_id, queryString.stringify(body), config)
      .then(
        (res) => {
          dispatch({
            type: actions.SET_SCH_SAVED,
            payload: res.data
          })
        }
      )
      .catch((err) => { console.error(err) })
  } else {
    // saving new schematic
    api.post('save/diagram', queryString.stringify(body), config)
      .then(
        (res) => {
          dispatch({
            type: actions.SET_SCH_SAVED,
            payload: res.data
          })
        }
      )
      .catch((err) => { console.error(err) })
  }
}

// Action for Loading on-cloud saved schematics
export const fetchSchematic = (saveId) => (dispatch, getState) => {
  // Get token from localstorage
  const token = getState().authReducer.token

  // add headers
  const config = {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  }

  // If token available add to headers
  if (token) {
    config.headers.Authorization = `Token ${token}`
  }

  api.get('save/diagram/' + saveId, config)
    .then(
      (res) => {
        dispatch({
          type: actions.SET_SCH_SAVED,
          payload: res.data
        })
        dispatch(setSchTitle(res.data.name))
        dispatch(setSchDescription(res.data.description))
        dispatch(setSchXmlData(res.data.data_dump))
        renderGalleryXML(res.data.data_dump)
      }
    )
    .catch((err) => { console.error(err) })
}

export const setSchShared = (share) => (dispatch, getState) => {
  // Get token from localstorage
  const token = getState().authReducer.token
  const schSave = getState().saveSchematicReducer

  // add headers
  const config = {
    headers: {
      'Content-Type': 'application/json'
    }
  }

  // If token available add to headers
  if (token) {
    config.headers.Authorization = `Token ${token}`
  }

  let isShared
  if (share === true) {
    isShared = 'on'
  } else {
    isShared = 'off'
  }

  api.post('save/' + schSave.details.save_id + '/sharing/' + isShared, {}, config)
    .then(
      (res) => {
        dispatch({
          type: actions.SET_SCH_SHARED,
          payload: res.data
        })
      }
    )
    .catch((err) => { console.error(err) })
}

// Action for Loading Gallery schematics
export const loadGallery = (saveId) => (dispatch, getState) => {
  // Find the gallery schematic that matches the given save_id
  const data = GallerySchSample.find(sample => sample.save_id === saveId)

  if (!data) {
    console.error(`No gallery schematic found with save_id: ${saveId}`)
    return
  }

  // FIXME: issue in rendering
  // dispatch(loadingDiagram(true))
  // Check if the data is xcos or xml
  const parser = new DOMParser()
  const xmlDoc = parser.parseFromString(data.data_dump, 'application/xml')
  const isXcos = xmlDoc.getElementsByTagName('XcosDiagram').length > 0

  const handleGalleryLoad = (dispatch, data, dataDump) => {
    dispatch({
      type: actions.LOAD_GALLERY,
      payload: { ...data, data_dump: dataDump }
    })
    dispatch(setTitle('* ' + data.name))
    dispatch(setSchTitle(data.name))
    dispatch(setSchDescription(data.description))
    dispatch(setSchXmlData(dataDump))
    renderGalleryXML(dataDump)
  }

  if (isXcos) {
    transformXcos(xmlDoc).then(xmlDoc => {
      const dataDump = new XMLSerializer().serializeToString(xmlDoc)
      handleGalleryLoad(dispatch, data, dataDump)
      dispatch(loadingDiagram(false))
    }).catch(error => {
      console.error('Error converting xcos to xml:', error)
    })
  } else {
    handleGalleryLoad(dispatch, data, data.dataDump)
    dispatch(loadingDiagram(false))
  }
  window.loadGalleryComplete = true
}

// Action for Loading local exported schematics
export const openLocalSch = (obj) => (dispatch, getState) => {
  const data = obj

  dispatch({ type: actions.CLEAR_DETAILS })
  dispatch(setTitle('* ' + data.title))
  dispatch(setSchTitle(data.title))
  dispatch(setSchDescription(data.description))
  dispatch(setSchXmlData(data.data_dump))
  renderGalleryXML(data.data_dump)
}
