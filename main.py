from database import init_db, add_transaction, get_all_transactions
from analysis import monthly_summary
from visualize import plot_expenses

init_db()

while True:
    print("\n--- Personal Finance Tracker ---")
    print("1. Add transaction")
    print("2. View transactions")
    print("3. Monthly summary")
    print("4. Plot expenses")
    print("5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        date = input("Date (YYYY-MM-DD): ")
        category = input("Category: ")
        description = input("Description: ")
        amount = float(input("Amount: "))
        add_transaction(date, category, description, amount)

    elif choice == "2":
        for row in get_all_transactions():
            print(row)

    elif choice == "3":
        monthly_summary()

    elif choice == "4":
        plot_expenses()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
