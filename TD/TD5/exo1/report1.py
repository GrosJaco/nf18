#!/usr/bin/python3
import psycopg2

HOST = "tuxa.sme.utc"
USER = "nf18a037"
PASSWORD = "ccvfUb8wXH86"
DATABASE = "dbnf18a037"

conn = psycopg2.connect(host=HOST, dbname=DATABASE, user=USER, password=PASSWORD)
cur = conn.cursor()

print("\t[N°] Nom (Population)")

cur.execute("SELECT num, nom, population FROM dpt2 ORDER BY num;")
for num, nom, pop in cur.fetchall():
    print(f"\t[{num}] {nom} ({pop})")

cur.execute("SELECT MAX(population), MIN(population) FROM dpt2;")
max_pop, min_pop = cur.fetchone()

print()
print(f"> Département le plus peuplé :   {max_pop}")
print()
print(f"> Département le moins peuplé :  {min_pop}")

cur.close()
conn.close()