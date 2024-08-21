import tkinter as tk
from tkinter import simpledialog
class TaskManager:
    def __init__(self, root):
        self.root = root
        self.task_list = tk.Listbox(self.root)
        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.edit_task_button = tk.Button(self.root, text="Edit Task", command=self.edit_task)
        self.complete_task_button = tk.Button(self.root, text="Complete Task", command=self.complete_task)
    def add_task(self):
        task_title = simpledialog.askstring("Add Task", "Enter task title:")
        if task_title:
            self.task_list.insert(tk.END, task_title)
    def edit_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            task_title = self.task_list.get(selected_task)
            new_task_title = simpledialog.askstring("Edit Task", "Enter new task title:", initialvalue=task_title)
            if new_task_title:
                self.task_list.delete(selected_task)
                self.task_list.insert(selected_task, new_task_title)
    def complete_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            self.task_list.delete(selected_task)