import { createRouter, createWebHistory } from 'vue-router'
import RegistroPage from '../views/Registro.vue'
import LoginPage from '../views/Login.vue'
import HomePage from '../views/Home.vue'
import DescriptionPage from '../views/Description.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomePage,
    },
    {
      path: '/login',
      name: 'login',
      component: LoginPage,
    },
    {
      path:'/registro',
      name: 'registro',
      component: RegistroPage,
    },
    {
      path:'/time/:id',
      name: 'time-detalhes',
      component: DescriptionPage,
    }
  ],
})

export default router
