#!/usr/bin/python3
import psycopg2
import display

HOST = "tuxa.sme.utc"
USER = "nf18a037"
PASSWORD = "ccvfUb8wXH86"
DATABASE = "dbnf18a037"

conn = psycopg2.connect(host=HOST, dbname=DATABASE, user=USER, password=PASSWORD)

while True:
    login = input("Entrez le login de l'étudiant recherché (entrez 0 pour sortir) : ").strip()
    
    if login == '0':
        break
    if not login:
        continue

    display.display(conn, login)
    print()

conn.close()