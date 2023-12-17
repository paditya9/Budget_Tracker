import pytest
import budgetTracker_Final as bt


def test1_date_handler():    
    # DATE format = YYYY-MM-DD
    # Creating an instance of "budgetTracker_Final"
    budget_tracker = bt.BudgetTracker(date=None, category=None, transaction_type=None, amount=None, description=None)

    # Case 1: Inputting right DATE format as per the Regex condition
    assert budget_tracker.date_handler(date='2023-12-12') == True

    # Case 2: Inputting wrong DATE format, raises a ValueError
    with pytest.raises(ValueError, match="Invalid date format used. Please use YYYY-MM-DD only"):
     budget_tracker.date_handler(date="12-12-2023")
    
    # Case 3: Inputting wrong DATE format, raises a ValueError
    with pytest.raises(ValueError, match="Invalid date format used. Please use YYYY-MM-DD only"):
     budget_tracker.date_handler(date="12-2023-12")
    
    # Case 4: Inputting wrong DATE format, raises a ValueError, absurd date
    with pytest.raises(ValueError, match="Invalid date format used. Please use YYYY-MM-DD only"):
     budget_tracker.date_handler(date="121-20123-112")


def test2_add_transaction():
     budget_tracker = bt.BudgetTracker(date=None, category=None, transaction_type=None, amount=None, description=None)

     # Case 1: All the required input by the user is received
     assert budget_tracker.add_transaction(date='2023-12-12', category="1", 
          transaction_type="cash", amount="900", description="House Rent") == True

def test3_total_expenses():
     budget_tracker = bt.BudgetTracker(date=None, category=None, transaction_type=None, amount=None, description=None)

     # Case 1: When no expense if recorded
     no_expense = budget_tracker.total_expenses()
     assert no_expense is None
     
     # Case 2: When expense exists, calculating the sum
     # Adding expenses with the help of .add_transaction method
     budget_tracker.add_transaction(date='2023-12-12', category="1", transaction_type="cash", amount=900, description="House Rent")
     budget_tracker.add_transaction(date='2023-12-13', category="2", transaction_type="creditcard", amount=1000, description="Idk")
     budget_tracker.add_transaction(date='2023-12-13', category="2", transaction_type="debitcard", amount=200.20, description="Decimals added")

     expense_recorded = budget_tracker.total_expenses()
     assert expense_recorded == 2100.20

def test4_view_transaction():
     budget_tracker = bt.BudgetTracker(date=None, category=None, transaction_type=None, amount=None, description=None)

     # Case 1: When no expense if recorded
     no_expense = budget_tracker.view_transaction()
     assert no_expense == "\nNo expense recorded. Please add an expense to view"

     # Case 2: When expense exists
     budget_tracker.add_transaction(date='2023-12-12', category="1", transaction_type="cash", amount=900, description="House Rent")
     budget_tracker.add_transaction(date='2023-12-13', category="2", transaction_type="creditcard", amount=1000, description="Idk")
     budget_tracker.add_transaction(date='2023-12-13', category="2", transaction_type="debitcard", amount=200.20, description="Decimals added")

     # Because the original outputs includes indentation, 
     # we are asseting it to the message when the .view_transaction method is called
     # we use the ".startswith" funtion that is used to compare to the original message "Below is the exsisting expenses recorded..."
     expense_recorded = budget_tracker.view_transaction()
     output_start = "Below is the exsisting expenses recorded"

     # Using ".startwith()" function to compare the output with the expected output
     assert expense_recorded.startswith(output_start)

def test5_export_to_csv():
     budget_tracker = bt.BudgetTracker(date=None, category=None, transaction_type=None, amount=None, description=None)

     # Case 1: When no expense if recorded
     no_expense = budget_tracker.export_to_csv()
     assert no_expense == ("No expenses recorded. Nothing to export")

     # Case 2: When expense exists
     budget_tracker.add_transaction(date='2023-12-12', category="1", transaction_type="cash", amount=900, description="House Rent")
     budget_tracker.add_transaction(date='2023-12-13', category="2", transaction_type="creditcard", amount=1000, description="Idk")
     budget_tracker.add_transaction(date='2023-12-13', category="2", transaction_type="debitcard", amount=200.20, description="Decimals added")

     # Because the original outputs includes indentation, 
     # we are asseting it to the message when the .export_to_csv method is called
     # we use the ".startswith" funtion that is used to compare to the original message "\nExpenses has been sucessfully exported as a CSV file named:..."
     expense_recorded = budget_tracker.export_to_csv()
     output_start = "\nExpenses has been sucessfully exported as a CSV file named:"

     # Using ".startwith()" function to compare the output with the expected output
     assert expense_recorded.startswith(output_start)