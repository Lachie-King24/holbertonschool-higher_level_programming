#!/usr/bin/python3
"""displays all values in the states table in db"""

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
    cur.execute("SELECT * FROM states WHERE BINARY name\
                 LIKE '{}%' ORDER BY id ASC".format(state))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
