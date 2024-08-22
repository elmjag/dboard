import { configureStore } from '@reduxjs/toolkit'
import blconfigReducer from '../features/blconfig/blconfigSlice'

export default configureStore({
  reducer: {
    blconfig: blconfigReducer,
  },
})
