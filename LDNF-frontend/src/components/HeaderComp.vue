<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useTheme } from '@/components/useTheme'


const router = useRouter()
const { theme, toggleTheme } = useTheme()

const nome = ref("")
const email = ref("")
const avatar = ref("")

onMounted(async () => {
  try {
    const info = await axios.get(`/api/eu/`)
    nome.value = info.data.nome
    email.value = info.data.email
    avatar.value = info.data.avatar
  } catch (error) {
    console.error("Erro ao carregar perfil:", error)
  }
})

async function logout() {
  const userStore = useUserStore();
  try {
    const refreshToken = localStorage.getItem('user.refresh')

    await axios.post('/api/logout/', {
      refresh: refreshToken
    });

  } catch (error) {
    console.error("Erro ao fazer logout:", error);
  } finally {
      userStore.removeToken();
      router.push('/Login');
  }
}

async function login() {
  router.push("/Login")
}

</script>

<template>
    <header class="navbar navbar-expand-md d-print-none shadow-sm">
    <div class="container-xl">
      
      <a href="/Home" class="navbar-brand fw-bold text-primary me-3">
        🏆 LDNF
      </a>
      <!-- USER -->
      
      <div class="navbar-nav flex-row order-md-last ms-auto">
        <button @click="toggleTheme" class="btn btn-ghost-secondary border-0 shadow-none p-1 me-2 bg-transparent">
          <span v-if="theme === 'light'">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor" class="icon icon-tabler-filled icon-tabler-bulb"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M4 11a1 1 0 0 1 .117 1.993l-.117 .007h-1a1 1 0 0 1 -.117 -1.993l.117 -.007h1z" /><path d="M12 2a1 1 0 0 1 .993 .883l.007 .117v1a1 1 0 0 1 -1.993 .117l-.007 -.117v-1a1 1 0 0 1 1 -1z" /><path d="M21 11a1 1 0 0 1 .117 1.993l-.117 .007h-1a1 1 0 0 1 -.117 -1.993l.117 -.007h1z" /><path d="M4.893 4.893a1 1 0 0 1 1.32 -.083l.094 .083l.7 .7a1 1 0 0 1 -1.32 1.497l-.094 -.083l-.7 -.7a1 1 0 0 1 0 -1.414z" /><path d="M17.693 4.893a1 1 0 0 1 1.497 1.32l-.083 .094l-.7 .7a1 1 0 0 1 -1.497 -1.32l.083 -.094l.7 -.7z" /><path d="M14 18a1 1 0 0 1 .117 -.007l.883 -.993a1 1 0 0 1 1 1a3 3 0 0 1 -6 0a1 1 0 0 1 .883 -.993l.117 -.007h4z" /><path d="M12 6a6 6 0 0 1 3.6 10.8a1 1 0 0 1 -.471 .192l-.129 .008h-6a1 1 0 0 1 -.6 -.2a6 6 0 0 1 3.6 -10.8z" /></svg>
          </span>
          <span v-else>
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler-outline icon-tabler-bulb"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M3 12h1m8 -9v1m8 8h1m-15.4 -6.4l.7 .7m12.1 -.7l-.7 .7" /><path d="M9 16a5 5 0 1 1 6 0a3.5 3.5 0 0 0 -1 3a2 2 0 0 1 -4 0a3.5 3.5 0 0 0 -1 -3" /><path d="M9.7 17l4.6 0" /></svg>
          </span>
        </button>
          
        <a href="#" class="nav-link d-flex align-items-center" data-bs-toggle="dropdown">
            <span 
            class="avatar avatar-sm me-2" 
            :style="{ backgroundImage: `url(${avatar})` }"
            ></span>

            <div class="d-none d-xl-block">
              <div class="fw-semibold" v-if="nome">{{ nome }}</div>
              <div class="fw-semibold" v-else>Convidado</div>
              <div class="small text-secondary">{{ email }}</div>
            </div>
          </a>
          <button v-if="nome" @click="logout" class="btn btn-ghost-secondary border-0 shadow-none p-1 bg-transparent">
            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler-logout"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M14 8v-2a2 2 0 0 0 -2 -2h-7a2 2 0 0 0 -2 2v12a2 2 0 0 0 2 2h7a2 2 0 0 0 2 -2v-2" /><path d="M7 12h14l-3 -3m0 6l3 -3" /></svg>
          </button>

          <button v-else @click="logout" class="btn btn-ghost-secondary border-0 shadow-none p-1 bg-transparent">
            <svg xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon icon-tabler-login"><path stroke="none" d="M0 0h24v24H0z" fill="none" /><path d="M15 8v-2a2 2 0 0 0 -2 -2h-7a2 2 0 0 0 -2 2v12a2 2 0 0 0 2 2h7a2 2 0 0 0 2 -2v-2" /><path d="M21 12h-13l3 -3" /><path d="M11 15l-3 -3" /></svg>
          </button>
        </div>
      </div>
  </header>
</template>

<style scoped>
  .btn-ghost-secondary:active,
  .btn-ghost-secondary:focus {
    background-color: transparent;
    color: inherit;
  }
</style>