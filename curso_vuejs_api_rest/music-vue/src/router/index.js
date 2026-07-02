import { createRouter, createWebHistory } from "vue-router";
import ListMusic from '../components/ListMusic.vue';
import ShowMusic from '../components/ShowMusic.vue';
import EditMusic from '../components/EditMusic.vue';
import AddMusic from '../components/AddMusic.vue';
import DeleteMusic from '../components/DeleteMusic.vue';

const routes = [
    {
        path: '/',
        name: 'list-music',
        component: ListMusic,
    },
    {
        path: '/music/:id',
        name: 'music-detail',
        component: ShowMusic,
    },
    {
        path: '/edit/:id',
        name: 'edit-music',
        component: EditMusic,
    },
    {
        path: '/add',
        name: 'add-music',
        component: AddMusic,
    },
    {
        path: '/delete/:id',
        name: 'delete-music',
        component: DeleteMusic,
    },
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;