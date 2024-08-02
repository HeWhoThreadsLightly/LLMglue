'''
FocusBlocks - Pomodoro Technique with Website and Application Blocking
This file contains the Pomodoro timer functionality.
'''
import time
import platform
if platform.system() == 'Windows':
    import winsound
class PomodoroTimer:
    def __init__(self):
        self.work_duration = 25 * 60  # 25 minutes in seconds
        self.short_break_duration = 5 * 60  # 5 minutes in seconds
        self.long_break_duration = 15 * 60  # 15 minutes in seconds
        self.remaining_time = self.work_duration
        self.is_running = False
        self.focus_sessions = 0
    def start(self):
        self.is_running = True
        while self.remaining_time > 0:
            if self.is_running:
                self.remaining_time -= 1
            time.sleep(1)
            if self.remaining_time == 0:
                if self.focus_sessions < 3:
                    self.remaining_time = self.short_break_duration
                    self.focus_sessions += 1
                    self.play_notification("Break time!")
                else:
                    self.remaining_time = self.long_break_duration
                    self.focus_sessions = 0
                    self.play_notification("Long break time!")
        self.is_running = False
    def pause(self):
        self.is_running = False
    def stop(self):
        self.is_running = False
        self.remaining_time = self.work_duration
    def set_work_duration(self, duration):
        self.work_duration = duration * 60
    def set_short_break_duration(self, duration):
        self.short_break_duration = duration * 60
    def set_long_break_duration(self, duration):
        self.long_break_duration = duration * 60
    def get_remaining_time(self):
        return self.remaining_time
    def play_notification(self, message):
        print(message)  # Replace with actual code to display visual notification
        if platform.system() == 'Windows':
            winsound.Beep(1000, 1000)  # Replace with actual code to play audio notification