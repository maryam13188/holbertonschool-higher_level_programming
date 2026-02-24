#!/usr/bin/python3
"""
Lists all states with name matching the argument (safe from SQL injection)
Arguments: mysql username, mysql password, database name, state name
"""

import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()

