from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

from main import app


client = TestClient(app)

def test_health_api():
    response = client.get('/')
    assert response.status_code == 200  # Check if response status is 200 OK
    assert response.json() == {"message": "this id CI/CD from backend !!!!"}  # Validate response body

    # Print response content (optional)
    print("\n\n\n here after api calling --> \n",response.json(), response.status_code, "\n------api calling")