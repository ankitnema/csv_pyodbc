#creating programm to updste data from in SQL database from CSV file
#import library to work with csv file
#import library pyodbc to connect with SQL server to performt the opration
#connect the SQL database with server details 
#create a function which creates the sqlquery 
#read the CSV file with Dict.reader, here you can read the perticular column data

import csv
import pyodbc

#connect with SQL server
cnxn_str = ("Driver={SQL Server Native Client 11.0};"  #database name should be within {}
            "Server=localhost\SQLEXPRESS;"
            "Database=master;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)

print("\nDatabase connected\n")

#create cursor
cursor = cnxn.cursor()

#Define function
def update_col(col1,col2):
    id_val=str(colid)
    updt_name=str(name)
    query="Update customer_data SET customer_Name= '"+updt_name+ "' Where customer_id="+colid

    return query


#with open('C:\\Users\\devops\\Desktop\\customer.csv', newline='') as csvfile:
#  csvdata = csv.DictReader(csvfile)

#create 'for loop' to read and use the customer_id one by one
#  for row in csvdata:
#   col = row['customer_id']
#    print(row['customer_id'])


#processing CSV file

with open('C:\\Users\\devops\\Desktop\\customer.csv', newline='') as csvfile:
    csv_data = csv.DictReader(csvfile)
#    print('customer_id customer_Name customer_address customer_Mob')

    for value in csv_data: #Create loop to extract id one by one
        print(value['customer_id'],value['customer_Name'],value['customer_address'],value['customer_Mob'])

        colid=value['customer_id']
        name=value['customer_Name']
        update_column= update_col(colid,name)

        print(update_column)

        cursor.execute(update_column) #query execution 
        cnxn.commit()       #commiting the updated data
        print("\nDatabase updated")

        
#        for row_data in cursor.fetchall():
#           print(row_data)
