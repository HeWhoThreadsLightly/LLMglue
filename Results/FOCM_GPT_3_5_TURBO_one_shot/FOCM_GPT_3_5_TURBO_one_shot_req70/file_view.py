'''
The file_view module of the File Organizer and Content Manager (FOCM) application.
'''
import tkinter as tk
class FileView:
    def __init__(self, parent):
        self.parent = parent
        self.listbox = tk.Listbox(self.parent)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    def load_files(self, files):
        # TODO: Implement loading the files in the view
        self.listbox.delete(0, tk.END)
        for file in files:
            self.listbox.insert(tk.END, file)
    def select_file(self, file):
        # TODO: Implement selecting a file in the view
        self.listbox.selection_clear(0, tk.END)
        index = self.listbox.get(0, tk.END).index(file)
        self.listbox.selection_set(index)