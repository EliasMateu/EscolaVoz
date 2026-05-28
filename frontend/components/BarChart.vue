<template>
  <Bar :data="chartData" :options="chartOptions" />
</template>

<script setup lang="ts">
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale,
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

const props = defineProps<{
  labels: string[]
  datasets: { label: string; data: number[]; backgroundColor: string }[]
}>()

const chartData = computed(() => ({
  labels: props.labels,
  datasets: props.datasets.map((d) => ({
    ...d,
    borderRadius: 4,
  })),
}))

const chartOptions = {
  responsive: true,
  plugins: {
    legend: { position: 'top' as const },
    title: { display: false },
  },
  scales: {
    y: { beginAtZero: true, ticks: { stepSize: 1 } },
  },
}
</script>