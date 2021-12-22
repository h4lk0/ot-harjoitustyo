from string import ascii_letters, printable

class Checks:
    """Contains methods to check a string for given characters
    """

    def __init__(self):
        """Constructor
        """
        self._exceptions = "/()' "

    def eng_is_valid(self, word):
        """Checks if given contains only latin characters

        Args:
            word (str): String being checked

        Returns:
            boolean:
                    False, if string contains other than latin characters
                    True, if only latin characters present
        """
        valid = True
        for i in enumerate(word):
            if i[1] not in ascii_letters or i[1] not in self._exceptions:
                valid = False
        return valid

    def kor_is_valid(self, word):
        """Checks if given string contains latin characters, numbers or punctuation

        Args:
            word (str): String being checked

        Returns:
            boolean:
                    False, if latin characters, numbers or punctuation present
                    True, if only other characters are present
        """
        valid = True
        for i in enumerate(word):
            if i[1] in printable:
                valid = False
        return valid
