import sqlite3
from sqlite3 import Error

def print_all_tables(db_file):
    """ Connect to the SQLite database and print all table names """
    conn = None
    try:

        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        query = "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';"
        cursor.execute(query)

        tables = cursor.fetchall()
        
        if tables:
            print(f"Tables in '{db_file}':")
            for table in tables:
                print(f"- {table[0]}")
        else:
            print(f"No user-defined tables found in '{db_file}'.")
            
    except Error as e:
        print(f"Error while connecting to SQLite: {e}")
        
    finally:

        if conn:
            conn.close()
            print("\nSQLite connection is closed.")

print_all_tables('your_database.db')