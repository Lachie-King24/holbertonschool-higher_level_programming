#!/usr/bin/python3
"""Displays all states where name matches the argument (safe from SQL injection)"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()

    # SAFE query using parameterization
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (state,)
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()