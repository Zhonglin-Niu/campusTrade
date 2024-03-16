import { createApp } from "vue";
import { createRouter, createWebHistory } from "vue-router";
import ElementPlus from "element-plus";
// import "element-plus/theme-chalk/dark/css-vars.css";
import "element-plus/dist/index.css";
import "./style.css";
import Main from "./components/Main.vue";
import App from "./App.vue";
import Detail from "./Detail.vue";

const app = createApp(App);

const routes = [
  {
    path: "/",
    name: "main",
    component: Main,
  },
  {
    path: "/detail/:id",
    name: "detail",
    component: Detail,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

app.use(ElementPlus);
app.use(router);
app.mount("#app");
