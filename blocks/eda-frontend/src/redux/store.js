import { configureStore } from '@reduxjs/toolkit'
import reducer from './reducers/index'
import componentPropertiesReducer, { fetchCompProperties, setBlockParameter } from './slices/componentPropertiesSlice'
import schematicEditorReducer from './slices/schematicEditorSlice'
import dashboardReducer from './slices/dashboardSlice'
const store = configureStore({
  reducer: {
    oldReducers: reducer,
    componentProperties: componentPropertiesReducer,
    schematicEditor: schematicEditorReducer,
    dashboardReducer: dashboardReducer
  }
})

store.dispatch(fetchCompProperties())
store.dispatch(setBlockParameter())

export default store
