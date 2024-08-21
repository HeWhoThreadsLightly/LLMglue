'''
Select difficulty window for the Memory Match game.
'''
import tkinter as tk
from game_window import GameWindow
class SelectDifficultyWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Select Difficulty")
        self.create_widgets()
    def create_widgets(self):
        # Instruction text
        self.instruction_label = tk.Label(self, text="Select the difficulty level:")
        self.instruction_label.pack()
        # Difficulty level buttons
        self.easy_button = tk.Button(self, text="Easy", command=lambda: self.start_game("Easy"))
        self.easy_button.pack()
        self.medium_button = tk.Button(self, text="Medium", command=lambda: self.start_game("Medium"))
        self.medium_button.pack()
        self.hard_button = tk.Button(self, text="Hard", command=lambda: self.start_game("Hard"))
        self.hard_button.pack()
        # Back button
        self.back_button = tk.Button(self, text="Back", command=self.return_to_main_menu)
        self.back_button.pack()
    def start_game(self, difficulty):
        self.withdraw()
        game_window = GameWindow(self.master, difficulty)
        game_window.mainloop()
    def return_to_main_menu(self):
        self.master.deiconify()
        self.destroy()
class HighScoresWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("High Scores")
        # Display high scores from previous games
        pass
    def return_to_main_menu(self):
        self.master.deiconify()
        self.destroy()
class SettingsWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Settings")
        # Settings options for sound, theme, and instructions
        pass
    def return_to_main_menu(self):
        self.master.deiconify()
        self.destroy()