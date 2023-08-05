import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Students")

    rows = cur.fetchall()

    for row in rows:
        print(row)

def select_task_by_national_number(conn, id):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM Students WHERE National_Number=?", (id,))

    rows = cur.fetchall()

    for row in rows:
        print(row)


def main():
    database = r"C:\Users\ENG-Mahmoud\Desktop\DataBase\pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query all Students")
        select_all_tasks(conn)
        
        print("------------------------------------------------------------------------------")
        
        print("2. Query Data by National Number:")
        select_task_by_national_number(conn,'30107170202655')


if __name__ == '__main__':
    main()
