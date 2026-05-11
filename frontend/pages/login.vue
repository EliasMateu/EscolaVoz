<template>
  <div class="min-h-screen flex items-center justify-center bg-gray-100">
    <div class="bg-white p-8 rounded-lg shadow-md w-full max-w-md">
      <h1 class="text-2xl font-bold text-center mb-6 text-primary">EscolaVoz</h1>
      <form @submit.prevent="handleLogin" class="space-y-4">
        <div>
          <label class="block text-sm font-medium text-gray-700">Email</label>
          <input
            v-model="username"
            type="text"
            class="mt-1 w-full px-3 py-2 border rounded-md"
            placeholder="seu@email.com"
            required
          />
        </div>
        <div>
          <label class="block text-sm font-medium text-gray-700">Senha</label>
          <input
            v-model="password"
            type="password"
            class="mt-1 w-full px-3 py-2 border rounded-md"
            required
          />
        </div>
        <div v-if="error" class="text-red-600 text-sm">{{ error }}</div>
        <button
          type="submit"
          :disabled="loading"
          class="w-full bg-primary text-white py-2 rounded-md hover:bg-primary-dark transition disabled:opacity-50"
        >
          {{ loading ? 'Entrando...' : 'Entrar' }}
        </button>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
definePageMeta({ layout: false })

const auth = useAuthStore()
const username = ref('')
const password = ref('')
const error = ref('')
const loading = ref(false)

async function handleLogin() {
  error.value = ''
  loading.value = true
  try {
    await auth.login(username.value, password.value)
    await navigateTo(auth.isAdmin ? '/admin/dashboard' : '/funcionario/demandas')
  } catch {
    error.value = 'Credenciais inválidas. Verifique email e senha.'
  } finally {
    loading.value = false
  }
}
</script>