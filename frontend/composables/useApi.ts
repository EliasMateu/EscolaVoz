import axios, { type AxiosInstance } from 'axios'
import { useAuthStore } from '~/frontend/stores/auth'

export function useApi(): AxiosInstance {
  const config = useRuntimeConfig()
  const auth = useAuthStore()

  const api = axios.create({
    baseURL: `${config.public.apiUrl}/api`,
    headers: { 'Content-Type': 'application/json' },
  })

  api.interceptors.request.use((config) => {
    if (auth.accessToken) {
      config.headers.Authorization = `Bearer ${auth.accessToken}`
    }
    return config
  })

  api.interceptors.response.use(
    (response) => response,
    (error) => {
      if (error.response?.status === 401) {
        auth.logout()
        navigateTo('/login')
      }
      return Promise.reject(error)
    }
  )

  return api
}