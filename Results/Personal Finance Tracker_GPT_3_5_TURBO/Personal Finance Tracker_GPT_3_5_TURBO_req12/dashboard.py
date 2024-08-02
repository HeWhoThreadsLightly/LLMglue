'''
This file contains the implementation of the DashboardWindow class.
'''
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
class DashboardWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Dashboard")
        self.master.geometry("800x600")
        self.current_balance_label = tk.Label(self, text="Current Balance: $0.00")
        self.current_balance_label.pack()
        self.recent_transactions_label = tk.Label(self, text="Recent Transactions:")
        self.recent_transactions_label.pack()
        self.upcoming_bills_label = tk.Label(self, text="Upcoming Bills:")
        self.upcoming_bills_label.pack()
        self.pack()
    def lift(self):
        self.master.lift()
        self.master.tkraise()