#!/usr/bin/python3

def printPhilo(conn):
  # Connect and retrieve data
  cur = conn.cursor()
  sql = "SELECT name, century FROM v_philosopher"
  cur.execute(sql)
  # Fetch data line by line
  raw = cur.fetchone()
  while raw:
    print ("- %s (%s)" % (raw[0], raw[1]))
    raw = cur.fetchone()