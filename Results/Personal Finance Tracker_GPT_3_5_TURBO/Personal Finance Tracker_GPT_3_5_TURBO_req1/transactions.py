'''
This file contains the implementation of the TransactionsWindow class.
'''
import tkinter as tk
class TransactionsWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title("Transactions")
        self.master.geometry("800x600")
        # Add transactions content here
        self.pack()