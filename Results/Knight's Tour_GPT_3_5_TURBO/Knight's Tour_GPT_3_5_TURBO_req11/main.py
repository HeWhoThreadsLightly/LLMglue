import tkinter as tk
from tkinter import messagebox
from game import Game
from board import Board
from knight import Knight
from settings import Settings
class GameWindow:
    def __init__(self, board, knight, settings):
        self.board = board
        self.knight = knight
        self.settings = settings
        self.move_counter = 0
    def move_knight(self, row, col):
        self.move_counter += 1
        self.game.move_knight(row, col)
        self.update_move_counter()
    def undo_move(self):
        self.move_counter -= 1
        self.game.undo()
        self.update_move_counter()
    def show_hint(self):
        self.game.show_hint()
    def update_move_counter(self):
        self.move_counter_label.config(text=f"Moves: {self.move_counter}")
    def create_game_window(self):
        self.window = tk.Toplevel()
        self.window.title("Knight's Tour")
        self.window.geometry("400x450")
        self.board_frame = tk.Frame(self.window)
        self.board_frame.pack()
        self.move_counter_label = tk.Label(self.window, text="Moves: 0")
        self.move_counter_label.pack()
        self.undo_button = tk.Button(self.window, text="Undo", command=self.undo_move)
        self.undo_button.pack()
        self.hint_button = tk.Button(self.window, text="Hint", command=self.show_hint)
        self.hint_button.pack()
        self.board.canvas = tk.Canvas(self.board_frame, width=400, height=400)
        self.board.canvas.pack()
        self.board.draw()
        self.knight.draw()
        self.board.canvas.bind("<Button-1>", self.handle_board_click)
    def handle_board_click(self, event):
        row = event.y // self.board.square_size
        col = event.x // self.board.square_size
        self.move_knight(row, col)
    def start(self):
        self.create_game_window()
        self.window.mainloop()
if __name__ == "__main__":
    settings = Settings(None)
    game = Game(Board(None, "", settings), Knight(None), settings)
    game_window = GameWindow(game.board, game.knight, settings)
    game_window.game = game
    game_window.start()