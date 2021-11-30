import unittest
from database.database_methods import Database


class TestDatabaseMethods(unittest.TestCase):
    
    def setUp(self) -> None:
        self.connection = Database()

    def test_get_table_nouns(self):
        assert type(self.connection.get_table_nouns()) is list
        self.assertGreater(len(self.connection.get_table_nouns()), 0)
