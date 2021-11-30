import random
import database.database_methods as db


class Exercise:

    def __init__(self):
        self.db = db()

    def get_options(self, table):
        options = random.sample(table, 5)
        asked = options[0][1]
        answer = options[0][0]
        return options, asked, answer

    def multiple_choice(self):
        options, asked, answer = self.get_options()
        choices = {i: random.shuffle(options) for i in range(1,6)}
        print("Choose option 1-5")
        print(choices)
        user_input = str(input("Answer: "))
        if choices[user_input] == answer:
            print("Well done!")
        else:
            print("Incorrect")

    def fill_in(self):
        options, asked, answer = self.get_options()
        choices = {i: random.shuffle(options) for i in range(1,6)}
        print("Type your answer")
        user_input = input("Answer: ")

        if user_input in answer:
            print("Good job!")
        else:
            print("Incorrect")

    def flashcard(self, table):
        eng, kor = random.choice(table)
        print(kor)
        user_input = str(input("Type '1' to show English translation"))
        if user_input == "1":
            print(eng) 
        else:
            pass
