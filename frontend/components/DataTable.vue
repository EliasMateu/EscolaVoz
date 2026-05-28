<template>
  <div class="overflow-x-auto bg-white rounded-lg shadow">
    <div v-if="loading" class="text-center py-8">Carregando...</div>
    <table v-else class="w-full text-sm">
      <thead class="bg-gray-50 border-b">
        <tr>
          <th class="px-4 py-3 text-left">Escola</th>
          <th class="px-4 py-3 text-left">Categoria</th>
          <th class="px-4 py-3 text-left">Descrição</th>
          <th class="px-4 py-3 text-left">Status</th>
          <th class="px-4 py-3 text-left">Data</th>
          <th v-if="editable" class="px-4 py-3 text-left">Ação</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="d in demands" :key="d.id" class="border-b hover:bg-gray-50">
          <td class="px-4 py-3">{{ d.school_name }}</td>
          <td class="px-4 py-3">{{ d.category_name }}</td>
          <td class="px-4 py-3 max-w-xs truncate">{{ d.description }}</td>
          <td class="px-4 py-3"><StatusBadge :status="d.status" /></td>
          <td class="px-4 py-3">{{ formatDate(d.created_at) }}</td>
          <td v-if="editable" class="px-4 py-3">
            <select
              :value="d.status"
              @change="emit('update-status', d.id, ($event.target as HTMLSelectElement).value)"
              class="text-xs border rounded px-1 py-0.5"
            >
              <option value="open">Aberta</option>
              <option value="in_progress">Em Andamento</option>
              <option value="resolved">Resolvida</option>
              <option value="rejected">Rejeitada</option>
            </select>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup lang="ts">
import type { Demand } from '~/types/demand'

defineProps<{ demands: Demand[]; loading: boolean; editable?: boolean }>()
const emit = defineEmits<{ 'update-status': [id: number, status: string] }>()
function formatDate(d: string) { return new Date(d).toLocaleDateString('pt-BR') }
</script>