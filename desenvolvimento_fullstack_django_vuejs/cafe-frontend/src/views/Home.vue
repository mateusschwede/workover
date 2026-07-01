<template>
    <div class="container mt-4">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1>Cafés de Paris</h1>
            <div>
                <router-link to="/add" class="btn btn-success">Adicionar Cafeteria</router-link>
            </div>
        </div>
        <button class="btn btn-sm btn-info me-2 mb-2" @click="toggleOrdenacao">
            {{ ordenado ? 'Ordenação original' : 'Ordenar por avaliação' }}
        </button>
        <CafeItem v-for="cafe in cafes" :key="cafe.id" :cafe="cafe" @delete="deleteCafe" />
    </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import api from '../services/api'
import CafeItem from '../components/CafeItem.vue'

const cafes = ref<any[]>([])
const cafesOriginais = ref<any[]>([])
const ordenado = ref(false)

const fetchCafes = async () => {
    const { data } = await api.get('cafes/')
    cafesOriginais.value = [...data]
    cafes.value = [...data]
}

const deleteCafe = async (id: number) => {
    await api.delete(`cafes/${id}/`)
    await fetchCafes()
    if (ordenado.value) {
        ordenarPorAvaliacao()
    }
}

const ordenarPorAvaliacao = () => {
    cafes.value = [...cafes.value].sort((a, b) => b.avaliacao - a.avaliacao)
}

const toggleOrdenacao = () => {
    if (!ordenado.value) {
        ordenarPorAvaliacao()
    } else {
        cafes.value = [...cafesOriginais.value]
    }
    ordenado.value = !ordenado.value
}

onMounted(fetchCafes)
</script>