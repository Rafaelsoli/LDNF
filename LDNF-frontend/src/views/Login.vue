<template>
  <div class="page page-center">
    <div class="container container-tight py-4">
      <div class="text-center mb-4">
        <router-link to="/" class="navbar-brand navbar-brand-autodark">
          <h1 class="text-primary">LDNF</h1>
        </router-link>
      </div>

      <form class="card card-md" @submit.prevent="submitForm" autocomplete="off">
        <div class="card-body">
          <h2 class="card-title text-center mb-4">Entrar na Conta</h2>
          
          <div class="mb-3">
            <label class="form-label">Endereço de E-mail</label>
            <input type="email" v-model="form.email" class="form-control" placeholder="exemplo@email.com" required>
          </div>

          <div class="mb-3">
            <label class="form-label">Senha</label>
            <input type="password" v-model="form.senha" class="form-control" placeholder="Sua senha" required>
          </div>

          <div v-if="errors.length" class="alert alert-danger" role="alert">
            <ul class="mb-0">
              <li v-for="error in errors" :key="error">{{ error }}</li>
            </ul>
          </div>

          <div class="form-footer">
            <button type="submit" class="btn btn-primary w-100" :disabled="isLoading">
              <span v-if="isLoading" class="spinner-border spinner-border-sm me-2"></span>
              {{ isLoading ? 'Entrando...' : 'Entrar' }}
            </button>
          </div>
        </div>
      </form>

      <div class="text-center text-secondary mt-3">
        Ainda não tem conta? <router-link to="/registrar">Criar conta</router-link>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, reactive } from 'vue'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { useUserStore } from '@/stores/user'

const router = useRouter()
const userStore = useUserStore()
const isLoading = ref(false)
const errors = ref<string[]>([])

const form = reactive({
    email: '',
    senha: '',
})

const submitForm = async () => {
    isLoading.value = true
    errors.value = []
     
    try {
        const response = await axios.post(`/api/token/pair`, {
            email: form.email,
            password: form.senha
        })

        if (response.status === 200) {
            console.log("Resposta do login: ", response.data)
            userStore.setToken(response.data)
            axios.defaults.headers.common["Authorization"] = "Bearer " + response.data.access
            localStorage.setItem('token', response.data.access)
            //Redirecionamento
            const RespostaUsuario = await axios.get('/api/eu/')
            userStore.setUserInfo(RespostaUsuario.data)
            console.log("user: ", RespostaUsuario.data)
            router.push('/Home')
        }
    } catch (error: any) {
        console.error("Erro no login:", error)
        
        if (error.response?.status === 401) {
            errors.value.push("E-mail ou senha incorretos.")
        } else if (error.response?.data?.detail) {
            errors.value.push(error.response.data.detail)
        } else {
            errors.value.push("Erro ao conectar com o servidor.")
        }
    } finally {
        isLoading.value = false
    }
}
</script>