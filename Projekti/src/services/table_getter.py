from database.database_methods import Database

class TableGetter:

    def __init__(self):
        self._db = Database()

    def get_tables(self):
        return self._db.get_table_names()