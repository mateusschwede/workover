import { mount } from '@vue/test-utils'
import ViewCafe from '../../views/ViewCafe.vue'
import { describe, it, expect, vi } from 'vitest'
import { createMemoryHistory, createRouter } from 'vue-router'
import api from '@/services/api'

vi.mock('@/services/api')

const mockCafe = {
    id: 1,
    nome: 'Café de Flore',
    data_inauguracao: '1887-01-01',
    endereco: '172 Boulevard Saint-Germain, Paris',
    avaliacao: 9.5,
}

const router = createRouter({
    history: createMemoryHistory(),
    routes: [{ path: '/view/:id', component: ViewCafe }],
})

describe('ViewCafe.vue', () => {
    it('exibe detalhes da cafeteria', async () => {
        (api.get as any).mockResolvedValue({ data: mockCafe })

        router.push('/view/1')
        await router.isReady()

        const wrapper = mount(ViewCafe, {
            global: {
                plugins: [router],
            },
        })

        await new Promise(resolve => setTimeout(resolve, 0))
        expect(wrapper.text()).toContain('Café de Flore')
        expect(wrapper.text()).toContain('1887')
        expect(wrapper.text()).toContain('172 Boulevard Saint-Germain')
        expect(wrapper.text()).toContain('9.5')
    })
})