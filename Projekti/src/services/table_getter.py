from services.database_methods import DatabaseMethods

class TableGetter:
    """Fetches all names of tables in database
    """

    def __init__(self):
        self._db = DatabaseMethods()

    def get_tables(self):
        """Creates a list with names of the tables in a database

        Returns:
            list: names of tables
        """
        return self._db.get_table_names()
