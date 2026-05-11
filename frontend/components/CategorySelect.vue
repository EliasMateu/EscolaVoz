<template>
  <select v-model="modelValue" class="w-full px-3 py-2 border rounded-md">
    <option :value="null" disabled>Selecione uma categoria</option>
    <option v-for="cat in categories" :key="cat.id" :value="cat.id">
      {{ cat.name }}
    </option>
  </select>
</template>

<script setup lang="ts">
const props = defineProps<{ modelValue: number | null }>()
const emit = defineEmits<{ 'update:modelValue': [value: number] }>()

const modelValue = computed({
  get: () => props.modelValue,
  set: (v) => emit('update:modelValue', v as number),
})

const catStore = useCategoriesStore()
const categories = computed(() => catStore.categories)
onMounted(() => catStore.fetchCategories())
</script>