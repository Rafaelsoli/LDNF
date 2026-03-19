// src/composables/useTheme.ts
import { ref, onMounted } from 'vue'

export function useTheme() {
  const theme = ref('light')

  const setTheme = (val: 'light' | 'dark') => {
    theme.value = val
    // Salva no navegador para a próxima visita
    localStorage.setItem('theme', val)
    // Aplica o atributo no <html> para o Bootstrap/CSS entender
    document.documentElement.setAttribute('data-bs-theme', val)
  }

  const toggleTheme = () => {
    const newTheme = theme.value === 'light' ? 'dark' : 'light'
    setTheme(newTheme)
  }

  onMounted(() => {
    const saved = localStorage.getItem('theme') as 'light' | 'dark'
    if (saved) {
      setTheme(saved)
    } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
      // Se não tem salvo, respeita a preferência do sistema operacional
      setTheme('dark')
    }
  })

  return { theme, toggleTheme }
}