'''
Game window for the Memory Match game.
'''
import tkinter as tk
from tkinter import messagebox
from select_difficulty_window import SelectDifficultyWindow
import random
class Card:
    def __init__(self, card_id):
        self.card_id = card_id
        self.is_face_up = False
    def flip(self):
        self.is_face_up = not self.is_face_up
class GameWindow(tk.Toplevel):
    def __init__(self, master, difficulty):
        super().__init__(master)
        self.title("Memory Match Game")
        self.protocol("WM_DELETE_WINDOW", self.return_to_main_menu)
        self.difficulty = difficulty
        self.cards = self.generate_cards()
        self.create_widgets()
    def generate_cards(self):
        # Determine the number of cards based on the selected difficulty level
        if self.difficulty == "Easy":
            num_cards = 8
        elif self.difficulty == "Medium":
            num_cards = 12
        elif self.difficulty == "Hard":
            num_cards = 16
        # Generate the cards and their matching pairs
        cards = []
        for i in range(num_cards):
            card_id = i + 1
            card1 = Card(card_id)
            card2 = Card(card_id)
            cards.extend([card1, card2])
        # Shuffle the cards
        random.shuffle(cards)
        return cards
    def create_widgets(self):
        # Create the game grid and score panel
        self.game_frame = tk.Frame(self)
        self.game_frame.pack(padx=10, pady=10)
        self.score_panel = tk.Frame(self)
        self.score_panel.pack(padx=10, pady=10)
        self.create_game_grid()
        self.create_score_panel()
    def create_game_grid(self):
        # Create the game grid based on the selected difficulty
        num_rows, num_cols = self.get_grid_size()
        for row in range(num_rows):
            for col in range(num_cols):
                card_index = row * num_cols + col
                card = self.cards[card_index]
                card_button = tk.Button(self.game_frame, text="?", width=5, height=3, command=lambda card=card: self.flip_card(card))
                card_button.grid(row=row, column=col, padx=5, pady=5)
    def create_score_panel(self):
        # Create the score panel
        self.attempts_label = tk.Label(self.score_panel, text="Attempts: 0")
        self.attempts_label.pack(side=tk.LEFT)
        self.matches_label = tk.Label(self.score_panel, text="Matches: 0")
        self.matches_label.pack(side=tk.LEFT)
        self.timer_label = tk.Label(self.score_panel, text="Time: 00:00")
        self.timer_label.pack(side=tk.LEFT)
    def get_grid_size(self):
        # Get the grid size based on the selected difficulty
        if self.difficulty == "Easy":
            return 4, 4
        elif self.difficulty == "Medium":
            return 6, 6
        elif self.difficulty == "Hard":
            return 8, 8
    def flip_card(self, card):
        # Flip the card and check for matches
        card.flip()
        # TODO: Implement logic to check for matches
    def return_to_main_menu(self):
        if messagebox.askyesno("Quit", "Are you sure you want to quit the game?"):
            self.master.deiconify()
            self.destroy()
class HighScoresWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("High Scores")
        # Display high scores from previous games
        pass
    def return_to_main_menu(self):
        self.master.deiconify()
        self.destroy()
class SettingsWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Settings")
        # Settings options for sound, theme, and instructions
        pass
    def return_to_main_menu(self):
        self.master.deiconify()
        self.destroy()