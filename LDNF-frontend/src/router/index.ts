import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/Registro.vue'
import LoginPage from '../views/Login.vue'
import InicioPage from '../views/Home.vue'
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
      path:'/Home',
      name: 'Inicial',
      component: InicioPage,
    }
  ],
})

export default router
