'''
FocusBlocks - Pomodoro Technique with Website and Application Blocking
This file contains the Pomodoro timer functionality.
'''
import time
import threading
import pygame
class PomodoroTimer:
    def __init__(self, audio_notification_sound="notification.wav"):
        self.work_duration = 25 * 60  # 25 minutes in seconds
        self.short_break_duration = 5 * 60  # 5 minutes in seconds
        self.long_break_duration = 15 * 60  # 15 minutes in seconds
        self.remaining_time = self.work_duration
        self.is_running = False
        self.focus_sessions = 0
        self.timer = None
        self.audio_notification_enabled = True
        self.audio_notification_sound = audio_notification_sound
        self.audio_player = None
        self.init_audio_player()
    def init_audio_player(self):
        try:
            pygame.mixer.init()
            self.audio_player = pygame.mixer.music
        except ModuleNotFoundError:
            self.audio_player = None
            print("Audio notification feature is not available. Please install the pygame library.")
    def enable_audio_notification(self):
        self.audio_notification_enabled = True
    def disable_audio_notification(self):
        self.audio_notification_enabled = False
    def set_notification_sound(self, sound_file):
        self.audio_notification_sound = sound_file
    def start(self):
        if self.is_running:
            return
        self.is_running = True
        self.timer = threading.Timer(1, self._update_remaining_time)
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
    def _update_remaining_time(self):
        self.remaining_time -= 1
        if self.remaining_time <= 0:
            self._session_end_callback()
        else:
            self.timer = threading.Timer(1, self._update_remaining_time)
            self.timer.start()
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
        print(message)
        if self.audio_notification_enabled and self.audio_player:
            try:
                self.audio_player.load(self.audio_notification_sound)
                self.audio_player.play()
            except Exception as e:
                print(f"Failed to play audio notification: {e}")