import allure

@allure.feature("Authorization")
@allure.story("Update without auth")
def test_tc_f010_update_without_auth(api_client, create_booking, test_data):
    payload = test_data["booking_update"].copy()
    response = api_client.update_booking(create_booking, payload)
    assert response.status_code in (401, 403)
