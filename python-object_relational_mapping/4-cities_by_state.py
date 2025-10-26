#!/usr/bin/python3
"""
Lists all cities from hbtn_0e_4_usa with their state names
"""

import MySQLdb
import sys


def list_all_cities(username, password, dbname):
    """lists all cities from the database hbtn_0e_4_usa"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )
    cursor = db.cursor()

    # use JOIN -- cities.state.id = states.id
    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )

    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_all_cities(sys.argv[1], sys.argv[2], sys.argv[3])
