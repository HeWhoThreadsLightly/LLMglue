import tkinter as tk
from tkinter import messagebox
class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.timer_label = tk.Label(self.root, text="25:00")
        self.start_button = tk.Button(self.root, text="Start", command=self.start_timer)
        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_timer)
        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_timer)
        self.is_running = False
    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.update_timer()
    def pause_timer(self):
        self.is_running = False
    def stop_timer(self):
        self.is_running = False
        self.timer_label.config(text="25:00")
    def update_timer(self):
        if self.is_running:
            time = self.timer_label.cget("text")
            minutes, seconds = map(int, time.split(":"))
            if minutes == 0 and seconds == 0:
                self.is_running = False
                self.timer_label.config(text="Time's up!")
                messagebox.showinfo("FocusBlocks", "Time's up!")
            elif seconds == 0:
                minutes -= 1
                seconds = 59
            else:
                seconds -= 1
            self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
            self.root.after(1000, self.update_timer)