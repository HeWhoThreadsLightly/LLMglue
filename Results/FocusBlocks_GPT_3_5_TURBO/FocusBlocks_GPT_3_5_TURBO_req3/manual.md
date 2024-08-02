# FocusBlocks User Manual

## Introduction

Welcome to FocusBlocks, a productivity tool designed to help you manage your time effectively using the Pomodoro technique with a twist. This application not only acts as a simple timer but also blocks distracting websites and applications during focus sessions. It includes features for task management, allowing you to allocate specific tasks to each focus session and track your progress over time.

## Installation

To use FocusBlocks, you need to have Python installed on your computer. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Once Python is installed, you can install the required dependencies by running the following command in your terminal or command prompt:

```
pip install -r requirements.txt
```

## Getting Started

To start using FocusBlocks, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where you have the FocusBlocks files.
3. Run the following command to start the application:

```
python main.py
```

## Main Functions

### Start a Focus Session

To start a focus session, click on the "Start" button or use the keyboard shortcut "Ctrl + S". The default duration for a focus session is 25 minutes.

### Pause a Focus Session

To pause a focus session, click on the "Pause" button or use the keyboard shortcut "Ctrl + P". This will temporarily stop the timer.

### Stop a Focus Session

To stop a focus session, click on the "Stop" button or use the keyboard shortcut "Ctrl + X". This will reset the timer to its initial state.

### Customize Session Duration

You can customize the duration of focus sessions and break intervals. By default, a focus session is set to 25 minutes, and a short break is set to 5 minutes. To change these durations, follow these steps:

1. Open the `pomodoro.py` file in a text editor.
2. Locate the following lines of code:

```python
self.work_duration = 25 * 60  # 25 minutes in seconds
self.short_break_duration = 5 * 60  # 5 minutes in seconds
```

3. Modify the values to your desired durations. For example, to set a focus session to 30 minutes and a short break to 10 minutes, change the code to:

```python
self.work_duration = 30 * 60  # 30 minutes in seconds
self.short_break_duration = 10 * 60  # 10 minutes in seconds
```

4. Save the file.

### Visual and Audio Notifications

FocusBlocks provides visual and audio notifications to alert you when a session starts or ends, and when it's time for a break. By default, the application prints the notification message to the terminal and plays a beep sound on Windows. To customize the notifications, you can modify the `play_notification` method in the `pomodoro.py` file.

## Task Management

FocusBlocks includes task management features that allow you to allocate specific tasks to each focus session and track your progress over time. To use the task management functionality, follow these steps:

1. Open the `task_manager.py` file in a text editor.
2. Use the `add_task` method to add tasks to the task manager. For example:

```python
task_manager.add_task("Complete project proposal")
task_manager.add_task("Review documentation")
```

3. Use the `get_tasks` method to retrieve the list of tasks. For example:

```python
tasks = task_manager.get_tasks()
for task in tasks:
    print(task)
```

4. Save the file.

## Conclusion

Congratulations! You are now ready to use FocusBlocks to manage your time effectively using the Pomodoro technique. Enjoy your focused and productive work sessions!