import api from '../../utils/Api'
import * as actions from './actions'

// Api call for fetching component library list
export const fetchLibraries = () => (dispatch) => {
// SAMPLE Response from API
// [
  //  {
  //   "id": 1
  //   "name": "Commonly Used Blocks",
  //   "sort_order": 1
  // },
// ] -- Multiple dicts in array
  api.get('categories/')
    .then(
      (res) => {
        dispatch({
          type: actions.FETCH_LIBRARIES,
          payload: res.data
        })
      }
    )
    .catch((err) => { console.error(err) })
}

// Api call for fetching components under specified library id
export const fetchComponents = (libraryId) => (dispatch) => {
// SAMPLE Response from API
//   [
  // {
  //   "id": 1,
  //   "blocktype": 1,
  //   "name": "LOGICAL_OP",
  //   "categories": [ 1 ],
  //   "initial_explicit_input_ports": 2,
  //   "initial_implicit_input_ports": 0,
  //   "initial_explicit_output_ports": 1,
  //   "initial_implicit_output_ports": 0,
  //   "initial_display_parameter": "AND",
  //   "p000_value_initial": "AND",
  //   "p001_value_initial": "AND",
  //   "p002_value_initial": "AND",
  //   "p003_value_initial": "AND",
  //   "p004_value_initial": null,
  //   ...
  //   "p039_value_initial": null,
  // },
// ] -- Multiple dicts in array
  const url = 'blocks/?categories=' + parseInt(libraryId)
  api.get(url)
    .then(
      (res) => {
        dispatch({
          type: actions.FETCH_COMPONENTS,
          payload: { components: res.data, id: libraryId }
        })
      }
    )
    .catch((err) => { console.error(err) })
}

// Action to keep only one component list dropdown open at a time
export const toggleCollapse = (id) => (dispatch) => {
  dispatch({
    type: actions.TOGGLE_COLLAPSE,
    payload: { id: id }
  })
}

// Action to hide components list to display simulation parameters
export const toggleSimulate = () => (dispatch) => {
  dispatch({
    type: actions.TOGGLE_SIMULATE
  })
}
