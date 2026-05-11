<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-2xl font-bold text-primary">Minhas Demandas</h1>
      <NuxtLink to="/funcionario/demandas/nova" class="bg-secondary text-white px-4 py-2 rounded-md">
        + Nova Demanda
      </NuxtLink>
    </div>
    <div v-if="demands.loading" class="text-center py-8">Carregando...</div>
    <div v-else-if="demands.demands.length === 0" class="text-center py-8 text-gray-500">
      Nenhuma demanda registrada ainda.
    </div>
    <div v-else class="grid gap-4 md:grid-cols-2">
      <DemandCard v-for="d in demands.demands" :key="d.id" :demand="d" />
    </div>
  </div>
</template>

<script setup lang="ts">
const demands = useDemandsStore()
onMounted(() => demands.fetchMyDemands())
</script>