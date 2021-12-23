import unittest
from services.csv_handler import ListFromCSV

class TestCSVHandler(unittest.TestCase):

    def setUp(self):
        self.handler = ListFromCSV()
        self.file = "src/tests/test-csvfile.csv"

    def test_file_to_list(self):
        templist = self.handler.file_to_list(self.file)
        self.assertGreater(len(templist), 0)