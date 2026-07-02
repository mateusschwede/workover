<template>
    <h1>Editar música</h1>
    <form @submit.prevent="submitEdit">
        <input type="text" placeholder="Título" v-model="music.title" required>
        <input type="text" placeholder="Artista" v-model="music.artist" required>
        <button type="submit">Confirmar</button>
        <button @click="cancelEdit">Cancelar</button>
    </form>

    <div v-if="errorMessage" class="error">{{ errorMessage }}</div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRoute, useRouter } from 'vue-router';

export default {
    setup() {
        const music = ref({ title: '', artist: '' });
        const originalMusic = ref({ title: '', artist: '' });
        const errorMessage = ref('');
        const router = useRouter();
        const route = useRoute();
        const musicId = route.params.id;
        const musics = ref([]);

        const fetchMusics = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/musics/');
                musics.value = response.data;
            } catch (error) {
                console.error('Erro ao buscar música', error);
            }
        };

        const fetchMusic = async () => {
            try {
                const response = await axios.get(`http://localhost:8000/api/musics/${musicId}/`);
                music.value = response.data;
                originalMusic.value = { ...response.data };
            } catch (error) {
                console.error('Erro ao buscar música', error);
            }
        };

        const validateMusic = () => {
            if (music.value.title === originalMusic.value.title && music.value.artist === originalMusic.value.artist) {
                return true;
            }

            const existingMusic = musics.value.find(
                (m) => m.title === music.value.title && m.artist === music.value.artist && m.id !== musicId
            );
            if (existingMusic) {
                errorMessage.value = 'Música já cadastrada';
                return false;
            }

            errorMessage.value = '';
            return true;
        };

        const submitEdit = async () => {
            if (!validateMusic()) {
                return;
            }

            try {
                await axios.put(`http://localhost:8000/api/musics/${musicId}/`, music.value);
                router.push({ name: 'list-music' });
            } catch (error) {
                console.error('Erro ao editar música', error);
            }
        };

        const cancelEdit = () => {
            router.push({ name: 'list-music' });
        };

        onMounted(() => {
            fetchMusics();
            fetchMusic();
            
        });

        return {
            music,
            errorMessage,
            submitEdit,
            cancelEdit,
        };
    },
};
</script>

<style scoped></style>