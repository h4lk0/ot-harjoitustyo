import database.database_methods
import entities.exercise_types

class Logic:

    def __init__(self):
        self._db = database.database_methods.Database()
        self._table = self._db.get_table_nouns()
        self._exercise = entities.exercise_types.Exercise()

    def initialize(self):
        print("Welcome")
        print("Type 0 to start exercises, -1 exists")

        user_input = input("Command: ")
        if user_input == "-1":
            print("Bye!")
        elif user_input == "0":
            print("Choose exercise: 1) Multiple choice 2) Fill blank 3) Flashcard")
            choice = input("Choice: ")
            print("Type 'next' for new exercise, 'exit' to exit")
            while True:
                cmd = input("Input: ")
                if cmd == "next":
                    if choice == "1":
                        self._exercise.multiple_choice(self._table)
                    if choice == "2":
                        self._exercise.fill_in(self._table)
                    if choice == "3":
                        self._exercise.flashcard(self._table)
                if cmd == "exit":
                    break
