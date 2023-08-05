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


def delete_task(conn, id):

    sql = 'DELETE FROM Students WHERE National_Number=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

# Delete All Students 

def delete_all_Students(conn):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM Students'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def main():
    database =  r"C:\Users\ENG-Mahmoud\Desktop\DataBase\pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        delete_task(conn, '30107170202677');
        # delete_all_Students(conn);


if __name__ == '__main__':
    main()
