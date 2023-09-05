import sqlite3

# Create a database
try:
    dbcon=sqlite3.connect('testdb.db')
    print("Database connected")
except Exception as e:
    print(e)

# Table Create
create_tbl="create table studinfo(id integer primary key autoincrement,name text,sub text)"
try:
    dbcon.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)