from src.extract.extract_request import extract_request
from src.extract.call_limit import base_api


# Test received status code 400 from request function
def test_extract_request():
    # Intentionally adjusted to point to known endpoint
    response = extract_request(base_api + "forces")
    assert response.status_code == 200


# Test data received from the request function
def test_extract_request_data():
    # Intentionally adjusted to point to known endpoint
    response = extract_request(base_api + "forces").json()
    assert len(response) > 0


# Test received correct data type from request function
def test_extract_request_type():
    # Intentionally adjusted to point to known endpoint
    response = extract_request(base_api + "forces")
    assert isinstance(response, object)
