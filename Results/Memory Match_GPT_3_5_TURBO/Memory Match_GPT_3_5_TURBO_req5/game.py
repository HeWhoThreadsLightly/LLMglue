'''
Game Class
'''
import tkinter as tk
import random
from card import Card
class Game:
    def __init__(self):
        self.grid_size = 4
        self.cards = []
        self.create_cards()
        self.create_grid()
    def create_cards(self):
        # Generate a list of card values
        card_values = list(range(1, self.grid_size**2 // 2 + 1))
        card_values *= 2
        random.shuffle(card_values)
        # Create Card objects with matching pairs
        for value in card_values:
            card1 = Card(value)
            card2 = Card(value)
            self.cards.append(card1)
            self.cards.append(card2)
    def create_grid(self):
        # Create a grid of buttons representing the cards
        self.grid = []
        for row in range(self.grid_size):
            row_buttons = []
            for column in range(self.grid_size):
                index = row * self.grid_size + column
                card = self.cards[index]
                card.row = row
                card.column = column
                button = tk.Button(text="?", command=lambda c=card: self.flip_card(c))
                button.grid(row=row, column=column)
                card.button = button
                row_buttons.append(button)
            self.grid.append(row_buttons)
    def flip_card(self, card):
        # Check if the card is already face up
        if card.is_face_up:
            return
        # Flip the selected card
        card.flip()
        # Check for matching pairs
        face_up_cards = [c for c in self.cards if c.is_face_up]
        if len(face_up_cards) == 2:
            if face_up_cards[0].value == face_up_cards[1].value:
                self.remove_cards(face_up_cards)
            else:
                self.flip_face_down(face_up_cards)
    def remove_cards(self, cards):
        # Remove matching pairs from the grid and the list of cards
        for card in cards:
            card.button.grid_forget()
            self.cards.remove(card)
    def flip_face_down(self, cards):
        # Flip face-up cards face down after a short delay
        self.root.after(1000, self.flip_cards_face_down, cards)
    def flip_cards_face_down(self, cards):
        # Flip the specified cards face down
        for card in cards:
            card.flip()
    def start(self):
        # Start the game by displaying the grid of cards
        self.root = tk.Tk()
        self.root.title("Memory Match Game")
        self.create_grid()
        self.root.mainloop()