<template>
  <div class="bg-white p-4 rounded-lg shadow-sm border border-gray-200">
    <div class="flex justify-between items-start mb-2">
      <span class="font-semibold text-primary">{{ demand.category_name }}</span>
      <StatusBadge :status="demand.status" />
    </div>
    <p class="text-gray-600 text-sm mb-2">{{ demand.description || 'Sem descrição' }}</p>
    <span class="text-xs text-gray-400">{{ formatDate(demand.created_at) }}</span>
  </div>
</template>

<script setup lang="ts">
import type { Demand } from '~/frontend/types/demand'

defineProps<{ demand: Demand }>()

function formatDate(d: string) {
  return new Date(d).toLocaleDateString('pt-BR')
}
</script>