import tkinter as tk
class Knight:
    def __init__(self, board):
        self.board = board
        self.current_row = 0
        self.current_col = 0
    def draw(self):
        x1, y1, x2, y2 = self.board.get_square_coordinates(self.current_row, self.current_col)
        self.board.canvas.create_oval(x1, y1, x2, y2, fill="blue")