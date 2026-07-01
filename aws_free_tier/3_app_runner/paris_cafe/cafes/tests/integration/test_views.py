import pytest
from rest_framework.test import APIClient
from model_bakery import baker

@pytest.mark.django_db
def test_lista_cafeterias():
    baker.make("cafes.Cafeteria", _quantity=3)
    client = APIClient()
    response = client.get("/cafes/")
    assert response.status_code == 200
    assert len(response.data) == 3

@pytest.mark.django_db
def test_cria_cafeteria_api():
    client = APIClient()
    data = {
        "nome": "API Café",
        "data_inauguracao": "2023-06-15",
        "endereco": "Avenida API, 789",
        "avaliacao": 7.2,
    }
    response = client.post("/cafes/", data=data, format='json')
    assert response.status_code == 201
    assert response.data["nome"] == "API Café"