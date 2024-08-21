import tkinter as tk
from tkinter import simpledialog
class WebsiteBlocker:
    def __init__(self, root):
        self.root = root
        self.block_list = tk.Listbox(self.root)
        self.add_website_button = tk.Button(self.root, text="Add Website", command=self.add_website)
        self.remove_website_button = tk.Button(self.root, text="Remove Website", command=self.remove_website)
    def add_website(self):
        website = simpledialog.askstring("Add Website", "Enter website URL:")
        if website:
            self.block_list.insert(tk.END, website)
    def remove_website(self):
        selected_website = self.block_list.curselection()
        if selected_website:
            self.block_list.delete(selected_website)