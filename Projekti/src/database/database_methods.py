import sqlite3
from config import DATABASE_FILE_PATH

class Database:

    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_FILE_PATH)

    def get_table_nouns(self):
        table = self.connection.execute("SELECT eng, kor FROM Nouns").fetchall()
        return table
