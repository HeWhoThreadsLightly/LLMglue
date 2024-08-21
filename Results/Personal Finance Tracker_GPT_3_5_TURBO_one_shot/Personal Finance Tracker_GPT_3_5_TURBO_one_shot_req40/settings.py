'''
Settings window for the personal finance management application.
'''
import tkinter as tk
class SettingsWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.currency_label = tk.Label(self, text="Default Currency:")
        self.currency_label.pack()
        self.currency_entry = tk.Entry(self)
        self.currency_entry.pack()
        self.date_format_label = tk.Label(self, text="Date Format:")
        self.date_format_label.pack()
        self.date_format_entry = tk.Entry(self)
        self.date_format_entry.pack()
        self.theme_label = tk.Label(self, text="Application Theme:")
        self.theme_label.pack()
        self.theme_entry = tk.Entry(self)
        self.theme_entry.pack()
        self.notification_label = tk.Label(self, text="Notification Preferences:")
        self.notification_label.pack()
        self.notification_entry = tk.Entry(self)
        self.notification_entry.pack()
        self.backup_button = tk.Button(self, text="Backup Data")
        self.backup_button.pack()
        self.restore_button = tk.Button(self, text="Restore Data")
        self.restore_button.pack()
        self.pack()