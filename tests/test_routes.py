import json
import pytest
from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config['TESTING'] = True
    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_calculate_distance(client):
    # Test a case where the address is inside MKAD
    response = client.get('/mkad/calculate_distance/Moscow')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert 'message' in data
    assert data['message'] == 'Address is inside MKAD'

    # Test a case where the address is outside MKAD
    response = client.get('/mkad/calculate_distance/Saratov')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert 'distance_km' in data

def test_calculate_distance_invalid_address(client):
    # Test a case where the address is not found
    response = client.get('/mkad/calculate_distance/zagundyaevskogo')
    data = json.loads(response.data)
    assert response.status_code == 404
    assert 'error' in data

def test_get_mkad(client):
    response = client.get('/mkad/')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert 'mkad_points' in data
    assert isinstance(data['mkad_points'], list)
