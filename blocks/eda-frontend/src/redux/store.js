// // Initialize Redux store which holds the whole state tree of application.
// import reducer from './reducers/index'
// import { createStore, applyMiddleware } from 'redux'
// import reduxThunk from 'redux-thunk'
// const createStoreWithMiddleware = applyMiddleware(reduxThunk)(createStore)
// const store = createStoreWithMiddleware(reducer)

// export default store

// store.js

import { configureStore } from '@reduxjs/toolkit'
import schematicEditorReducer from './slices/schematicEditorSlice'
import componentPropertiesReducer from './slices/compPropertiesSlice'
import netlistReducer from './slices/netlistSlice'
import simulationReducer from './slices/simulationSlice'
import authReducer from './slices/authSlice'
import saveSchematicReducer from './slices/saveSchematicSlice'
import dashboardReducer from './slices/dashboardSlice'

const store = configureStore({
  reducer: {
    schematicEditor: schematicEditorReducer,
    componentProperties: componentPropertiesReducer,
    netlist: netlistReducer,
    simulation: simulationReducer,
    auth: authReducer,
    saveSchematic: saveSchematicReducer,
    dashboard: dashboardReducer
  }
})

export default store
