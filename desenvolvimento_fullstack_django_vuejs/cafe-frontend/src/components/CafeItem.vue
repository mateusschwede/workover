<template>
    <b-card class="mb-2">
        <div class="d-flex justify-content-between align-items-center">
            <div>
                <h5>{{ cafe.nome }}</h5>
                <p class="mb-0">Avaliação: {{ cafe.avaliacao }}/10</p>
            </div>
            <div>
                <router-link :to="`/view/${cafe.id}`" class="btn btn-sm btn-primary me-1">Ver</router-link>
                <router-link :to="`/edit/${cafe.id}`" class="btn btn-sm btn-warning me-1">Editar</router-link>
                <b-button size="sm" variant="danger" @click="$emit('delete', cafe.id)">Deletar</b-button>
            </div>
        </div>
    </b-card>
</template>

<script setup lang="ts">
defineProps<{ cafe: any }>()
defineEmits(['delete'])
</script>