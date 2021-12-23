from database.database_connection import get_connection
from services.csv_handler import ListFromCSV
from services.valid_entry_check import Checks

class DatabaseMethods:
    """Class responsible for database management
    """

    def __init__(self):
        """Creates a new database management interface
        """
        self._db = get_connection()
        self._checker = Checks()
        self.converter = ListFromCSV()

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
        created = False
        if not self._db[table_name].exists():
            self._db[table_name].create({
                "eng": str,
                "kor": str
            }, pk="kor")
            created = True
        return created

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
        if not self._checker.eng_is_valid(eng):
            passed = 0
        if not self._checker.kor_is_valid(kor):
            passed = -1
        else:
            self._db[table_name].insert({"eng": eng, "kor": kor}, pk="kor", replace=True)
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
        to_add = self.converter.file_to_list(file)
        valid = self._validate_list(to_add)
        if not valid:
            return False
        self._db[table_name].insert_all(to_add, pk="kor", replace=True)
        return True

    def _validate_list(self, wordlist):

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

    def drop_table(self, table_name):
        """Drops table from database if it exists

        Args:
            table_name (str): Name of table being deleted
        """
        self._db[table_name].drop(ignore=True)

    def clear_table(self, table_name):
        """Deletes all rows in given table

        Args:
            table_name (str): table being cleared
        """
        self._db[table_name].delete_where()
