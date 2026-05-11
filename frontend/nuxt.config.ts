export default defineNuxtConfig({
  modules: ['@nuxtjs/tailwindcss', '@pinia/nuxt'],
  runtimeConfig: {
    public: {
      apiUrl: process.env.NUXT_PUBLIC_API_URL || 'http://localhost:8000',
    },
  },
  ssr: false,
  devtools: { enabled: false },
  tailwindcss: {
    configPath: 'frontend/tailwind.config.ts',
  },
})