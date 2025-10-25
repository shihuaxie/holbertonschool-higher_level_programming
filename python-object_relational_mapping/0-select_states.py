#!/usr/bin/python3
"""This module lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


def list_all_states(username, password, dbname):
    # Connect with MySQL using MySQLdb.connect()
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    results = cur.fetchall()

    # Loop the results and print it in row
    for row in results:
        print(row)

    # close cursor and connection
    cur.close()
    conn.close()


if __name__ == "__main__":
    list_all_states(sys.argv[1], sys.argv[2], sys.argv[3])
