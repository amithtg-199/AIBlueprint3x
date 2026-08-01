import allure

@allure.feature("Booking")
@allure.story("Create booking")
def test_tc_f002_create_booking(api_client, test_data):
    payload = test_data["booking_valid"].copy()
    response = api_client.create_booking(payload)
    assert response.status_code == 200
    body = response.json()
    assert body.get("bookingid") is not None
    booking = body.get("booking")
    assert booking["firstname"] == payload["firstname"]
    assert booking["lastname"] == payload["lastname"]

    booking_id = body["bookingid"]
    token_response = api_client.create_token(test_data["auth_valid"])
    token_response.raise_for_status()
    cleanup = api_client.delete_booking(booking_id, cookies={"token": token_response.json().get("token")})
    assert cleanup.status_code in (200, 201, 204)
