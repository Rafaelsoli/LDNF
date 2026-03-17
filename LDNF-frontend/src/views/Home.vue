<template>
<div class="page-body">
  <div class="card">
    <div class="card-body">
      <h2>Sobre a LDNF</h2>
      <p>{{ sobre }}</p>
    </div>
  </div>
  <!-- <div class="mt-3">
    <a href="/titulos" class="btn btn-primary">Títulos</a>
    <a href="/cronologia" class="btn btn-secondary">Cronologia</a>
  </div> -->
</div>
</template>

<script setup lang="ts">
import { ref, reactive, onMounted } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const sobre = ref("")
onMounted(async () =>{
  try {
    const response = await axios.get(`/api/test/`,)
    sobre.value = response.data.sobre
  } catch (error) {
    console.error("Erro ao buscar dados:", error)
  }
})
</script>