<template>
  <div class="bg-white p-4 rounded-lg shadow flex flex-wrap gap-4 items-end">
    <div>
      <label class="block text-sm font-medium text-gray-700 mb-1">Escola</label>
      <select v-model="filters.school_id" @change="emit('filter', filters)" class="px-3 py-2 border rounded-md">
        <option value="">Todas</option>
        <option v-for="s in schools" :key="s.id" :value="s.id">{{ s.name }}</option>
      </select>
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700 mb-1">Categoria</label>
      <select v-model="filters.category_id" @change="emit('filter', filters)" class="px-3 py-2 border rounded-md">
        <option value="">Todas</option>
        <option v-for="c in categories" :key="c.id" :value="c.id">{{ c.name }}</option>
      </select>
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700 mb-1">Status</label>
      <select v-model="filters.status" @change="emit('filter', filters)" class="px-3 py-2 border rounded-md">
        <option value="">Todos</option>
        <option value="open">Aberta</option>
        <option value="in_progress">Em Andamento</option>
        <option value="resolved">Resolvida</option>
        <option value="rejected">Rejeitada</option>
      </select>
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700 mb-1">De</label>
      <input type="date" v-model="filters.created_after" @change="emit('filter', filters)" class="px-3 py-2 border rounded-md" />
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700 mb-1">Até</label>
      <input type="date" v-model="filters.created_before" @change="emit('filter', filters)" class="px-3 py-2 border rounded-md" />
    </div>
    <button @click="resetFilters" class="px-4 py-2 border rounded-md text-sm">Limpar</button>
  </div>
</template>

<script setup lang="ts">
const emit = defineEmits<{ filter: [filters: Record<string, string>] }>()
const filters = reactive({ school_id: '', category_id: '', status: '', created_after: '', created_before: '' })
const schoolsStore = useSchoolsStore()
const categoriesStore = useCategoriesStore()
const schools = computed(() => schoolsStore.schools)
const categories = computed(() => categoriesStore.categories)

onMounted(() => {
  schoolsStore.fetchSchools()
  categoriesStore.fetchCategories()
})

function resetFilters() {
  Object.assign(filters, { school_id: '', category_id: '', status: '', created_after: '', created_before: '' })
  emit('filter', filters)
}
</script>