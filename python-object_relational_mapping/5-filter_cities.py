#!/usr/bin/python3
<<<<<<< HEAD
"""
Script that takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""

=======
"""Script that takes in the name of a state and lists all cities of that
state using the database hbtn_0e_4_usa - safe from SQL injection"""
>>>>>>> e661c15b6b49a5fef89f84892b61b9bc570da797
import MySQLdb
import sys


if __name__ == "__main__":
<<<<<<< HEAD
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

=======
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
>>>>>>> e661c15b6b49a5fef89f84892b61b9bc570da797
    cur = db.cursor()
    cur.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
<<<<<<< HEAD
    """, (state_name,))

    rows = cur.fetchall()
    cities = []
    for row in rows:
        cities.append(row[0])

    print(", ".join(cities))

    cur.close()
    db.close()

=======
    """, (sys.argv[4],))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    db.close()
>>>>>>> e661c15b6b49a5fef89f84892b61b9bc570da797
