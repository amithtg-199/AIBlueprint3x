import allure

@allure.feature("Booking")
@allure.story("Delete booking with auth")
def test_tc_f011_delete_with_auth(api_client, test_data):
    create_response = api_client.create_booking(test_data["booking_valid"].copy())
    assert create_response.status_code == 200
    booking_id = create_response.json().get("bookingid")

    token_response = api_client.create_token(test_data["auth_valid"])
    token_response.raise_for_status()
    token = token_response.json().get("token")

    delete_response = api_client.delete_booking(booking_id, cookies={"token": token})
    assert delete_response.status_code in (200, 201, 204)
    assert api_client.get_booking(booking_id).status_code in (400, 404)
