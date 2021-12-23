from random import choice, choices
from database.database_methods import Database

class Logic:

    """Class responsible for creating a random sample of five entries in a wordlist
    """

    def __init__(self, table):
        self._db = Database()
        self._wordlist = None
        self._table = table

    def _fetch_wordlist(self):
        table = self._db.get_table(self._table)
        return table

    def randomize(self):
        """Method to get five random entries from a wordlist

        Returns:
            options (list): list containing five dictionaries each containing one wordlist entry
            answer (dict): random dictionary out of the five options
        """
        if self._wordlist is None:
            self._wordlist = self._fetch_wordlist()
        options = choices(self._wordlist, k=5)
        answer = choice(options)

        return answer, options
