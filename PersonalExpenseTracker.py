#PERSONAL EXPENSE TRACKER
import csv

#Collect user input
date = input("Expense Date? ")
expense = input("How much was it? ")
description = input("What store? ")
category = input("What categoy should this go in? ")

#store user input as one value
NewExpense = [date, expense, description, category]

#write new input to csv and display contents of csv
with open('Expense_Tracker.csv', 'a', newline='') as f:
    write = csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    
    write.writerow(NewExpense)

with open('Expense_Tracker.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(', '.join(row))
