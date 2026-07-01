from cafes.serializers import CafeteriaSerializer

def test_cafe_serializer_valid_data():
    data = {
        "nome": "Café Central",
        "data_inauguracao": "2021-01-01",
        "endereco": "Av. Principal, 456",
        "avaliacao": 8.7
    }
    serializer = CafeteriaSerializer(data=data)
    assert serializer.is_valid()
    assert serializer.validated_data["nome"] == "Café Central"