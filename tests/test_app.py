from fastapi.testclient import TestClient
from app_customer.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenue dans l'API d'analyse de satisfaction client"}

def test_analyze():
    response = client.post("/predict/", json={"text": "This product is amazing!"})
    assert response.status_code == 200
    assert "sentiment" in response.json()
    assert "score" in response.json()
