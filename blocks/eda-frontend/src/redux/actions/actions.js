// Actions for schematic editor
export const COMPONENT_IMAGES = 'COMPONENT_IMAGES'
export const FETCH_LIBRARIES = 'FETCH_LIBRARIES'
export const TOGGLE_COLLAPSE = 'TOGGLE_COLLAPSE'
export const FETCH_COMPONENTS = 'FETCH_COMPONENTS'
export const TOGGLE_SIMULATE = 'TOGGLE_SIMULATE'

// Actions for handling compProperties
export const GET_COMP_PROPERTIES = 'GET_COMP_PROPERTIES'
export const SET_COMP_PROPERTIES = 'SET_COMP_PROPERTIES'
export const CLOSE_COMP_PROPERTIES = 'CLOSE_COMP_PROPERTIES'

// Actions for handling and generating netlist
export const SET_NETLIST = 'SET_NETLIST'
export const SET_TITLE = 'SET_TITLE'
export const SET_MODEL = 'SET_MODEL'

// Actions for handling simualtion result display
export const SET_RESULT_TITLE = 'SET_RESULT_TITLE'
export const SET_RESULT_GRAPH = 'SET_RESULT_GRAPH'
export const SET_RESULT_TEXT = 'SET_RESULT_TEXT'

// Actions for handling user authentication and registeration
export const USER_LOADING = 'USER_LOADING'
export const USER_LOADED = 'USER_LOADED'
export const LOGIN_SUCCESSFUL = 'LOGIN_SUCCESSFUL'
export const AUTHENTICATION_ERROR = 'AUTHENTICATION_ERROR'
export const LOGIN_FAILED = 'LOGIN_FAILED'
export const LOGOUT_SUCCESSFUL = 'LOGOUT_SUCCESSFUL'
export const LOADING_FAILED = 'LOADING_FAILED'
export const SIGNUP_SUCCESSFUL = 'SIGNUP_SUCCESSFUL'
export const SIGNUP_FAILED = 'SIGNUP_FAILED'
export const DEFAULT_STORE = 'DEFAULT_STORE'

// Actions for saving scheamtics and loading saved, gallery and local schematics.
export const SAVE_SCHEMATICS = 'SAVE_SCHEMATICS'
export const SET_SCH_SAVED = 'SET_SCH_SAVED'
export const SET_SCH_TITLE = 'SET_SCH_TITLE'
export const SET_SCH_DESCRIPTION = 'SET_SCH_DESCRIPTION'
export const SET_SCH_XML_DATA = 'SET_SCH_XML_DATA'
export const SET_SCH_SHARED = 'SET_SCH_SHARED'
export const CLEAR_DETAILS = 'CLEAR_DETAILS'
export const LOAD_GALLERY = 'LOAD_GALLERY'

// Action for fetching on-cloud saved schematics for authenticated user to display in dashboard
export const FETCH_SCHEMATICS = 'FETCH_SCHEMATICS'
