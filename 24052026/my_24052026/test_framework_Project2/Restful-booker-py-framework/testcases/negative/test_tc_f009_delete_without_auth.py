def test_tc_f009_delete_without_auth(api_client, create_booking):
    response = api_client.delete_booking(create_booking)
    assert response.status_code in (401, 403)
