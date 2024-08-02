'''
This file contains the implementation of the TransactionsWindow class.
'''
import tkinter as tk
class TransactionsWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Transactions")
        self.master.geometry("800x600")
        self.pack()
        self.add_transaction_button = tk.Button(self, text="Add Transaction", command=self.add_transaction)
        self.add_transaction_button.pack()
    def add_transaction(self):
        # Add logic to add a new transaction here
        # Prompt the user for transaction details
        transaction_details = self.prompt_transaction_details()
        # Update the transaction data
        self.update_transaction_data(transaction_details)
    def prompt_transaction_details(self):
        # Create a new dialog or form to prompt the user for transaction details
        transaction_dialog = tk.Toplevel(self.master)
        transaction_dialog.title("Add Transaction")
        transaction_dialog.geometry("400x300")
        # Create labels and entry fields for transaction details
        date_label = tk.Label(transaction_dialog, text="Date:")
        date_label.pack()
        date_entry = tk.Entry(transaction_dialog)
        date_entry.pack()
        category_label = tk.Label(transaction_dialog, text="Category:")
        category_label.pack()
        category_entry = tk.Entry(transaction_dialog)
        category_entry.pack()
        type_label = tk.Label(transaction_dialog, text="Type:")
        type_label.pack()
        type_entry = tk.Entry(transaction_dialog)
        type_entry.pack()
        amount_label = tk.Label(transaction_dialog, text="Amount:")
        amount_label.pack()
        amount_entry = tk.Entry(transaction_dialog)
        amount_entry.pack()
        # Create a button to submit the transaction details
        submit_button = tk.Button(transaction_dialog, text="Submit", command=lambda: self.update_transaction_data({
            "date": date_entry.get(),
            "category": category_entry.get(),
            "type": type_entry.get(),
            "amount": amount_entry.get()
        }))
        submit_button.pack()
        # Wait for the user to close the dialog
        transaction_dialog.wait_window()
        # Return the entered transaction details
        return {
            "date": date_entry.get(),
            "category": category_entry.get(),
            "type": type_entry.get(),
            "amount": amount_entry.get()
        }
    def update_transaction_data(self, transaction_details):
        # Add logic to update the transaction data with the new transaction details
        # Example code:
        transaction_data = {
            "date": transaction_details["date"],
            "category": transaction_details["category"],
            "type": transaction_details["type"],
            "amount": transaction_details["amount"]
        }
        # Update the transaction data in the application
        self.master.transaction_data.append(transaction_data)