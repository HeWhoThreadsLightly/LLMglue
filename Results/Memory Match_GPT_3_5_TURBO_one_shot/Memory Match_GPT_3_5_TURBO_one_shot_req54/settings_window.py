'''
Settings window for the Memory Match game.
'''
import tkinter as tk
class SettingsWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Settings")
        # Settings options for sound, theme, and instructions
        pass
    def return_to_main_menu(self):
        self.master.deiconify()
        self.destroy()