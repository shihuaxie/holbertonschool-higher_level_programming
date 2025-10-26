#!/usr/bin/python3
"""This module is for task 2"""

import MySQLdb
import sys


def list_all_states_by_user_input(username, password, dbname, stname):
    """ Connect to a MySQL server to display all states
    that matches with user input """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    cursor = db.cursor()

    query = (
        "SELECT * FROM states"
        "WHERE BINARY name = '{}'"
        "ORDER BY states.id ASC"
        .format(stname)

    cursor.execute(query)
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_all_states_by_user_input(
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    )
