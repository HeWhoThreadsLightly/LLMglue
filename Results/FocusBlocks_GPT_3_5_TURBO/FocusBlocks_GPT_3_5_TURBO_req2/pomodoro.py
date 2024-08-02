'''
FocusBlocks - Pomodoro Technique with Website and Application Blocking
This file contains the Pomodoro timer functionality.
'''
import time
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
            self.remaining_time -= 1
            time.sleep(1)
            if self.remaining_time == 0:
                if self.focus_sessions < 3:
                    self.remaining_time = self.short_break_duration
                    self.focus_sessions += 1
                else:
                    self.remaining_time = self.long_break_duration
                    self.focus_sessions = 0
        self.is_running = False
    def pause(self):
        self.is_running = False
    def stop(self):
        self.is_running = False
        self.remaining_time = self.work_duration