#!/usr/bin/python3

def quote(s):
  if s:
    return '\'%s\'' % s
  else:
    return 'NULL'

def addPhilo(conn):
  surname = quote(input("Surname : "))
  givenname = quote(input("Given name : "))
  century = int(input("Century : "))
  # Connect, execute SQL, close
  cur = conn.cursor()
  sql = "INSERT INTO philosopher VALUES (%s, %s, %i)" % (surname, givenname, century)
  cur.execute(sql)
  conn.commit()