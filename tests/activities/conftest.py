import pytest
import random


@pytest.fixture
def random_number_list() -> list[int]:
    return [random.randint(0, 1000) for _ in range(random.randint(0, 100))]
