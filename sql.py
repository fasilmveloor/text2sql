import sqlite3

# connecting to sqlite 3
connection = sqlite3.connect('sql.db')

# cursor
cursor = connection.cursor()

# create table
table_info = """
Create table STUDENT(NAME VARCHAR(20), CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""

# execute
cursor.execute(table_info)

# insert records
cursor.execute("INSERT INTO STUDENT VALUES('John', '12th', 'A', 90)")
cursor.execute("INSERT INTO STUDENT VALUES('Jane', '12th', 'A', 80)")
cursor.execute("INSERT INTO STUDENT VALUES('Jim', '10th', 'B', 70)")
cursor.execute("INSERT INTO STUDENT VALUES('Jack', '10th', 'B', 60)")
cursor.execute("INSERT INTO STUDENT VALUES('Jill', '10th', 'B', 50)")

# display all records
print('Inserted records are:')

data = cursor.execute("SELECT * FROM STUDENT")

for row in data:
    print(row)

# close the connection
connection.commit()
connection.close()
