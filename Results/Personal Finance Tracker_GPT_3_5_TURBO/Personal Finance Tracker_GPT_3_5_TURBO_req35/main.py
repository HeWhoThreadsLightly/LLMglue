'''
This file contains the main entry point of the application.
'''
import tkinter as tk
from tkinter import messagebox
from dashboard import DashboardWindow
from transactions import TransactionsWindow
from reports import ReportsWindow
from settings import SettingsWindow
import pandas as pd
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Personal Finance Manager")
        self.geometry("800x600")
        self.transaction_data = []  # Store transaction data
        self.dashboard_window = DashboardWindow(self)
        self.transactions_window = TransactionsWindow(self)
        self.reports_window = ReportsWindow(self)
        self.settings_window = SettingsWindow(self)
        self.menu_bar = tk.Menu(self)
        self.menu_bar.add_command(label="Dashboard", command=self.show_dashboard)
        self.menu_bar.add_command(label="Transactions", command=self.show_transactions)
        self.menu_bar.add_command(label="Reports", command=self.show_reports)
        self.menu_bar.add_command(label="Settings", command=self.show_settings)
        self.config(menu=self.menu_bar)
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.show_dashboard()
    def show_dashboard(self):
        self.dashboard_window.lift()
        self.dashboard_window.tkraise()
    def show_transactions(self):
        self.transactions_window.lift()
        self.transactions_window.tkraise()
    def show_reports(self):
        self.reports_window.lift()
        self.reports_window.tkraise()
    def show_settings(self):
        self.settings_window.lift()
        self.settings_window.tkraise()
    def on_close(self):
        if messagebox.askokcancel("Quit", "Are you sure you want to quit?"):
            self.destroy()
    def get_transaction_data(self):
        return pd.DataFrame(self.transaction_data)  # Replace with the actual implementation to fetch the transaction data
    def add_transaction(self, transaction_data):
        self.transaction_data.append(transaction_data)
    def edit_transaction(self, index, transaction_data):
        self.transaction_data[index] = transaction_data
    def delete_transaction(self, index):
        del self.transaction_data[index]
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()