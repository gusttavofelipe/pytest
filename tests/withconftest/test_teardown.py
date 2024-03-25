from sqlalchemy.sql import text


def test_db_connection(db_connection):
    result = db_connection.execute(text("SELECT 1"))
    assert result.fetchone()[0] == 1
