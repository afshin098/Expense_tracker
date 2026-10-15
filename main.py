from db import get_connection
from expenses import (
    get_all_expenses,
    get_expense,
    add_expense,
    update_expense,
    delete_expense,
    get_expenses_by_category,
)

def show_categories():
    print("1.Healthy")
    print("2.Books")
    print("3.Food")
    print("4.Entertainment")
    print("5.Travel")
    print("6.All")


def main(cursor, connection):
    while True:
        print("========== Expense Tracker ==========")
        print("1. Show all expenses")
        print("2. Find an expense")
        print("3. Add an expense")
        print("4. Update an expense")
        print("5. Delete an expense")
        print("6. Exit")
        print("=====================================")
        choice = input("Enter Your Choice:")

        if choice == "1":
            show_categories()
            try:
                selected_category_id = int(input("Enter a ID: "))

                if selected_category_id == 6:
                    expenses = get_all_expenses(cursor)

                elif 1 <= selected_category_id <= 5:
                    expenses = get_expenses_by_category(cursor, selected_category_id)
                else:
                    print("Invalid Category ID. Chose From 1 to 6.")
                    continue

                if not expenses:
                    print("No Expenses Found")
                else:
                    print(
                        f"{'id':<5}{'Title':<30}{'Amount':<15}{'Date':<13}{'Category':<10}"
                    )
                    for expense in expenses:
                        print(
                            f"{expense[0]:<5}{expense[1]:<30}{expense[2]:<15}{expense[3]!s:<13}{expense[5]:<10}"
                        )
            except ValueError:
                print("Id Must be Number")

        elif choice == "2":
            try:
                expense_id = int(input("Enter Expense ID:"))
            except ValueError:
                print("ID Must be a Number.")
                continue

            expense = get_expense(cursor, expense_id)

            if expense is not None:
                print(
                    f"{'ID':<4}{'Title':<15}{'Amount':<15}{'Date':<12}{'Category_name':<15}"
                )
                print(
                    f"{expense[0]:<4}{expense[1]:<15}{expense[2]:<15}{expense[3]!s:<12}{expense[4]:<15}"
                )
            else:
                print(f"Expense {expense_id} was not Find")
        elif choice == "3":

            def set_category_name(category_id):
                if category_id == 1:
                    return "Healthy"
                elif category_id == 2:
                    return "Books"
                elif category_id == 3:
                    return "Food"
                elif category_id == 4:
                    return "Entertainment"
                elif category_id == 5:
                    return "Travel"

            title = input("Title: ").strip()
            if title == "":
                print("Title Can Not be Empty")
                continue

            try:
                amount = int(input("Amount: "))

                if amount > 0:
                    print("1. Healthy")
                    print("2. Books")
                    print("3. Food")
                    print("4. Entertainment")
                    print("5. Travel")
                    category_id = int(input("Category ID: "))
                else:
                    print("Amount Must Be Greater than Zero")
                    continue
            except ValueError:
                print("Amount and Category ID must be numbers.")
                continue

            try:
                new_expense_id = add_expense(cursor, title, amount, category_id)
                connection.commit()
                print("Expense added successfully.")
                print(f"{'id':<5}{'Title':<12}{'Amount':<12}{'Category':<8}")
                print(
                    f"{new_expense_id:<5}{title:<12}{amount:<12} {set_category_name(category_id):<8}"
                )

            except Exception as error:
                connection.rollback()
                print(f"Could not add expense: {error}")
        elif choice == "4":
            try:
                expense_id = int(input("Expense ID:"))
                new_amount = int(input("New Amount:"))
                if new_amount <= 0:
                    print("New amount must be greater than zero.")
                    continue
            except ValueError:
                print("expense id and new amount must be Number")
                continue

            try:
                updated = update_expense(cursor, expense_id, new_amount)
                connection.commit()

                if updated:
                    print(f"ID: {expense_id} Update Amount to {new_amount}")
                else:
                    print(f"Expense {expense_id} was not found")
            except Exception as error:
                connection.rollback()
                print(f"Error: {error}")

        elif choice == "5":
            try:
                expense_id = int(input("Expense ID: "))
            except ValueError:
                print("expense id must be Number")
                continue
            try:
                deleted = delete_expense(cursor, expense_id)
                connection.commit()

                if deleted:
                    print(f"Expense {expense_id} was deleted.")
                else:
                    print(f"Expense {expense_id} was not found")
            except Exception as error:
                connection.rollback()
                print(f"Error: {error}")
        elif choice == "6":
            print("Bye")
            break
        else:
            print("Invalid Input\nTry Again")
            continue


with get_connection() as connection:
    with connection.cursor() as cursor:
        main(cursor, connection)
