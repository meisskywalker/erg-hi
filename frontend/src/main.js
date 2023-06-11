import { createApp } from 'vue';
import { createPinia } from 'pinia';
import axios from 'axios';

import './style.css';
import router from './router';
import App from './App.vue';
import VueCookies from 'vue-cookies';

axios.defaults.baseURL = import.meta.env.VITE_API_URL;
axios.defaults.withCredentials = true;

const app = createApp(App);
const pinia = createPinia();

app.use(pinia);
app.use(router);
app.use(VueCookies);

app.mount('#app');
