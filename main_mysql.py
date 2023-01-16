import mysql.connector

config = {
  'user': 'root',
  'password': 'root',
  'host': 'localhost',
  'unix_socket': '/Applications/MAMP/tmp/mysql/mysql.sock',
  'database': 'test',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cursor = cnx.cursor(dictionary=True)

cursor.execute('SHOW TABLES')

for x in cursor :
  print (x)

print ('\n************************')
print('\nEmployees Table')


cursor.execute("SELECT * FROM test.Employees")
emp_result = cursor.fetchall()
print(emp_result)


print ('\n************************')
print('\nDepartment Table')

cursor.execute("SELECT * FROM test.Department")
dept_result = cursor.fetchall()
print(dept_result)

print ('\n************************')
print('\nSalaries Table')

cursor.execute("SELECT * FROM test.Salaries")
sal_result = cursor.fetchall()
print(sal_result)

print ('\n************************')



## Fragmentation

## Primary horizontal Fragmentation

# First Query

# Employees older than 30 years
# Employees older than 30 will be saved on this site
# Younger than 30 will be saved on site 2


# cursor.execute("CREATE TABLE IF NOT EXISTS q1A (SELECT * FROM test.Employees WHERE Employees.Age > 30)")

print('Employees older than 30:')
cursor.execute("SELECT * FROM q1A")
q1A_result = cursor.fetchall()
print('Q1 query in Site 1:')
print(q1A_result)


print ('\n************************')

# employees younger in a backup fragment

# cursor.execute("CREATE TABLE IF NOT EXISTS q1B_Dup (SELECT * FROM test.Employees WHERE Employees.Age < 30)")

print('Employees younger than 30:')
cursor.execute("SELECT * FROM q1B_Dup")
q1B_result = cursor.fetchall()
print('Q1 query in Site 1:')
print(q1B_result)


print ('\n************************')



# Second Query 

# Employees in the IT department ,  will be on site 1
# Other employees from the other departments will be in the other sites

#cursor.execute("CREATE TABLE IF NOT EXISTS q2A (SELECT test.Employees.Full_Name, test.Employees.Age, test.Department.Dept_Name FROM test.Employees INNER JOIN test.Department ON  test.Employees.Dept_ID = test.Department.Dept_ID WHERE test.Department.Dept_Name = 'IT')")
print('Employees in the IT department:')
cursor.execute("SELECT * FROM q2A")
q2A_result = cursor.fetchall()
print('Q2 query in Site 1:')
print(q2A_result)

print ('\n************************')

# Second query Duplicate

# cursor.execute("CREATE TABLE IF NOT EXISTS q2B_Dup (SELECT test.Employees.Full_Name, test.Employees.Age, test.Department.Dept_Name FROM test.Employees INNER JOIN test.Department ON  test.Employees.Dept_ID = test.Department.Dept_ID WHERE NOT test.Department.Dept_Name = 'IT')")
print('Employees NOT the IT department:')
cursor.execute("SELECT * FROM q2B_Dup")
q2B_result = cursor.fetchall()
print('Q2 query in Site 1:')
print(q2B_result)

print ('\n************************')

# Third Query

# Employees who earn more than 80,000 and are not from IT

#cursor.execute("CREATE TABLE IF NOT EXISTS q3A (SELECT test.Employees.Full_Name, test.Salaries.Amount, test.Department.Dept_Name FROM test.Employees JOIN test.Salaries ON test.Employees.Emp_ID = test.Salaries.Emp_ID JOIN test.Department ON test.Employees.Dept_ID = test.Department.Dept_ID WHERE NOT test.Department.Dept_Name = 'IT' AND test.Salaries.Amount > 80000)")
print('\nEmployees earning more than 80K not in IT :')
cursor.execute("SELECT * FROM q3A")
q3A_result = cursor.fetchall()
print('\n')
print(q3A_result)

# Third query Second Fragment

# Employees who earn less than 80,000 and are not from IT

# cursor.execute("CREATE TABLE IF NOT EXISTS q3B (SELECT test.Employees.Full_Name, test.Salaries.Amount, test.Department.Dept_Name FROM test.Employees JOIN test.Salaries ON test.Employees.Emp_ID = test.Salaries.Emp_ID JOIN test.Department ON test.Employees.Dept_ID = test.Department.Dept_ID WHERE NOT test.Department.Dept_Name = 'IT' AND test.Salaries.Amount < 80000)")
print('\nEmployees earning LESS than 80K NOT in IT :')
cursor.execute("SELECT * FROM q3B")
q3B_result = cursor.fetchall()
print('\n')
print(q3B_result)

# Third query Third Fragment

# Employees who earn MORE than 80,000 and ARE from IT

# cursor.execute("CREATE TABLE IF NOT EXISTS q3C (SELECT test.Employees.Full_Name, test.Salaries.Amount, test.Department.Dept_Name FROM test.Employees JOIN test.Salaries ON test.Employees.Emp_ID = test.Salaries.Emp_ID JOIN test.Department ON test.Employees.Dept_ID = test.Department.Dept_ID WHERE test.Department.Dept_Name = 'IT' AND test.Salaries.Amount > 80000)")
print('\nEmployees earning LESS than 80K AND ARE IN IT :')
cursor.execute("SELECT * FROM q3C")
q3C_result = cursor.fetchall()
print('')
print(q3C_result)

# Third query Fourth Fragment

# Employees who earn LESS than 80,000 and ARE from IT

# cursor.execute("CREATE TABLE IF NOT EXISTS q3D (SELECT test.Employees.Full_Name, test.Salaries.Amount, test.Department.Dept_Name FROM test.Employees JOIN test.Salaries ON test.Employees.Emp_ID = test.Salaries.Emp_ID JOIN test.Department ON test.Employees.Dept_ID = test.Department.Dept_ID WHERE test.Department.Dept_Name = 'IT' AND test.Salaries.Amount < 80000)")
print('\nEmployees earning LESS than 80K AND ARE in IT :')
cursor.execute("SELECT * FROM q3D")
q3D_result = cursor.fetchall()
print('')
print(q3D_result)
















  

