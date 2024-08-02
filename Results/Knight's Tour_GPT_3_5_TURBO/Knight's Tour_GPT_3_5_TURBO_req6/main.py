import tkinter as tk
from game import Game
from board import Board
from knight import Knight
class ChessGame:
    def __init__(self):
        self.root = tk.Tk()
        self.game = None
    def start(self):
        self.game = Game(Board(self.root, ""), Knight(None))
        self.game.start()
        self.root.mainloop()
if __name__ == "__main__":
    chess_game = ChessGame()
    chess_game.start()