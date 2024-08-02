'''
Memory Match Game
'''
import tkinter as tk
from game import Game
class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Memory Match Game")
        self.geometry("400x300")
        title_label = tk.Label(self, text="Memory Match Game", font=("Arial", 24))
        title_label.pack(pady=50)
        start_button = tk.Button(self, text="Start Game", command=self.start_game)
        start_button.pack(pady=20)
    def start_game(self):
        self.destroy()
        select_difficulty = SelectDifficulty()
        select_difficulty.mainloop()
class SelectDifficulty(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Select Difficulty")
        self.geometry("400x300")
        instruction_label = tk.Label(self, text="Select Difficulty", font=("Arial", 24))
        instruction_label.pack(pady=50)
        easy_button = tk.Button(self, text="Easy", command=self.start_game_easy)
        easy_button.pack(pady=20)
        medium_button = tk.Button(self, text="Medium", command=self.start_game_medium)
        medium_button.pack(pady=20)
        hard_button = tk.Button(self, text="Hard", command=self.start_game_hard)
        hard_button.pack(pady=20)
    def start_game_easy(self):
        self.destroy()
        game = Game(difficulty="easy")
        game.start()
    def start_game_medium(self):
        self.destroy()
        game = Game(difficulty="medium")
        game.start()
    def start_game_hard(self):
        self.destroy()
        game = Game(difficulty="hard")
        game.start()
if __name__ == "__main__":
    main_menu = MainMenu()