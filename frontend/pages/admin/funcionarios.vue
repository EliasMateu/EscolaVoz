<template>
  <div>
    <h1 class="text-2xl font-bold text-primary mb-6">Funcionários</h1>
    <div class="bg-white p-6 rounded-lg shadow mb-6">
      <h2 class="font-semibold mb-4">Cadastrar Novo Funcionário</h2>
      <form @submit.prevent="handleCreate" class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <input v-model="form.username" placeholder="Username *" class="px-3 py-2 border rounded-md" required />
        <input v-model="form.email" type="email" placeholder="Email *" class="px-3 py-2 border rounded-md" required />
        <input v-model="form.password" type="password" placeholder="Senha *" class="px-3 py-2 border rounded-md" required />
        <input v-model="form.role" placeholder="Cargo *" class="px-3 py-2 border rounded-md" required />
        <select v-model="form.school_id" class="px-3 py-2 border rounded-md" required>
          <option :value="null" disabled>Selecione a escola *</option>
          <option v-for="s in schools" :key="s.id" :value="s.id">{{ s.name }}</option>
        </select>
        <label class="flex items-center gap-2">
          <input type="checkbox" v-model="form.is_admin" class="w-4 h-4" />
          Admin?
        </label>
        <button type="submit" class="bg-primary text-white px-4 py-2 rounded-md col-span-full">
          Cadastrar
        </button>
      </form>
    </div>
    <DataTable :demands="employees" :loading="empLoading" :editable="false" />
  </div>
</template>

<script setup lang="ts">
const api = useApi()
const schoolsStore = useSchoolsStore()
const schools = computed(() => schoolsStore.schools)
const employees = ref<any[]>([])
const empLoading = ref(false)
const form = reactive({
  username: '',
  email: '',
  password: '',
  role: '',
  school_id: null as number | null,
  is_admin: false,
})

onMounted(async () => {
  schoolsStore.fetchSchools()
  empLoading.value = true
  try {
    const { data } = await api.get('/employees/')
    employees.value = data.data?.results || []
  } finally {
    empLoading.value = false
  }
})

async function handleCreate() {
  await api.post('/employees/', form)
  location.reload()
}
</script>