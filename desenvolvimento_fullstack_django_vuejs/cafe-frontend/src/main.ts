import { createApp } from "vue";
import App from './App.vue';
import router from './router';
import * as BootstrapVueNext from 'bootstrap-vue-next';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css';

import {
    BButton,
    BForm,
    BFormInput,
    BFormTextarea,
    BCard
} from 'bootstrap-vue-next';

const app = createApp(App);
app.use(router);
app.component('BButton', BButton);
app.component('BForm', BForm);
app.component('BFormInput', BFormInput);
app.component('BFormTextarea', BFormTextarea);
app.component('BCard', BCard);
app.mount('#app');