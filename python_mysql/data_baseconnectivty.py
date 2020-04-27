import mysql.connector

conn = mysql.connector.connect(
    host='localhost', user='root', password='12ajayteja', database='new_database')

my_cursor = conn.cursor()

#query = "CREATE DATABASE new_database"
#query = "show databases"
# query = "create table student(name varchar(255),age int)
#query = "insert into students(name,age) values (%s, %s)"
values = [
    ('ajay', 19),
    ('sai', 22),
    ('shrisha', 24),
    ('thrinath', 59),
    ('swarupa', 53),
    ('shakunthala', 72)
]
query = "SELECT * FROM students"
my_cursor.execute(query)
for row in my_cursor:
    print(row)

# for database_name in my_cursor:
#   print(database_name)
# print(my_cursor.fetchall())
conn.commit()
conn.close()
