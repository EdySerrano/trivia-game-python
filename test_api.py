from fastapi.testclient import TestClient
from trivia import app

client = TestClient(app)

def test_create_question():
    response = client.post("/questions/", json={
        "description": "What is 2 + 2?",
        "options": ["1", "2", "3", "4"],
        "correct_answer": "4"
    })
    assert response.status_code == 201

def test_get_question():
    response = client.get("/questions/1")
    assert response.status_code == 200
    assert response.json()["description"] == "What is 2 + 2?"
