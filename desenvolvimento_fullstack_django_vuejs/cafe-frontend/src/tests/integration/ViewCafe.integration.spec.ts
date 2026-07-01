import { mount } from '@vue/test-utils'
import ViewCafe from '../../views/ViewCafe.vue'
import api from '@/services/api'
import { describe, it, expect, vi } from 'vitest'

const mockCafe = {
    id: 1,
    nome: 'Café Teste',
    data_inauguracao: '2023-07-20',
    endereco: 'Rua Teste, 123',
    avaliacao: 8.5,
}

vi.mock('@/services/api', () => ({
    default: {
        get: vi.fn(() => Promise.resolve({ data: mockCafe })),
    },
}))

vi.mock('vue-router', () => ({
    useRoute: () => ({
        params: { id: '1' },
    }),
}))

describe('ViewCafe - teste de integração', () => {
    it('exibe os detalhes da cafeteria corretamente', async () => {
        const wrapper = mount(ViewCafe, {
            global: {
                stubs: ['router-link'],
            },
        })

        await wrapper.vm.$nextTick()
        await wrapper.vm.$nextTick()

        expect(wrapper.text()).toContain('Café Teste')
        expect(wrapper.text()).toContain('20/07/2023')
        expect(wrapper.text()).toContain('Rua Teste, 123')
        expect(wrapper.text()).toContain('8.5')
    })
})