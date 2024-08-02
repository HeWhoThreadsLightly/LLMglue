import tkinter as tk
from game import Game
from board import Board
from knight import Knight
from settings import Settings
class ChessGame:
    def __init__(self):
        self.root = tk.Tk()
        self.settings = Settings()
        self.game = None
    def start(self):
        self.game = Game(Board(self.root, "", self.settings), Knight(None), self.settings)
        self.game.start()
        self.root.mainloop()
if __name__ == "__main__":
    chess_game = ChessGame()
    chess_game.start()