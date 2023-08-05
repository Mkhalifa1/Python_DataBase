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


def update_students(conn, task):

    sql = ''' UPDATE Students
              SET age = ? ,
                  course = ? ,
                  phone = ?
              WHERE National_Number = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()


def main():
    database = r"C:\Users\ENG-Mahmoud\Desktop\DataBase\pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        update_students(conn, (23,'Java','01287832606','30107170202677'))


if __name__ == '__main__':
    main()
