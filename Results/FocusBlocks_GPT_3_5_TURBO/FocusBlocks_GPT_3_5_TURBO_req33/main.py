'''
FocusBlocks - Pomodoro Technique with Website and Application Blocking
This file contains the main functionality of the application.
'''
import pygame
from pomodoro import PomodoroTimer
from task_manager import TaskManager
from blocker import Blocker
# Check if pygame is available for audio notifications
try:
    pygame.mixer.init()
    audio_player = pygame.mixer
    audio_notification_available = True
except ModuleNotFoundError:
    audio_player = None
    audio_notification_available = False
    print("Audio notification feature is not available. Please install the pygame library.")
except Exception as e:
    audio_player = None
    audio_notification_available = False
    print(f"Failed to initialize audio player: {e}")
# Create an instance of the PomodoroTimer class
pomodoro_timer = PomodoroTimer(audio_player)
# Create an instance of the TaskManager class
task_manager = TaskManager()
# Create an instance of the Blocker class
blocker = Blocker()
# Function to start the Pomodoro timer
def start_pomodoro():
    # Check if any blocked websites or applications are present
    if blocker.is_website_blocked("example.com") or blocker.is_application_blocked("example.exe"):
        print("Blocked websites or applications detected. Timer cannot start.")
        return
    blocker.block_websites()
    blocker.block_applications()
    pomodoro_timer.start()
# Function to pause the Pomodoro timer
def pause_pomodoro():
    pomodoro_timer.pause()
# Function to stop the Pomodoro timer
def stop_pomodoro():
    pomodoro_timer.stop()
    blocker.unblock_websites()
    blocker.unblock_applications()
# Function to add a task
def add_task(title, description, duration):
    task = {
        "title": title,
        "description": description,
        "duration": duration,
        "completed": False
    }
    task_manager.add_task(task)
# Function to remove a task
def remove_task(title):
    task_manager.remove_task(title)
# Function to get the list of tasks
def get_tasks():
    return task_manager.get_tasks()
# Function to mark a task as complete
def complete_task(title):
    task_manager.complete_task(title)
# Function to edit a task
def edit_task(title, new_title, new_description, new_duration):
    task_manager.edit_task(title, new_title, new_description, new_duration)
# Function to add a website to the block list
def add_blocked_website(website):
    blocker.add_blocked_website(website)
# Function to remove a website from the block list
def remove_blocked_website(website):
    blocker.remove_blocked_website(website)
# Function to add an application to the block list
def add_blocked_application(application):
    blocker.add_blocked_application(application)
# Function to remove an application from the block list
def remove_blocked_application(application):
    blocker.remove_blocked_application(application)
# Function to block websites and applications
def block_websites_and_applications():
    blocker.block_websites()
    blocker.block_applications()
# Function to unblock websites and applications
def unblock_websites_and_applications():
    blocker.unblock_websites()
    blocker.unblock_applications()