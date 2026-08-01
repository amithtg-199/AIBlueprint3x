import allure

@allure.feature("Booking")
@allure.story("Get booking by ID")
def test_tc_f005_get_booking_by_id(api_client, create_booking):
    response = api_client.get_booking(create_booking)
    assert response.status_code == 200
    body = response.json()
    assert body.get("firstname") is not None
    assert body.get("lastname") is not None
