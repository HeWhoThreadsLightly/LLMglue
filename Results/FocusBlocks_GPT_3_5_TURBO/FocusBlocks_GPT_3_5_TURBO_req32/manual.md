# FocusBlocks User Manual

## Introduction

FocusBlocks is a productivity tool designed to help users manage their time effectively using the Pomodoro technique with a twist. The application acts as a timer and also blocks distracting websites and applications during focus sessions. It includes features for task management, allowing users to allocate specific tasks to each focus session and track their progress over time.

## Installation

To use FocusBlocks, you need to have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

Once Python is installed, you can install FocusBlocks using pip, the Python package installer. Open a terminal or command prompt and run the following command:

```
pip install focusblocks
```

FocusBlocks also requires the pygame library for audio notifications. You can install it using pip:

```
pip install pygame
```

## Getting Started

To start using FocusBlocks, you can import the necessary classes from the `focusblocks` package:

```python
from focusblocks import PomodoroTimer, TaskManager, Blocker
```

## Pomodoro Timer

The Pomodoro timer is the core feature of FocusBlocks. It allows you to start, pause, and stop focus sessions based on the Pomodoro technique.

### Creating a Pomodoro Timer

To create a Pomodoro timer, you can instantiate the `PomodoroTimer` class:

```python
pomodoro_timer = PomodoroTimer()
```

### Starting a Focus Session

To start a focus session, use the `start()` method:

```python
pomodoro_timer.start()
```

### Pausing a Focus Session

To pause a focus session, use the `pause()` method:

```python
pomodoro_timer.pause()
```

### Stopping a Focus Session

To stop a focus session, use the `stop()` method:

```python
pomodoro_timer.stop()
```

### Customizing Focus and Break Durations

By default, the focus duration is set to 25 minutes and the short break duration is set to 5 minutes. You can customize these durations using the `set_work_duration()` and `set_short_break_duration()` methods:

```python
pomodoro_timer.set_work_duration(30)  # Set focus duration to 30 minutes
pomodoro_timer.set_short_break_duration(10)  # Set short break duration to 10 minutes
```

### Enabling/Disabling Audio Notifications

By default, audio notifications are enabled. You can disable them using the `disable_audio_notification()` method:

```python
pomodoro_timer.disable_audio_notification()
```

### Setting a Custom Notification Sound

You can set a custom notification sound by providing the path to an audio file:

```python
pomodoro_timer.set_notification_sound("path/to/notification.wav")
```

## Task Management

FocusBlocks allows you to create and manage tasks for each focus session.

### Creating a Task

To create a task, you can use the `TaskManager` class:

```python
task_manager = TaskManager()
task_manager.add_task("Task 1", "Description 1", 2)  # Add a task with title, description, and duration in Pomodoros
```

### Removing a Task

To remove a task, use the `remove_task()` method:

```python
task_manager.remove_task("Task 1")  # Remove a task by title
```

### Getting the List of Tasks

To get the list of tasks, use the `get_tasks()` method:

```python
tasks = task_manager.get_tasks()  # Get the list of tasks
for task in tasks:
    print(task["title"], task["description"], task["duration"], task["completed"])
```

### Marking a Task as Complete

To mark a task as complete, use the `complete_task()` method:

```python
task_manager.complete_task("Task 1")  # Mark a task as complete by title
```

### Editing a Task

To edit a task, use the `edit_task()` method:

```python
task_manager.edit_task("Task 1", "New Title", "New Description", 3)  # Edit a task by title
```

## Website and Application Blocking

FocusBlocks can block distracting websites and applications during focus sessions.

### Creating a Blocker

To create a blocker, you can instantiate the `Blocker` class:

```python
blocker = Blocker()
```

### Adding a Website to the Block List

To add a website to the block list, use the `add_blocked_website()` method:

```python
blocker.add_blocked_website("example.com")
```

### Removing a Website from the Block List

To remove a website from the block list, use the `remove_blocked_website()` method:

```python
blocker.remove_blocked_website("example.com")
```

### Adding an Application to the Block List

To add an application to the block list, use the `add_blocked_application()` method:

```python
blocker.add_blocked_application("example.exe")
```

### Removing an Application from the Block List

To remove an application from the block list, use the `remove_blocked_application()` method:

```python
blocker.remove_blocked_application("example.exe")
```

### Blocking Websites and Applications

To block websites and applications, use the `block_websites_and_applications()` method:

```python
blocker.block_websites_and_applications()
```

### Unblocking Websites and Applications

To unblock websites and applications, use the `unblock_websites_and_applications()` method:

```python
blocker.unblock_websites_and_applications()
```

## Conclusion

FocusBlocks is a powerful productivity tool that helps you manage your time effectively using the Pomodoro technique. With its task management and website/application blocking features, you can stay focused and improve your productivity. Start using FocusBlocks today and take control of your time!

```

This user manual provides a detailed guide on how to install and use FocusBlocks, including instructions on using the Pomodoro timer, managing tasks, and blocking distracting websites and applications. It also includes information on customizing settings and audio notifications.