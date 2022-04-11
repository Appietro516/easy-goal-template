from fastapi.testclient import TestClient

from app import app


def test_is_working():
    print("Testing that unit testing is working")
    assert True is True

def test_read_root():
    print("Testing Read Root")
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to this fantastic app."}

def test_get_goals():
    print("Testing getting goals")
    client = TestClient(app)
    response = client.get("/goal")
    assert response.status_code == 200

def test_get_progress():
    print("Testing getting progress")
    client = TestClient(app)
    response = client.get("/progress")
    assert response.status_code == 200

def test_show_failure():
    print("Demonstrating failed test")
    client = TestClient(app)
    response = client.get("/not_an_endpoint")
    print(f"Test returned:\n {response.json()}")
    assert response.status_code == 200