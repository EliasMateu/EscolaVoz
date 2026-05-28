import { defineStore } from 'pinia'
import type { School, DemandCategory } from '~/types/core'

export const useSchoolsStore = defineStore('schools', {
  state: () => ({
    schools: [] as School[],
    loading: false,
  }),

  actions: {
    async fetchSchools() {
      this.loading = true
      try {
        const api = useApi()
        const { data } = await api.get<{ results: School[] }>('/schools/')
        this.schools = data.results
      } finally {
        this.loading = false
      }
    },
  },
})

export const useCategoriesStore = defineStore('categories', {
  state: () => ({
    categories: [] as DemandCategory[],
    loading: false,
  }),

  actions: {
    async fetchCategories() {
      this.loading = true
      try {
        const api = useApi()
        const { data } = await api.get<{ results: DemandCategory[] }>('/categories/')
        this.categories = data.results
      } finally {
        this.loading = false
      }
    },
  },
})