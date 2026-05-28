<template>
  <form @submit.prevent="handleSubmit" class="space-y-4">
    <div>
      <label class="block text-sm font-medium text-gray-700 mb-1">Categoria *</label>
      <CategorySelect v-model="categoryId" />
      <span v-if="errors.category" class="text-red-500 text-xs">{{ errors.category }}</span>
    </div>
    <div>
      <label class="block text-sm font-medium text-gray-700 mb-1">Descrição</label>
      <textarea
        v-model="description"
        rows="4"
        class="w-full px-3 py-2 border rounded-md"
        placeholder="Descreva a necessidade..."
      />
    </div>
    <div v-if="serverError" class="text-red-600 text-sm">{{ serverError }}</div>
    <div class="flex gap-2">
      <button type="submit" :disabled="loading" class="bg-primary text-white px-4 py-2 rounded-md hover:bg-primary-dark transition disabled:opacity-50">
        {{ loading ? 'Enviando...' : 'Registrar Demanda' }}
      </button>
      <NuxtLink to="/funcionario/demandas" class="px-4 py-2 border rounded-md">Cancelar</NuxtLink>
    </div>
  </form>
</template>

<script setup lang="ts">
const emit = defineEmits<{ success: [] }>()
const categoryId = ref<number | null>(null)
const description = ref('')
const errors = reactive({ category: '' })
const serverError = ref('')
const loading = ref(false)

function validate() {
  errors.category = categoryId.value ? '' : 'Categoria é obrigatória'
  return !errors.category
}

async function handleSubmit() {
  if (!validate()) return
  loading.value = true
  serverError.value = ''
  try {
    const demands = useDemandsStore()
    await demands.createDemand(categoryId.value!, description.value)
    emit('success')
  } catch {
    serverError.value = 'Erro ao registrar demanda. Tente novamente.'
  } finally {
    loading.value = false
  }
}
</script>