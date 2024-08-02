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
        self.mainloop()
    def start_game(self):
        self.destroy()
        game = Game()
        game.start()
if __name__ == "__main__":
    main_menu = MainMenu()