import allure

@allure.feature("Booking")
@allure.story("Query filters")
def test_tc_f007_query_filters(api_client, test_data):
    booking_payload = test_data["booking_sally"].copy()
    response = api_client.create_booking(booking_payload)
    assert response.status_code == 200
    booking_id = response.json().get("bookingid")

    filter_response = api_client.get_bookings({"firstname": booking_payload["firstname"], "checkin": booking_payload["bookingdates"]["checkin"]})
    assert filter_response.status_code == 200
    results = filter_response.json()
    assert any(item.get("bookingid") == booking_id for item in results)

    token_response = api_client.create_token(test_data["auth_valid"])
    token_response.raise_for_status()
    cleanup = api_client.delete_booking(booking_id, cookies={"token": token_response.json().get("token")})
    assert cleanup.status_code in (200, 201, 204)
