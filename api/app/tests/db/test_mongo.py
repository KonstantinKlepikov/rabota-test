from typing import Generator


class TestDB:
    """Db connections tests
    """

    async def test_test_db_connection(self, db: Generator) -> None:
        """Test dev db is available
        """
        assert db.name == 'test-db', 'wrong dev db'
