import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    // fail if port already in use
    strictPort: true,
    proxy: {
      '/api': 'http://127.0.0.1:5000/',
    },
  },
  build: {
    outDir: 'build',
    sourcemap: true,
  },
})
