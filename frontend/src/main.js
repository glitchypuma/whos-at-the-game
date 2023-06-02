import * as Vue from 'vue'
import axios from 'axios';
import VueAxios from 'vue-axios'
import App from './App.vue'

const app = Vue.createApp(App)

app.config.globalProperties.$http = axios;

app
    .use(VueAxios, axios)
    .mount('#app')