import pytest
from cafes.models import Cafeteria

@pytest.mark.django_db
def test_cria_cafeteria():
    cafe = Cafeteria.objects.create(
        nome="Café do Centro",
        data_inauguracao="2020-01-01",
        endereco="Rua Principal, 123",
        avaliacao=9.5,
    )
    assert cafe.nome == "Café do Centro"
    assert cafe.avaliacao == 9.5