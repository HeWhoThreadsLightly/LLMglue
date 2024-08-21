import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib.pyplot as plt
import pandas as pd
class ReportingAnalytics:
    def __init__(self, root):
        self.root = root
        self.daily_report_button = tk.Button(self.root, text="Daily Report", command=self.daily_report)
        self.weekly_report_button = tk.Button(self.root, text="Weekly Report", command=self.weekly_report)
        self.monthly_report_button = tk.Button(self.root, text="Monthly Report", command=self.monthly_report)
        self.productivity_graph_button = tk.Button(self.root, text="Productivity Graph", command=self.productivity_graph)
    def daily_report(self):
        messagebox.showinfo("Daily Report", "This is the daily report.")
    def weekly_report(self):
        messagebox.showinfo("Weekly Report", "This is the weekly report.")
    def monthly_report(self):
        messagebox.showinfo("Monthly Report", "This is the monthly report.")
    def productivity_graph(self):
        data = {
            'Date': ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05'],
            'Focus Sessions': [4, 5, 6, 3, 7],
            'Tasks Completed': [8, 10, 12, 6, 14],
            'Time Spent (minutes)': [100, 120, 150, 90, 180]
        }
        df = pd.DataFrame(data)
        plt.figure(figsize=(8, 6))
        plt.plot(df['Date'], df['Focus Sessions'], label='Focus Sessions')
        plt.plot(df['Date'], df['Tasks Completed'], label='Tasks Completed')
        plt.plot(df['Date'], df['Time Spent (minutes)'], label='Time Spent (minutes)')
        plt.xlabel('Date')
        plt.ylabel('Count')
        plt.title('Productivity Trends')
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()