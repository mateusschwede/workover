<template>
    <h1>Música:</h1>
    <p>Id: {{ music.id }}</p>
    <p>Título: {{ music.title }}</p>
    <p>Artista: {{ music.artist }}</p>
    <button @click="goBack">Voltar</button>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

export default {
    setup() {
        const music = ref({});
        const router = useRouter();
        const musicId = router.currentRoute.value.params.id;

        const fetchMusicDetails = async () => {
            try {
                const response = await axios.get(`http://localhost:8000/api/musics/${musicId}/`);
                music.value = response.data;
            } catch (error) {
                console.error("Erro ao buscar dados da música:", error);
            }
        };

        onMounted(fetchMusicDetails);

        const goBack = () => {
            router.push({ name: 'list-music' });
        };
        return {
            music,
            goBack,
        };
    },
};
</script>

<style scoped></style>