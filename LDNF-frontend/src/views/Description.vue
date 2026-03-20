<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import axios from 'axios'
import { useTheme } from '@/components/useTheme'
import { useRoute } from 'vue-router'

const { theme, toggleTheme } = useTheme()
const route = useRoute()

// Dados do usuário (mockados ou vindo de outra store)
const nomeUser = ref("Usuário") 
const emailUser = ref("usuario@ldnf.com")

interface TimeInfo {
  nome: string
  descricao: string
  localidade: string 
}

const time = ref<TimeInfo>()

onMounted(async () => {
  const timeId = route.params.id
  try {
    const resposta = await axios.get(`/api/time/${timeId}`)
    time.value = resposta.data
  } catch (e) {
    console.error("Erro ao buscar time!", e)
  }
})
</script>



<template>
  <header class="navbar navbar-expand-md d-print-none shadow-sm">
    <div class="container-xl">
      <a href="#" class="navbar-brand fw-bold text-primary me-3">
        LDNF
      </a>

      <ul class="navbar-nav">
        <li class="nav-item active">
          <a class="nav-link" href="#">
            <span class="nav-link-title">Home</span>
          </a>
        </li>

        <!-- <li class="nav-item">
          <a class="nav-link" href="#">
            <span class="nav-link-title">Profile</span>
          </a>
        </li> exemplo de botao de navbar --> 
      </ul>

      <!-- USER -->
      <div class="navbar-nav flex-row order-md-last ms-auto">
        <button @click="toggleTheme" class="btn me-2">
          <span v-if="theme === 'light'">Branco</span>
          <span v-else>Escuro</span>
        </button>
        <div class="nav-item dropdown">
          <a href="#" class="nav-link d-flex align-items-center"
            data-bs-toggle="dropdown">

            <span class="avatar avatar-sm me-2"
              style="background-image: url(/static/avatars/044m.jpg)">
            </span>

            <div class="d-none d-xl-block">
              <div class="fw-semibold">{{ nomeUser }}</div>
              <div class="small text-secondary">{{ emailUser }}</div>
            </div>
          </a>

          <div class="dropdown-menu dropdown-menu-end">
            <a class="dropdown-item">Profile</a>
            <a class="dropdown-item">Settings</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item text-danger">Logout</a>
          </div>
        </div>
      </div>
    </div>
  </header>
  <div class="page-body">
    <div class="container-xl">

      <!-- HEADER -->
      <div class="page-header mb-4">
        <h2 class="page-title">{{time.nome}}</h2>  
        <div class="text-secondary">
          <i>The league of the impossible</i>
        </div>
      </div>

      <!-- SOBRE -->
      <div class="card mb-4 shadow-sm">
        <div class="card-header d-flex justify-content-between align-items-center">
          <h3 class="card-title mb-0">Sobre a LDNF</h3>

          <button 
            class="btn btn-outline-primary btn-sm"
            data-bs-toggle="collapse"
            data-bs-target="#sobreCollapse"
          >
            Ver mais
          </button>
        </div>

        <div id="sobreCollapse" class="collapse show">
          <div class="card-body">
            <p class="text-secondary lh-lg fonte-mono">
              
            </p>
          </div>
        </div>
      </div>
    </div>
</div>
</template>