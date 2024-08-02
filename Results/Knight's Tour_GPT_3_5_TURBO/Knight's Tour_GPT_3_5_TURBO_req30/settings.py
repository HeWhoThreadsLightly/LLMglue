'''
Settings class that represents the game settings.
'''
import tkinter.simpledialog as sd
from tkinter import messagebox
class Settings:
    def __init__(self, master):
        self.master = master
        self.sound_volume = 50
        self.visual_theme = "Default"
        self.knight_appearance = "Default"
        self.chessboard_appearance = "Default"
        self.visited_square_appearance = "LightGray"
    def adjust_sound_volume(self, volume):
        self.sound_volume = volume
    def change_visual_theme(self, theme):
        self.visual_theme = theme
    def modify_knight_appearance(self, appearance):
        self.knight_appearance = appearance
    def modify_chessboard_appearance(self, appearance):
        self.chessboard_appearance = appearance
    def show_settings(self):
        messagebox.showinfo("Settings",
                            f"Sound Volume: {self.sound_volume}\nVisual Theme: {self.visual_theme}\nKnight Appearance: {self.knight_appearance}\nChessboard Appearance: {self.chessboard_appearance}")
    def customize_settings(self):
        options = ["Adjust Sound Volume", "Change Visual Theme", "Modify Knight Appearance", "Modify Chessboard Appearance"]
        choice = sd.askoption("Customize Settings", "Select an option", options=options, parent=self.master)
        if choice == "Adjust Sound Volume":
            volume = sd.askinteger("Adjust Sound Volume", "Enter sound volume (0-100)", minvalue=0, maxvalue=100, initialvalue=self.sound_volume, parent=self.master)
            self.adjust_sound_volume(volume)
        elif choice == "Change Visual Theme":
            theme = sd.askstring("Change Visual Theme", "Enter visual theme", initialvalue=self.visual_theme, parent=self.master)
            self.change_visual_theme(theme)
        elif choice == "Modify Knight Appearance":
            appearance = sd.askstring("Modify Knight Appearance", "Enter knight appearance", initialvalue=self.knight_appearance, parent=self.master)
            self.modify_knight_appearance(appearance)
        elif choice == "Modify Chessboard Appearance":
            appearance = sd.askstring("Modify Chessboard Appearance", "Enter chessboard appearance", initialvalue=self.chessboard_appearance, parent=self.master)
            self.modify_chessboard_appearance(appearance)