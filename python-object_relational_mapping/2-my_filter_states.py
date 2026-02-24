#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
where name matches the argument.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create cursor
    cur = db.cursor()

    # Execute query with format (required by task)
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id".format(state_name))

    # Print results
    for row in cur.fetchall():
        print(row)

    # Clean up
    cur.close()
    db.close()

