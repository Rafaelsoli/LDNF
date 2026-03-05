<template>
  <div class="page page-center">
    <div class="container container-tight py-4">
      <div class="text-center mb-4">
        <a href="." class="navbar-brand navbar-brand-autodark">
          <h1 class="text-primary">LDNF</h1>
        </a>
      </div>

      <form class="card card-md" @submit.prevent="submitForm" autocomplete="off">
        <div class="card-body">
          <h2 class="card-title text-center mb-4">Criar nova conta</h2>
          
          <div class="mb-3">
            <label class="form-label">Nome Completo</label>
            <input type="text" v-model="form.nome" class="form-control" placeholder="Digite seu nome" required>
          </div>

          <div class="mb-3">
            <label class="form-label">Endereço de E-mail</label>
            <input type="email" v-model="form.email" class="form-control" placeholder="exemplo@email.com" required>
          </div>

          <div class="mb-3">
            <label class="form-label">Senha</label>
            <div class="input-group input-group-flat">
              <input type="password" v-model="form.senha" class="form-control" placeholder="Senha forte" autocomplete="off" required>
            </div>
          </div>

          <div class="mb-3">
            <label class="form-label">Confirmar Senha</label>
            <input type="password" v-model="form.confirmar_senha" class="form-control" placeholder="Repita a senha" required>
          </div>

          <div v-if="errors.length" class="alert alert-danger" role="alert">
            <ul class="mb-0">
              <li v-for="error in errors" :key="error">{{ error }}</li>
            </ul>
          </div>

          <div class="form-footer">
            <button type="submit" class="btn btn-primary w-100" :disabled="isLoading">
              <span v-if="isLoading" class="spinner-border spinner-border-sm me-2" role="status"></span>
              {{ isLoading ? 'Processando...' : 'Criar minha conta' }}
            </button>
          </div>
        </div>
      </form>

      <div class="text-center text-secondary mt-3">
        Já possui uma conta? <router-link to="/login" tabindex="-1">Entrar</router-link>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'

const router = useRouter()
const isLoading = ref(false)
const errors = ref<string[]>([])

const form = reactive({
  nome: '',
  email: '',
  senha: '',
  confirmar_senha: ''
})

const submitForm = async () => {
  errors.value = []
  
  if (form.nome == ''){
    errors.value.push("Nome Faltando")
  }
  if (form.email == ""){
    errors.value.push("Email Faltante")
  }
  if (form.senha !== form.confirmar_senha) {
    errors.value.push("As senhas não coincidem.")
    return
  }

  if(errors.value.length === 0){
    isLoading.value = true
    try{
      const response = await axios.post('/api/registrar/', form)
      if (response.data.success || response.data.message === 'success') {
          //toastStore.showToast(5000, 'O usuário foi registrado com sucesso!', 'success')
          console.log("sucesso")
          // Limpa o formulário
          form.email = ''
          form.nome = ''
          form.senha = ''
          form.confirmar_senha = ''

          // Redireciona para o login após 2 segundos
          // setTimeout(() => router.push('/login'), 2000)
        }
      } catch (error: any) {
        console.error(error)
        //toastStore.showToast(5000, 'Algo deu errado no servidor', 'error')
        
        // Se o Django Ninja retornar um erro específico (ex: e-mail já existe)
        if (error.response?.data?.error) {
          errors.value.push(error.response.data.error)
        }
      } finally {
        isLoading.value = false // Desativa o loading independente de dar certo ou errado
      }
    }
  }
</script>

<style scoped>
.page-center {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f4f6fa;
}
</style>