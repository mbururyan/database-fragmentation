import sqlite3
import mysql.connector

connection_obj = sqlite3.connect('test.db')

cursor_sqlite = connection_obj.cursor()


config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
  'database': 'test',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cursor_local = cnx.cursor(dictionary=True)

# Creating tables
#First dropping some tables
#cursor_sqlite.execute("DROP TABLE doctors")
#cursor_sqlite.execute("DROP TABLE q2B")

#Create q1B fragment table
#cursor_sqlite.execute("CREATE TABLE IF NOT EXISTS q1B (Emp_ID VARCHAR(255) PRIMARY KEY, Full_Name VARCHAR(255), Age INT, Dept_ID VARCHAR(255))")
print("Query 1 Fragment B successfully created")
print("")

#Check all the available tables in the sqlite database
cursor_sqlite.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor_sqlite.fetchall())

print ('\n************************')

# Horizontal fragmentation on site 2

# Employees younger than 30 years

print('Employees younger than 30:')
print('Located at site 2 @ q1B')
cursor_local.execute("SELECT * FROM test.Employees WHERE Employees.Age < 30")
q1B_result = cursor_local.fetchall()
print(q1B_result)


# Insert into the q2B fragment
cursor_sqlite.execute("DELETE FROM q1B")
query_q1B_values = [('E1', 'Ryan Mburu', 23, 'D1'), ('E3', 'Agnes Nzembi', 29, 'D1'), ('E6', 'Sospeter Otieno', 24, 'D1')]
insert_query = "INSERT INTO q1B (Emp_ID, Full_Name, Age, Dept_ID) VALUES (?, ?, ?, ?)"
cursor_sqlite.executemany(insert_query, query_q1B_values)
connection_obj.commit()

# Print the q2B fragment
cursor_sqlite.execute("SELECT * FROM q1B")
q1B_result = cursor_sqlite.fetchall()
print(q1B_result)

print ('\n************************')

#Create q1B fragment table
cursor_sqlite.execute("CREATE TABLE IF NOT EXISTS q2B (Full_Name VARCHAR(255), Age INT, Dept_Name VARCHAR(255))")
print("Query 2 Fragment B successfully created")
print("")

#Check all the available tables in the sqlite database
cursor_sqlite.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor_sqlite.fetchall())

print ('\n************************')

# Horizontal fragmentation on site 2

# Employees younger than 30 years

print('Employees NOT IN THE IT Department:')
print('Located at site 2 @ q2B')
cursor_local.execute("SELECT test.Employees.Full_Name, test.Employees.Age, test.Department.Dept_Name FROM test.Employees INNER JOIN test.Department ON  test.Employees.Dept_ID = test.Department.Dept_ID WHERE test.Department.Dept_Name = 'IT'")
q2B_result = cursor_local.fetchall()
print(q2B_result)

print ('\n************************')

# Employees who earn less than 80,000 and are not from IT

#Create q1B fragment table
cursor_sqlite.execute("CREATE TABLE IF NOT EXISTS q3B (Full_Name VARCHAR(255), Salaries INT, Dept_Name VARCHAR(255))")
print("Query 3 Fragment B successfully created")
print("")

#Check all the available tables in the sqlite database
cursor_sqlite.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor_sqlite.fetchall())

#cursor.execute("CREATE TABLE IF NOT EXISTS q3A (SELECT test.Employees.Full_Name, test.Salaries.Amount, test.Department.Dept_Name FROM test.Employees JOIN test.Salaries ON test.Employees.Emp_ID = test.Salaries.Emp_ID JOIN test.Department ON test.Employees.Dept_ID = test.Department.Dept_ID WHERE NOT test.Department.Dept_Name = 'IT' AND test.Salaries.Amount > 80000)")
print('Employees earning less than 80K not in IT :')
print('Located at site 3 @ q3B')
cursor_local.execute("SELECT test.Employees.Full_Name, test.Salaries.Amount, test.Department.Dept_Name FROM test.Employees JOIN test.Salaries ON test.Employees.Emp_ID = test.Salaries.Emp_ID JOIN test.Department ON test.Employees.Dept_ID = test.Department.Dept_ID WHERE NOT test.Department.Dept_Name = 'IT' AND test.Salaries.Amount < 80000")
q3B_result = cursor_local.fetchall()
print('Q3 query in Site 2:')
print(q3B_result)











