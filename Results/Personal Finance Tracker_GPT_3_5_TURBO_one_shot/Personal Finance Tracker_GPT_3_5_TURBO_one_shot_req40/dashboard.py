'''
Dashboard window for the personal finance management application.
'''
import tkinter as tk
class DashboardWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.balance_label = tk.Label(self, text="Current Balance: $0.00")
        self.balance_label.pack()
        self.transactions_label = tk.Label(self, text="Recent Transactions:")
        self.transactions_label.pack()
        self.transactions_listbox = tk.Listbox(self)
        self.transactions_listbox.pack()
        self.bills_label = tk.Label(self, text="Upcoming Bills:")
        self.bills_label.pack()
        self.bills_listbox = tk.Listbox(self)
        self.bills_listbox.pack()
        self.graph_label = tk.Label(self, text="Spending Trends:")
        self.graph_label.pack()
        # TODO: Implement spending trends graph
        self.pack()