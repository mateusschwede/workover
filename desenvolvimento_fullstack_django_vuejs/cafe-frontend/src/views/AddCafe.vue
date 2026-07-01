<template>
    <div class="container mt-4">
        <h2>Adicionar Cafeteria:</h2>
        <b-form @submit.prevent="addCafe">
            <b-form-input v-model="form.nome" placeholder="Nome" name="nome" class="mb-2" maxlength="255" required />
            <b-form-input v-model="form.data_inauguracao" type="date" name="data_inauguracao" class="mb-2" :max="new Date().toLocaleDateString('sv-SE')" required />
            <b-form-textarea v-model="form.endereco" placeholder="Endereço" name="endereco" class="mb-2" maxlength="255" required />
            <b-form-input v-model.number="form.avaliacao" type="number" step="0.01" min="0" max="10" name="avaliacao" class="mb-2"
                required />
            <b-button type="submit" variant="success" class="me-2">Confirmar</b-button>
            <router-link to="/" class="btn btn-secondary">Cancelar</router-link>
        </b-form>
    </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '../services/api'

const router = useRouter()
const form = ref({ nome: '', data_inauguracao: '', endereco: '', avaliacao: 0 })

const addCafe = async () => {
    await api.post('cafes/', form.value)
    router.push('/')
}
</script>