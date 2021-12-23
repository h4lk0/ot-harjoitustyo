import unittest

from services.valid_entry_check import Checks

class TestChecks(unittest.TestCase):

    def setUp(self):
        self.checker = Checks()

    def test_eng_is_valid_true(self):
        word = "python"
        ok = self.checker.eng_is_valid(word)
        self.assertEqual(ok, True)

    def test_eng_is_valid_false(self):
        word = "error404"
        ok = self.checker.eng_is_valid(word)
        self.assertEqual(ok, False)

    def test_kor_is_valid_true(self):
        word = "파이썬"
        ok = self.checker.kor_is_valid(word)
        self.assertEqual(ok, True)

    def test_kor_is_valid_false(self):
        word = "python"
        ok = self.checker.kor_is_valid(word)
        self.assertEqual(ok, False)