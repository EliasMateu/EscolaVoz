import { defineStore } from 'pinia'
import type { Demand, DemandCreate, PaginatedResponse } from '~/frontend/types/demand'

export const useDemandsStore = defineStore('demands', {
  state: () => ({
    demands: [] as Demand[],
    loading: false,
    total: 0,
  }),

  actions: {
    async fetchMyDemands() {
      this.loading = true
      try {
        const api = useApi()
        const { data } = await api.get<PaginatedResponse<Demand>>('/demands/my/')
        this.demands = data.results
        this.total = data.count
      } finally {
        this.loading = false
      }
    },

    async createDemand(categoryId: number, description: string) {
      const api = useApi()
      const payload: DemandCreate = { category: categoryId, description }
      const { data } = await api.post<Demand>('/demands/', payload)
      this.demands.unshift(data)
      return data
    },

    async fetchAllDemands(filters: Record<string, string> = {}) {
      this.loading = true
      try {
        const api = useApi()
        const params = new URLSearchParams(filters).toString()
        const { data } = await api.get<PaginatedResponse<Demand>>(`/demands/?${params}`)
        this.demands = data.results
        this.total = data.count
      } finally {
        this.loading = false
      }
    },

    async updateDemandStatus(id: number, status: string) {
      const api = useApi()
      await api.patch(`/demands/${id}/`, { status })
    },
  },
})