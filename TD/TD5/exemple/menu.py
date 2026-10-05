#!/usr/bin/python3

import psycopg2
import TD5.exemple.forms as forms
import TD5.exemple.reports as reports

HOST = "tuxa.sme.utc"
USER = "nf18a037"
PASSWORD = "ccvfUb8wXH86"
DATABASE = "dbnf18a037"

conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))

choice = '1'
while choice == '1' or choice == '2':
    print ("Pour ajouter un philosophe à la base, entrez 1")
    print ("Pour voir la liste des philosophes, entrez 2")
    print ("Pour sortir, entrez autre chose")

    choice = input()  

    if choice == '1':
        forms.addPhilo(conn)
    if choice == '2':
        reports.printPhilo(conn)

    print(choice)

conn.close()
