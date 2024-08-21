'''
Main menu window for the Memory Match game.
'''
import tkinter as tk
from select_difficulty_window import SelectDifficultyWindow
from high_scores_window import HighScoresWindow
from settings_window import SettingsWindow
class MainMenuWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Memory Match Game")
        self.create_widgets()
    def create_widgets(self):
        # Game title
        self.title_label = tk.Label(self, text="Memory Match Game", font=("Arial", 24))
        self.title_label.pack(pady=20)
        # Play button
        self.play_button = tk.Button(self, text="Play", command=self.open_select_difficulty)
        self.play_button.pack(pady=10)
        # High scores button
        self.high_scores_button = tk.Button(self, text="High Scores", command=self.open_high_scores)
        self.high_scores_button.pack(pady=10)
        # Settings button
        self.settings_button = tk.Button(self, text="Settings", command=self.open_settings)
        self.settings_button.pack(pady=10)
        # Exit button
        self.exit_button = tk.Button(self, text="Exit", command=self.quit)
        self.exit_button.pack(pady=10)
    def open_select_difficulty(self):
        self.withdraw()
        select_difficulty_window = SelectDifficultyWindow(self)
        select_difficulty_window.mainloop()
    def open_high_scores(self):
        self.withdraw()
        high_scores_window = HighScoresWindow(self)
        high_scores_window.mainloop()
    def open_settings(self):
        self.withdraw()
        settings_window = SettingsWindow(self)
        settings_window.mainloop()
if __name__ == "__main__":
    main_menu_window = MainMenuWindow()
    main_menu_window.mainloop()