def test_tc_f003_missing_lastname(api_client, test_data):
    payload = test_data["booking_missing_lastname"].copy()
    response = api_client.create_booking(payload)
    assert 400 <= response.status_code < 500
