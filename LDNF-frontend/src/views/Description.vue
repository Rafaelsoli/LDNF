<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'
import { useTheme } from '@/components/useTheme'
import { useRoute } from 'vue-router'
import PlacarForm from '@/components/PlacarForm.vue' 

const { theme, toggleTheme } = useTheme()
const route = useRoute()

const Usernome = ref("")
const Useremail = ref("")
const jogos = ref<any[]>([])
const mostrarModal = ref(false)
const combates = ref<any[]>([])
interface Jogador {
  nome: string
  numero_camisa: number
}

interface TimeInfo {
  nome: string
  descricao: string
  localidade: string
  escudo: string | null
  jogadores: Jogador[]
}

const time = ref<TimeInfo>()

const placarDesteTime = computed(() => {
  const idDaUrl = route.params.id
  if (!jogos.value.length) return null
  
  return jogos.value.find((item: any) => {
    // No seu log, o UUID do time está vindo direto no campo 'id'
    const idNoPlacar = item.id 
    
    return String(idNoPlacar) === String(idDaUrl)
  })
})

const carregarDados = async () => {
  const timeId = route.params.id
  try {
    // Executa as chamadas em paralelo para ser mais rápido
    const [resTime, resUser, resPlacar, resCombates] = await Promise.all([
      axios.get(`/api/time/${timeId}`),
      axios.get(`/api/eu/`),
      axios.get(`/api/placar/`),
      axios.get(`/api/jogos/${timeId}`)
    ])
    
    time.value = resTime.data
    Usernome.value = resUser.data.nome
    Useremail.value = resUser.data.email
    jogos.value = resPlacar.data
    combates.value = resCombates.data
  } catch (e) {
    console.error("Erro ao carregar dados da página:", e)
  }
}

onMounted(carregarDados)
</script>

<template>
  <header class="navbar navbar-expand-md d-print-none shadow-sm">
    <div class="container-xl">
      <a href="/Home" class="navbar-brand fw-bold text-primary me-3">🏆 LDNF</a>
      <ul class="navbar-nav">
        <li class="nav-item active">
          <a class="nav-link" href="/Home">
            <span class="nav-link-title">Home</span>
          </a>
        </li>
      </ul>

      <div class="navbar-nav flex-row order-md-last ms-auto">
        <button @click="toggleTheme" class="btn me-2">
          {{ theme === 'light' ? 'Escuro' : 'Claro' }}
        </button>
        <div class="nav-item dropdown">
          <a href="#" class="nav-link d-flex align-items-center">
            <span class="avatar avatar-sm me-2" style="background-image: url(/static/avatars/044m.jpg)"></span>
            <div class="d-none d-xl-block">
              <div class="fw-semibold">{{ Usernome }}</div>
              <div class="small text-secondary">{{ Useremail }}</div>
            </div>
          </a>
        </div>
      </div>
    </div>
  </header>

  <div class="page-body">
    <div class="container-xl">
      <div v-if="time">
        <div class="page-header mb-4">
          <h2 class="page-title">{{ time.nome }}</h2>
          <div class="text-secondary"><i>{{ time.localidade }}</i></div>
        </div>

        <div class="card mb-4 shadow-sm">
          <div class="card-header"><h3 class="card-title">Sobre o {{ time.nome }}</h3></div>
          <div class="card-body">
            <p class="text-secondary lh-lg">{{ time.descricao }}</p>
          </div>
        </div>
      </div>

      <div v-if="time" class="mb-5">
        <h3 class="page-title mb-3">Jogadores do {{ time.nome }}</h3>
        <div class="row row-cards">
          <div v-for="jogador in time.jogadores" :key="jogador.nome" class="col-sm-6 col-md-4 col-lg-3">
            <div class="card shadow-sm border-primary border-2">
              <div class="card-body p-3">
                <h5 class="card-title mb-0">
                  <span class="badge bg-primary-lt me-2">{{ jogador.numero_camisa }}</span>
                  {{ jogador.nome }}
                </h5>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div v-if="time && placarDesteTime" class="mt-5">
        <div class="page-header mb-4 d-flex justify-content-between align-items-center">
          <h3 class="page-title">Placar atual do {{ time.nome }}</h3>
        </div>

        <div class="card shadow-sm">
          <div class="card-body py-4">
            <div class="d-flex justify-content-around text-center">
              <div>
                <div class="text-secondary small fw-bold">VITÓRIAS</div>
                <div class="h2 text-success mb-0">{{ placarDesteTime.vitorias }}</div>
              </div>
              <div class="border-start"></div>
              <div>
                <div class="text-secondary small fw-bold">EMPATES</div>
                <div class="h2 text-warning mb-0">{{ placarDesteTime.empate }}</div>
              </div>
              <div class="border-start"></div>
              <div>
                <div class="text-secondary small fw-bold">DERROTAS</div>
                <div class="h2 text-danger mb-0">{{ placarDesteTime.derrotas }}</div>
              </div>
              <div class="border-start"></div>
              <div>
                <div class="text-secondary small fw-bold">GOLS (P/C)</div>
                <div class="h2 mb-0">{{ placarDesteTime.GM }} / {{ placarDesteTime.GS }}</div>
              </div>
            </div>
          </div>
        </div>
        <div class="page-header mb-4 d-flex justify-content-between align-items-center pt-4">
          <button class="btn btn-primary" @click="mostrarModal = true">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon me-2"><path d="M4 20h4l10.5 -10.5a2.828 2.828 0 1 0 -4 -4l-10.5 10.5v4" /><path d="M13.5 6.5l4 4" /></svg>
            Atualizar Placar  
          </button>
        </div>
      </div>

      <div v-else-if="time && !placarDesteTime" class="alert alert-info">
        Nenhum dado de placar encontrado para este time.
      </div>
    </div>
  </div>

  <PlacarForm 
    v-if="mostrarModal" 
    :timeId="route.params.id" 
    :dadosAtuais="placarDesteTime"
    @fechar="mostrarModal = false"
    @atualizado="carregarDados"
  />

<div v-for="combate in combates" :key="combate.id" class="col-md-6 col-lg-4 mb-3 container-xl">
  <div class="card shadow-sm border-2" :class="{'border-success': combate.vencedor}">
    <div class="card-body p-3">
      <div class="d-flex justify-content-between align-items-center">
        
        <div class="text-center" :class="{'fw-bold text-success': combate.vencedor?.id === combate.time_casa.id}">
          {{ combate.time_casa.nome }}
        </div>
        
        <div class="h4 mb-0 ">
          {{ combate.gols_casa }} - {{ combate.gols_visitante }}
        </div>

        <div class="text-center" :class="{'fw-bold text-success': combate.vencedor?.id === combate.time_visitante.id}">
          {{ combate.time_visitante.nome }}
        </div>
        
      </div>
      <div class="text-center mt-2 small text-secondary">
        {{ new Date(combate.data_jogo).toLocaleDateString('pt-BR') }}
      </div>
    </div>
  </div>
</div>
 
</template>