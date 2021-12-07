import sqlite3
from config import DATABASE_FILE_PATH

class Database:

    def __init__(self):
        self.connection = sqlite3.connect(DATABASE_FILE_PATH)

    def get_table_nouns(self):
        table = self.connection.execute("SELECT eng, kor FROM Nouns").fetchall()
        return table

    def create_wordlist(self):
        list_name = input("Name of list: ")
        create_command = f'CREATE TABLE IF NOT EXISTS {list_name} (id INTEGER PRIMARY KEY, eng TEXT, kor TEXT)'
        insert_command = f'INSERT INTO {list_name} values (?, ?)'
        self.connection.execute(create_command)
        while True:
            values = input("Insert values using format 'eng,kor', -1 to stop: ")

            if values == "-1":
                break
            parts = values.split(",")
            for part in parts:
                part.strip()
            self.connection.execute(insert_command, (parts[0], parts[1]))

    def get_own_wordlist(self, list_name):
        fetch_command = f'SELECT eng, kor FROM {list_name}'
        table = self.connection.execute(fetch_command).fetchall()
        return table
