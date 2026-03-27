<script setup lang="ts">
import { reactive } from 'vue'
import axios from 'axios'
const props = defineProps<{
  combateId: string
  dadosAtuais: any
}>()
const emit = defineEmits(['fechar', 'atualizado'])
const form = reactive({ ...props.dadosAtuais })
const salvar = async () => {
    try {
        await axios.post(`/api/jogos/${props.combateId}/create`, form)
        emit('atualizado') 
        emit('fechar')     
    } catch (e) {
        alert("Erro ao atualizar combate")
    }
}
</script>

<template>
 <div class="modal modal-blur fade show d-block" tabindex="-1" style="background: rgba(0,0,0,0.5)">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Criar Jogo</h5>
          <button type="button" class="btn-close" @click="$emit('fechar')"></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-6 mb-3">
              <label class="form-label">Casa</label>
              <input type="number" v-model="form.time_casa" class="form-control">
            </div>
            <div class="col-6 mb-3">
              <label class="form-label text-success">Visitante</label>
              <input type="number" v-model="form.time_visitante" class="form-control">
            </div>
            <div class="col-6 mb-3">
              <label class="form-label text-warning">Gols Casa</label>
              <input type="number" v-model="form.gols_casa" class="form-control">
            </div>
            <div class="col-6 mb-3">
              <label class="form-label text-danger">Gols Visitante</label>
              <input type="number" v-model="form.gols_visitante" class="form-control">
            </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-link link-secondary" @click="$emit('fechar')">Cancelar</button>
          <button type="button" class="btn btn-primary" @click="salvar">Salvar Alterações</button>
        </div>
      </div>
    </div>
  </div>
</div> 
</template>

<style scoped>
</style>