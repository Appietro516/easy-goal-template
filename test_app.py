from fastapi.testclient import TestClient

from app import app

client = TestClient(app)

def test_dummy():
    assert True is True