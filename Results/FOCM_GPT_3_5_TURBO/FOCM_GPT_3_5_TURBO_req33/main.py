import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, simpledialog
from tkinter.ttk import Treeview, Label
import os
import glob
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Organizer and Content Manager")
        self.create_directory_tree()
        self.create_content_view()
        self.create_toolbar()
        self.create_status_bar()
    def create_directory_tree(self):
        '''
        Create the directory tree pane in the main window
        '''
        self.directory_tree = Treeview(self)
        self.directory_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.update_directory_tree()
    def create_content_view(self):
        '''
        Create the content view pane in the main window
        '''
        self.content_view = Treeview(self)
        self.content_view.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    def create_toolbar(self):
        '''
        Create the toolbar with buttons for common actions in the main window
        '''
        toolbar = tk.Frame(self)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        new_folder_button = ttk.Button(toolbar, text="New Folder", command=self.create_new_folder)
        new_folder_button.pack(side=tk.LEFT)
        delete_file_button = ttk.Button(toolbar, text="Delete File", command=self.delete_file)
        delete_file_button.pack(side=tk.LEFT)
        refresh_view_button = ttk.Button(toolbar, text="Refresh View", command=self.refresh_view)
        refresh_view_button.pack(side=tk.LEFT)
        toggle_view_button = ttk.Button(toolbar, text="Toggle View", command=self.toggle_view)
        toggle_view_button.pack(side=tk.LEFT)
        self.search_bar = ttk.Entry(toolbar)
        self.search_bar.pack(side=tk.RIGHT)
        search_button = ttk.Button(toolbar, text="Search", command=self.perform_search)
        search_button.pack(side=tk.RIGHT)
    def create_status_bar(self):
        '''
        Create the status bar displaying information in the main window
        '''
        self.status_bar = Label(self, text="Total Files: 0 | Total Size: 0")
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    def create_new_folder(self):
        '''
        Handle the logic for creating a new folder
        '''
        selected_directory = self.directory_tree.focus()
        if selected_directory:
            new_folder_name = simpledialog.askstring("New Folder", "Enter the name of the new folder:")
            if new_folder_name:
                new_folder_path = os.path.join(selected_directory, new_folder_name)
                try:
                    os.mkdir(new_folder_path)
                    messagebox.showinfo("New Folder", f"Successfully created new folder: {new_folder_name}")
                except OSError:
                    messagebox.showerror("New Folder", f"Failed to create new folder: {new_folder_name}")
        else:
            messagebox.showwarning("New Folder", "Please select a directory first.")
    def delete_file(self):
        '''
        Handle the logic for deleting a file
        '''
        selected_file = self.content_view.focus()
        if selected_file:
            result = messagebox.askyesno("Delete File", "Are you sure you want to delete this file?")
            if result:
                try:
                    os.remove(selected_file)
                    messagebox.showinfo("Delete File", "File deleted successfully.")
                except OSError:
                    messagebox.showerror("Delete File", "Failed to delete file.")
        else:
            messagebox.showwarning("Delete File", "Please select a file first.")
    def refresh_view(self):
        '''
        Handle the logic for refreshing the view
        '''
        self.update_directory_tree()
        self.update_content_view()
    def toggle_view(self):
        '''
        Handle the logic for toggling between list/grid view
        '''
        current_view = self.content_view["view"]
        if current_view == "list":
            self.content_view["view"] = "grid"
        else:
            self.content_view["view"] = "list"
    def perform_search(self):
        '''
        Handle the logic for performing a search
        '''
        query = self.search_bar.get()
        if query:
            search_results = glob.glob(f"**/{query}*", recursive=True)
            self.update_content_view(search_results)
        else:
            messagebox.showwarning("Perform Search", "Please enter a search query.")
    def update_directory_tree(self):
        '''
        Update the directory tree with the current file system structure
        '''
        self.directory_tree.delete(*self.directory_tree.get_children())
        for dirpath, dirnames, filenames in os.walk("."):
            parent = self.directory_tree.insert("", "end", text=dirpath, open=True)
            for dirname in dirnames:
                self.directory_tree.insert(parent, "end", text=dirname)
            for filename in filenames:
                self.directory_tree.insert(parent, "end", text=filename)
    def update_content_view(self, files=None):
        '''
        Update the content view with the given list of files
        '''
        self.content_view.delete(*self.content_view.get_children())
        if files is None:
            files = []
        for file in files:
            if os.path.isdir(file):
                self.content_view.insert("", "end", text=file, tags=("folder",))
            else:
                self.content_view.insert("", "end", text=file, tags=("file",))
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()