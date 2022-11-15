import api from '../../utils/Api'
import * as actions from './actions'

// Actions for listing stored component properites on double click on component
export const getCompProperties = (block) => (dispatch) => {
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
            compProperties: res.data[0]
          }
        })
      }
    )
    .catch((err) => { console.error(err) })
}

// Actions for updating entered component properites on clicking set parameters
export const setCompProperties = (block, parameterValues) => (dispatch) => {
  const url = 'setblockparameter'
  const filteredParameterValues = Object.fromEntries(Object.entries(parameterValues).filter(([k, v]) => v != null))
  const data = { block: block.style, ...filteredParameterValues }
  api.post(url, data)
    .then(
      (res) => {
        block.parameter_values = filteredParameterValues
        dispatch({
          type: actions.SET_COMP_PROPERTIES,
          payload: {
            block,
            parameter_values: parameterValues,
            displayProperties: res.data
          }
        })
      }
    )
    .catch((err) => { console.error(err) })
}

// Handling hiding of compProperties sidebar
export const closeCompProperties = () => (dispatch) => {
  dispatch({
    type: actions.CLOSE_COMP_PROPERTIES
  })
}
