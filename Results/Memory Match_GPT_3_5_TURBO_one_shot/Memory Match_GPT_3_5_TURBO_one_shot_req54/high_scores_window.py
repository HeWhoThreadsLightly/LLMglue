'''
High scores window for the Memory Match game.
'''
import tkinter as tk
class HighScoresWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("High Scores")
        # Display high scores from previous games
        pass
    def return_to_main_menu(self):
        self.master.deiconify()
        self.destroy()