#!/usr/bin/python3
"""This module is for task 3"""

import MySQLdb
import sys


def safe_filter_states(username, password, dbname, stname):
    """
    Connect to MySQL and print states where name = stname
    (safe from SQL injection)
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )

    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC", (stname,)
    )
    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()


    
if __name__ == "__main__":
    safe_filter_states(
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    )
