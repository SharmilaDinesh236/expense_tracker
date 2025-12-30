from tracker import ExpenseTracker

def main():
    tracker = ExpenseTracker("expenses.csv")

    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Expense")
        print("2. View Monthly Report")
        print("3. Generate Pie Chart")
        print("4. Generate Bar Chart")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            date = input("Date (YYYY-MM-DD): ")
            category = input("Category: ")
            amount = float(input("Amount: "))
            desc = input("Description: ")

            tracker.add_expense(date, category, amount, desc)

        elif choice == "2":
            month = input("Enter month (YYYY-MM): ")
            tracker.monthly_report(month)

        elif choice == "3":
            month = input("Enter month (YYYY-MM): ")
            tracker.pie_chart(month)

        elif choice == "4":
            month = input("Enter month (YYYY-MM): ")
            tracker.bar_chart(month)

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
