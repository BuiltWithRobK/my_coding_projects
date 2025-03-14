#PERSONAL EXPENSE TRACKER
import csv
import os


fileName = "expenseTracker.csv"
headers = ["Date", "Expense", "Description", "Category"]

#create a way to check for the referenced file; if no file create one with specific headers (should only occur once)
if not os.path.exists(fileName):
    with open('expenseTracker.csv', 'w', newline='') as f:
        write = csv.writer(f)
        write.writerow(headers)

#Collect user expense input
date = input("Expense Date? ")
expense = input("How much was it? ")
description = input("What store? ")

#only certain categories are allowed, return error to reenter a possible category. error should include categories allowed.
while True:
    try:
        category = input("What categoy should this go in? ")
        if category.lower() == "gas":
            category = "gas"
            break
        elif category.lower() == "groceries":
            category = "groceries"
            break 
        elif category.lower() == "bills":
            category = "groceries"
            break 
        elif category.lower() == "fun":
            category = "groceries"
            break
        elif category.lower() == "fast food":
            category = "groceries"
            break
        else:
            print("Unrecognized category, try gas/groceries/bills/fun/fast food")
    except ValueError:
        print("Unrecognized category, try gas/groceries/bills/fun/fast food")

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
