import api from '../../utils/Api'
import * as actions from './actions'

// Actions for setting isLoading
const loadingGetCompProperties = (block, isLoading) => (dispatch) => {
  dispatch({
    type: actions.LOADING_GET_COMP_PROPERTIES,
    payload: {
      name: block.style,
      isLoading
    }
  })
}

const loadingSetCompProperties = (isLoading) => (dispatch) => {
  dispatch({
    type: actions.LOADING_SET_COMP_PROPERTIES,
    payload: {
      isLoading
    }
  })
}

// Actions for listing stored component properites on double click on component
export const getCompProperties = (block) => (dispatch) => {
  dispatch(loadingGetCompProperties(block, true))
  const url = 'block_parameters/?block__name=' + block.style
  api.get(url)
    .then(
      (res) => {
        dispatch({
          type: actions.GET_COMP_PROPERTIES,
          payload: {
            block,
            name: block.style,
            parameter_values: block.parameter_values,
            errorFields: block.errorFields,
            displayProperties: block.displayProperties,
            compProperties: res.data[0]
          }
        })
      }
    )
    .catch((err) => {
      console.error(err)
      dispatch(loadingGetCompProperties(block, false))
    })
}

// Actions for updating entered component properites on clicking set parameters
export const setCompProperties = (block, parameterValues, errorFields) => (dispatch) => {
  dispatch(loadingSetCompProperties(true))
  const url = 'setblockparameter'
  const filteredParameterValues = Object.fromEntries(Object.entries(parameterValues).filter(([k, v]) => v != null))
  const data = { block: block.style, ...filteredParameterValues }
  api.post(url, data)
    .then(
      (res) => {
        block.parameter_values = filteredParameterValues
        block.errorFields = errorFields
        dispatch({
          type: actions.SET_COMP_PROPERTIES,
          payload: {
            block,
            parameter_values: parameterValues,
            errorFields,
            displayProperties: res.data
          }
        })
      }
    )
    .catch((err) => {
      console.error(err)
      dispatch(loadingSetCompProperties(false))
    })
}

// Handling hiding of compProperties sidebar
export const closeCompProperties = () => (dispatch) => {
  dispatch({
    type: actions.CLOSE_COMP_PROPERTIES
  })
}
