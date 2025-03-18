#PERSONAL EXPENSE TRACKER
import csv
import os

class ExpenseTracker():
    
    def __init__(self, fileName = "expenseTracker.csv"): 
        self.fileName = fileName
        self.headers = ["Date", "Expense", "Description", "Category"]

        #create a way to check for the referenced file; if no file create one with specific headers (should only occur once)
        if not os.path.exists(fileName):
            with open('expenseTracker.csv', 'w', newline='') as f:
                write = csv.writer(f)
                write.writerow(self.headers)


    def collect_user_expense(self):
        #Collect user expense input
        self.date = input("Expense Date? ")
        self.expense = input("How much was it? ")
        self.description = input("What store? ")
        

    def verify_category(self):
        #only certain categories are allowed, return error to reenter a possible category. error should include categories allowed.
        while True:
            try:
                category = input("What categoy should this go in? ")
                if category.lower() == "gas":
                    self.category = "gas"
                    break
                elif category.lower() == "groceries":
                    self.category = "groceries"
                    break 
                elif category.lower() == "bills":
                    self.category = "bills"
                    break 
                elif category.lower() == "fun":
                    self.category = "fun"
                    break
                elif category.lower() == "fast food":
                    self.category = "food"
                    break
                else:
                    print("Unrecognized category, try gas/groceries/bills/fun/fast food")
            except ValueError:
                print("Unrecognized category, try gas/groceries/bills/fun/fast food")


    def update_tracker(self):
        #store user input as one value
        self.NewExpense = [self.date, self.expense, self.description, self.category]    
        #write new input to csv and display contents of csv
        with open('expenseTracker.csv', 'a', newline='') as f:
            write = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            write.writerow(self.NewExpense)


    def display_expense(self):
        with open('expenseTracker.csv', 'r', newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                print(', '.join(row))


    def monthly_trends(self):
        #ask user if they want to see monthly trends for each spending category
        #(start with returning total spent in each)
        while True:
            try:
                monthlyTrend = input("Would you like to see monthly expense trends? ")
                if monthlyTrend.lower == "yes":
                    #read csv. need to sort by month, then by category, then total expense column as
                    #total for "category". should be done for all categories (5)
                    print()
                else:
                    print("User elected to pass monthly trends.")
                    break
            except ValueError:
                print("Invalid input, please enter yes or no. ")


def main():
    tracker = ExpenseTracker()
    new_expense = tracker.collect_user_expense()
    tracker.verify_category()
    tracker.update_tracker()
    tracker.display_expense()


if __name__ == "__main__":
    main()