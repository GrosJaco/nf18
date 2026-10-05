#!/usr/bin/python3

import psycopg2

conn = psycopg2.connect("dbname='mydb' user='me' host='localhost' password='secret'")

sql = "SELECT name, population/area AS density FROM region ORDER BY density DESC";

resultat = conn.cursor()
resultat.execute(sql)

ligne = resultat.fetchone()
while ligne:
        name = ligne[0]
        density = ligne[1]
        print(name, density)
        ligne = resultat.fetchone()
        