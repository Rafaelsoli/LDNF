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

const sobre = ref("")
const router = useRouter()

onMounted(async () =>{
    try {
      // chamadas da api
      const response = await axios.get(`/api/sobre/`,)
      const tabela = await axios.get(`/api/placar/`)
      
      // atribuição de valor
      sobre.value = response.data.titulo
      
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
        </div>
          <div class="card-body">
            <p class="text-secondary lh-lg fonte-mono">
              {{ sobre }}
            </p>
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
</style>