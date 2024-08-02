import tkinter as tk
import tkinter.simpledialog as sd
from tkinter import messagebox
class Board:
    def __init__(self, master, difficulty):
        self.master = master
        self.difficulty = difficulty
        self.size = self.get_board_size()
        self.canvas = tk.Canvas(self.master, width=400, height=400)
        self.canvas.pack()
        self.square_size = 400 // self.size
    def get_board_size(self):
        if self.difficulty == "Easy":
            return 5
        elif self.difficulty == "Medium":
            return 6
        elif self.difficulty == "Hard":
            return 8
    def draw(self):
        self.canvas.delete("all")
        for row in range(self.size):
            for col in range(self.size):
                x1, y1, x2, y2 = self.get_square_coordinates(row, col)
                self.canvas.create_rectangle(x1, y1, x2, y2, fill="white")
    def get_square_coordinates(self, row, col):
        x1 = col * self.square_size
        y1 = row * self.square_size
        x2 = x1 + self.square_size
        y2 = y1 + self.square_size
        return x1, y1, x2, y2
    def select_difficulty(self):
        difficulty = sd.askstring("Select Difficulty", "Choose difficulty level", initialvalue="Easy", parent=self.master)
        return difficulty
    def is_valid_move(self, row, col):
        if row < 0 or row >= self.size or col < 0 or col >= self.size:
            return False
        return True