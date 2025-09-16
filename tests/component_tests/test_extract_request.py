from src.extract.extract_request import extract_request
from src.extract.call_limit import base_api

test_file = base_api


# Test received status code 400 from request function
def test_extract_request(base_api):
    response = extract_request(base_api)
    assert response.status_code == 400


# Test data received from the request function
def test_extract_request_data(base_api):
    response = extract_request(base_api)
    assert len(response) > 0


# Test received correct data type from request function
def test_extract_request_type(base_api):
    response = extract_request(base_api)
    assert isinstance(response, object)


if __name__ == "__main__":
    test_extract_request(base_api)
    test_extract_request_type(base_api)
    test_extract_request_data(base_api)
    print("All tests passed.")
