#creating programm to extract data from in SQL database with keys from CSV file
#import library to work with csv file
#import library pyodbc to connect with SQL server to performt the opration
#connect the SQL database with server details 
#create a function which creates the sqlquery 
#read the CSV file with Dict.reader(), here you can read the perticular column data

import csv
import pyodbc

#Connecting database Server 
cnxn_str = ("Driver={SQL Server Native Client 11.0};" #database name should be within {}
            "Server=localhost\SQLEXPRESS;"
            "Database=master;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)
print("\nDatabase connected \n")

#Creating cursor
cursor = cnxn.cursor()

#print("Fetech all the data from table \n")

#defining function to create SQL query
def select_col(a):
  col1= str(col)
  fetch_data = "select * from customer_data where customer_id ="+col1	     #creating query 

  return fetch_data

#-----CSV-----#
with open('C:\\Users\\devops\\Desktop\\customer.csv', newline='') as csvfile:
  csvdata = csv.DictReader(csvfile)

#create 'for loop' to read and use the customer_id one by one
  for id_value in csvdata:
   col = id_value['customer_id']
#  print(row['customer_id'])
#  print(col)
   column_in = select_col(col)  #calling the function to create select query 
   print(column_in)             #Display the created query
   cursor.execute(column_in)    #execute the slect query

   for row_data in cursor.fetchall():
     print(row_data)


#
#column = select_col(col)
#   print (column)
   


		#converting value to string for sql

# col1 = str(cust_id) 
#fetch_data = "select * from customer_data where customer_id ="+col1	     #creating query 

# return fetch_data


