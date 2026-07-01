import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import AddCafe from '../views/AddCafe.vue'
import EditCafe from '../views/EditCafe.vue'
import ViewCafe from '../views/ViewCafe.vue'

const routes = [
    { path: '/', name: 'Home', component: Home },
    { path: '/add', name: 'AddCafe', component: AddCafe },
    { path: '/edit/:id', name: 'EditCafe', component: EditCafe },
    { path: '/view/:id', name: 'ViewCafe', component: ViewCafe }
]

export default createRouter({
    history: createWebHistory(),
    routes
})