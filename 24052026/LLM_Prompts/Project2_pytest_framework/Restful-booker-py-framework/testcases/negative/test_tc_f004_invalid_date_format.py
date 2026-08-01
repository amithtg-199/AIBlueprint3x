def test_tc_f004_invalid_date_format(api_client, test_data):
    payload = test_data["booking_invalid_date"].copy()
    response = api_client.create_booking(payload)
    assert 400 <= response.status_code < 500
