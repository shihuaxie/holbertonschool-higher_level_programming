#!/usr/bin/python3
"""Lists all cities of a given state (SQL injection safe)"""

import MySQLdb
import sys


def list_cities_of_state(username, password, dbname, state_name):
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )
    cursor = db.cursor()

    # parameterised query - safe from sql injection
    cursor.execute(
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (state_name,),
    )
    results = cursor.fetchall()
 
    cities = [row[0] for row in results]
    print(", ".join(cities))

    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities_of_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
