#!/usr/bin/python3
"""
Module for task 3: My safe filter states
This script lists all states with name matching the argument from the database.
It is safe from SQL injection by using parameterized queries.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """
    Main function that connects to MySQL database and retrieves states
    matching the provided state name (safe from SQL injection).
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

