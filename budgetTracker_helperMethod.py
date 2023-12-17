import re 
import pandas as pd 
import csv

class BudgetTracker:
    """
    This class is used to make all the helper methods that are required for my mainBudgetTracking file. 

    Methods:
        1. date_handler() : used to handle to DATE format. Uses Regular Expressions to ensure the right format
        2. add_transaction() : used to add an expenses in the Budget Tracket Analysis 
        3. total_expenses() : used to sum all of the recorded expenses and display of the cumalative to the user
        4. view_transaction() : used to view the entered expenses of the user if any
        5. export_to_csv : used to export any expense recorded by the user into a CSV file for future referneces

    Parameters:
        date(int) = The day of the expense recorded. Follows particularly the YYYY-MM-DD format only
        category (str) = Gives the user to choose their expense based of a predefined list of 
                        cateogies which will help the user make more informed decisions about their expenses
        trasnaction_type (str) = Gives the user to choose their expense based of a predefined 
                        list of transaction type (cash/creditcard/debitcard) which will help the use understand their spending in each payment method
        amount (int) = The cost (in $) paid by a user for a particular transaction
        description (str) = Gives an opportunity to the user to describe or add notes their expense for future purposes
    """

    def __init__(self, date, category, transaction_type, amount, description):
        self.date = date
        self.category = category
        self.transaction_type = transaction_type
        self.amount = amount
        self.description = description
        self.budget = pd.DataFrame(columns=["Date", "Category", "Transaction Type", "Amount", "Description"])


    def date_handler(self, date):
        """
        This method is used to handle to DATE format. Used Regex to make sure the right format is used

        Parameters: 
            date(int) = The day of the expense recorded. Follows particularly the YYYY-MM-DD format only
        
        Returns:
            Returns TRUE is the date is matched with the specified Regex, else returns FALSE
        """
        # Making a Regular expression that should follow the format of YYYY-MM-DD only. 
        pattern = r'^\d{4}-\d{2}-\d{2}$'
        matched = re.match(pattern,date)

        # This "if-else" condition checks for the format of the date that the user has entered. 
        # If the format is matched, it will let the user continue, else will throw an error message and ask for the right input
        if matched:
            return True
        else:
            raise ValueError("Invalid date format used. Please use YYYY-MM-DD only")
    

    def add_transaction(self, date, category, transaction_type, amount, description):
        """"
        This method is used to add the expense in the Budget Tracker

        Parameter: 
            date(int) = The day of the expense recorded. Follows particularly the YYYY-MM-DD format only
            category (str) = Gives the user to choose their expense based of a predefined list of 
                            cateogies which will help the user make more informed decisions about their expenses
            trasnaction_type (str) = Gives the user to choose their expense based of a predefined 
                            list of transaction type (cash/creditcard/debitcard) which will help the use understand their spending in each payment method
            amount (int) = The cost (in $) paid by a user for a particular transaction
            description (str) = Gives an opportunity to the user to describe or add notes their expense for future purposes

        Returns:
            Returns TRUE when all the conditions for adding the expense is matched, else returns FALSE
        """
        
        # This "if-else" condition check if all the required parameters are entered by the user to feed their data
        # If the condition is not met, an error message is throw and asked for the inputs again
        if not all([date, category, transaction_type, amount, description]):
            raise ValueError("Missing entry types. Make sure to add all the fields")

        else:
        # Created a dict (key value pair) to help the user enter all the necessary information into the program so that it can be saved and viewed later
            add_trans = {"Date": [date],
                         "Category": [category],
                         "Transaction Type": [transaction_type],
                         "Amount": [amount],
                         "Description": [description]}
        
        transaction_df = pd.DataFrame(add_trans)
        self.budget = pd.concat([self.budget, transaction_df])

        # A simple print statement that shows the transactional information that was entered by the user. Displays all the information that the user entered
        print("\nThe following transaction has been added successfully:\n"
              "Date: {date_t}\nCategory: {category_t}\nTransaction Type: {trans_type}\nAmount: {amt}\nDescription: {des} \n".format(
            date_t=date, category_t=category, trans_type=transaction_type, amt=amount, des=description))

        return True
    
    def total_expenses(self):
        """
        This method is used to calculate the sum of all the recorded expenses

        Returns:
            Returns NONE if there is no expenses, else it returns the sum of the "Amount" recorded by the user
        """

        # This "if-else" condition is used to calculate the sum of all the expenses that were recorded by the user. 
        # If there is an expense it will display the sum, else it will display None
        if self.budget.empty:
            return None
        else:
            return self.budget["Amount"].sum()

    def view_transaction(self):
        """
        This method is used to view the added expenses by the user. 
        If no expense has been recorded, the program will display the message requesting for an expense, 
        else it will display the all the expenses recorded

        Returns:
            If there no expenses, it displays the below messages else displays all the recorded expenses
            of the user
        """

        # This "if-else" condition is used to check if there is any data/transaction recorded that has been entered by the user
        # If data is present, it will display them, else it will throw the message below to enter the transaction before viewing
        if self.budget.empty:
            return ("\nNo expense recorded. Please add an expense to view")
        
        else:
            return ("Below is the exsisting expenses recorded \n{x}\n".format(x=self.budget))
    
    def export_to_csv(self, filename='BudgetTracker_expenses.csv'):
        """
        This method is used to convert all user expenses recorded into a CSV file for personal references.

        Parameters:
            filename (str): The name of the CSV file = "BudgetTracker_expenses.csv"

        Returns:
            If there no expenses, it displays the below messages else converts the recorded expenses by the user
            into a CSV file called 'BudgetTracker_expenses.csv'
        """
        
        # This "if-else" condition is used to check if their any user expenses recorded in order to be converted into a CSV
        # If there is no expense, it will print the below message, reuqesting the user to make a record
        # Else, it will give them a CSV file with their expense records 
        if self.budget.empty:
            return("No expenses recorded. Nothing to export")
        else:
            # Using the "with open" to open the file and using "w (write-mode)" for the program to truncate if the file already
            # exsist with the latest records of user expenses
            with open(filename, 'w') as file:
                # Creating a "writer" object that can be used to write rows and iterate thru it 
                csv_file = csv.writer(file)

                # Using a "for loop" to iterate thru the rows of self.budget DF 
                for row in self.budget.iterrows():
                    # Using "list-comprehension" to iterate thru the key-value pair
                    data = ', '.join(['{x}: {y}'.format(x = heading, y = user_input) for heading, user_input in row[1].items()])
                    csv_file.writerow([data])

            return("\nExpenses has been sucessfully exported as a CSV file named: {name}".format(name = filename))
    