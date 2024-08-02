class Game:
    def __init__(self, board, knight):
        self.board = board
        self.knight = knight
    def move_knight(self, row, col):
        # Update the knight's position
        self.knight.current_row = row
        self.knight.current_col = col
        # Redraw the board
        self.board.draw()
        self.knight.draw()
    def start(self):
        difficulty = self.board.master.select_difficulty()
        self.board = Board(self.board.master, difficulty)
        self.knight = Knight(self.board)
        self.board.draw()
        self.knight.draw()