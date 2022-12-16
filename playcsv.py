import csv as csv

with open('customer.csv', newline = '') as csvfile:
    csv_row = csv.DictReader('customer_id')
    for row in csvfile:
        print(row)
