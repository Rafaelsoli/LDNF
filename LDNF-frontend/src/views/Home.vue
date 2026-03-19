<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

interface TimeInfo{
  nome: string
  jogos: number
  pontos: number
  vitorias: number
  empate: number
  derrotas: number
}

const sobre = ref("")
const nome = ref("")
const email = ref("")
const time = ref<TimeInfo[]>([])
const userStore = useUserStore()
onMounted(async () =>{
    try {
      // chamadas da api
      const response = await axios.get(`/api/sobre/`,)
      const info = await axios.get(`/api/eu/`)
      const melhor = await axios.get(`/api/time/`)
      // atribuição de valor
      sobre.value = response.data.titulo
      nome.value = info.data.nome
      email.value = info.data.email
      time.value = melhor.data
    } catch (error) {
      console.error("Erro ao buscar dados:", error)
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
        <div class="nav-item dropdown">
          <a href="#" class="nav-link d-flex align-items-center"
            data-bs-toggle="dropdown">

            <span class="avatar avatar-sm me-2"
              style="background-image: url(/static/avatars/044m.jpg)">
            </span>

            <div class="d-none d-xl-block">
              <div class="fw-semibold">{{ nome }}</div>
              <div class="small text-secondary">{{ email }}</div>
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

  <!-- BODY -->
  <div class="page-body">
    <div class="container-xl">

      <!-- HEADER -->
      <div class="page-header mb-4">
        <h2 class="page-title">Liga LDNF</h2>
        <div class="text-secondary">
          Classificação e informações da liga
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
              {{ sobre }}
            </p>
          </div>
        </div>
      </div>

      <!-- TABELA -->
      <div class="card shadow-sm">
        <div class="card-header">
          <h3 class="card-title">Classificação</h3>
        </div>

        <div class="table-responsive">
          <table class="table table-vcenter table-hover table-striped">
            <thead>
              <tr>
                <th>#</th>
                <th>Time</th>
                <th>J</th>
                <th>V</th>
                <th>E</th>
                <th>D</th>
                <th class="text-end">Pts</th>
              </tr>
            </thead>

            <tbody>
              <tr v-for="(item, index) in time" :key="index">
                
                <td class="fw-bold text-primary">
                  {{ index + 1 }}º
                </td>

                <td class="fw-semibold">
                  {{ item.nome }}
                </td>

                <td>{{ item.jogos }}</td>
                <td class="text-success">{{ item.vitorias }}</td>
                <td class="text-warning">{{ item.empate }}</td>
                <td class="text-danger">{{ item.derrotas }}</td>

                <td class="text-end fw-bold">
                  {{ item.pontos}}
                </td>

              </tr>
            </tbody>
          </table>
        </div>
      </div>

    </div>
  </div>
</template>

<style scoped>
.fonte-mono {
  font-family: 'JetBrains Mono', monospace;
}

.table-hover tbody tr:hover {
  transform: scale(1.01);
  transition: 0.2s;
}
</style>