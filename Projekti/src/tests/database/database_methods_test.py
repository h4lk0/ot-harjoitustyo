import unittest
from database.database_methods import Database
from services.csv_handler import ListFromCSV

class TestDatabaseMethods(unittest.TestCase):

    def setUp(self):
        self.table = "Vehicles"

    def test_get_table_names(self):
        db = Database()
        tn = db.get_table_names()
        self.assertEqual(len(tn), 2)

    def test_create_new(self):
        db = Database()
        new_table = "Test1"
        before = len(db.get_table_names())
        db.create_new_table(new_table)
        self.assertGreater(len(db.get_table_names()), before)
        db.drop_table(new_table)

    def test_add_to_list(self):
        db = Database()
        db.clear_table(self.table)
        db.add_to_list(self.table, "car", "자동차")
        length = len(db.get_table(self.table))
        self.assertGreater(length, 0)
        db.clear_table(self.table)

    def test_get_table(self):
        db = Database()
        table1 = "Fruits and vegetables"
        length = len(db.get_table(table1))
        self.assertEqual(length, 6)

    def test_drop_table(self):
        db = Database()
        table = "Testi"
        db.create_new_table(table)
        len1 = len(db.get_table_names())
        db.drop_table(table)
        len2 = len(db.get_table_names())
        self.assertLess(len2, len1)

    def test_clear_table(self):
        db = Database()
        db.add_to_list(self.table, "car", "자동차")
        len1 = len(db.get_table(self.table))
        db.clear_table(self.table)
        len2 = len(db.get_table(self.table))
        self.assertTrue(len1 > len2 and len2 == 0)

    def test_add_from_file(self):
        db = Database()
        db.clear_table(self.table)
        file = "src/tests/test-csvfile.csv"
        ok = db.add_from_file(self.table, file)
        self.assertEqual(ok, True)
        db.clear_table(self.table)
    
    def test_validate_list_true(self):
        db = Database()
        convert = ListFromCSV()
        file = "src/tests/test-csvfile.csv"
        ls = convert.file_to_list(file)
        ok = db._validate_list(ls)
        self.assertEqual(ok, True)

    def test_validate_list_eng_is_not_valid(self):
        db = Database()
        wordlist = [{"eng": "123", "kor":"자동차"}]
        ok = db._validate_list(wordlist)
        self.assertEqual(ok, False)

    def test_validate_list_kor_is_not_valid(self):
        db = Database()
        wordlist = [{"eng": "car", "kor":"123"}]
        ok = db._validate_list(wordlist)
        self.assertEqual(ok, False)
