import pytest
import requests
import sqlalchemy
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


@pytest.fixture
def db_connection():
    engine = sqlalchemy.create_engine("sqlite:///:memory:")
    conn = engine.connect()
    yield conn
    conn.close()
