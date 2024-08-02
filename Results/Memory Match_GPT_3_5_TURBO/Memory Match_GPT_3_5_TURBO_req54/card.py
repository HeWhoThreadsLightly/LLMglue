'''
Card Class
'''
import tkinter as tk
class Card:
    def __init__(self, value):
        self.value = value
        self.row = None
        self.column = None
        self.button = None
        self.is_face_up = False
    def flip(self):
        self.is_face_up = not self.is_face_up
        if self.is_face_up:
            self.button.config(text=str(self.value))
        else:
            self.button.config(text="?")