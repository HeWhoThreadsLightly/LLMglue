'''
This file contains the implementation of the ReportsWindow class.
'''
import tkinter as tk
class ReportsWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Reports")
        self.master.geometry("800x600")
        # Add reports content here
        self.pack()