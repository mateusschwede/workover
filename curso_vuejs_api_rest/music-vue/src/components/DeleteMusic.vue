<template>
    <h1>Exclusão</h1>
    <p>Excluir música?</p>
    <p>Id: {{ music.id }}</p>
    <p>Título: {{ music.title }}</p>
    <p>Artista: {{ music.artist }}</p>
    <button @click="confirmDelete">Confirmar</button>
    <button @click="cancel">Cancelar</button>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

export default {
    setup() {
        const router = useRouter();
        const music = ref({});
        const musicId = router.currentRoute.value.params.id;

        const fetchMusicDetails = async () => {
            try {
                const response = await axios.get(`http://localhost:8000/api/musics/${musicId}/`);
                music.value = response.data;
            } catch (error) {
                console.error('Erro ao buscar dados da música:', error);
            }
        };

        const confirmDelete = async () => {
            try {
                await axios.delete(`http://localhost:8000/api/musics/${musicId}/`);
                router.push({ name: 'list-music' });
            } catch (error) {
                console.error('Erro ao excluir música:', error);
            }
        };

        const cancel = () => {
            router.push({ name: 'list-music' });
        };

        onMounted(fetchMusicDetails);
        return {
            music,
            confirmDelete,
            cancel,
        };
    },
};
</script>

<style scoped></style>