'''
Transactions window for the personal finance management application.
'''
import tkinter as tk
class Transaction:
    def __init__(self, date, amount, category, payment_method, notes):
        self.date = date
        self.amount = amount
        self.category = category
        self.payment_method = payment_method
        self.notes = notes
class TransactionsWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.transactions = []
        self.filter_frame = tk.Frame(self)
        self.filter_frame.pack()
        self.date_label = tk.Label(self.filter_frame, text="Date Range:")
        self.date_label.pack(side=tk.LEFT)
        self.date_entry = tk.Entry(self.filter_frame)
        self.date_entry.pack(side=tk.LEFT)
        self.category_label = tk.Label(self.filter_frame, text="Category:")
        self.category_label.pack(side=tk.LEFT)
        self.category_entry = tk.Entry(self.filter_frame)
        self.category_entry.pack(side=tk.LEFT)
        self.type_label = tk.Label(self.filter_frame, text="Type:")
        self.type_label.pack(side=tk.LEFT)
        self.type_entry = tk.Entry(self.filter_frame)
        self.type_entry.pack(side=tk.LEFT)
        self.transactions_listbox = tk.Listbox(self)
        self.transactions_listbox.pack()
        self.add_button = tk.Button(self, text="Add Transaction", command=self.add_transaction)
        self.add_button.pack()
        self.pack()
    def add_transaction(self):
        # Get the transaction details from the user input
        transaction_date = self.date_entry.get()
        transaction_amount = self.amount_entry.get()
        transaction_category = self.category_entry.get()
        transaction_payment_method = self.payment_method_entry.get()
        transaction_notes = self.notes_entry.get()
        # Create a new transaction object
        new_transaction = Transaction(transaction_date, transaction_amount, transaction_category, transaction_payment_method, transaction_notes)
        # Add the new transaction to the list of transactions
        self.transactions.append(new_transaction)
        # Update the transactions listbox to display the newly added transaction
        self.transactions_listbox.insert(tk.END, str(new_transaction))