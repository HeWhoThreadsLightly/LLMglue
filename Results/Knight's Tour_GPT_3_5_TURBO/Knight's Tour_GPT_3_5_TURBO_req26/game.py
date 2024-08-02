'''
Game class that represents the puzzle game based on the Knight's Tour problem.
'''
from tkinter import messagebox
from board import Board
from knight import Knight
class Game:
    def __init__(self, board, knight, settings):
        self.board = board
        self.knight = knight
        self.settings = settings
        self.move_history = []  # Keep track of the moves made by the player
        self.is_paused = False
        self.is_completed = False
    def move_knight(self, row, col):
        if self.is_paused or self.is_completed:
            return
        # Check if the move is valid and the square has not been visited
        if self.board.is_valid_move(row, col) and not self.board.is_visited(row, col):
            # Update the knight's position
            self.knight.move_knight(row, col)
            # Add the move to the move history
            self.move_history.append((row, col))
            # Mark the square as visited
            self.board.mark_visited(row, col)
            # Redraw the board
            self.board.draw()
            # Check if all squares have been visited
            if len(self.move_history) == self.board.size ** 2:
                self.is_completed = True
                messagebox.showinfo("Game Completed", "Congratulations! You have completed the game.")
                self.board.master.quit()
        else:
            # Display an error message for invalid move or visited square
            if self.board.is_visited(row, col):
                messagebox.showerror("Invalid Move", "This square has already been visited! Please select a different square.")
            else:
                messagebox.showerror("Invalid Move", "Invalid move! Please select a valid move.")
    def undo(self):
        if self.is_paused or self.is_completed:
            return
        if self.move_history:
            # Get the last move from the move history
            last_move = self.move_history.pop()
            # Revert the knight's position
            self.knight.move_knight(last_move[0], last_move[1])
            # Unmark the square as visited
            self.board.unmark_visited(last_move[0], last_move[1])
            # Redraw the board
            self.board.draw()
    def get_hint(self):
        if self.is_paused or self.is_completed:
            return None
        # Get the current position of the knight
        current_row, current_col = self.knight.current_row, self.knight.current_col
        # Get the list of unvisited squares on the board
        unvisited_squares = []
        for row in range(self.board.size):
            for col in range(self.board.size):
                if not self.board.is_visited(row, col):
                    unvisited_squares.append((row, col))
        # Calculate the distances from the current position to each unvisited square
        distances = []
        for square in unvisited_squares:
            row, col = square
            distance = abs(row - current_row) + abs(col - current_col)
            distances.append(distance)
        # Find the square with the minimum distance
        min_distance = min(distances)
        min_distance_index = distances.index(min_distance)
        hint_square = unvisited_squares[min_distance_index]
        # Return the hint square
        return hint_square
    def show_hint(self):
        if self.is_paused or self.is_completed:
            return
        hint_square = self.get_hint()
        if hint_square:
            messagebox.showinfo("Hint", f"The next move is to square {hint_square[0] + 1}, {hint_square[1] + 1}.")
        else:
            messagebox.showinfo("Hint", "No more hints available.")
    def start(self):
        difficulty = self.board.select_difficulty()
        self.board = Board(self.board.master, difficulty, self.settings)
        self.knight = Knight(self.board)
        self.board.draw()
        self.knight.draw()