import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  server: {
    proxy: {
      "/api": {
        target: "http://calvin.myh2o.top:66",
        changeOrigin: true,
        rewrite: path => path.replace(/^\/api/, ""),
      },
      "/static": {
        target: "http://calvin.myh2o.top:66/static",
        changeOrigin: true,
        rewrite: path => path.replace(/^\/static/, ""),
      },
    },
  },
});
