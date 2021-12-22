from services.logic import Logic

class Exercise:

    def __init__(self, wordlist):
        self._answer = None
        self._options = None
        self._logic = Logic(wordlist)

    def new_values(self):
        self._answer, self._options = self._logic.randomize()
    
    def get_answer(self):
        return self._answer

    def get_options(self):
        return self._options

    def check(self, chosen):
        if chosen in self._answer["eng"]:
            return True
        return False

