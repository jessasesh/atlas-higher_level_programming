#!/usr/bin/python3
""" Takes in name of state as arg """

import sys
import MySQLdb


def all_cities():

    DB = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cursor = DB.cursor()

    cursor.execute("SELECT cities.name \
                    FROM cities \
                    INNER JOIN states ON cities.state_id = states.id \
                    WHERE states.name = %s \
                    ORDER BY cities.id ASC", (sys.argv[4],))
    
    cities = cursor.fetchall()

    print(", ".join([record[0] for record in cities]))

    cursor.close()
    DB.close()


if __name__ == "__main__":
    all_cities()