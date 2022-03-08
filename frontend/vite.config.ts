import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import * as path from "path";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    lib: {
      entry: path.resolve(__dirname, 'src', 'lib.ts'),
      name: "STLViewerWidget",
      fileName: (format) => `stl-viewer-widget.${format}.js`
    }
  }
});
