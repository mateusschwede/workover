<template>
    <div class="confirm-dialog">
        <p>Excluir música "{{ music.title }}" (id: {{ music.id }})?</p>
        <button @click="cancel">Cancelar</button>
        <button @click="confirm">Confirmar</button>
    </div>
</template>

<script>
export default {
    props: {
        music: {
            type: Object,
            required: true
        }
    },
    methods: {
        cancel() {
            this.$emit('cancel');
        },
        confirm() {
            this.$emit('confirm', this.music.id);
        }
    }
};
</script>

<style scoped></style>