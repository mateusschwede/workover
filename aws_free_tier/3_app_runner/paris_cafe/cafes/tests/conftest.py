import pytest
from model_bakery import baker

@pytest.fixture
def cafe():
    return baker.make("cafes.Cafeteria")