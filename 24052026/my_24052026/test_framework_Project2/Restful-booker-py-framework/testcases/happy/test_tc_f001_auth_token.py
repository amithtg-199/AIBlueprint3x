import allure

@allure.feature("Authentication")
@allure.story("Auth token creation")
def test_tc_f001_auth_token(api_client, test_data):
    response = api_client.create_token(test_data["auth_valid"])
    assert response.status_code == 200
    assert response.json().get("token") is not None
