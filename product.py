import pyodbc

cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=localhost\SQLEXPRESS;"
            "Database=master;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)
print("\nDatabase connected \n")
cursor = cnxn.cursor()
print("Fetech all the data from table \n")
#print()
row = cursor.execute("select * from customer_data")
   
for row in cursor.fetchall():
    print (row)

