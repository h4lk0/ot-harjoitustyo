import sqlite_utils as sqlu

from config import DATABASE_FILE_PATH

connection = sqlu.db.Database(DATABASE_FILE_PATH)

def get_connection():
    return connection
