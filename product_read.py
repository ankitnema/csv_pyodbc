"""
#Creating program to Update the SQL server through python 
#Added pandas library to read data from csv through dataframe
#Added pyodbc to connect SQl server
"""

import pandas as pd
import pyodbc

#Connecting Server 
cnxn_str = ("Driver={SQL Server Native Client 11.0};"
            "Server=localhost\SQLEXPRESS;"
            "Database=master;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)
print("\nDatabase connected \n")

#Creating cursor
cursor = cnxn.cursor()

print("Fetech all the data from table \n")
#print()
#cursor.execute("select * from customer_data")

# Defining CSV file path 
def column():
    file_csv = pd.read_csv("C:\\Users\\devops\\Desktop\\customer.csv", usecols = ['customer_id'])

    df = pd.DataFrame(file_csv)	#Dataframe created for csv file

    col = df.iloc[count, 0]

    return col

count = 0
for col_rd in open("C:\\Users\\devops\\Desktop\\customer.csv", 'r'):

 print (column())
 count=1
 
#cust_id = file_csv.customer_id

#print (file_csv)

"""
count = 0	#creating variable to use in dataframe 
#open_csv = open("C:\\Users\\devops\\Desktop\\customer.csv", "r")

for col_rd in open_csv:
  
  count+=1
  print (col_rd[0])

  

#col = df.iloc[col_rd, 0]	#extra first column value from CSV

#print(col)

##
#col1= str(col)		#converting value to string for sql
##

col1 = str(cust_id) 
data = "select * from customer_data where customer_id ="+col1	     #creating query 

print (data)

cursor.execute(data)

for row in cursor.fetchall():
  print(row)

#print(df.iloc[0, 0])

#print(file_csv.head(4))

"""
