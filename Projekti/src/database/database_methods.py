from table_names import table_getter
from database_connection import get_connection

class Database:

    def __init__(self):
        self.connection = get_connection()
        return self.connection

    def get_table(self, name):
        table = self.connection.execute(table_getter(name)).fetchall
        return table