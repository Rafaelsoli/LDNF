<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'
import { useTheme } from '@/components/useTheme'
import HeaderComp from '@/components/HeaderComp.vue'


interface PlacarInfo{
  id: string
  nome: string
  jogos: number
  pontos: number
  vitorias: number
  empate: number
  derrotas: number
  GM: number
  GS: number 
  DG: number 
  PCT: number 
}
const placar = ref<PlacarInfo[]>([])
const carddejogos = ref<any[]>([])
const sobre = ref("")
const router = useRouter()

onMounted(async () =>{
    try {
      // chamadas da api
      const response = await axios.get(`/api/sobre/`,)
      const tabela = await axios.get(`/api/placar/`)
      const jogos = await axios.get(`/api/jogos/`)
      // atribuição de valor
      sobre.value = response.data.titulo
      carddejogos.value = jogos.data
      placar.value = tabela.data
    } catch (error) {
      console.error("Erro ao buscar dados:", error)
  }
})
</script>

<template>
  <header-comp></header-comp>

  <!-- BODY -->
  <div class="page-body">
    <div class="container-xl">

      <!-- HEADER -->
      <div class="page-header mb-4">
        <h2 class="page-title">LDNF</h2>  
        <div class="text-secondary">
          <i>The league of the impossible</i>
        </div>
      </div>

      <!-- SOBRE -->
      <div class="card mb-4 shadow-sm">
        <div class="card-header d-flex justify-content-between align-items-center">
          <h3 class="card-title mb-0">Sobre a LDNF</h3>
          <button class="btn btn-sm btn-outline-secondary" type="button" data-bs-toggle="collapse" data-bs-target="#sobreCollapse" aria-expanded="false" aria-controls="sobreCollapse">
        <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-chevron-down" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
          <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
          <polyline points="6,9 12,15 18,9"></polyline>
        </svg>
          </button>
        </div>
        <div id="sobreCollapse" class="collapse">
          <div class="card-body">
        <p class="text-secondary lh-lg fonte-mono">
          {{ sobre }}
        </p>
          </div>
        </div>
      </div>


      <!-- Cards de jogos -->
      <div class="mb-4">
        <div class="d-flex justify-content-between align-items-center mb-2">
          <h3 class="card-title mb-0">Confrontos da Temporada</h3>
          <span class="badge bg-blue-lt">{{ carddejogos.length }} jogos</span>
        </div>

        <div class="carousel-container d-flex g-3 pb-3">
          <div v-for="combate in carddejogos" :key="combate.data_jogo" class="carousel-item-custom">
            <div class="card shadow-sm border-0 h-100 card-game">
              <div class="card-body p-3">
                <div class="row align-items-center g-2 text-center">
                  
                  <div class="col">
                    <img :src="combate.time_casa.escudo" class="avatar avatar-md mb-2 bg-transparent" style="object-fit: contain;">
                    <div class="small fw-bold text-truncate">{{ combate.time_casa.nome }}</div>
                  </div>

                  <div class="col-auto">
                    <div class="scoreboard mx-2">
                      <span class="h2 mb-0 fw-black">{{ combate.gols_casa }}</span>
                      <span class="mx-2 text-muted">-</span>
                      <span class="h2 mb-0 fw-black">{{ combate.gols_visitante }}</span>
                    </div>
                  </div>

                  <div class="col">
                    <img :src="combate.time_visitante.escudo" class="avatar avatar-md mb-2 bg-transparent" style="object-fit: contain;">
                    <div class="small fw-bold text-truncate">{{ combate.time_visitante.nome }}</div>
                  </div>
                </div>
                
                <div class="text-center mt-2 small text-secondary border-top pt-2">
                  {{ new Date(combate.data_jogo).toLocaleDateString('pt-BR', { day: '2-digit', month: 'short' }) }}
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- Cards de jogos -->

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
                <th>Pts</th>
                <th>J</th>
                <th>V</th>
                <th>E</th>
                <th>D</th>
                <th>GM</th>
                <th>GS</th>
                <th>DG</th>
                <th class="text-end">PCT</th>
              </tr>
            </thead>

            <tbody>
              <tr v-for="(item, index) in placar" :key="index">
                
                <td class="fw-bold text-primary">
                  {{ index + 1 }}º
                </td>

                <td class="fw-semibold" v-on:click="">
                  <router-link :to="`/time/${item.id}`">{{ item.nome }}</router-link>
                </td>

                <td>{{ item.pontos }}</td>
                <td>{{ item.jogos }}</td>
                <td class="text-success">{{ item.vitorias }}</td>
                <td class="text-warning">{{ item.empate }}</td>
                <td class="text-danger">{{ item.derrotas }}</td>
                <td>{{ item.GM }}</td>
                <td>{{ item.GS }}</td>
                <td>{{ item.DG }}</td>

                <td class="text-end fw-bold">
                  {{ item.PCT}}
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

/* Container que permite o scroll horizontal */
.carousel-container {
  display: flex;
  overflow-x: auto;
  gap: 1rem;
  scroll-snap-type: x mandatory; /* Faz o "imã" no card ao rolar */
  -webkit-overflow-scrolling: touch;
  scrollbar-width: thin; /* Firefox */
}

/* Esconder scrollbar no Chrome/Safari (opcional) */
.carousel-container::-webkit-scrollbar {
  height: 6px;
}
.carousel-container::-webkit-scrollbar-thumb {
  background: #cbd5e1;
  border-radius: 10px;
}

/* Largura de cada card no carrossel */
.carousel-item-custom {
  flex: 0 0 280px; /* Não deixa o card encolher e fixa em 280px */
  scroll-snap-align: start;
}

.card-game {
  transition: transform 0.2s;
}

.card-game:hover {
  transform: translateY(-5px);
}

.scoreboard {
  background: rgba(0, 0, 0, 0.05);
  padding: 0.25rem 0.75rem;
  border-radius: 8px;
  display: flex;
  align-items: center;
}
</style>