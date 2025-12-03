from server.constants import config as config
from sqlite3 import OperationalError
import sqlite3

def connect_to_db(db_file: str) -> sqlite3.Connection:
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except OperationalError as e:
        print(e)
    except Exception as e:
        print(e)

    return connection


def execute_query(sql_str: str) -> list:
    result_set = []
    try:
        connection = connect_to_db(db_file = config.db_file)
        cursor = connection.cursor()
        result_set = cursor.execute(sql_str).fetchall()
        result_set_metadata = cursor.description
        connection.commit()
        connection.close()
    except sqlite3.OperationalError as e:
        print(e)
    except sqlite3.IntegrityError as e:
        print(e)
    except sqlite3.ProgrammingError as e:
        print(e)

    return result_set, result_set_metadata
