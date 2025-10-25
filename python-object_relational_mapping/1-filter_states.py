#!/usr/bin/python3
"""This module lists all states with a name starting with
N from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


def list_all_states_with_name_starting_N(username, password, dbname):
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC")
    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    list_all_states_with_name_starting_N(sys.argv[1], sys.argv[2], sys.argv[3])
