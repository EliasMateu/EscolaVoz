export default defineNuxtPlugin(() => {
  const auth = useAuthStore()
  auth.restoreFromStorage()

  const router = useRouter()
  router.beforeEach((to) => {
    const publicRoutes = ['/login']
    if (!auth.isAuthenticated && !publicRoutes.includes(to.path)) {
      return navigateTo('/login')
    }
    if (auth.isAuthenticated && to.path === '/login') {
      return navigateTo(auth.isAdmin ? '/admin/dashboard' : '/funcionario/demandas')
    }
  })
})