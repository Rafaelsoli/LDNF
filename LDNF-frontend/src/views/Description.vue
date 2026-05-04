<script setup lang="ts">
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'
import { useRoute } from 'vue-router'
import PlacarForm from '@/components/PlacarForm.vue' 
import CombateForm from '@/components/CombateForm.vue'
import HeaderComp from '@/components/HeaderComp.vue'

const route = useRoute()

const jogos = ref<any[]>([])
const mostrarModal = ref(false)
const mostrarModalCombate = ref(false)
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
    const idNoPlacar = item.id 
    
    return String(idNoPlacar) === String(idDaUrl)
  })
})
const isLoggedIn = ref(false)

onMounted(async() => {
  try {
    const {data} = await axios.get(`/api/eu/`)
    isLoggedIn.value = !!data
  } catch (error) {
    console.error("Convidado", error)
    isLoggedIn.value = false
  }
})

const carregarDados = async () => {
  const timeId = route.params.id
  try {
    const [resTime, resPlacar, resCombates] = await Promise.all([
      axios.get(`/api/time/${timeId}`),
      axios.get(`/api/placar/`),
      axios.get(`/api/jogos/${timeId}`)
    ])
    
    time.value = resTime.data
    jogos.value = resPlacar.data
    combates.value = resCombates.data
  } catch (e) {
    console.error("Erro ao carregar dados da página:", e)
  }
}

onMounted(carregarDados)

const excluirJogo = async (jogoId: string) => {
  if (!confirm("Tem certeza que deseja excluir este jogo?")) return

  try {
    await axios.delete(`/api/jogo/${jogoId}`)
    await carregarDados()
  } catch (e) {
    console.error("Erro ao excluir jogo:", e)
    alert("Não foi possível excluir o jogo.")
  }
} 
</script>

<template>
  <header-comp></header-comp>
  <div class="page-body">
    <div class="container-xl">
        <div v-if="time">
          <div class="page-header mb-4">
          <div class="d-flex align-items-center">
            <img v-if="time.escudo" 
                :src="time.escudo" 
                class="me-3" 
                style="width: 80px; height: 80px; object-fit: contain; background: transparent;">

            <div>
              <h2 class="page-title mb-0">{{ time.nome }}</h2>
              <div class="text-secondary"><i>{{ time.localidade }}</i></div>
            </div>
          </div>

          <div class="card mb-4 shadow-sm">
            <div class="card-header"><h3 class="card-title">Sobre o {{ time.nome }}</h3></div>
            <div class="card-body">
              <p class="text-secondary lh-lg">{{ time.descricao }}</p>
            </div>
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
          <h3 class="page-title p-3">Placar atual do {{ time.nome }}</h3>
          <button v-if="isLoggedIn" class="btn btn-primary" @click="mostrarModal = true">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="icon me-2"><path d="M4 20h4l10.5 -10.5a2.828 2.828 0 1 0 -4 -4l-10.5 10.5v4" /><path d="M13.5 6.5l4 4" /></svg>
            Atualizar Placar  
          </button>
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
      </div>
      <div v-else-if="time && !placarDesteTime" class="alert alert-info">
        Nenhum dado de placar encontrado para este time.
      </div>
    </div>
  </div>

  <PlacarForm
    v-if="mostrarModal"
    :timeId = "String(route.params.id)"
    :dadosAtuais="placarDesteTime"
    @fechar="mostrarModal = false"
    @atualizado="carregarDados"
  />

<div v-if="time" class="container-xl mt-5">
  <div class="page-header mb-4 d-flex justify-content-between align-items-center">
    <h3 class="page-title p-3">Jogos do {{ time.nome }}</h3>
    <button v-if="isLoggedIn" class="btn btn-outline-primary" @click="mostrarModalCombate = true">
      <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-plus" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M12 5l0 14" /><path d="M5 12l14 0" /></svg>
      Novo Jogo
    </button>
  </div>
  
    <div v-for="combate in combates" :key="combate.data_jogo" class="col-md-6 col-lg-4 mb-3 container-xl ">
      <div 
        class="card shadow-sm border-2 h-100" 
        :class="{
          'border-success': (String(combate.time_casa.id) === String(route.params.id) && combate.gols_casa > combate.gols_visitante) || 
                            (String(combate.time_visitante.id) === String(route.params.id) && combate.gols_visitante > combate.gols_casa),
          'border-danger': (String(combate.time_casa.id) === String(route.params.id) && combate.gols_casa < combate.gols_visitante) || 
                           (String(combate.time_visitante.id) === String(route.params.id) && combate.gols_visitante < combate.gols_casa),
          'border-warning': combate.gols_casa === combate.gols_visitante
        }"
      >
        <button v-if="isLoggedIn"
          @click="excluirJogo(combate.id)" 
          class="btn-close position-absolute top-0 end-0 m-2" 
          aria-label="Excluir jogo"
          style="font-size: 0.7rem; z-index: 10;"
        ></button>
        <div class="card-body p-3">
        <div class="row align-items-center g-0">
          
          <div class="col d-flex align-items-center justify-content-end text-end" 
              :class="{'fw-bold': combate.gols_casa > combate.gols_visitante}">
            <span class="me-2 d-none d-md-inline">{{ combate.time_casa.nome }}</span>
            <img :src="combate.time_casa.escudo" 
                alt="Escudo Casa"
                style="width: 32px; height: 32px; object-fit: contain;">
          </div>

          <div class="col-auto px-3">
            <div class="bg-body px-2 py-1 rounded border fw-bold h3 mb-0" style="min-width: 70px; text-align: center;">
              {{ combate.gols_casa }} - {{ combate.gols_visitante }}
            </div>
          </div>

          <div class="col d-flex align-items-center justify-content-start text-start" 
              :class="{'fw-bold': combate.gols_visitante > combate.gols_casa}">
            <img :src="combate.time_visitante.escudo" 
                alt="Escudo Visitante"
                class="me-2"
                style="width: 32px; height: 32px; object-fit: contain;">
            <span class="d-none d-md-inline">{{ combate.time_visitante.nome }}</span>
          </div>

        </div>

        <div class="text-center mt-3 small text-muted">
          <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-inline me-1" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M4 7a2 2 0 0 1 2 -2h12a2 2 0 0 1 2 2v12a2 2 0 0 1 -2 2h-12a2 2 0 0 1 -2 -2v-12z" /><path d="M16 3v4" /><path d="M8 3v4" /><path d="M4 11h16" /><path d="M11 15h1" /><path d="M12 15v3" /></svg>
          {{ new Date(combate.data_jogo).toLocaleString('pt-BR', { dateStyle: 'short', timeStyle: 'short' }) }}
        </div>
      </div>
      </div>
    </div>
</div>

<CombateForm 
  v-if="mostrarModalCombate" 
  :timeIdDaPagina="String(route.params.id)" 
  @fechar="mostrarModalCombate = false"
  @atualizado="carregarDados" 
/>
 
</template>
 