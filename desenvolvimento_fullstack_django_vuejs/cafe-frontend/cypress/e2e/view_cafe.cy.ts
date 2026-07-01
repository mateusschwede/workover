describe('Visualização de uma cafeteria', () => {
    it('deve exibir os detalhes corretamente', () => {
        cy.visit('http://localhost:5173/view/2') // Necessário alterar ID da cafeteria conforme possuir no banco de dados
        cy.contains('Cafeteria 2:')
        cy.contains('Nome:')
        cy.contains('Avaliação:')
        cy.contains('/10')
        cy.get('a').contains('Voltar').click()
        cy.url().should('eq', 'http://localhost:5173/')
    })
})