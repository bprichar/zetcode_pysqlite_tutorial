#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

try:
    con = lite.connect('test.db')

    cur = con.cursor()

    cur.executescript("""
        DROP TABLE IF EXISTS Cars;
        CREATE TABLE Cars(Id INT, Name TEXT, Price INT);
        INSERT INTO Cars Values(1,'Audi',52642);
        INSERT INTO Cars Values(2,'Mercedes',57127);
        INSERT INTO Cars Values(3,'Skoda',9000);
        INSERT INTO Cars Values(4,'Volvo',29000);
        INSERT INTO Cars Values(5,'Bentley',35000);
        INSERT INTO Cars Values(6,'Citroen',21000);
        INSERT INTO Cars Values(7,'Hummer',41400);
        INSERT INTO Cars Values(8,'Volkswagon',21600);
        """)

    con.commit()

except lite.Error, e:

    if con:
        con.rollback()

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con:
        con.close()
