from budgetTracker_Final import BudgetTracker

def main():
    # Making an instance of the BudgetTracker Class
    budget_tracker = BudgetTracker(date=None, category=None, transaction_type=None, amount=None, description=None)

    print("Welcome to Budget Expense Tracker Analysis. Which service would you choose today?")
    # Running a "While" loop so that the user can make multiple user inputs untill they hit "5" and "exit"
    while True:
        # Displaying options for users to choose from
        print("\n1. Add new Expense")
        print("2. View existing Expense")
        print("3. View total Expense")
        print("4. Export your expense recorded into a CSV")
        print("5. Exit (you can also enter 'exit' if you wish to)")
        

        # Taking user input to choose which option they would like
        user_input = input("Enter which option would you like [1-5]:")

        # Using "try-except" block, if there is any error in the inputs, it throws an error with the associated message
        try:
            # Converting the user's inputs "Exit" into lowercase ("exit") 
            # Accepts "exit" or "5" as an user_input option to terminate the program
            if user_input.lower() == "exit" or user_input == "5":
                print("Thank you for using the Budget Expense Tracker Analysis\n")
                break
            
            # Converting user input option choice from (str) -> (int)
            user_input = int(user_input)

            # If user_input = 1, user gets to add an expense
            if user_input == 1:

                # Asking user for DATE input options. If the format (YYYY-MM-DD) is right, it will continue, 
                # else takes it back to making a new option (continues only if the DATE format is right)
                expense_date = input("Enter expense Date in YYYY-MM-DD format: ")

                # Calls the .date_handler method, and checks for the right DATE format with the REGEX 
                if not budget_tracker.date_handler(expense_date):
                    raise ValueError("Please use YYYY-MM-DD only")
                
                # Making a "list" for expense category option to make the program cleaner
                expense_category = [
                    "House", "Food", "Work", "Personal", "Entertainment", "Miscellaneous"
                ]

                while True:
                    print("Select a category:")

                # Running a "for-loop" (starts at 1) to make the a Serial Number sequence for the expense_category list
                    for serial, category_type in enumerate(expense_category, start=1):
                        print("{x}. {y}".format(x=serial, y=category_type))

                    # Taking user input to choose the category the want to add their expense as
                    category_input = input("Enter a category number [1-6]: ")

                    # A "try-except" block to make sure to have the right expense_cateogry choice 
                    # It continues to ask untill the user makes the right option (1-6)
                    try:
                        category_choice = int(category_input)
                        if 1 <= category_choice <= 6:
                            break
                        else:
                            raise ValueError("Invalid Category option.")
                    except ValueError:
                        print("Invalid option! Please enter a valid category number.")

                # Using "lambda" expressions and make use of "set" to create a predefined options of transaction_type
                is_valid_transaction_type = (lambda type: type.lower() in {"cash", "creditcard", "debitcard"})

                while True:
                    # Takes user's inputs, if their input is with the predefined set, then it will proceed,
                    # else will ask them to make the expense_transactionType again
                    # Converts to user_input to ".lower()" to make it more efficient
                    expense_transactionType = input("Enter expense Transaction Type from cash/creditcard/debitcard: ").lower()
                    if is_valid_transaction_type(expense_transactionType):
                        break
                    else:
                        print("Invalid option! Choose from the given choices only.")

                # Converting it to float, and making sure user can input the values with decimals for accuracy of their expenses
                expense_amount = float(input("Enter expense Amount: "))

                # Asking user to write a description of their expense for future understanding
                expense_description = input("Enter expense description: ")

                # Once all the details about the expenses has been recorded and entered, 
                # calls the .add_transaction method to add the expenses into the respective key-value pair 
                budget_tracker.add_transaction(
                    expense_date, expense_category[category_choice - 1], expense_transactionType, expense_amount, expense_description)

            # If user_input = 2, user gets to view all the expenses recorded
            elif user_input == 2:
                # Calls the .view_transaction method and view any expenses recorded
                view = budget_tracker.view_transaction()
                print(view)

            # If user_input = 3, user gets to see the total expenses recorded
            elif user_input == 3:

                # Using "if-else" condiiton to display the total amount of all recorded transactions if exists. 
                # else, it will display the below message requesting to add a transaction
                # Calls the .total_expenses method to calculate the sum of total expenses recorded
                expense_total = budget_tracker.total_expenses()
                if expense_total is None:
                    print("\nNo expenses recorded. Please add an expense first")
                else:
                    print("\nYour total expenses recorded is =  ${x}".format(x = expense_total))

            # If the user_input = 4, then the program converts any expense recorded into a CSV file
            elif user_input == 4:
                # Calls the .export_to_csv method to convert the expenses into CSV
                view = budget_tracker.export_to_csv()
                print(view)
            
            # This "else" conditon checks for the user selected option within the listed range
            # If the user goes beyond the range, it will ask to the user to enter their option choice again
            else:
                raise ValueError("Please enter a service from [1-5].")

        # Used to display the appropiate error message which is associated with their respective error
        except ValueError as e:
            print(f"Invalid input: {e}\n")

if __name__ == "__main__":
    main()