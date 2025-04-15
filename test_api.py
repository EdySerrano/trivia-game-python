from fastapi.testclient import TestClient
from trivia import app

client = TestClient(app)

def test_get_easy_questions():
    response = client.get("/questions/easy")
    assert response.status_code == 200
    assert len(response.json()) == 10
    assert "description" in response.json()[0]

def test_get_medium_questions():
    response = client.get("/questions/medium")
    assert response.status_code == 200
    assert len(response.json()) == 10

def test_get_hard_questions():
    response = client.get("/questions/hard")
    assert response.status_code == 200
    assert len(response.json()) == 10
