# The fragments will be reconstructed to check if the reconstruction indicator of fragmentation is satisfied.

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

print ('Reconstruction of the Fragments')
print('')

print('***************************************')
print('')

print("All tables available in sqlite db: ")
cursor_sqlite.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor_sqlite.fetchall())
print('')

print('Query 1')

# Display Q1A table

print('Employees over 30')
cursor_local.execute('SELECT * FROM q1A')
q1A_result = cursor_local.fetchall()
print(q1A_result)
print('')

# Display Q1B table

print('Employees under 30')
cursor_local.execute('SELECT * FROM q1B_Dup')
q1B_result = cursor_local.fetchall()
print(q1B_result)
print('')

# Reconstruct the two fragments
print('Q1 reconstructed')
merge_query = "SELECT * FROM q1A UNION SELECT * FROM q1B_Dup"
cursor_local.execute(merge_query)
merge_Q1 = cursor_local.fetchall()
print(merge_Q1)
print('')



## QUERY 2

print('Query 2')
print('')

# Display Q2A table
print('Employees from IT')
cursor_local.execute('SELECT * FROM q2A')
q2A_result = cursor_local.fetchall()
print(q2A_result)
print('')

# Display Q2B table
print('Employees not from IT')
cursor_local.execute('SELECT * FROM q2B_Dup')
q2B_result = cursor_local.fetchall()
print(q2B_result)
print('')

# Reconstruct the two fragments
print('Q2 reconstructed')
merge_query = "SELECT * FROM q2A UNION SELECT * FROM q2B_Dup"
cursor_local.execute(merge_query)
merge_Q2 = cursor_local.fetchall()
print(merge_Q2)
print('')


## QUERY 3

print('Query 3')
print('')

# Display Q3A table
print('Employees earning more than 80K not in IT :')
cursor_local.execute('SELECT * FROM q3A')
q3A_result = cursor_local.fetchall()
print(q3A_result)
print('')

# Display Q3B table
print('Employees earning LESS than 80K not in IT :')
cursor_local.execute('SELECT * FROM q3B')
q3B_result = cursor_local.fetchall()
print(q3B_result)
print('')

# Display Q3C table
print('Employees earning MORE than 80K IN IT :')
cursor_local.execute('SELECT * FROM q3C')
q3C_result = cursor_local.fetchall()
print(q3C_result)
print('')

# Display Q3D table
print('Employees earning LESS than 80K IN IT :')
cursor_local.execute('SELECT * FROM q3D')
q3D_result = cursor_local.fetchall()
print(q3D_result)
print('')



# Reconstruct the two fragments
print('Q3 Reconstructed')
merge_query = "SELECT * FROM q3A UNION SELECT * FROM q3B UNION SELECT * FROM q3C UNION SELECT * FROM q3D "
cursor_local.execute(merge_query)
merge_Q3 = cursor_local.fetchall()
print(merge_Q3)
print('')





