<template>
  <div class="max-w-xl">
    <h1 class="text-2xl font-bold text-primary mb-6">Registrar Nova Demanda</h1>
    <div class="bg-white p-6 rounded-lg shadow">
      <DemandForm @success="navigateTo('/funcionario/demandas')" />
    </div>
  </div>
</template>