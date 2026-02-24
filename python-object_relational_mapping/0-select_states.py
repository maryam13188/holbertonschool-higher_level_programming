#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
Arguments: mysql username, mysql password, database name
Results sorted in ascending order by states.id
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # Execute query
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Print results
    for row in cur.fetchall():
        print(row)

    # Clean up
    cur.close()
    db.close()
