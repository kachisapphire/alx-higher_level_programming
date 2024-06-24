#!/usr/bin/python3
""" This module contains a database. """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    arg = db.cursor()
    arg.execute("SELECT * FROM states")
    rows = arg.fetchall()
    for row in rows:
        print(row)
    arg.close()
    db.close()
