import unittest
import exercise

class TestExercise(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_database_created(self):
        db = exercise.Exercise.create_database
        self.assertTrue(bool(db))

class TestExerciseLogic(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()