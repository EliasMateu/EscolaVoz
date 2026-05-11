<template>
  <nav class="bg-primary text-white shadow-md">
    <div class="container mx-auto px-4 py-3 flex items-center justify-between">
      <div class="font-bold text-lg">EscolaVoz</div>
      <div class="flex items-center gap-4">
        <NuxtLink v-if="auth.isAdmin" to="/admin/dashboard" class="hover:underline">Dashboard</NuxtLink>
        <NuxtLink v-if="auth.isFuncionario" to="/funcionario/demandas" class="hover:underline">Demandas</NuxtLink>
        <button @click="handleLogout" class="bg-secondary px-3 py-1 rounded text-sm font-medium">
          Sair
        </button>
      </div>
    </div>
  </nav>
</template>

<script setup lang="ts">
const auth = useAuthStore()

function handleLogout() {
  auth.logout()
  navigateTo('/login')
}
</script>