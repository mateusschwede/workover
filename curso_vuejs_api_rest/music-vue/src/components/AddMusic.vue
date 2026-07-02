<template>
    <h1>Adicionar Música</h1>
    <form @submit.prevent="addMusic">
        <input type="text" placeholder="Título" v-model="newMusic.title" required>
        <input type="text" placeholder="Artista" v-model="newMusic.artist" required>
        <button type="submit">Confirmar</button>
        <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
    </form>
    <button @click="goBack">Cancelar</button>
</template>

<script>
import { ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

export default {
    setup() {
        const newMusic = ref({ title: '', artist: '' });
        const errorMessage = ref('');
        const router = useRouter();

        const addMusic = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/musics/', {
                    params: {
                        title: newMusic.value.title,
                        artist: newMusic.value.artist,
                    },
                });

                const musicExists = response.data.some(
                    (music) =>
                        music.title === newMusic.value.title &&
                        music.artist === newMusic.value.artist
                );

                if (musicExists) {
                    errorMessage.value = 'Música já cadastrada';
                } else {
                    await axios.post('http://localhost:8000/api/musics/', newMusic.value);
                    router.push({ name: 'list-music' });
                }
            } catch (error) {
                console.error("Erro ao adicionar música", error);
                errorMessage.value = 'Erro ao adicionar música';
            }
        };

        const goBack = () => {
            router.push({ name: 'list-music' });
        };

        return {
            newMusic,
            errorMessage,
            addMusic,
            goBack,
        };
    },
};
</script>

<style scoped></style>