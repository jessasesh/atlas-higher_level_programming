#!/usr/bin/python3
"""  Lists all states from specified database """

import sys
import MySQLdb


def all_states():

    DB = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cursor = DB.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    DB.close()


if __name__ == "__main__":
    all_states()