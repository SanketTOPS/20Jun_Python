import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='tempdb')
    print("Database connected!")
except Exception as e:
    print(e)

cr=dbcon.cursor()
# Create a Table
create_tbl="create table studinfo(id integer primary key auto_increment,name text,city text)"
try:
    cr.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)

# Insert data
"""insert_data="insert into studinfo(name,city)values('sanket','rajkot'),('mitesh','baroda'),('parth','navsari'),('hiren','surat'),('ashok','morbi')"
try:
    cr.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""

# Update data
"""update_data="update studinfo set city='ahmedabad' where id=4"
try:
    cr.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

# Delete data
"""delete_data="delete from studinfo where id=5"
try:
    cr.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""

# Show Data
show_data="select * from studinfo"
try:
    cr.execute(show_data)
    #data=cr.fetchall()
    #data=cr.fetchmany(2)
    data=cr.fetchone()
    print(data)
except Exception as e:
    print(e)