import csv
import matplotlib.pyplot as plt
from collections import defaultdict
import os

class ExpenseTracker:
    def __init__(self, filename):
        self.filename = filename

        # Create CSV file if it doesn't exist
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["date", "category", "amount", "description"])

    def add_expense(self, date, category, amount, description):
        with open(self.filename, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([date, category, amount, description])
        print("✅ Expense added successfully!")

    def read_expenses(self):
        expenses = []
        with open(self.filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                expenses.append(row)
        return expenses

    def monthly_report(self, month):
        expenses = self.read_expenses()
        totals = defaultdict(float)

        for e in expenses:
            if e["date"].startswith(month):
                totals[e["category"]] += float(e["amount"])

        if not totals:
            print("⚠️ No data found for this month.")
            return

        print(f"\n📊 Expense Report for {month}")
        for category, amount in totals.items():
            print(f"{category}: ₹{amount}")

    def pie_chart(self, month):
        expenses = self.read_expenses()
        totals = defaultdict(float)

        for e in expenses:
            if e["date"].startswith(month):
                totals[e["category"]] += float(e["amount"])

        if not totals:
            print("⚠️ No data available for chart.")
            return

        plt.figure()
        plt.pie(totals.values(), labels=totals.keys(), autopct="%1.1f%%")
        plt.title(f"Expense Distribution - {month}")
        plt.show()

    def bar_chart(self, month):
        expenses = self.read_expenses()
        totals = defaultdict(float)

        for e in expenses:
            if e["date"].startswith(month):
                totals[e["category"]] += float(e["amount"])

        if not totals:
            print("⚠️ No data available for chart.")
            return

        plt.figure()
        plt.bar(totals.keys(), totals.values())
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.title(f"Expenses by Category - {month}")
        plt.show()
