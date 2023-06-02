import * as Vue from 'vue'
import axios from 'axios';
import VueAxios from 'vue-axios'
import App from './App.vue'

const cors = require('cors')
const app = Vue.createApp(App)

app.config.globalProperties.$http = axios;
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

app
    .use(VueAxios, axios)
    .use(cors)
    .mount('#app')