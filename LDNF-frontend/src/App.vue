<script setup lang="ts">
import { useUserStore } from '@/stores/user'
import axios from 'axios'
const userStore = useUserStore()

userStore.initStore()

const token = userStore.user.access

if (token) {
  console.log("token encontrado")
  axios.defaults.headers.common["Authorization"] = `Bearer ${token}`
} else {
  axios.defaults.headers.common["Authorization"] = ""
}
</script>

<template>
  <RouterView />
</template>
