import api from '../../utils/Api'
import * as actions from './actions'

// Actions for listing stored component properites on double click on component
export const getCompProperties = (block) => (dispatch) => {
  const url = 'block_parameters/?block=' + parseInt(block.block_id)
  api.get(url)
    .then(
      (res) => {
        dispatch({
          type: actions.GET_COMP_PROPERTIES,
          payload: {
            id: block.block_id,
            block: block,
            compProperties: res.data
          }
        })
      }
    )
    .catch((err) => { console.error(err) })
}

// Actions for updating entered component properites on clicking set parameters
export const setCompProperties = (id, block) => (dispatch) => {
  dispatch({
    type: actions.SET_COMP_PROPERTIES,
    payload: {
      id: id,
      block: block
    }
  })
}

// Handeling hiding of component properties sidebar
export const closeCompProperties = () => (dispatch) => {
  dispatch({
    type: actions.CLOSE_COMP_PROPERTIES
  })
}
