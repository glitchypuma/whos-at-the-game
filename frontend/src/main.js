import * as Vue from 'vue'
import axios from 'axios';
import VueAxios from 'vue-axios'
import App from './App.vue'

//import { createApp } from 'vue'
//import VueRouter from 'vue-router';


//axios.defaults.baseURL = 'http://localhost:8080/'
// const routes = [
//     {
//     name: 'Home',
//     path: '/',
//     component: App
//     }
// ];

// const router = new VueRouter({ mode: 'history', routes: routes })

const app = Vue.createApp(App)

app
    .use(VueAxios, axios)
    .mount('#app')