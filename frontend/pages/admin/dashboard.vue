<template>
  <div>
    <div class="flex justify-between items-center mb-6">
      <h1 class="text-2xl font-bold text-primary">Dashboard</h1>
      <button @click="exportCSV" class="bg-green-600 text-white px-4 py-2 rounded-md text-sm">
        Exportar CSV
      </button>
    </div>
    <FilterBar @filter="handleFilter" class="mb-6" />
    <div class="bg-white p-6 rounded-lg shadow">
      <BarChart v-if="chartData.datasets.length" :labels="chartData.labels" :datasets="chartData.datasets" />
      <div v-else class="text-center py-8 text-gray-500">Nenhum dado disponível</div>
    </div>
  </div>
</template>

<script setup lang="ts">
const api = useApi()
const filters = ref<Record<string, string>>({})

const chartData = reactive({ labels: [] as string[], datasets: [] as any[] })

async function fetchAndBuild(f: Record<string, string> = {}) {
  const params = new URLSearchParams()
  Object.entries(f).forEach(([k, v]) => { if (v) params.append(k, v) })
  const { data } = await api.get<{ results: any[] }>(`/demands/?${params.toString()}`)
  const demands = data.results
  const schoolMap: Record<string, Record<string, number>> = {}
  const categorySet = new Set<string>()

  for (const d of demands) {
    if (!schoolMap[d.school_name]) schoolMap[d.school_name] = {}
    schoolMap[d.school_name][d.category_name] = (schoolMap[d.school_name][d.category_name] || 0) + 1
    categorySet.add(d.category_name)
  }

  const schools = Object.keys(schoolMap)
  const categories = Array.from(categorySet)
  const colors = ['#1E3A5F', '#F59E0B', '#10B981', '#EF4444', '#8B5CF6', '#EC4899', '#06B6D4']

  chartData.labels = schools
  chartData.datasets = categories.map((cat, i) => ({
    label: cat,
    data: schools.map(s => schoolMap[s][cat] || 0),
    backgroundColor: colors[i % colors.length],
  }))
}

function handleFilter(f: Record<string, string>) {
  filters.value = f
  fetchAndBuild(f)
}

onMounted(() => fetchAndBuild())

async function exportCSV() {
  const params = new URLSearchParams()
  Object.entries(filters.value).forEach(([k, v]) => { if (v) params.append(k, v) })
  const { data } = await api.get(`/demands/export/csv/?${params.toString()}`, { responseType: 'blob' })
  const url = URL.createObjectURL(new Blob([data]))
  const a = document.createElement('a')
  a.href = url
  a.download = 'demandas.csv'
  a.click()
  URL.revokeObjectURL(url)
}
</script>