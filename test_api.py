from fastapi.testclient import TestClient
from trivia import app

client = TestClient(app)

def test_create_and_get_question():
   
    create_response = client.post("/questions/", json={
        "description": "What is 2 + 2?",
        "options": ["1", "2", "3", "4"],
        "correct_answer": "4"
    })
    assert create_response.status_code == 201
    assert create_response.json() == {"message": "Question created"}

   
    get_response = client.get("/questions/1")
    assert get_response.status_code == 200
    question = get_response.json()
    assert question["description"] == "What is 2 + 2?"
    assert "4" in question["options"]
