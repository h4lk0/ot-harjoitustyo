import unittest

from services.table_getter import TableGetter

class TestTableGetter(unittest.TestCase):

    def setUp(self):
        self.getter = TableGetter()

    def test_get_table_names(self):
        ls = self.getter.get_tables()
        self.assertEqual(len(ls), 2)