'''
Main script to run the Knight's Tour puzzle game.
'''
import tkinter as tk
from tkinter import messagebox
from game import Game
from board import Board
from knight import Knight
from settings import Settings
class GameWindow:
    def __init__(self, game):
        self.game = game
        self.move_counter = 0
        self.is_paused = False
        self.is_completed = False
    def move_knight(self, row, col):
        if self.is_paused or self.is_completed:
            return
        self.move_counter += 1
        self.game.move_knight(row, col)
        self.update_move_counter()
    def undo_move(self):
        if self.is_paused or self.is_completed:
            return
        self.move_counter -= 1
        self.game.undo()
        self.update_move_counter()
    def show_hint(self):
        if self.is_paused or self.is_completed:
            return
        self.game.show_hint()
    def update_move_counter(self):
        self.move_counter_label.config(text=f"Moves: {self.move_counter}")
    def toggle_pause(self):
        self.is_paused = not self.is_paused
        if self.is_paused:
            self.pause_button.config(text="Resume")
        else:
            self.pause_button.config(text="Pause")
    def open_menu(self):
        if self.is_paused or self.is_completed:
            return
        self.toggle_pause()  # Pause the game
        menu = tk.Menu(self.window)
        menu.add_command(label="Settings", command=self.game.settings.customize_settings)
        menu.add_command(label="Return to Main Menu", command=self.return_to_main_menu)
        menu.add_command(label="Restart Game", command=self.restart_game)
        self.window.config(menu=menu)
    def return_to_main_menu(self):
        self.window.destroy()  # Close the game window
        self.game.board.master.deiconify()  # Show the main menu window
    def restart_game(self):
        self.window.destroy()  # Close the game window
        self.game.start()  # Start a new game
        self.create_game_window()  # Create a new game window
        self.toggle_pause()  # Initialize the game as not paused
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
        self.pause_button = tk.Button(self.window, text="Pause/Menu", command=self.open_menu)
        self.pause_button.pack()
        self.board.canvas = tk.Canvas(self.board_frame, width=400, height=400)
        self.board.canvas.pack()
        self.board.draw()
        self.knight.draw()
        self.board.canvas.bind("<Button-1>", self.handle_board_click)
    def handle_board_click(self, event):
        if self.is_completed:
            messagebox.showinfo("Game Completed", "The game has already been completed.")
            return
        if self.is_paused:
            return
        row = event.y // self.board.square_size
        col = event.x // self.board.square_size
        if self.board.is_valid_move(row, col):
            if not self.board.is_visited(row, col):
                self.move_knight(row, col)
                self.update_move_counter()  # Update the move counter label
            else:
                messagebox.showerror("Invalid Move", "This square has already been visited! Please select a different square.")
        else:
            messagebox.showerror("Invalid Move", "Invalid move! Please select a valid move.")
    def start(self):
        self.game.start()
        self.create_game_window()
        self.toggle_pause()  # Initialize the game as not paused
        self.window.mainloop()
if __name__ == "__main__":
    settings = Settings(None)
    board = Board(None, "", settings)
    knight = Knight(None)
    game = Game(board, knight, settings)
    game_window = GameWindow(game)
    game_window.start()