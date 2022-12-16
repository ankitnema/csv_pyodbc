import csv
import pyodbc

#connect with SQL server
cnxn_str = ("Driver={SQL Server Native Client 11.0};"  #database name should be within {}
            "Server=localhost\SQLEXPRESS;"
            "Database=master;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)

print("\nDatabase connected\n")

#create cursor to fetch all the data
cursor = cnxn.cursor()

row = cursor.execute('select * from customer_data')

for row_data in cursor.fetchall():
          print(row_data)
