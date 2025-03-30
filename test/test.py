from fastapi.testclient import TestClient
import sys
import os

# Ensure the main app module is correctly imported
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/.."))

from main import app  # Import the FastAPI app

client = TestClient(app)

def test_health_api():
    """Test the health check endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"message": "Server is running", "status": "200"}
    print("\nHealth API Response:", response.json())

def test_get_data_empty():
    """Test retrieving data when the store is empty"""
    response = client.get('/getData')
    assert response.status_code == 200
    assert response.json() == {'message': 'Data retrieved successfully', 'data': []}
    print("\nGet Data Empty Response:", response.json())

def test_insert_data():
    """Test inserting valid data"""
    payload = {
        "name": "Test Product",
        "description": "A sample product",
        "price": 99.99
    }
    response = client.post('/insert', json=payload)
    assert response.status_code == 200
    assert response.json()["message"] == "Data inserted successfully"
    assert len(response.json()["data"]) == 1  # Ensure data is added
    print("\nInsert API Response:", response.json())

def test_get_data_after_insert():
    """Test retrieving data after inserting an entry"""
    response = client.get('/getData')
    assert response.status_code == 200
    assert len(response.json()["data"]) == 1  # Data store should have 1 entry
    print("\nGet Data After Insert Response:", response.json())

def test_insert_duplicate_data():
    """Test inserting duplicate data (should still allow duplicates in this implementation)"""
    payload = {
        "name": "Test Product",
        "description": "A sample product",
        "price": 99.99
    }
    response = client.post('/insert', json=payload)
    assert response.status_code == 200
    assert len(response.json()["data"]) == 2  # Second entry should be added
    print("\nInsert Duplicate API Response:", response.json())

def test_insert_invalid_data():
    """Test inserting invalid data (missing required field)"""
    payload = {
        "description": "No name field",
        "price": 49.99
    }
    response = client.post('/insert', json=payload)
    assert response.status_code == 422  # Unprocessable Entity
    print("\nInsert Invalid Data Response:", response.json())
