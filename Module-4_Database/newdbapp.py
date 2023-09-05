import sqlite3

#Database connect
try:
    dbcon=sqlite3.connect('sampledb.db')
    print("Database connected!")
except Exception as e:
    print(e)

# Create a Table
create_tbl="create table studinfo(id integer primary key autoincrement,name text,city text)"
try:
    dbcon.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)

# Insert data
"""insert_data="insert into studinfo(name,city)values('sanket','rajkot'),('mitesh','baroda'),('parth','navsari'),('hiren','surat'),('ashok','morbi')"
try:
    dbcon.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""

# Update data
"""update_data="update studinfo set city='ahmedabad' where id=4"
try:
    dbcon.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

# Delete data
"""delete_data="delete from studinfo where id=5"
try:
    dbcon.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""

# Show Data
cr=dbcon.cursor()
show_data="select * from studinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchmany(3)
    #data=cr.fetchone()
    #print(data)

    for i in data:
        print(i)
        #print(i[2])

except Exception as e:
    print(e)

    
