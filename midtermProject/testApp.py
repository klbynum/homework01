import pytest
from main import main

@pytest.fixture
def client():
    with main.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Welcome to the ISS API" in response.json