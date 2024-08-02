class Game:
    def __init__(self, board, knight):
        self.board = board
        self.knight = knight
    def move_knight(self, row, col):
        # Check if the move is valid
        if self.board.is_valid_move(row, col):
            # Update the knight's position
            self.knight.move_knight(row, col)
            # Redraw the board
            self.board.draw()
        else:
            # Display an error message for invalid move
            messagebox.showerror("Invalid Move", "Invalid move! Please select a valid move.")
    def start(self):
        difficulty = self.board.select_difficulty()
        self.board = Board(self.board.master, difficulty)
        self.knight = Knight(self.board)
        self.board.draw()
        self.knight.draw()