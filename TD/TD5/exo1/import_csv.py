#!/usr/bin/python3
import psycopg2

HOST = "tuxa.sme.utc"
USER = "nf18a037"
PASSWORD = "ccvfUb8wXH86"
DATABASE = "dbnf18a037"

conn = psycopg2.connect(host=HOST, dbname=DATABASE, user=USER, password=PASSWORD)
cur = conn.cursor()

cur.execute("""
    DROP TABLE IF EXISTS dpt2;
    CREATE TABLE dpt2 (
        num VARCHAR(3) PRIMARY KEY,
        nom VARCHAR(50) NOT NULL,
        population INTEGER NOT NULL
    );
""")
conn.commit()

with open("dpt2.csv", "r", encoding="utf-8") as f:
    sql_copy = """
        COPY dpt2 (num, nom, population)
        FROM STDIN 
        WITH (FORMAT csv, HEADER true, DELIMITER ';');
    """
    cur.copy_expert(sql_copy, f)

conn.commit()

cur.close()
conn.close()