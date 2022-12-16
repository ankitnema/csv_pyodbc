import pyodbc as odbc
import csv

connection_string = ("Driver={SQL Server Native Client 11.0};"
		     "Server=localhost\SQLEXPRESS;"
		     "Database=master;"
		     "Trusted_connection=yes;")
connection = odbc.connect(connection_string)

print ("\nDatabse connected\n")
