<script setup lang="ts">
const auth = useAuthStore()
auth.restoreFromStorage()
if (!auth.isAuthenticated) {
  await navigateTo('/login')
} else {
  await navigateTo(auth.isAdmin ? '/admin/dashboard' : '/funcionario/demandas')
}
</script>