import sqlite3
import sqlite_utils as sql
from config import DATABASE_FILE_PATH
from services.csv_handler import ListFromCSV
from services.valid_entry_check import Checks

class Database:
    """Class responsible for database management
    """

    def __init__(self):
        """Creates a new database management interface
        """
        self._db = sql.Database(sqlite3.connect(DATABASE_FILE_PATH))
        self._checker = Checks()

    def get_table_names(self):
        """Fetches all table names from database

        Returns:
            tables: list of names
        """
        tables = self._db.table_names()
        return tables

    def create_new_table(self, table_name):
        """Creates a new table in database if no table with given name exists

        Args:
            table_name (str): Name of table being created

        Returns:
            boolean:
                    True, if table was created
                    False, if it already exists
        """
        if not self._db[table_name].exists():
            self._db[table_name].create({
                "eng": str,
                "kor": str
            })
            return True
        return False

    def add_to_list(self, table_name, eng, kor):
        """Adds a single entry to given table

        Args:
            table_name (str): Target table
            eng (str): English word being inserted
            kor (str): Korean equivalent of the English word

        Returns:
            int:
                0 = entry for English contains invalid characters
                1 = entry for Korean contains latin characters
                2 = insert successful
        """
        passed = 2
        if self._checker.eng_is_valid(eng) is False:
            passed = 0
        if self._checker.kor_is_valid(kor) is False:
            passed = -1
        else:
            self._db[table_name].insert({"eng": eng, "kor": kor})
        return passed

    def add_from_file(self, table_name, file):
        """Inserts rows from a .csv file into given table

        Args:
            table_name (str): Target table
            file (str): .csv filepath

        Returns:
            boolean:
                    False, if all entries not valid
                    True, if all entries inserted successfully  
        """
        convert = ListFromCSV()
        to_add = convert.file_to_list(file)
        valid = self._validate_list(to_add)
        if not valid:
            return False
        self._db[table_name].insert_all(to_add)
        return True

    def _validate_list(self, wordlist):
        """Checks if all entries in wordlist for invalid characters

        Args:
            wordlist (list): List of dictionaries containing database entries

        Returns:
            boolean: 
                    False, if any entry contains invalid characters
                    True, if all entries valid
        """
        valid = True
        for entry in wordlist:
            if not self._checker.eng_is_valid(entry["eng"]):
                valid = False
            if not self._checker.kor_is_valid(entry["kor"]):
                valid = False
        return valid

    def get_table(self, table_name):
        """Fetches given table from database

        Args:
            table_name (str): Target table

        Returns:
            list: List of table rows converted into dictionaries
        """
        wordlist = []
        for row in self._db[table_name].rows_where(select="eng, kor"):
            wordlist.append(row)
        return wordlist
