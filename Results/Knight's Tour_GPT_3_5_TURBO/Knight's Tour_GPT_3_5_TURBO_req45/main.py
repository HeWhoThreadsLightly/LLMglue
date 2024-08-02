'''
Main script to run the Knight's Tour puzzle game.
'''
import tkinter as tk
from tkinter import messagebox
from game_window import GameWindow
from game import Game
from board import Board
from knight import Knight
from settings import Settings
class MainMenu:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Knight's Tour")
        self.window.geometry("400x400")
        self.settings = Settings(self.window)
        self.difficulty = None
    def start_game(self):
        self.difficulty = self.board.select_difficulty()
        if self.difficulty:
            self.window.withdraw()  # Hide the main menu window
            self.board.master = self.window
            self.game = Game(self.board, self.knight, self.settings)
            self.game_window = GameWindow(self.game, self.board, self.knight)
            self.game_window.start()
    def customize_settings(self):
        self.settings.customize_settings()
    def create_main_menu(self):
        self.board = Board(self.window, self.difficulty, self.settings)
        self.knight = Knight(self.board)
        self.board.draw()
        start_button = tk.Button(self.window, text="Start Game", command=self.start_game)
        start_button.pack()
        settings_button = tk.Button(self.window, text="Settings", command=self.customize_settings)
        settings_button.pack()
        self.window.mainloop()
if __name__ == "__main__":
    main_menu = MainMenu()
    main_menu.create_main_menu()