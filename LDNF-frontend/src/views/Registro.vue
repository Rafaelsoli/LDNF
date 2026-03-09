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
            <input type="password" v-model="form.senha" class="form-control" placeholder="Senha forte" required>
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
              <span v-if="isLoading" class="spinner-border spinner-border-sm me-2"></span>
              {{ isLoading ? 'Processando...' : 'Criar minha conta' }}
            </button>
          </div>
        </div>
      </form>

      <div class="text-center text-secondary mt-3">
        Já possui uma conta? <router-link to="/login">Entrar</router-link>
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
  
  // Validação simples de senha
  if (form.senha !== form.confirmar_senha) {
    errors.value.push("As senhas não coincidem.")
    return
  }

  isLoading.value = true
  
  try {
    const response = await axios.post(`/api/registrar/`, {
      nome: form.nome,
      email: form.email,
      senha: form.senha
    })

    // Se o Django retornar success: true ou status 200/201
    if (response.data.success || response.status === 200 || response.status === 201) {
      console.log("Usuário registrado com sucesso!")
      
      // Limpar formulário
      Object.assign(form, { nome: '', email: '', senha: '', confirmar_senha: '' })

      // Redirecionar (opcional)
      router.push('/Login')
    }
  } catch (error: any) {
    console.error("Erro na requisição:", error)
    
    // Captura a mensagem de erro que configuramos no Python: return 400, {"error": "..."}
    if (error.response?.data?.error) {
      errors.value.push(error.response.data.error)
    } else if (error.response?.data?.detail) {
      // Caso o Django Ninja envie um erro de validação automática
      errors.value.push("Dados inválidos. Verifique os campos.")
    } else {
      errors.value.push("Algo deu errado no servidor. Tente novamente mais tarde.")
    }
  } finally {
    isLoading.value = false
  }
}
</script>