import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_project(conn, project):

    sql = ''' INSERT INTO Students(National_Number,name,address,age,course,phone,email)
              VALUES(?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid





def main():
    database = r"C:\Users\ENG-Mahmoud\Desktop\DataBase\pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        project = ('30107170202677','Mahmoud','Alexandria',22,'Python','01287832504','mk2174644@gmail.com');
        project_id = create_project(conn, project)

       

if __name__ == '__main__':
    main()
