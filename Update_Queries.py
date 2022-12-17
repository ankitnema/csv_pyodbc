#creating programm to updste data from in SQL database from CSV file
#import library to work with csv file
#import library pyodbc to connect with SQL server to performt the opration
#connect the SQL database with server details 
#create a function which creates the sqlquery 
#read the CSV file with Dict.reader, here you can read the perticular column data

import csv
import pyodbc
from datetime import datetime

#connect with SQL server
cnxn_str = ("Driver={SQL Server Native Client 11.0};"  #database name should be within {}
            "Server=localhost\SQLEXPRESS;"
            "Database=master;"
            "Trusted_Connection=yes;")
cnxn = pyodbc.connect(cnxn_str)

print("\nDatabase connected\n")

#create cursor
cursor = cnxn.cursor()

#---------------------------------------------------
#Define function for creating update query in table

def update_col(col1,col2):

    id_val=str(col1)
    updt_colmn=str(col2)

#format 1 direct update
#    query="Update customer_data SET customer_Name= 'Kathey Milon' Where customer_id="+colid

#format 2 with multiple columns
    query="Update customer_data\
             SET customer_Name= '"+updt_colmn+"',\
                 timestamp='"+timestamp_str+"'\
             Where customer_id="+colid

#format 3 all columns with %s
    query="Update customer_data SET customer_Name=%s, customer_address=%s, customer_Mob=%s, timestamp=%s WHERE customer_id=%s"

    return query

#----------------------------------------------------

current_datetime = datetime.now()
#print ("current time is :", current_datetime)

timestamp_str = str(current_datetime)
#print (len(timestamp_str))


#with open('C:\\Users\\devops\\Desktop\\customer.csv', newline='') as csvfile:
#  csvdata = csv.DictReader(csvfile)

#create 'for loop' to read and use the customer_id one by one
#  for row in csvdata:
#   col = row['customer_id']
#    print(row['customer_id'])


#processing CSV file

with open('C:\\Users\\devops\\Desktop\\customer_data.csv', newline='') as csvfile:
    csv_data = csv.DictReader(csvfile)
#    print('customer_id customer_Name customer_address customer_Mob timestamp')

    for value in csv_data: #Create loop to extract id one by one
#        val = (value['customer_Name'],value['customer_address'],value['customer_Mob'],value['timestamp'],value['customer_id'])
#        val_str = str(val)
#        print(value['customer_id'],value['customer_Name'],value['customer_address'],value['customer_Mob'],value['timestamp'])

        ids=value['customer_id']
        nm=value['customer_Name']
        add=value['customer_address']
        mob=value['customer_Mob']
        tim=value['timestamp']
        _list_ = (nm, add, mob, tim, ids)
#        update_query= update_col(colid,up_col)
        update_query="Update customer_data SET customer_Name='%s', customer_address='%s', customer_Mob='%s', timestamp='%s' WHERE customer_id=%s"


        print(update_query % _list_)

        cursor.execute(update_query %_list_) #query execution 
        cnxn.commit()       #commiting the updated data
#        print("\nDatabase updated\n")

#        row_data = cursor.execute("select * from cutomer_data")
        
        
#        for row_data in cursor.fetchall():
#           print(row_data)
