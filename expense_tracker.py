from datetime import datetime


# =========================
# PERSONAL EXPENSE TRACKER
# =========================

print("=== PERSONAL EXPENSE TRACKER ===")
print("Project 4")
print("Built by Obedience Jay 🚀")
print()

expenses = []
categories = {}


# =========================
# LOAD SAVED EXPENSES
# =========================

try:
    with open("expenses.txt", "r") as file:

        for line_number, line in enumerate(file, start=1):

            line = line.strip()

            if not line:
                continue

            try:
                parts = line.split(" | ")

                if len(parts) != 4:
                    raise ValueError("expected 4 fields")

                name = parts[0].strip()

                if not name:
                    raise ValueError("expense name is empty")

                amount_text = (
                    parts[1]
                    .replace("₦", "")
                    .replace(",", "")
                    .strip()
                )

                amount = float(amount_text)

                if amount <= 0:
                    raise ValueError(
                        "amount must be greater than zero"
                    )

                category = parts[2].strip().lower()
                date = parts[3].strip()

                parsed_date = datetime.strptime(
                    date,
                    "%Y-%m-%d"
                )

                if date != parsed_date.strftime("%Y-%m-%d"):
                    raise ValueError("invalid date")

                expense = {
                    "name": name,
                    "amount": amount,
                    "category": category,
                    "date": date
                }

                expenses.append(expense)

                if category not in categories:
                    categories[category] = 0

                categories[category] += amount

            except (ValueError, TypeError) as error:

                print(
                    f"Warning: Skipping invalid record "
                    f"on line {line_number}: {error}"
                )

    print("Saved expenses loaded successfully.")

except FileNotFoundError:

    print(
        "No saved expenses file found. "
        "Starting fresh."
    )


# =========================
# ADD EXPENSES
# =========================

while True:

    print()

    expense_name = input(
        "Enter expense name (or done to finish): "
    ).strip()

    if expense_name.lower() == "done":
        break

    if not expense_name:

        print("Expense name cannot be empty.")
        continue

    print("Expense recorded:", expense_name)


    # =========================
    # AMOUNT VALIDATION
    # =========================

    while True:

        try:

            amount_input = input(
                "Enter expense amount: "
            ).strip()

            amount = float(
                amount_input.replace(",", "")
            )

            if amount <= 0:

                print(
                    "Amount must be greater than zero."
                )

                continue

            break

        except ValueError:

            print(
                "Invalid amount. Please enter a number."
            )

    print(f"Amount recorded: ₦{amount:,.2f}")


    # =========================
    # CATEGORY VALIDATION
    # =========================

    allowed_categories = [
        "food",
        "data",
        "transport",
        "rent",
        "bills",
        "health",
        "other"
    ]

    while True:

        category = input(
            "Enter expense category "
            "(food/data/transport/rent/bills/health/other): "
        ).strip().lower()

        if category not in allowed_categories:

            print(
                "Invalid category. Please choose from "
                "food, data, transport, rent, bills, health, or other."
            )

            continue

        break

    print("Category recorded:", category)


    # =========================
    # DATE VALIDATION
    # =========================

    while True:

        date = input(
            "Enter expense date (YYYY-MM-DD): "
        ).strip()

        try:

            parsed_date = datetime.strptime(
                date,
                "%Y-%m-%d"
            )

            if date != parsed_date.strftime("%Y-%m-%d"):
                raise ValueError

            break

        except ValueError:

            print(
                "Invalid date. Please use YYYY-MM-DD."
            )

    print("Date recorded:", date)


    # =========================
    # SAVE EXPENSE IN MEMORY
    # =========================

    expense = {
        "name": expense_name,
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)

    if category not in categories:
        categories[category] = 0

    categories[category] += amount

    print()
    print("Expense added successfully.")


# =========================
# SAVE EXPENSES
# =========================

print()
print("=== SAVE EXPENSES ===")

backup_file = "expenses_backup.txt"

try:

    # Create backup before overwriting main file
    with open("expenses.txt", "r") as original_file:

        saved_data = original_file.read()

    with open(backup_file, "w") as backup:

        backup.write(saved_data)

    print("Backup created successfully.")


    # Save current expenses
    with open("expenses.txt", "w") as file:

        for expense in expenses:

            file.write(
                f"{expense['name']} | "
                f"₦{expense['amount']:.2f} | "
                f"{expense['category']} | "
                f"{expense['date']}\n"
            )

    print(
        "Expenses saved successfully to expenses.txt"
    )

except FileNotFoundError:

    print(
        "No existing expenses file found. "
        "Creating a new expenses file."
    )

    with open("expenses.txt", "w") as file:

        for expense in expenses:

            file.write(
                f"{expense['name']} | "
                f"₦{expense['amount']:.2f} | "
                f"{expense['category']} | "
                f"{expense['date']}\n"
            )

    print(
        "Expenses saved successfully to expenses.txt"
    )

except OSError as error:

    print(f"Save failed: {error}")


# =========================
# EXPENSE SUMMARY
# =========================

print()
print("=== EXPENSE SUMMARY ===")

total_spending = 0

for expense in expenses:

    total_spending += expense["amount"]

expense_count = len(expenses)

if expense_count > 0:

    average_expense = (
        total_spending / expense_count
    )

else:

    average_expense = 0

print(
    f"Total spending: ₦{total_spending:,.2f}"
)

print(
    f"Number of expenses: {expense_count}"
)

print(
    f"Average expense: ₦{average_expense:,.2f}"
)


# =========================
# CATEGORY BREAKDOWN
# =========================

print()
print("=== CATEGORY BREAKDOWN ===")

for category, amount in categories.items():

    print(
        f"{category:<10} : ₦{amount:,.2f}"
    )

if categories:

    highest_category = max(
        categories,
        key=categories.get
    )

    print()
    print(
        "Highest spending category:",
        highest_category
    )


# =========================
# CATEGORY SEARCH
# =========================

print()
print("=== CATEGORY SEARCH ===")

search_category = input(
    "Search category: "
).strip().lower()

if search_category in categories:

    print()
    print(
        "Category found:",
        search_category
    )

    print(
        f"Amount spent: "
        f"₦{categories[search_category]:,.2f}"
    )

else:

    print()
    print("Category not found.")


# =========================
# LARGEST EXPENSE
# =========================

print()
print("=== LARGEST EXPENSE ===")

if expenses:

    largest_expense = max(
        expenses,
        key=lambda expense: expense["amount"]
    )

    print(
        "Expense:",
        largest_expense["name"]
    )

    print(
        f"Amount: "
        f"₦{largest_expense['amount']:,.2f}"
    )

    print(
        "Category:",
        largest_expense["category"]
    )

    print(
        "Date:",
        largest_expense["date"]
    )

else:

    print("No expenses available.")


# =========================
# SMALLEST EXPENSE
# =========================

print()
print("=== SMALLEST EXPENSE ===")

if expenses:

    smallest_expense = min(
        expenses,
        key=lambda expense: expense["amount"]
    )

    print(
        "Expense:",
        smallest_expense["name"]
    )

    print(
        f"Amount: "
        f"₦{smallest_expense['amount']:,.2f}"
    )

    print(
        "Category:",
        smallest_expense["category"]
    )

    print(
        "Date:",
        smallest_expense["date"]
    )

else:

    print("No expenses available.")


# =========================
# DAILY SPENDING
# =========================

print()
print("=== DAILY SPENDING ===")

daily_spending = {}

for expense in expenses:

    date = expense["date"]
    amount = expense["amount"]

    if date not in daily_spending:

        daily_spending[date] = 0

    daily_spending[date] += amount


for date, amount in sorted(
    daily_spending.items()
):

    print(
        f"{date} : ₦{amount:,.2f}"
    )


# =========================
# CATEGORY PERCENTAGES
# =========================

print()
print("=== CATEGORY PERCENTAGES ===")

if total_spending > 0:

    for category, amount in categories.items():

        percentage = (
            amount / total_spending
        ) * 100

        print(
            f"{category:<10} : "
            f"₦{amount:,.2f} "
            f"({percentage:.2f}%)"
        )

else:

    print("No spending recorded.")


# =========================
# DAILY SPENDING PERCENTAGES
# =========================

print()
print("=== DAILY SPENDING PERCENTAGES ===")

if total_spending > 0:

    for date, amount in sorted(
        daily_spending.items()
    ):

        percentage = (
            amount / total_spending
        ) * 100

        print(
            f"{date} : "
            f"₦{amount:,.2f} "
            f"({percentage:.2f}%)"
        )

else:

    print("No spending recorded.")


# =========================
# SPENDING BY WEEKDAY
# =========================

print()
print("=== SPENDING BY WEEKDAY ===")

weekday_spending = {}

for expense in expenses:

    date = expense["date"]

    parsed_date = datetime.strptime(
        date,
        "%Y-%m-%d"
    )

    weekday = parsed_date.strftime("%A")

    amount = expense["amount"]

    if weekday not in weekday_spending:

        weekday_spending[weekday] = 0

    weekday_spending[weekday] += amount


for weekday, amount in sorted(
    weekday_spending.items(),
    key=lambda item:
        datetime.strptime(
            item[0],
            "%A"
        ).weekday()
):

    print(
        f"{weekday:<10} : ₦{amount:,.2f}"
    )


# =========================
# WEEKDAY SPENDING PERCENTAGES
# =========================

print()
print("=== WEEKDAY SPENDING PERCENTAGES ===")

if total_spending > 0:

    for weekday, amount in sorted(
        weekday_spending.items(),
        key=lambda item:
            datetime.strptime(
                item[0],
                "%A"
            ).weekday()
    ):

        percentage = (
            amount / total_spending
        ) * 100

        print(
            f"{weekday:<10} : "
            f"₦{amount:,.2f} "
            f"({percentage:.2f}%)"
        )

else:

    print("No spending recorded.")


# =========================
# EXPENSE HISTORY
# =========================

print()
print("=== EXPENSE HISTORY ===")

print("-" * 65)

print(
    "Name".ljust(20),
    "Amount".ljust(15),
    "Category".ljust(15),
    "Date"
)

print("-" * 65)

for number, expense in enumerate(
    expenses,
    start=1
):

    print(
        f"{number}. "
        f"{expense['name']:<17} "
        f"₦{expense['amount']:>12,.2f} "
        f"{expense['category']:<15} "
        f"{expense['date']}"
    )

print("-" * 65)
# =========================
# EXPORT PROFESSIONAL REPORT
# =========================

print()
print("=== EXPORT REPORT ===")

report_file = "expense_report.txt"

try:

    with open(report_file, "w") as report:

        report.write("============================================\n")
        report.write("       PERSONAL EXPENSE TRACKER REPORT\n")
        report.write("       Built by Obedience Jay 🚀\n")
        report.write("============================================\n\n")

        # Summary
        report.write("=== EXPENSE SUMMARY ===\n")
        report.write(
            f"Total spending: ₦{total_spending:,.2f}\n"
        )
        report.write(
            f"Number of expenses: {expense_count}\n"
        )
        report.write(
            f"Average expense: ₦{average_expense:,.2f}\n"
        )

        # Category breakdown
        report.write("\n=== CATEGORY BREAKDOWN ===\n")

        for category, amount in categories.items():

            report.write(
                f"{category:<10} : "
                f"₦{amount:,.2f}\n"
            )

        if categories:

            report.write(
                f"\nHighest spending category: "
                f"{highest_category}\n"
            )

        # Largest expense
        report.write("\n=== LARGEST EXPENSE ===\n")

        if expenses:

            report.write(
                f"Expense: "
                f"{largest_expense['name']}\n"
            )

            report.write(
                f"Amount: "
                f"₦{largest_expense['amount']:,.2f}\n"
            )

            report.write(
                f"Category: "
                f"{largest_expense['category']}\n"
            )

            report.write(
                f"Date: "
                f"{largest_expense['date']}\n"
            )

        # Smallest expense
        report.write("\n=== SMALLEST EXPENSE ===\n")

        if expenses:

            report.write(
                f"Expense: "
                f"{smallest_expense['name']}\n"
            )

            report.write(
                f"Amount: "
                f"₦{smallest_expense['amount']:,.2f}\n"
            )

            report.write(
                f"Category: "
                f"{smallest_expense['category']}\n"
            )

            report.write(
                f"Date: "
                f"{smallest_expense['date']}\n"
            )

        # Daily spending
        report.write("\n=== DAILY SPENDING ===\n")

        for date, amount in sorted(
            daily_spending.items()
        ):

            report.write(
                f"{date} : "
                f"₦{amount:,.2f}\n"
            )

        # Category percentages
        report.write(
            "\n=== CATEGORY PERCENTAGES ===\n"
        )

        if total_spending > 0:

            for category, amount in categories.items():

                percentage = (
                    amount / total_spending
                ) * 100

                report.write(
                    f"{category:<10} : "
                    f"₦{amount:,.2f} "
                    f"({percentage:.2f}%)\n"
                )

        # Daily percentages
        report.write(
            "\n=== DAILY SPENDING PERCENTAGES ===\n"
        )

        if total_spending > 0:

            for date, amount in sorted(
                daily_spending.items()
            ):

                percentage = (
                    amount / total_spending
                ) * 100

                report.write(
                    f"{date} : "
                    f"₦{amount:,.2f} "
                    f"({percentage:.2f}%)\n"
                )

        # Weekday spending
        report.write(
            "\n=== SPENDING BY WEEKDAY ===\n"
        )

        for weekday, amount in sorted(
            weekday_spending.items(),
            key=lambda item:
                datetime.strptime(
                    item[0],
                    "%A"
                ).weekday()
        ):

            report.write(
                f"{weekday:<10} : "
                f"₦{amount:,.2f}\n"
            )

        # Weekday percentages
        report.write(
            "\n=== WEEKDAY SPENDING PERCENTAGES ===\n"
        )

        if total_spending > 0:

            for weekday, amount in sorted(
                weekday_spending.items(),
                key=lambda item:
                    datetime.strptime(
                        item[0],
                        "%A"
                    ).weekday()
            ):

                percentage = (
                    amount / total_spending
                ) * 100

                report.write(
                    f"{weekday:<10} : "
                    f"₦{amount:,.2f} "
                    f"({percentage:.2f}%)\n"
                )

        # Expense history
        report.write("\n=== EXPENSE HISTORY ===\n")
        report.write("-" * 65 + "\n")

        report.write(
            "Name".ljust(20)
            + "Amount".ljust(15)
            + "Category".ljust(15)
            + "Date\n"
        )

        report.write("-" * 65 + "\n")

        for number, expense in enumerate(
            expenses,
            start=1
        ):

            report.write(
                f"{number}. "
                f"{expense['name']:<17} "
                f"₦{expense['amount']:>12,.2f} "
                f"{expense['category']:<15} "
                f"{expense['date']}\n"
            )

        report.write("-" * 65 + "\n")

        report.write("\n=== END OF REPORT ===\n")

    print(
        f"Report exported successfully to "
        f"{report_file}"
    )

except OSError as error:

    print(
        f"Report export failed: {error}"
    )


# =========================
# PROGRAM COMPLETE
# =========================

print()
print("=== PROGRAM COMPLETE ===")
print("Thank you for using Personal Expense Tracker 🚀")


