// vite.config.js or vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import VitePluginTailwind from 'vite-plugin-tailwind';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    react(),
    VitePluginTailwind(),
  ],
  server: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  },
});
