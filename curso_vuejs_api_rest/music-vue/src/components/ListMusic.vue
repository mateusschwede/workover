<template>
    <div v-if="musics.length === 0">
        <p>Não há músicas disponíveis.</p>
    </div>

    <ul v-else>
        <li v-for="music in musics" :key="music.id">
            <div v-if="!confirmingMusicId || confirmingMusicId !== music.id">
                Id: {{ music.id }}
                Título: {{ music.title }}
                Artista: {{ music.artist }}
                <button @click="viewMusic(music.id)">Ver</button>
                <button @click="goToEditMusic(music.id)">Editar</button>
                <button @click="goToDeleteMusic(music.id)">Excluir</button>
                <button @click="startConfirmDelete(music.id)">ExcluirDiretamente</button>
            </div>

            <ConfirmDialogDelete v-if="confirmingMusicId === music.id" :music="music" @cancel="cancelDelete" @confirm="confirmDelete" />
        </li>
    </ul>

    <button @click="goToAddMusic">Adicionar música</button>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import ConfirmDialogDelete from './ConfirmDialogDelete.vue';

export default {
    components: {
        ConfirmDialogDelete
    },
    setup() {
        const musics = ref([]);
        const confirmingMusicId = ref(null);
        const router = useRouter();

        const fetchMusics = async () => {
            try {
                const response = await axios.get('http://localhost:8000/api/musics/');
                musics.value = response.data;
            } catch (error) {
                console.error('Erro ao buscar música', error);
            }
        };

        onMounted(fetchMusics);

        const viewMusic = (id) => {
            router.push({ name: 'music-detail', params: { id } });
        };

        const goToDeleteMusic = (id) => {
            router.push({ name: 'delete-music', params: { id } });
        };

        const goToEditMusic = (id) => {
            router.push({ name: 'edit-music', params: { id } });
        };

        const goToAddMusic = () => {
            router.push({ name: 'add-music' });
        };

        const startConfirmDelete = (id) => {
            confirmingMusicId.value = id;
        };

        const cancelDelete = () => {
            confirmingMusicId.value = null;
        };

        const confirmDelete = async (id) => {
            try {
                await axios.delete(`http://localhost:8000/api/musics/${id}/`);
                musics.value = musics.value.filter((music) => music.id !== id);
                confirmingMusicId.value = null;
            } catch (error) {
                console.error('Erro ao excluir música', error);
            }
        };

        return {
            musics,
            confirmingMusicId,
            viewMusic,
            goToDeleteMusic,
            goToEditMusic,
            goToAddMusic,
            startConfirmDelete,
            cancelDelete,
            confirmDelete,
        };
    },
};
</script>

<style scoped></style>