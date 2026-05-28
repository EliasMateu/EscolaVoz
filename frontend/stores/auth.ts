import { defineStore } from 'pinia'
import type { AuthResponse } from '~/types/auth'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    accessToken: null as string | null,
    refreshToken: null as string | null,
    profile: null as 'admin' | 'funcionario' | null,
    schoolId: null as number | null,
  }),

  getters: {
    isAuthenticated: (state) => !!state.accessToken,
    isAdmin: (state) => state.profile === 'admin',
    isFuncionario: (state) => state.profile === 'funcionario',
  },

  actions: {
    setAuth(data: AuthResponse) {
      this.accessToken = data.access
      this.refreshToken = data.refresh
      this.profile = data.profile
      this.schoolId = data.school_id
      if (import.meta.client) {
        localStorage.setItem('auth', JSON.stringify({
          access: data.access,
          refresh: data.refresh,
          profile: data.profile,
          schoolId: data.school_id,
        }))
      }
    },

    async login(username: string, password: string) {
      const api = useApi()
      const { data } = await api.post<AuthResponse>('/auth/login/', { username, password })
      this.setAuth(data)
    },

    logout() {
      this.accessToken = null
      this.refreshToken = null
      this.profile = null
      this.schoolId = null
      if (import.meta.client) {
        localStorage.removeItem('auth')
      }
    },

    restoreFromStorage() {
      if (import.meta.client) {
        const stored = localStorage.getItem('auth')
        if (stored) {
          const data = JSON.parse(stored)
          this.accessToken = data.access
          this.refreshToken = data.refresh
          this.profile = data.profile
          this.schoolId = data.schoolId
        }
      }
    },
  },
})