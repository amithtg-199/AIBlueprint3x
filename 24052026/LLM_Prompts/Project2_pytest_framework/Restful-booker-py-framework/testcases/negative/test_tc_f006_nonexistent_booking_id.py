import allure

@allure.feature("Booking")
@allure.story("Get non-existent booking")
def test_tc_f006_nonexistent_booking_id(api_client):
    response = api_client.get_booking(999999)
    assert response.status_code in (400, 404)
