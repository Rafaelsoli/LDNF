<script setup lang="ts">
import { reactive, onMounted, ref } from 'vue'
import axios from 'axios'

const props = defineProps<{
  // aqui passando isso pra deixar já preenchido o time atual no form que aparece.
  timeIdDaPagina: string 
}>()

const emit = defineEmits(['fechar', 'atualizado'])

const listaTimes = ref<any[]>([])

const form = reactive({
  time_casa: props.timeIdDaPagina, 
  time_visitante: '',
  gols_casa: 0,
  gols_visitante: 0,
  data_jogo: new Date().toLocaleDateString('pt-BR')
})

const carregarTimesParaSelecao = async () => {
  try {
    const res = await axios.get('/api/placar/')
    listaTimes.value = res.data
  } catch (e) {
    console.error("Erro ao carregar times", e)
  }
}

const salvar = async () => {
  try {
    // Validar se não é o mesmo time jogando contra ele mesmo
    if (form.time_casa === form.time_visitante) {
      alert("Um time não pode jogar contra ele mesmo!")
      return
    }

    await axios.post('/api/jogos/create', form)
    
    emit('atualizado') 
    emit('fechar')     
  } catch (e) {
    console.error(e)
    alert("Erro ao criar jogo. Verifique se os IDs estão corretos.")
  }
}

onMounted(carregarTimesParaSelecao)
</script>

<template>
  <div class="modal modal-blur fade show d-block" tabindex="-1" style="background: rgba(0,0,0,0.5)">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Registrar Partida</h5>
          <button type="button" class="btn-close" @click="$emit('fechar')"></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-12 mb-3">
              <label class="form-label">Time da Casa</label>
              <select v-model="form.time_casa" class="form-select">
                <option v-for="t in listaTimes" :key="t.id" :value="t.id">
                  {{ t.nome }}
                </option>
              </select>
            </div>

            <div class="col-12 mb-3">
              <label class="form-label">Time Visitante</label>
              <select v-model="form.time_visitante" class="form-select">
                <option value="">Selecione o adversário...</option>
                <option v-for="t in listaTimes" :key="t.id" :value="t.id">
                  {{ t.nome }}
                </option>
              </select>
            </div>

            <div class="col-6 mb-3">
              <label class="form-label">Gols Casa</label>
              <input type="number" v-model.number="form.gols_casa" class="form-control">
            </div>
            <div class="col-6 mb-3">
              <label class="form-label">Gols Visitante</label>
              <input type="number" v-model.number="form.gols_visitante" class="form-control">
            </div>
          </div>
            <div class="col-12 mb-3">
              <label class="form-label">Data do jogo</label>
              <input type="date" v-model="form.data_jogo" class="form-control">
            </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-link link-secondary" @click="$emit('fechar')">Cancelar</button>
          <button type="button" class="btn btn-primary" @click="salvar">Criar Jogo</button>
        </div>
      </div>
    </div>
  </div>
</template>