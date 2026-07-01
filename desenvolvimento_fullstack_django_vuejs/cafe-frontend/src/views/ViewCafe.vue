<template>
    <div class="container mt-4">
        <h2 class="mb-3">Cafeteria {{ cafe?.id }}:</h2>
        <p><strong>Nome:</strong> {{ cafe?.nome }}</p>
        <p><strong>Inauguração:</strong> {{ cafe?.data_inauguracao.split('-').reverse().join('/') }}</p>
        <p><strong>Endereço:</strong> {{ cafe?.endereco }}</p>
        <p><strong>Avaliação:</strong> {{ cafe?.avaliacao }}/10</p>
        <router-link to="/" class="btn btn-secondary mt-2">Voltar</router-link>
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import api from '../services/api'

const cafe = ref<any>(null)
const route = useRoute()

onMounted(async () => {
    const { data } = await api.get(`cafes/${route.params.id}/`)
    cafe.value = data
})
</script>