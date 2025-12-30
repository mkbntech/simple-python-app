import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    """Test the base route returns 200 and the correct message."""
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Hello from Python inside Kubernetes!" in rv.data