import pyodbc

#x = open("costomer1", "r")
cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=localhost\SQLEXPRESS;"
            "Database=master;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)
print("\nDatabase connected \n")
cursor = cnxn.cursor()

print("run bulk insert fromt the csv file\n")

query=("BULK insert customer_data FROM 'C:\\Users\\devops\\Desktop\\costomer1.csv' WITH (FIELDTERMINATOR=',', ROWTERMINATOR='\\n', FIRSTROW= 2)")
cursor.execute(query)   
cnxn.commit()
cursor.close()

print("\nInsert completed\n")
#x.close()