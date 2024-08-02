import tkinter as tk
from game import Game
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Knight's Tour")
        self.geometry("400x400")
        self.game = Game(self)
        self.menu_frame = tk.Frame(self)
        self.menu_frame.pack(pady=20)
        self.difficulty_label = tk.Label(self.menu_frame, text="Select Difficulty:")
        self.difficulty_label.pack()
        self.difficulty_var = tk.StringVar()
        self.difficulty_var.set("Easy")
        self.difficulty_menu = tk.OptionMenu(self.menu_frame, self.difficulty_var, "Easy", "Medium", "Hard")
        self.difficulty_menu.pack()
        self.start_button = tk.Button(self.menu_frame, text="Start Game", command=self.start_game)
        self.start_button.pack()
    def start_game(self):
        difficulty = self.difficulty_var.get()
        self.game.start(difficulty)
if __name__ == "__main__":
    app = Application()
    app.mainloop()