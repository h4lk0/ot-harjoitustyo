class ListFromCSV:
    """Service class to convert a .csv file to a list of dictionaries
    """

    def __init__(self):
        """Class constructor
        """
        self._list = []

    def file_to_list(self, file_name):
        """Converts rows into dictionaries and adds them to a list

        Args:
            file_name (str): filepath of .csv file

        Returns:
            list: Returns list of dictionaries
        """
        with open(file_name, encoding="utf-8") as csv_file:
            for line in csv_file:
                line = line.replace("\n","")
                line.strip()
                parts = line.split(",")
                eng = parts[0]
                kor = parts[1]
                self._list.append({"eng": eng, "kor": kor})
        csv_file.close()
        return self._list
