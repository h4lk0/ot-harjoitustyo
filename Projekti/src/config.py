import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except:
    pass

DATABASE_FILENAME = os.getenv("DATABASE_FILENAME") or "wordlists.db"
DATABASE_FILE_PATH = os.path.join(dirname, "..", "database", DATABASE_FILENAME"
