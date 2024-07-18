from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_api_v1():
    response = client.get("/api/v1")
    assert response.status_code == 200
    assert response.json().get('data') == {"message": "API V1"}

def test_api_v2():
    response = client.get("/api/v2")
    assert response.status_code == 200
    assert response.json().get('data') == {"message": "API V2"}