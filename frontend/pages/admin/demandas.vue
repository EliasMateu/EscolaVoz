<template>
  <div>
    <h1 class="text-2xl font-bold text-primary mb-6">Todas as Demandas</h1>
    <FilterBar @filter="handleFilter" class="mb-6" />
    <DataTable :demands="demands" :loading="loading" :editable="true" @update-status="handleStatusUpdate" />
  </div>
</template>

<script setup lang="ts">
const api = useApi()
const demands = ref<any[]>([])
const loading = ref(false)
const filters = ref<Record<string, string>>({})

async function fetchDemands(f: Record<string, string> = {}) {
  loading.value = true
  const params = new URLSearchParams()
  Object.entries(f).forEach(([k, v]) => { if (v) params.append(k, v) })
  try {
    const { data } = await api.get<{ results: any[] }>(`/demands/?${params.toString()}`)
    demands.value = data.results
  } finally {
    loading.value = false
  }
}

async function handleStatusUpdate(id: number, status: string) {
  await api.patch(`/demands/${id}/`, { status })
  await fetchDemands(filters.value)
}

function handleFilter(f: Record<string, string>) {
  filters.value = f
  fetchDemands(f)
}

onMounted(() => fetchDemands())
</script>