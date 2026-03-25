<script setup lang="ts">
import { reactive } from 'vue'
import axios from 'axios'

const props = defineProps<{
  timeId: string
  dadosAtuais: any
}>()

const emit = defineEmits(['fechar', 'atualizado'])

const form = reactive({ ...props.dadosAtuais })

const salvar = async () => {
  try {
    await axios.post(`/api/placar/${props.timeId}/update`, form)
    emit('atualizado') // Avisa o pai para recarregar a lista
    emit('fechar')     // Fecha o modal
  } catch (e) {
    alert("Erro ao atualizar placar")
  }
}
</script>

<template>
  <div class="modal modal-blur fade show d-block" tabindex="-1" style="background: rgba(0,0,0,0.5)">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">Atualizar Placar Oficial</h5>
          <button type="button" class="btn-close" @click="$emit('fechar')"></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-6 mb-3">
              <label class="form-label">Jogos</label>
              <input type="number" v-model="form.jogos" class="form-control">
            </div>
            <div class="col-6 mb-3">
              <label class="form-label text-success">Vitórias</label>
              <input type="number" v-model="form.vitorias" class="form-control">
            </div>
            <div class="col-6 mb-3">
              <label class="form-label text-warning">Empates</label>
              <input type="number" v-model="form.empate" class="form-control">
            </div>
            <div class="col-6 mb-3">
              <label class="form-label text-danger">Derrotas</label>
              <input type="number" v-model="form.derrotas" class="form-control">
            </div>
            <div class="col-6">
              <label class="form-label">Gols Marcados (GM)</label>
              <input type="number" v-model="form.GM" class="form-control">
            </div>
            <div class="col-6">
              <label class="form-label">Gols Sofridos (GS)</label>
              <input type="number" v-model="form.GS" class="form-control">
            </div>
          </div>
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-link link-secondary" @click="$emit('fechar')">Cancelar</button>
          <button type="button" class="btn btn-primary" @click="salvar">Salvar Alterações</button>
        </div>
      </div>
    </div>
  </div>
</template>