import { createSlice } from '@reduxjs/toolkit'

export const blconfigSlice = createSlice({
  name: 'blconfig',
  initialState: {
    sampleDelivery: "osc",
    detector: "eiger",
  },
  reducers: {
    setCompleteConfiguration: (state, action) => {
      const conf = action.payload;
      state.detector = conf.detector;
      state.sampleDelivery = conf.sampleDelivery;
    },
    setDetector: (state, action) => {
      state.detector = action.payload
    },
    setSampleDelivery: (state, action) => {
      state.sampleDelivery = action.payload
    },
  },
})

export const {
  setDetector,
  setSampleDelivery,
  setCompleteConfiguration,
} = blconfigSlice.actions;

export default blconfigSlice.reducer;
