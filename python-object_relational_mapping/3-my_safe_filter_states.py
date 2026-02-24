#!/usr/bin/python3
"""
This module lists all states with name matching the argument from database.
It is safe from SQL injection attacks by using parameterized queries.
"""

import MySQLdb
import sys


def main():
    """
    Connects to MySQL database and retrieves all states matching the provided
    state name. Uses parameterized queries to prevent SQL injection.
    Results are sorted in ascending order by states.id.
    """
    # Get command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    # Create cursor and execute query with parameter (safe from injection)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (state_name,))

    # Fetch and print results
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close cursor and database connection
    cur.close()
    db.close()


if __name__ == "__main__":
    main()

