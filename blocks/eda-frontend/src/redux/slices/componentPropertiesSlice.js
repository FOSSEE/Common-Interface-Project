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

const componentPropertiesSlice = createSlice({
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
      state.block = action.payload.block
      state.name = action.payload.name
      state.parameterValues = action.payload.parameterValues
      state.errorFields = action.payload.errorFields
      state.isPropertiesWindowOpen = true
      state.displayProperties = action.payload.displayProperties
      state.compProperties = action.payload.compProperties
      state.isLoading = false
    },
    loadingSetCompProperties: (state, action) => {
      state.isPropertiesWindowOpen = true
      state.isLoading = action.payload.isLoading
    },
    setCompProperties: (state, action) => {
      state.block = action.payload.block
      state.parameterValues = action.payload.parameterValues
      state.errorFields = action.payload.errorFields
      state.isPropertiesWindowOpen = false
      state.displayProperties = action.payload.displayProperties
      state.isLoading = false
    },
    closeCompProperties: (state) => {
      editorZoomAct()
      state.isPropertiesWindowOpen = false
    }
  }
})

export const getCompProperties = (block) => async (dispatch) => {
  dispatch(componentPropertiesSlice.actions.loadingGetCompProperties({ name: block.style, isLoading: true }))

  try {
    const url = `block_parameters/?block__name=${block.style}`
    const res = await api.get(url)
    dispatch(
      componentPropertiesSlice.actions.getCompProperties({
        block,
        name: block.style,
        parameterValues: block.parameterValues,
        errorFields: block.errorFields,
        displayProperties: block.displayProperties,
        compProperties: res.data[0]
      })
    )
  } catch (err) {
    console.error(err)
    dispatch(componentPropertiesSlice.actions.loadingGetCompProperties({ name: block.style, isLoading: false }))
  }
}

export const setCompProperties = (block, parameterValues, errorFields) => async (dispatch) => {
  dispatch(componentPropertiesSlice.actions.loadingSetCompProperties({ isLoading: true }))

  try {
    const url = 'setblockparameter'
    const filteredParameterValues = Object.fromEntries(
      Object.entries(parameterValues).filter(([k, v]) => v != null)
    )
    const data = { block: block.style, ...filteredParameterValues }
    const res = await api.post(url, data)
    block.parameterValues = filteredParameterValues
    block.errorFields = errorFields
    dispatch(
      componentPropertiesSlice.actions.setCompProperties({
        block,
        parameterValues: parameterValues,
        errorFields,
        displayProperties: res.data
      })
    )
  } catch (err) {
    console.error(err)
    dispatch(componentPropertiesSlice.actions.loadingSetCompProperties({ isLoading: false }))
  }
}

export const closeCompProperties = () => (dispatch) => {
  dispatch(componentPropertiesSlice.actions.closeCompProperties())
}

export const {
  loadingGetCompProperties,
  loadingSetCompProperties
} = componentPropertiesSlice.actions

export default componentPropertiesSlice.reducer
