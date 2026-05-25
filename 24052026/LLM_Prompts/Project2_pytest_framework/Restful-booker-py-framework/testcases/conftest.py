import pytest
from framework.api_client import ApiClient
from framework.data_loader import load_test_data
from framework.utils import unique_string


@pytest.fixture(scope="session")
def api_client():
    return ApiClient()


@pytest.fixture(scope="session")
def test_data():
    return load_test_data()


@pytest.fixture
def auth_token(api_client, test_data):
    response = api_client.create_token(test_data["auth_valid"])
    response.raise_for_status()
    return response.json().get("token")


@pytest.fixture
def create_booking(api_client, test_data):
    booking_payload = test_data["booking_valid"].copy()
    booking_payload["firstname"] = unique_string(booking_payload["firstname"])
    response = api_client.create_booking(booking_payload)
    response.raise_for_status()
    body = response.json()
    booking_id = body.get("bookingid")
    token_response = api_client.create_token(test_data["auth_valid"])
    token_response.raise_for_status()
    token = token_response.json().get("token")
    yield booking_id
    if booking_id:
        api_client.delete_booking(booking_id, cookies={"token": token})
