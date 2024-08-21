'''
The file_tree module of the File Organizer and Content Manager (FOCM) application.
'''
import tkinter as tk
from tkinter import ttk
class FileTree:
    def __init__(self, parent):
        self.parent = parent
        self.tree = ttk.Treeview(self.parent)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    def load_directory(self, directory):
        # TODO: Implement loading the directory tree
        root_node = DirectoryNode(directory)
        self._load_directory(root_node, self.tree)
    def _load_directory(self, directory_node, tree_node):
        tree_node.delete(*tree_node.get_children())
        self._display_directory(directory_node, tree_node)
        for child_node in directory_node.children:
            child_tree_node = tree_node.insert(tree_node, tk.END, text=child_node.name)
            self._load_directory(child_node, child_tree_node)
    def _display_directory(self, directory_node, tree_node):
        tree_node.delete(*tree_node.get_children())
        for child_node in directory_node.children:
            tree_node.insert(tree_node, tk.END, text=child_node.name)
    def select_directory(self, directory):
        # TODO: Implement selecting a directory in the tree
        selected_node = self._find_directory_node(directory, self.tree)
        if selected_node:
            self.tree.selection_set(selected_node)
    def _find_directory_node(self, directory, tree_node):
        for child_node in tree_node.get_children():
            if tree_node.item(child_node)["text"] == directory:
                return child_node
        return None
class DirectoryNode:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
    def add_child(self, child):
        self.children.append(child)
    def remove_child(self, child):
        self.children.remove(child)
    def get_path(self):
        if self.parent is None:
            return self.name
        else:
            return self.parent.get_path() + "/" + self.name
    def __str__(self):
        return self.get_path()