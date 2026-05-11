<template>
  <span :class="badgeClass" class="px-2 py-1 rounded-full text-xs font-medium">
    {{ label }}
  </span>
</template>

<script setup lang="ts">
import type { DemandStatus } from '~/types/demand'

const props = defineProps<{ status: DemandStatus }>()

const labels: Record<DemandStatus, string> = {
  open: 'Aberta',
  in_progress: 'Em Andamento',
  resolved: 'Resolvida',
  rejected: 'Rejeitada',
}

const classes: Record<DemandStatus, string> = {
  open: 'bg-blue-100 text-blue-800',
  in_progress: 'bg-yellow-100 text-yellow-800',
  resolved: 'bg-green-100 text-green-800',
  rejected: 'bg-red-100 text-red-800',
}

const label = computed(() => labels[props.status])
const badgeClass = computed(() => classes[props.status])
</script>