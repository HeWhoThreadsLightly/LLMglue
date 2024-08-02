'''
FocusBlocks - Pomodoro Technique with Website and Application Blocking
This file contains the main functionality of the application.
'''
from pomodoro import PomodoroTimer
from task_manager import TaskManager
# Create an instance of the PomodoroTimer class
pomodoro_timer = PomodoroTimer()
# Create an instance of the TaskManager class
task_manager = TaskManager()
# Function to start the Pomodoro timer
def start_pomodoro():
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