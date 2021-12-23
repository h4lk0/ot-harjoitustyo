from services.logic import Logic

class Exercise:
    """Class to represent a single exercise
    """

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
        """Checks if the given string is in the english entry in answer

        Args:
            chosen (str): User's answer to exercise

        Returns:
            boolean:
                    True, if given string is in the english entry
                    False, if not
        """
        if chosen in self._answer["eng"]:
            return True
        return False

