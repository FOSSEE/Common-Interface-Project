import * as actions from './actions'
import queryString from 'query-string'
import api from '../../utils/Api'
import { renderGalleryXML } from '../../components/SchematicEditor/Helper/ToolbarTools'
import { setTitle } from './index'
import { transformXcos } from '../../utils/GalleryUtils'

export const setLoadingDiagram = (isLoading) => (dispatch) => {
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

export const setSchScriptDump = (scriptDump) => (dispatch) => {
  dispatch({
    type: actions.SET_SCH_SCRIPT_DUMP,
    payload: {
      scriptDump
    }
  })
}

// Api call to save new schematic or updating saved schematic.
export const saveSchematic = (title, description, xml, base64, scriptDump) => (dispatch, getState) => {
  const body = {
    data_dump: xml,
    base64_image: base64,
    name: title,
    description,
    script_dump: scriptDump
  }

  // Get token from localstorage
  const token = getState().authReducer.token
  const details = getState().saveSchematicReducer.details
  const isSaved = getState().saveSchematicReducer.isSaved

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

  if (isSaved) {
    //  Updating saved schemaic
    api.post('save/diagram/' + details.save_id, queryString.stringify(body), config)
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

export const fetchDiagram = (saveId) => (dispatch) => {
  api.get('save/gallery/' + saveId)
    .then(
      (res) => {
        dispatch(loadGallery(res.data))
      }
    )
    .catch((err) => { console.error(err) })
}

export const setSchShared = (share) => (dispatch, getState) => {
  // Get token from localstorage
  const token = getState().authReducer.token
  const details = getState().saveSchematicReducer.details

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

  api.post('save/' + details.save_id + '/sharing/' + isShared, {}, config)
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
export const loadGallery = (data) => async (dispatch) => {
  if (!data) {
    console.error(`No gallery schematic found with save_id: ${data}`)
    return
  }

  dispatch(setLoadingDiagram(true))

  try {
    // Check if the data is xcos or xml
    const parser = new DOMParser()
    const xmlDoc = parser.parseFromString(data.data_dump, 'application/xml')
    const isXcos = xmlDoc.getElementsByTagName('XcosDiagram').length > 0

    const handleGalleryLoad = (data, dataDump) => {
      dispatch({
        type: actions.LOAD_GALLERY,
        payload: { ...data, data_dump: dataDump }
      })
      dispatch(setTitle('* ' + data.name))
      dispatch(setSchTitle(data.name))
      dispatch(setSchDescription(data.description))
      dispatch(setSchXmlData(dataDump))
      dispatch(setSchScriptDump(data.script_dump))
      renderGalleryXML(dataDump)
    }

    if (isXcos) {
      const transformedXml = await transformXcos(xmlDoc)
      const dataDump = new XMLSerializer().serializeToString(transformedXml)
      handleGalleryLoad(data, dataDump)
    } else {
      handleGalleryLoad(data, data.data_dump)
    }
  } catch (error) {
    console.error('Error loading gallery:', error)
  } finally {
    dispatch(setLoadingDiagram(false))
    window.loadGalleryComplete = true
  }
}

// Action for Loading local exported schematics
export const openLocalSch = (obj) => (dispatch) => {
  const data = obj

  dispatch({ type: actions.CLEAR_DETAILS })
  dispatch(setTitle('* ' + data.title))
  dispatch(setSchTitle(data.title))
  dispatch(setSchDescription(data.description))
  dispatch(setSchXmlData(data.data_dump))
  dispatch(setSchScriptDump(data.script_dump))
  renderGalleryXML(data.data_dump)
}
