import random

class Exercise:

    def __init__(self):
        pass

    def get_options(self, table):
        options = random.sample(table, 5)
        asked = options[0][1]
        answer = options[0][0]
        return options, asked, answer

    def multiple_choice(self, table):
        options, asked, answer = self.get_options(table)
        random.shuffle(options)
        print(asked)
        print("Choose option 1-5")
        for option in options:
            print(option[0])
        user_input = input("Answer: ")
        if user_input == answer:
            print("Well done!")
        else:
            print("Incorrect")
   

    def fill_in(self, table):
        options, asked, answer = self.get_options(table)
        random.shuffle(options)
        print(asked)
        user_input = input("Type your answer: ")

        if user_input in answer:
            print("Good job!")
        else:
            print("Incorrect")

    def flashcard(self, table):
        eng, kor = random.choice(table)
        print(kor)
        user_input = str(input("Type '1' to show English translation: "))
        if user_input == "1":
            print(eng) 
        else:
            pass
