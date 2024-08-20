import { createSlice } from '@reduxjs/toolkit'
import api from '../../utils/Api'
import { editorZoomAct } from '../../components/SchematicEditor/Helper/ToolbarTools'

const initialState = {
  block: null,
  name: '',
  parameterValues: {},
  errorFields: {},
  isPropertiesWindowOpen: false,
  compProperties: {},
  displayProperties: {},
  isLoading: false
}

export const componentPropertiesSlice = createSlice({
  name: 'componentProperties',
  initialState,
  reducers: {
    loadingGetCompProperties: (state, action) => {
      state.name = action.payload.name
      state.isPropertiesWindowOpen = true
      state.compProperties = undefined
      state.isLoading = action.payload.isLoading
    },
    getCompProperties: (state, action) => {
      const {
        block,
        name,
        parameterValues,
        errorFields,
        displayProperties,
        compProperties
      } = action.payload
      state.block = block
      state.name = name
      state.parameterValues = parameterValues
      state.errorFields = errorFields
      state.isPropertiesWindowOpen = true
      state.displayProperties = displayProperties
      state.compProperties = compProperties
      state.isLoading = false
    },
    loadingSetCompProperties: (state, action) => {
      state.isPropertiesWindowOpen = true
      state.isLoading = action.payload.isLoading
    },
    setCompProperties: (state, action) => {
      const {
        block,
        parameterValues,
        errorFields,
        displayProperties
      } = action.payload
      state.block = block
      state.parameterValues = parameterValues
      state.errorFields = errorFields
      state.isPropertiesWindowOpen = false
      state.displayProperties = displayProperties
      state.isLoading = false
    },
    closeCompProperties: (state) => {
      editorZoomAct()
      state.isPropertiesWindowOpen = false
    }
  }
})

export const {
  loadingGetCompProperties,
  getCompProperties,
  loadingSetCompProperties,
  setCompProperties,
  closeCompProperties
} = componentPropertiesSlice.actions

// Async action creators remain the same
export const getCompPropertiesAsync = (block) => (dispatch) => {
  dispatch(loadingGetCompProperties(block, true))
  const url = 'block_parameters/?block__name=' + block.style
  api.get(url)
    .then((res) => {
      dispatch(getCompProperties({
        block,
        name: block.style,
        parameterValues: block.parameterValues,
        errorFields: block.errorFields,
        displayProperties: block.displayProperties,
        compProperties: res.data[0]
      }))
    })
    .catch((err) => {
      console.error(err)
      dispatch(loadingGetCompProperties(block, false))
    })
}

export const setCompPropertiesAsync = (block, parameterValues, errorFields) => (dispatch) => {
  dispatch(loadingSetCompProperties(true))
  const url = 'setblockparameter'
  const filteredParameterValues = Object.fromEntries(Object.entries(parameterValues).filter(([k, v]) => v != null))
  const data = { block: block.style, ...filteredParameterValues }
  api.post(url, data)
    .then((res) => {
      block.parameterValues = filteredParameterValues
      block.errorFields = errorFields
      dispatch(setCompProperties({
        block,
        parameterValues: parameterValues,
        errorFields,
        displayProperties: res.data
      }))
    })
    .catch((err) => {
      console.error(err)
      dispatch(loadingSetCompProperties(false))
    })
}

export default componentPropertiesSlice.reducer
