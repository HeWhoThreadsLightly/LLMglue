'''
This file contains the implementation of the ReportsWindow class.
'''
import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
class ReportsWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Reports")
        self.master.geometry("800x600")
        self.pack()
        self.report_type_var = tk.StringVar()
        self.report_type_var.set("Spending by Category")
        self.date_range_var = tk.StringVar()
        self.date_range_var.set("All Time")
        self.category_var = tk.StringVar()
        self.category_var.set("All Categories")
        self.income_expense_var = tk.StringVar()
        self.income_expense_var.set("All")
        self.report_type_label = tk.Label(self, text="Report Type:")
        self.report_type_label.pack()
        self.report_type_dropdown = tk.OptionMenu(
            self,
            self.report_type_var,
            "Spending by Category",
            "Income vs. Expenses",
            "Monthly Comparison",
            command=self.update_report_options
        )
        self.report_type_dropdown.pack()
        self.date_range_label = tk.Label(self, text="Date Range:")
        self.date_range_label.pack()
        self.date_range_entry = tk.Entry(self, textvariable=self.date_range_var)
        self.date_range_entry.pack()
        self.category_label = tk.Label(self, text="Category:")
        self.category_label.pack()
        self.category_entry = tk.Entry(self, textvariable=self.category_var)
        self.category_entry.pack()
        self.income_expense_label = tk.Label(self, text="Income/Expense:")
        self.income_expense_label.pack()
        self.income_expense_dropdown = tk.OptionMenu(
            self,
            self.income_expense_var,
            "All",
            "Income",
            "Expense"
        )
        self.income_expense_dropdown.pack()
        self.generate_report_button = tk.Button(self, text="Generate Report", command=self.fetch_and_generate_report)
        self.generate_report_button.pack()
    def update_report_options(self, report_type):
        if report_type == "Spending by Category":
            self.category_label.config(text="Category:")
            self.income_expense_label.pack()
            self.income_expense_dropdown.pack()
        elif report_type == "Income vs. Expenses":
            self.category_label.config(text="Category:")
            self.income_expense_label.config(text="Type:")
            self.income_expense_dropdown.pack()
        elif report_type == "Monthly Comparison":
            self.category_label.config(text="Month:")
            self.income_expense_label.pack_forget()
            self.income_expense_dropdown.pack_forget()
    def fetch_and_generate_report(self):
        report_type = self.report_type_var.get()
        date_range = self.date_range_var.get()
        category = self.category_var.get()
        income_expense = self.income_expense_var.get()
        # Fetch necessary data
        report_data = self.fetch_report_data(report_type, date_range, category, income_expense)
        if report_data.empty:
            messagebox.showerror("Error", "No data available for the selected criteria.")
            return
        # Generate report
        report = self.generate_report_from_data(report_data)
        if report.empty:
            messagebox.showerror("Error", "Invalid report data.")
            return
        # Display report
        self.display_report(report)
    def fetch_report_data(self, report_type, date_range, category, income_expense):
        # Fetch necessary data from the application's transaction data or database
        report_data = self.master.transaction_data  # Replace with actual transaction data or database retrieval
        if report_type == "Spending by Category":
            # Filter data based on category
            if category != "All Categories":
                report_data = report_data[report_data["category"] == category]
        elif report_type == "Income vs. Expenses":
            # Filter data based on income/expense type
            if income_expense != "All":
                report_data = report_data[report_data["type"] == income_expense]
        elif report_type == "Monthly Comparison":
            # Filter data based on date range
            if date_range != "All Time":
                # Apply date range filter logic
                pass
        return report_data
    def generate_report_from_data(self, report_data):
        # Add logic to generate the report from the fetched data
        # Example code:
        columns = report_data.columns
        if "category" in columns:
            report = report_data.groupby("category")["amount"].sum().reset_index()
            report["type"] = ""
            report["month"] = ""
            report["income"] = 0
            report["expenses"] = 0
        elif "type" in columns:
            report = report_data.groupby("type")["amount"].sum().reset_index()
            report["category"] = ""
            report["month"] = ""
            report["income"] = 0
            report["expenses"] = 0
        elif "month" in columns:
            report = report_data.copy()
            report["category"] = ""
            report["type"] = ""
            report["income"] = 0
            report["expenses"] = 0
        else:
            return pd.DataFrame()  # Return an empty DataFrame if report data is not recognized
        return report
    def display_report(self, report):
        # Add logic to display the generated report
        # Example code:
        if isinstance(report, pd.DataFrame):
            if "category" in report.columns:
                # Generate bar chart for spending by category
                categories = report["category"]
                amounts = report["amount"]
                plt.bar(categories, amounts)
                plt.xlabel("Category")
                plt.ylabel("Amount")
                plt.title("Spending by Category")
                plt.show()
            elif "type" in report.columns:
                # Generate pie chart for income vs. expenses
                types = report["type"]
                amounts = report["amount"]
                plt.pie(amounts, labels=types, autopct="%1.1f%%")
                plt.title("Income vs. Expenses")
                plt.show()
            elif "month" in report.columns:
                # Generate line chart for monthly comparison
                months = report["month"]
                incomes = report["income"]
                expenses = report["expenses"]
                plt.plot(months, incomes, marker="o", label="Income")
                plt.plot(months, expenses, marker="o", label="Expenses")
                plt.xlabel("Month")
                plt.ylabel("Amount")
                plt.title("Monthly Comparison")
                plt.legend()
                plt.show()
        else:
            messagebox.showerror("Error", "Invalid report data.")
    def lift(self):
        self.master.lift()
        self.master.tkraise()