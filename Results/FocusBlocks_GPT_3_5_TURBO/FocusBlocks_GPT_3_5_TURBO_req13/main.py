'''
FocusBlocks - Pomodoro Technique with Website and Application Blocking
This file contains the main functionality of the application.
'''
from pomodoro import PomodoroTimer
from task_manager import TaskManager
from blocker import Blocker
import pygame
import platform
import subprocess
# Create an instance of the PomodoroTimer class
pomodoro_timer = PomodoroTimer()
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
    pomodoro_timer.start()
# Function to pause the Pomodoro timer
def pause_pomodoro():
    pomodoro_timer.pause()
# Function to stop the Pomodoro timer
def stop_pomodoro():
    pomodoro_timer.stop()
# Function to add a task
def add_task(task):
    task_manager.add_task(task)
# Function to remove a task
def remove_task(task):
    task_manager.remove_task(task)
# Function to get the list of tasks
def get_tasks():
    return task_manager.get_tasks()
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