import allure

@allure.feature("Booking")
@allure.story("Update booking with auth")
def test_tc_f008_update_booking_with_auth(api_client, create_booking, test_data, auth_token):
    payload = test_data["booking_update"].copy()
    response = api_client.update_booking(create_booking, payload, cookies={"token": auth_token})
    assert response.status_code == 200
    body = response.json()
    assert body["firstname"] == payload["firstname"]
    assert body["lastname"] == payload["lastname"]
