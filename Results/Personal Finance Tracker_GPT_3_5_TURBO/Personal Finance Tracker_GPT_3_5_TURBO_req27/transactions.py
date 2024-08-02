'''
This file contains the implementation of the TransactionsWindow class.
'''
import tkinter as tk
from tkinter import messagebox
class TransactionsWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Transactions")
        self.master.geometry("800x600")
        self.pack()
        self.transaction_data = []
        self.transaction_listbox = tk.Listbox(self)
        self.transaction_listbox.pack()
        self.filter_frame = tk.Frame(self)
        self.filter_frame.pack()
        self.date_range_label = tk.Label(self.filter_frame, text="Date Range:")
        self.date_range_label.pack(side=tk.LEFT)
        self.date_range_entry = tk.Entry(self.filter_frame)
        self.date_range_entry.pack(side=tk.LEFT)
        self.category_label = tk.Label(self.filter_frame, text="Category:")
        self.category_label.pack(side=tk.LEFT)
        self.category_entry = tk.Entry(self.filter_frame)
        self.category_entry.pack(side=tk.LEFT)
        self.income_expense_label = tk.Label(self.filter_frame, text="Income/Expense:")
        self.income_expense_label.pack(side=tk.LEFT)
        self.income_expense_entry = tk.Entry(self.filter_frame)
        self.income_expense_entry.pack(side=tk.LEFT)
        self.add_transaction_button = tk.Button(self, text="Add Transaction", command=self.add_transaction)
        self.add_transaction_button.pack()
        self.edit_transaction_button = tk.Button(self, text="Edit Transaction", command=self.edit_transaction)
        self.edit_transaction_button.pack()
        self.delete_transaction_button = tk.Button(self, text="Delete Transaction", command=self.delete_transaction)
        self.delete_transaction_button.pack()
        self.load_transactions()
    def load_transactions(self):
        self.transaction_listbox.delete(0, tk.END)
        for transaction in self.transaction_data:
            self.transaction_listbox.insert(tk.END, transaction)
    def add_transaction(self):
        # Add logic to add a new transaction here
        # Prompt the user for transaction details
        transaction_details = self.prompt_transaction_details()
        if transaction_details is None:
            return
        # Update the transaction data
        self.update_transaction_data(transaction_details)
        # Reload transactions
        self.load_transactions()
    def edit_transaction(self):
        # Get the selected transaction from the listbox
        selected_index = self.transaction_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "No transaction selected.")
            return
        selected_transaction = self.transaction_data[selected_index[0]]
        # Prompt the user for updated transaction details
        updated_transaction_details = self.prompt_transaction_details()
        # Update the selected transaction with the updated details
        self.transaction_data[selected_index[0]] = updated_transaction_details
        # Reload transactions
        self.load_transactions()
    def delete_transaction(self):
        # Get the selected transaction from the listbox
        selected_index = self.transaction_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Error", "No transaction selected.")
            return
        # Remove the selected transaction from the transaction data
        del self.transaction_data[selected_index[0]]
        # Reload transactions
        self.load_transactions()
    def prompt_transaction_details(self):
        # Create a new dialog or form to prompt the user for transaction details
        transaction_dialog = tk.Toplevel(self.master)
        transaction_dialog.title("Add Transaction")
        transaction_dialog.geometry("400x300")
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
        submit_button = tk.Button(
            transaction_dialog,
            text="Submit",
            command=lambda: self.validate_transaction_details(transaction_dialog, {
                "date": date_entry.get(),
                "category": category_entry.get(),
                "type": type_entry.get(),
                "amount": amount_entry.get()
            })
        )
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
    def validate_transaction_details(self, transaction_dialog, transaction_details):
        # Add logic to validate the entered transaction details
        # Example code:
        if not transaction_details["date"] or not transaction_details["category"] or not transaction_details["type"] or not transaction_details["amount"]:
            messagebox.showerror("Error", "Please enter all transaction details.")
            return
        try:
            float(transaction_details["amount"])
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a valid number.")
            return
        transaction_dialog.destroy()
        self.update_transaction_data(transaction_details)
        self.load_transactions()
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
        self.transaction_data.append(transaction_data)
    def lift(self):
        self.master.lift()
        self.master.tkraise()