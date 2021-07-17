import psycopg2
import os
import fnmatch

def get_sql_files(target_dir):
    """Get all the SQL files!"""
    for path, _, files in os.walk(os.path.abspath(target_dir)):
        for filename in fnmatch.filter(files, "*.sql"):
            filepath = os.path.join(path, filename)
            with open(filepath) as file:
                source = file.read()
            print(source)

def create_object():
    """Create DB object!"""


def create_db_objects(target_dir):
    """Create all DB objects!"""
    get_sql_files(target_dir)