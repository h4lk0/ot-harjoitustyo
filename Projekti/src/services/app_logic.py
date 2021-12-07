import database.database_methods
import entities.exercise_types

class Logic:

    def __init__(self):
        self._db = database.database_methods.Database()
        self._table = None
        self._exercise = entities.exercise_types.Exercise()

    def initialize(self):
        print("Welcome")
        self._table = self.choose_wordlist()
        print("Type 0 to start exercises, -1 exits")

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

    def choose_wordlist(self):
        list_of_tables = self._db.connection.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()
        length = len(list_of_tables)
        print(list_of_tables)
        list_index = int(input(f'Choose from list of tables(1-{length})'))
        table_name = list_of_tables[list_index-1][0]
        table = self._db.get_own_wordlist(table_name)
        return table

    def new_wordlist(self):
        self._db.create_wordlist()
