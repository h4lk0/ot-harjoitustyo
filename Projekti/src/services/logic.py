from database.database_methods import Database
from random import choice, choices

class Logic:

    def __init__(self, table):
        self._db = Database()
        self._wordlist = None
        self._table = table

    def _fetch_wordlist(self):
        table = self._db.get_table(self._table)
        return table

    def randomize(self):
        if not self._wordlist:
            self._wordlist = self._fetch_wordlist()
        options = choices(self._wordlist, k=5)
        answer = choice(options)

        return answer, options


    
    


