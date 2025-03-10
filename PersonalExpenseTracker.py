#PERSONAL EXPENSE TRACKER
import csv
import os

#create a way to check for the referenced file; if no file create one with specific headers (should only occur once)
fileName = "expenseTracker.csv"

if not os.path.exists(fileName):
    with open('expenseTracker.csv', 'w', newline='') as f:
        write = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        write.writerow("Date", "Expense", "Description", "Category")

#Collect user expense input
date = input("Expense Date? ")
expense = input("How much was it? ")
description = input("What store? ")
category = input("What categoy should this go in? ")

#store user input as one value
NewExpense = [date, expense, description, category]

#write new input to csv and display contents of csv
with open('expenseTracker.csv', 'a', newline='') as f:
    write = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    write.writerow(NewExpense)

with open('expenseTracker.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(', '.join(row))
