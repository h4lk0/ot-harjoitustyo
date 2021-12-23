import unittest

from services.logic import Logic

class TestLogic(unittest.TestCase):

    def setUp(self):
        self.l = Logic("Fruits and vegetables")

    def test_randomize(self):
        answer, options = self.l.randomize()
        self.assertEqual(len(answer),2)
        self.assertEqual(len(options),5)