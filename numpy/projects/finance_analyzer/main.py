import numpy as np
import json
import os
from datetime import datetime

# -------------
# Student Class
# -------------

class Student:

    def __init__(self, name, department, semester):
        self.name = name
        self.department = department
        self.semester = semester

    def display_info(self):
        print("\n----- Student Information -----")
        print("Name:", self.name)
        print("Department:", self.department)
        print("Semester:", self.semester)

# ---------------
# Finance Manager
# ---------------

class FinanceManager:

    def __init__(self):
        self.income = 0
        self.expenses = []
        self.budget = 0

    # -------
    # Income
    # -------

    def add_income(self):
        while True:
            try:
                amount = float(input("Enter your monthly income: "))

                if amount <= 0:
                    print("Income must be greater than 0.")
                    continue

                self.income = amount
                print("Income added successfully.")
                break

            except ValueError:
                print("Please enter a valid number.")

    # -------
    # Budget
    # -------

    def set_budget(self):
        while True:
            try:
                amount = float(input("Enter your monthly budget: "))

                if amount <= 0:
                    print("Budget must be greater than 0.")
                    continue

                self.budget = amount
                print("Budget set successfully.")
                break

            except ValueError:
                print("Please enter a valid number.")

    # -------------
    # Add Expense
    # -------------

    def add_expense(self):

        description = input("Enter expense description: ")

        print("\nCategories:")
        print("1. Food")
        print("2. Transport")
        print("3. Education")
        print("4. Bills")
        print("5. Shopping")
        print("6. Entertainment")
        print("7. Other")

        category_choice = input("Choose category: ")

        categories = {
            "1": "Food",
            "2": "Transport",
            "3": "Education",
            "4": "Bills",
            "5": "Shopping",
            "6": "Entertainment",
            "7": "Other"
        }

        if category_choice not in categories:
            print("Invalid category.")
            return

        category = categories[category_choice]

        while True:
            try:
                amount = float(input("Enter expense amount: "))

                if amount <= 0:
                    print("Amount must be greater than 0.")
                    continue

                break

            except ValueError:
                print("Please enter a valid number.")

        expense = {
            "description": description,
            "category": category,
            "amount": amount,
            "date": datetime.now().strftime("%Y-%m-%d")
        }

        self.expenses.append(expense)

        print("Expense added successfully.")

    # -----------------
    # Display Expenses
    # -----------------

    def show_expenses(self):

        if len(self.expenses) == 0:
            print("\nNo expenses have been added yet.")
            return

        print("\n------------- Expenses -------------")

        for i, expense in enumerate(self.expenses, start=1):

            print(
                f"{i}. "
                f"{expense['description']:<8} | "
                f"{expense['category']:<15} | "
                f"Rs. {expense['amount']:>10.2f} | "
                f"{expense['date']:>10}"
            )

    # ---------------
    # NumPy Analysis
    # ---------------

    def analyze_expenses(self):

        if len(self.expenses) == 0:
            print("\nNo expenses available for analysis.")
            return

        amounts = []

        for expense in self.expenses:
            amounts.append(expense["amount"])

        # Convert Python list into NumPy array
        expense_array = np.array(amounts)

        total = np.sum(expense_array)
        average = np.mean(expense_array)
        highest = np.max(expense_array)
        lowest = np.min(expense_array)

        print("\n========== Expense Analysis ==========")

        print(f"Total Expenses: Rs. {total:.2f}")
        print(f"Average Expense: Rs. {average:.2f}")
        print(f"Highest Expense: Rs. {highest:.2f}")
        print(f"Lowest Expense: Rs. {lowest:.2f}")

        # --------
        # Savings
        # --------

        savings = self.income - total

        print(f"Monthly Income: Rs. {self.income:.2f}")
        print(f"Remaining Money: Rs. {savings:.2f}")

        if savings > 0:
            print("Status: You are saving money.")
        elif savings == 0:
            print("Status: You used all your income.")
        else:
            print("Status: You are spending more than your income.")

    # ------------------
    # Category Analysis
    # ------------------

    def category_analysis(self):

        if len(self.expenses) == 0:
            print("\nNo expenses available.")
            return

        category_totals = {}

        for expense in self.expenses:

            category = expense["category"]
            amount = expense["amount"]

            if category in category_totals:
                category_totals[category] += amount
            else:
                category_totals[category] = amount

        print("\n========== Category Analysis ==========")

        for category, amount in category_totals.items():

            print(f"{category}: Rs. {amount:.2f}")

        # Find category with highest spending

        highest_category = max(
            category_totals,
            key=category_totals.get
        )

        print(
            f"\nHighest Spending Category: "
            f"{highest_category}"
        )

        print(
            f"Amount Spent: "
            f"Rs. {category_totals[highest_category]:.2f}"
        )

    # ----------------
    # Budget Analysis
    # ----------------

    def budget_analysis(self):

        if self.budget == 0:
            print("\nPlease set your budget first.")
            return

        total_expenses = 0

        for expense in self.expenses:
            total_expenses += expense["amount"]

        print("\n========== Budget Analysis ==========")

        print(f"Budget: Rs. {self.budget:.2f}")
        print(f"Spent: Rs. {total_expenses:.2f}")

        remaining = self.budget - total_expenses

        if remaining > 0:

            print(
                f"Remaining Budget: "
                f"Rs. {remaining:.2f}"
            )

            percentage = (total_expenses / self.budget) * 100

            print(
                f"Budget Used: "
                f"{percentage:.2f}%"
            )

        elif remaining == 0:

            print("You have used your entire budget.")

        else:

            exceeded = abs(remaining)

            print(
                f"Budget exceeded by: "
                f"Rs. {exceeded:.2f}"
            )

    # ------------------------
    # Simple Financial Advice
    # ------------------------

    def give_advice(self):

        if len(self.expenses) == 0:
            print("\nAdd some expenses first.")
            return

        total = 0

        for expense in self.expenses:
            total += expense["amount"]

        print("\n========== Financial Advice ==========")

        if self.income == 0:
            print("Add your income first.")
            return

        spending_percentage = (total / self.income) * 100

        if spending_percentage < 50:

            print(
                "Your spending is relatively low."
            )
            print(
                "You have a good amount of money left."
            )

        elif spending_percentage < 80:

            print(
                "Your spending is moderate."
            )
            print(
                "Keep monitoring your expenses."
            )

        elif spending_percentage <= 100:

            print(
                "You are using most of your income."
            )
            print(
                "Try to reduce unnecessary expenses."
            )

        else:

            print(
                "Warning: Your expenses are higher "
                "than your income."
            )
            print(
                "You should review your spending."
            )

# -----------
# Save Data
# -----------

def save_data(student, finance):

    data = {

        "student": {
            "name": student.name,
            "department": student.department,
            "semester": student.semester
        },

        "finance": {
            "income": finance.income,
            "budget": finance.budget,
            "expenses": finance.expenses
        }
    }

    with open("finance_data.json", "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )

    print("\nData saved successfully.")

# -----------
# Load Data
# -----------

def load_data(finance):

    if not os.path.exists("finance_data.json"):
        return

    try:

        with open("finance_data.json", "r") as file:

            data = json.load(file)

        finance.income = data["finance"]["income"]
        finance.budget = data["finance"]["budget"]
        finance.expenses = data["finance"]["expenses"]

        print("Previous financial data loaded.")

    except (json.JSONDecodeError, KeyError):

        print("Could not load previous data.")

# ---------------
# Monthly Report
# ---------------

def monthly_report(student, finance):

    print("\n")
    print("=" * 45)
    print("        MONTHLY FINANCE REPORT")
    print("=" * 45)

    print("\nStudent:", student.name)
    print("Department:", student.department)
    print("Semester:", student.semester)

    print("\nIncome:")
    print(f"Rs. {finance.income:.2f}")

    total_expenses = 0

    for expense in finance.expenses:
        total_expenses += expense["amount"]

    print("\nTotal Expenses:")
    print(f"Rs. {total_expenses:.2f}")

    savings = finance.income - total_expenses

    print("\nRemaining Money:")
    print(f"Rs. {savings:.2f}")

    if finance.budget > 0:

        print("\nBudget:")
        print(f"Rs. {finance.budget:.2f}")

        if total_expenses > finance.budget:

            print("Budget Status: Exceeded")

        else:

            print("Budget Status: Within Budget")

    print("\nNumber of Expenses:")
    print(len(finance.expenses))

    print("=" * 45)

# ---------------
# Main Program
# ---------------

def main():

    print("=" * 45)
    print("   STUDENT MONTHLY EXPENSE ANALYZER")
    print("=" * 45)

    # --------------------
    # Student Information
    # --------------------

    name = input("\nEnter your name: ")
    department = input("Enter your department: ")
    semester = input("Enter your semester: ")

    student = Student(
        name,
        department,
        semester
    )

    finance = FinanceManager()

    # Load previous data
    load_data(finance)

    # ----------
    # Main Menu
    # ----------

    while True:

        print("\n")
        print("========== MAIN MENU ==========")

        print("1. Show Student Information")
        print("2. Add Monthly Income")
        print("3. Set Monthly Budget")
        print("4. Add Expense")
        print("5. Show All Expenses")
        print("6. Analyze Expenses")
        print("7. Category Analysis")
        print("8. Budget Analysis")
        print("9. Financial Advice")
        print("10. Monthly Report")
        print("11. Save Data")
        print("12. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            student.display_info()

        elif choice == "2":

            finance.add_income()

        elif choice == "3":

            finance.set_budget()

        elif choice == "4":

            finance.add_expense()

        elif choice == "5":

            finance.show_expenses()

        elif choice == "6":

            finance.analyze_expenses()

        elif choice == "7":

            finance.category_analysis()

        elif choice == "8":

            finance.budget_analysis()

        elif choice == "9":

            finance.give_advice()

        elif choice == "10":

            monthly_report(
                student,
                finance
            )

        elif choice == "11":

            save_data(
                student,
                finance
            )

        elif choice == "12":

            save_data(
                student,
                finance
            )

            print("\nThank you for using the program.")
            break

        else:

            print("Invalid choice. Please try again.")

# --------------
# Start Program
# --------------

if __name__ == "__main__":
    main()
