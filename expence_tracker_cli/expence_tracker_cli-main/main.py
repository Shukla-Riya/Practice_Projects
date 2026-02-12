class Expense:
    def __init__(self, date, amount, category, description):
        self.date = date
        self.amount = amount
        self.category = category
        self.description = description

    def __str__(self):
        return f"{self.date} | {self.amount} | {self.category} | {self.description}"
    
class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.filename = "expenses.csv"
    def add_expense(self,date,amount, category, description):
        expense = Expense(date, amount, category, description)
        self.expenses.append(expense)
        print("Entry Successful!")


    def view_expenses(self):
        if len(self.expenses) ==0:
            print("No Expense Found")
        else:
            print("\n EXPENSES")

            for i in self.expenses:
                print(i)

    def get_total_spending(self):
        return sum(expense.amount for expense in self.expenses)
    
    def get_category_summary(self):
         category_totals = {}
    
         for expense in self.expenses:
             if expense.category in category_totals:
                 category_totals[expense.category] += expense.amount
             else:
                 category_totals[expense.category] = expense.amount
    
         return category_totals


def main():
    tracker = ExpenseTracker()

    while True:
        print("\n --> EXPENSE TRACKER <--")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spending")
        print("4. View Category Summary")
        print("5. Exit")

        try:
            choice = input('\nEnter your choice: ')
        except:
            print("Enter valid choice")

        if choice == '1':
            date = input("Enter date (YY-MM-DD): ")
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            description = input("Enter discription: ")

            tracker.add_expense(date,amount,category,description)

        elif choice == '2':
            tracker.view_expenses
        
        elif choice == '3':
            total = tracker.get_total_spending
            print(f"Total spending is: ",{total})

        elif choice == '4':
            summary = tracker.get_category_summary()
            print("\n CATEGORY WISE SUMMARY")
            for category, amount in summary.items():
                print(f"{category} : {amount}")

        elif choice == '5':
            print("GOODBYE!")

if __name__ == "__main__":
    main()


