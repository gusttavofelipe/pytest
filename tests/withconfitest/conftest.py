import pytest
import requests
from unittest.mock import MagicMock


@pytest.fixture
def list_():
    return [1, 2]


@pytest.fixture
def mock_response():
    mock = MagicMock(spec=requests.Response)
    mock.status_code = 200
    mock.json.return_value = {"message": "Success"}
    return mock
