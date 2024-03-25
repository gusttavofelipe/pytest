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


@pytest.fixture(scope="function")  # default scope
def fixture_function():
    """instancias novas criadas e destruidas para cada função de teste"""
    return "function scope"


@pytest.fixture(scope="class")
def fixture_class():
    """instancia criada e destruida uma vez para cada classe de teste"""
    return "class scope"


@pytest.fixture(scope="module")
def fixture_module():
    """instancia criada e destruida uma vez para cada módulo de teste"""
    return "module scope"


@pytest.fixture(scope="session")
def fixture_session():
    """
    instancia criada e destruida uma vez para a execução de todo o conjunto de testes
    """
    return "session scope"
