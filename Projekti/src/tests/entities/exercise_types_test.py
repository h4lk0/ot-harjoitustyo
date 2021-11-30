import unittest

from entities.exercise_types import Exercise

class TestExercise(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_get_options(self):
        table = [(1, "yes"), (2, "no"), (3, "hello"), (4, "bye"), (5, "cat"), (6, "dog"), (7, "example")]
        options, asked, answer = Exercise.get_options(self, table)

        self.assertEqual(len(options), 5)
        assert type(answer) is int
        assert type(asked) is str