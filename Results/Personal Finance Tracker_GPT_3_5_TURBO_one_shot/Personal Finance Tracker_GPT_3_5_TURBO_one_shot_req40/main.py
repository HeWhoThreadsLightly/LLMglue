'''
Main file for the personal finance management application.
'''
import tkinter as tk
from dashboard import DashboardWindow
from transactions import TransactionsWindow
from reports import ReportsWindow
from settings import SettingsWindow
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Personal Finance Manager")
        self.geometry("800x600")
        self.dashboard_window = DashboardWindow(self)
        self.transactions_window = TransactionsWindow(self)
        self.reports_window = ReportsWindow(self)
        self.settings_window = SettingsWindow(self)
        self.show_dashboard()
        self.menu = tk.Menu(self)
        self.menu.add_command(label="Dashboard", command=self.show_dashboard)
        self.menu.add_command(label="Transactions", command=self.show_transactions)
        self.menu.add_command(label="Reports", command=self.show_reports)
        self.menu.add_command(label="Settings", command=self.show_settings)
        self.config(menu=self.menu)
    def show_dashboard(self):
        self.dashboard_window.tkraise()
    def show_transactions(self):
        self.transactions_window.tkraise()
    def show_reports(self):
        self.reports_window.tkraise()
    def show_settings(self):
        self.settings_window.tkraise()
if __name__ == "__main__":
    app = Application()
    app.mainloop()