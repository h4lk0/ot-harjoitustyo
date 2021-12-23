import unittest

from entities.exercise import Exercise

class TestExercise(unittest.TestCase):
    def setUp(self):
        self.wordlist = "Fruits and vegetables"
        self.ex = Exercise(self.wordlist)

    def test_new_values(self):
        answer = self.ex.get_answer()
        options = self.ex.get_options()
        self.assertIsNone(answer)
        self.assertIsNone(options)
        self.ex.new_values()
        new1 = self.ex.get_answer()
        new2 = self.ex.get_options()
        self.assertEqual(len(new1), 2)
        self.assertEqual(len(new2), 5)

    def test_get_answer(self):
        self.ex.new_values()
        self.assertIsInstance(self.ex.get_answer(), dict)

    def test_get_options(self):
        self.ex.new_values()
        self.assertIsInstance(self.ex.get_options(), list)

    def test_check(self):
        self.ex.new_values()
        eng = ["strawberry", "apple", "watermelon", "garlic", "potato", "radish"]
        b = False
        for word in eng:
            if self.ex.check(word):
                b = True
        self.assertIsNot(b, False)
