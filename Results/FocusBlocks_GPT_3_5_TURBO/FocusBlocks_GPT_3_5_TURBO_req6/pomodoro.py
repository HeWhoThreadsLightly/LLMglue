'''
FocusBlocks - Pomodoro Technique with Website and Application Blocking
This file contains the Pomodoro timer functionality.
'''
import time
import platform
import threading
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
        self.timer = None
    def start(self):
        if self.is_running:
            return
        self.is_running = True
        self.timer = threading.Timer(self.remaining_time, self._session_end_callback)
        self.timer.start()
        self.play_notification("Session started!")
    def pause(self):
        if not self.is_running:
            return
        self.is_running = False
        self.timer.cancel()
        self.play_notification("Session paused!")
    def stop(self):
        if not self.is_running:
            return
        self.is_running = False
        self.timer.cancel()
        self.remaining_time = self.work_duration
        self.play_notification("Session stopped!")
    def set_work_duration(self, duration):
        self.work_duration = duration * 60
    def set_short_break_duration(self, duration):
        self.short_break_duration = duration * 60
    def set_long_break_duration(self, duration):
        self.long_break_duration = duration * 60
    def get_remaining_time(self):
        return self.remaining_time
    def _session_end_callback(self):
        if self.focus_sessions < 3:
            self.remaining_time = self.short_break_duration
            self.focus_sessions += 1
            self.play_notification("Break time!")
        else:
            self.remaining_time = self.long_break_duration
            self.focus_sessions = 0
            self.play_notification("Long break time!")
        self.start()
    def play_notification(self, message):
        # Replace with actual code to display visual notification
        print(message)
        # Replace with actual code to play audio notification
        if platform.system() == 'Windows':
            winsound.Beep(1000, 1000)