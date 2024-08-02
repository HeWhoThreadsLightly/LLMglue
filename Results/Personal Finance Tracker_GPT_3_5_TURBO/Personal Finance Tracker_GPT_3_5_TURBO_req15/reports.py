'''
This file contains the implementation of the ReportsWindow class.
'''
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import pandas as pd
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
            "Monthly Comparison"
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
        self.generate_report_button = tk.Button(self, text="Generate Report", command=self.generate_report)
        self.generate_report_button.pack()
    def generate_report(self):
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
        # Display report
        self.display_report(report)
    def fetch_report_data(self, report_type, date_range, category, income_expense):
        # Add logic to fetch necessary data for the report
        # Example code:
        if report_type == "Spending by Category":
            report_data = {
                "Category": ["Food", "Rent", "Transportation", "Entertainment"],
                "Amount": [500, 1000, 300, 200]
            }
        elif report_type == "Income vs. Expenses":
            report_data = {
                "Type": ["Income", "Expenses"],
                "Amount": [5000, 3000]
            }
        elif report_type == "Monthly Comparison":
            report_data = {
                "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
                "Income": [1000, 2000, 1500, 1800, 2500, 3000],
                "Expenses": [800, 1500, 1200, 1400, 2000, 2500]
            }
        else:
            return pd.DataFrame()
        df = pd.DataFrame(report_data)
        if date_range != "All Time":
            # Filter data based on date range
            df = self.filter_data_by_date(df, date_range)
        if category != "All Categories":
            # Filter data based on category
            df = self.filter_data_by_category(df, category)
        if income_expense != "All":
            # Filter data based on income/expense type
            df = self.filter_data_by_income_expense(df, income_expense)
        return df
    def filter_data_by_date(self, df, date_range):
        # Add logic to filter data by date range
        # Example code:
        if date_range == "This Month":
            df = df[df["Date"].dt.month == pd.Timestamp.now().month]
        elif date_range == "Last Month":
            df = df[df["Date"].dt.month == pd.Timestamp.now().month - 1]
        elif date_range == "Last 3 Months":
            df = df[df["Date"].dt.month >= pd.Timestamp.now().month - 3]
        elif date_range == "Last 6 Months":
            df = df[df["Date"].dt.month >= pd.Timestamp.now().month - 6]
        elif date_range == "Last Year":
            df = df[df["Date"].dt.year == pd.Timestamp.now().year - 1]
        return df
    def filter_data_by_category(self, df, category):
        # Add logic to filter data by category
        # Example code:
        df = df[df["Category"] == category]
        return df
    def filter_data_by_income_expense(self, df, income_expense):
        # Add logic to filter data by income/expense type
        # Example code:
        if income_expense == "Income":
            df = df[df["Type"] == "Income"]
        elif income_expense == "Expense":
            df = df[df["Type"] == "Expense"]
        return df
    def generate_report_from_data(self, report_data):
        # Add logic to generate the report from the fetched data
        # Example code:
        columns = report_data.columns
        if "Category" in columns:
            report = report_data.groupby("Category")["Amount"].sum().reset_index()
            report["Type"] = ""
            report["Month"] = ""
            report["Income"] = 0
            report["Expenses"] = 0
        elif "Type" in columns:
            report = report_data.groupby("Type")["Amount"].sum().reset_index()
            report["Category"] = ""
            report["Month"] = ""
            report["Income"] = 0
            report["Expenses"] = 0
        elif "Month" in columns:
            report = report_data.copy()
            report["Category"] = ""
            report["Type"] = ""
            report["Income"] = 0
            report["Expenses"] = 0
        else:
            messagebox.showerror("Error", "Invalid report type.")
            return pd.DataFrame(columns=["Category", "Amount", "Type", "Month", "Income", "Expenses"])
        return report
    def display_report(self, report):
        # Add logic to display the generated report
        # Example code:
        if isinstance(report, pd.DataFrame):
            if "Category" in report.columns:
                # Generate bar chart for spending by category
                categories = report["Category"]
                amounts = report["Amount"]
                plt.bar(categories, amounts)
                plt.xlabel("Category")
                plt.ylabel("Amount")
                plt.title("Spending by Category")
                plt.show()
            elif "Type" in report.columns:
                # Generate pie chart for income vs. expenses
                types = report["Type"]
                amounts = report["Amount"]
                plt.pie(amounts, labels=types, autopct="%1.1f%%")
                plt.title("Income vs. Expenses")
                plt.show()
            elif "Month" in report.columns:
                # Generate line chart for monthly comparison
                months = report["Month"]
                incomes = report["Income"]
                expenses = report["Expenses"]
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