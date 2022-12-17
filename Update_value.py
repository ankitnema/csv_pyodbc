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

current_datetime = datetime.now()
print ("current time is :", current_datetime)

timestamp_str = str(current_datetime)
print (len(timestamp_str))

#------------
def Create_query(col1,col2,col3): 
    nm = "new name for the customer will be : ", name 
    tim = timestamp_str
#    ids = str(input("enter the customer id want to update : " ))
    ids = custid
    update_value = (nm, tim, ids)
    #update_value = list(update_value)
    print (update_value)

    query = "UPDATE customer_data SET customer_Name='"+nm+"', timestamp='"+tim+"' WHERE customer_id="+ids

    print(query, (nm, tim, ids))

    return(query)


#    cursor.execute(query)
#    cnxn.commit()

#--------------
with open('C:\\Users\\devops\\Desktop\\customer_data.csv', newline='') as csvfile:
    csv_data = csv.DictReader(csvfile)
    for row in csv_data:
        name = row['customer_Name']
        custid = row['customer_id']
#        sql_query = Create_query(name, timestamp_str, custid)
        query = "UPDATE customer_data SET customer_Name='"+name+"', timestamp='"+timestamp_str+"' WHERE customer_id="+custid
        print(query)

        
print("\nDatabase Update\n")

#-----------
##with open('C:\\Users\\devops\\Desktop\\customer.csv', newline='') as csvfile:
##    csv_data = csv.DictReader(csvfile)
##    for row in csv_data:
        

##
##         print(update_query,UPDAT)
##
##         cursor.execute(update_query, UPDAT) #query execution 
##cnxn.commit()       #commiting the updated data
##print("\nDatabase updated\n")

#        row_data = cursor.execute("select * from cutomer_data")
        
        
#        for row_data in cursor.fetchall():
#           print(row_data)
