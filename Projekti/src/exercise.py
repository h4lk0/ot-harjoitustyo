import random

class Exercise:
    """TBD
    """

    def __init__(self) -> None:
        self.initialize()

    def initialize(self):
        db = self.create_database()
        while True:
            print("Exercise: 0\n"
                  "Exit: -1")
            cmd = input("Give command:")
            if cmd == "-1":
                break
            else:
                ExerciseLogic(db)

    def create_database():
        db = {}
        with open("data/nouns.txt") as nouns:
            for line in nouns:
                line = line.replace("\n","")
                parts = line.split(";")
                db[parts[1]] = parts[0]
        return db

class ExerciseLogic:
    """TBD
    """

    def __init__(self, db) -> None:
        self.options = [random.choice(list(db)) for i in range(5)]
        self.answer = self.options[0]
        self.question = db[self.answer]
        self.multiple_choice(self.answer, self.options, self.question)

    def correct(i):
        if i == 3:
            print("Amazing!")
        if i == 2:
            print("Great!")
        if i == 1:
            print("Good!")

    def multiple_choice(self, answer, options, question):
        print(question)
        print("Select correct:")
        print(options)

        for i in range(3, 0, -1):
            guess = input("Answer: ")

            if guess == answer:
                self.correct(i)
                break
            else:
                print(f'Try again ({i}) guesses left')