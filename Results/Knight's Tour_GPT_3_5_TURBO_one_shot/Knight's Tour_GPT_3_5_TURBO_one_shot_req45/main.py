'''
Main file for the Knight's Tour puzzle game.
'''
import tkinter as tk
from game_window import GameWindow
class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Knight's Tour")
        self.geometry("400x300")
        self.start_button = tk.Button(self, text="Start Game", command=self.start_game)
        self.start_button.pack()
        self.options_button = tk.Button(self, text="Options/Settings", command=self.open_options)
        self.options_button.pack()
        self.tutorial_button = tk.Button(self, text="Tutorial", command=self.open_tutorial)
        self.tutorial_button.pack()
        self.high_scores_button = tk.Button(self, text="High Scores", command=self.open_high_scores)
        self.high_scores_button.pack()
        self.exit_button = tk.Button(self, text="Exit", command=self.quit)
        self.exit_button.pack()
    def start_game(self):
        self.game_window = GameWindow(self)
        self.withdraw()
    def open_options(self):
        options_window = OptionsWindow(self)
        self.wait_window(options_window)
    def open_tutorial(self):
        tutorial_window = TutorialWindow(self)
        self.wait_window(tutorial_window)
    def open_high_scores(self):
        high_scores_window = HighScoresWindow(self)
        self.wait_window(high_scores_window)
class OptionsWindow(tk.Toplevel):
    def __init__(self, main_menu):
        super().__init__()
        self.title("Options/Settings")
        self.geometry("400x300")
        self.visual_settings_button = tk.Button(self, text="Visual Settings", command=self.open_visual_settings)
        self.visual_settings_button.pack()
        self.difficulty_settings_button = tk.Button(self, text="Difficulty Settings", command=self.open_difficulty_settings)
        self.difficulty_settings_button.pack()
        self.back_button = tk.Button(self, text="Back", command=self.return_to_main_menu)
        self.back_button.pack()
    def open_visual_settings(self):
        visual_settings_window = VisualSettingsWindow(self)
        self.wait_window(visual_settings_window)
    def open_difficulty_settings(self):
        difficulty_settings_window = DifficultySettingsWindow(self)
        self.wait_window(difficulty_settings_window)
    def return_to_main_menu(self):
        self.destroy()
        main_menu.deiconify()
class VisualSettingsWindow(tk.Toplevel):
    def __init__(self, options_window):
        super().__init__()
        self.title("Visual Settings")
        self.geometry("400x300")
        # TODO: Implement visual settings options
        self.back_button = tk.Button(self, text="Back", command=self.return_to_options_window)
        self.back_button.pack()
    def return_to_options_window(self):
        self.destroy()
        options_window.deiconify()
class DifficultySettingsWindow(tk.Toplevel):
    def __init__(self, options_window):
        super().__init__()
        self.title("Difficulty Settings")
        self.geometry("400x300")
        # TODO: Implement difficulty settings options
        self.back_button = tk.Button(self, text="Back", command=self.return_to_options_window)
        self.back_button.pack()
    def return_to_options_window(self):
        self.destroy()
        options_window.deiconify()
class TutorialWindow(tk.Toplevel):
    def __init__(self, main_menu):
        super().__init__()
        self.title("Tutorial")
        self.geometry("400x300")
        self.text_label = tk.Label(self, text="This is a tutorial on how to play the game.")
        self.text_label.pack()
        self.back_button = tk.Button(self, text="Back", command=self.return_to_main_menu)
        self.back_button.pack()
    def return_to_main_menu(self):
        self.destroy()
        main_menu.deiconify()
class HighScoresWindow(tk.Toplevel):
    def __init__(self, main_menu):
        super().__init__()
        self.title("High Scores")
        self.geometry("400x300")
        self.score_list_label = tk.Label(self, text="High Scores:")
        self.score_list_label.pack()
        self.filters_button = tk.Button(self, text="Filters", command=self.open_filters)
        self.filters_button.pack()
        self.back_button = tk.Button(self, text="Back", command=self.return_to_main_menu)
        self.back_button.pack()
    def open_filters(self):
        filters_window = FiltersWindow(self)
        self.wait_window(filters_window)
    def return_to_main_menu(self):
        self.destroy()
        main_menu.deiconify()
class FiltersWindow(tk.Toplevel):
    def __init__(self, high_scores_window):
        super().__init__()
        self.title("Filters")
        self.geometry("400x300")
        # TODO: Implement filters options
        self.back_button = tk.Button(self, text="Back", command=self.return_to_high_scores_window)
        self.back_button.pack()
    def return_to_high_scores_window(self):
        self.destroy()
        high_scores_window.deiconify()
if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.mainloop()