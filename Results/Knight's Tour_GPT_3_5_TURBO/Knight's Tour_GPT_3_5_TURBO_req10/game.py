from tkinter import messagebox
class Game:
    def __init__(self, board, knight, settings):
        self.board = board
        self.knight = knight
        self.settings = settings
        self.move_history = []  # Keep track of the moves made by the player
    def move_knight(self, row, col):
        # Check if the move is valid
        if self.board.is_valid_move(row, col):
            # Update the knight's position
            self.knight.move_knight(row, col)
            # Add the move to the move history
            self.move_history.append((row, col))
            # Redraw the board
            self.board.draw()
        else:
            # Display an error message for invalid move
            messagebox.showerror("Invalid Move", "Invalid move! Please select a valid move.")
    def undo(self):
        if self.move_history:
            # Get the last move from the move history
            last_move = self.move_history.pop()
            # Revert the knight's position
            self.knight.move_knight(last_move[0], last_move[1])
            # Redraw the board
            self.board.draw()
    def get_hint(self):
        # Get the current position of the knight
        current_row, current_col = self.knight.current_row, self.knight.current_col
        # Get the list of unvisited squares on the board
        unvisited_squares = []
        for row in range(self.board.size):
            for col in range(self.board.size):
                if (row, col) not in self.move_history:
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
        hint_square = self.get_hint()
        messagebox.showinfo("Hint", f"The next move is to square {hint_square[0] + 1}, {hint_square[1] + 1}.")
    def start(self):
        difficulty = self.board.select_difficulty()
        self.board = Board(self.board.master, difficulty, self.settings)
        self.knight = Knight(self.board)
        self.board.draw()
        self.knight.draw()