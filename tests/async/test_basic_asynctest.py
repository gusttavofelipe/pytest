import pytest

from functions import tech_data


@pytest.mark.asyncio
async def test_fetch_data():
    result = await tech_data()
    assert result == {"data": "something"}
