import './assets/base.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'

import '@tabler/core/dist/css/tabler.min.css'
import '@tabler/core/dist/js/tabler.min.js'

axios.defaults.baseURL = "http://127.0.0.1:8000"

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(axios)
app.mount('#app')
