import * as Vue from 'vue'
import axios from 'axios';
import VueAxios from 'vue-axios'
import App from './App.vue'

//import { createApp } from 'vue'
//import VueRouter from 'vue-router';


// axios.defaults.baseURL = 'http://localhost:8080/'
// const routes = [
//     {
//     name: 'Home',
//     path: '/',
//     component: App
//     }
// ];

// const router = new VueRouter({ mode: 'history', routes: routes })
// const bodyParser = require('body-parser')
const cors = require('cors')
const app = Vue.createApp(App)

app.config.globalProperties.$http = axios;
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

app
    //.use(axios)
    //.use(bodyParser.json())
    .use(VueAxios, axios)
    .use(cors)
    .mount('#app')