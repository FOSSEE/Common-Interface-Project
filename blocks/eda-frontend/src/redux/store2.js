import { configureStore } from '@reduxjs/toolkit'
import componentPropertiesReducer from './slices/componentPropertiesSlice'

const store = configureStore({
  reducer: {
    componentProperties: componentPropertiesReducer
  }
})

export default store
