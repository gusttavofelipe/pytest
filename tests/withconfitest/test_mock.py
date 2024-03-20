def test_mock_response_return_success(mock_response):
    response = mock_response
    assert response.status_code == 200
    assert response.json.return_value.get("message") == "Success"
