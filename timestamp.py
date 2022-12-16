from datetime import datetime

current_datetime = datetime.now()
print ("Currrent time is : ", current_datetime)

timestamp_str = str(current_datetime)
#print (len(timestamp_str))

date = current_datetime.strftime("%d%m%y")
print(date)
print(current_datetime.day)

