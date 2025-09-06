import sqlite3

# create a database
connection = sqlite3.connect('student.db')

# create a cursor
cursor = connection.cursor()
# create a table
create_table_query = '''
CREATE TABLE IF NOT EXISTS students (
    Name VARCHAR(25),
    Age INT,
    Gender VARCHAR(10),
    Course VARCHAR(25),
    Section VARCHAR(25),
    Marks INT
);
'''
cursor.execute(create_table_query)

# insert data into the table
sql_query = '''
INSERT INTO students (Name, Age, Gender, Course, Section, Marks)
    VALUES (?, ?, ?, ?, ?, ?);
''' 
data = [
    ('Alice', 25, 'Female', 'Computer Science', 'A', 85),
    ('Bob', 23, 'Male', 'Mathematics', 'B', 90),
    ('Charlie', 24, 'Female', 'Physics', 'A', 78),
    ('Alaa', 24, 'Male', 'Data Science', 'C', 95),
    ('Eve', 22, 'Female', 'Chemistry', 'B', 88)
]

cursor.executemany(sql_query, data)
connection.commit()

# fetch all records from the table
data = cursor.execute('SELECT * FROM students;').fetchall()

for row in data:
    print(row)

# close the connection
if connection:
    connection.close()
    