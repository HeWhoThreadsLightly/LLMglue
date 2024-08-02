# FocusBlocks User Manual

## Introduction

FocusBlocks is a productivity tool designed to help users manage their time effectively using the Pomodoro technique with a twist. The application not only acts as a simple timer but also blocks distracting websites and applications during focus sessions. It includes features for task management, allowing users to allocate specific tasks to each focus session and track their progress over time.

## Installation

To use FocusBlocks, you need to have Python installed on your computer. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Once you have Python installed, you can install FocusBlocks by following these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where you want to install FocusBlocks.
3. Run the following command to install FocusBlocks:

   ```
   pip install focusblocks
   ```

   If you are using a virtual environment, make sure it is activated before running the command.

## Getting Started

To start using FocusBlocks, you can import the necessary modules and create instances of the main classes:

```python
from focusblocks import PomodoroTimer, TaskManager, Blocker

# Create an instance of the PomodoroTimer class
pomodoro_timer = PomodoroTimer()

# Create an instance of the TaskManager class
task_manager = TaskManager()

# Create an instance of the Blocker class
blocker = Blocker()
```

## Pomodoro Timer

The Pomodoro timer is the core feature of FocusBlocks. It allows you to start, pause, and stop focus sessions based on the Pomodoro technique.

### Starting a Focus Session

To start a focus session, use the `start()` method of the `PomodoroTimer` class:

```python
pomodoro_timer.start()
```

This will start a focus session with the default duration of 25 minutes.

### Pausing a Focus Session

To pause a focus session, use the `pause()` method of the `PomodoroTimer` class:

```python
pomodoro_timer.pause()
```

### Stopping a Focus Session

To stop a focus session, use the `stop()` method of the `PomodoroTimer` class:

```python
pomodoro_timer.stop()
```

### Customizing Focus Session Duration

By default, a focus session has a duration of 25 minutes. You can customize the duration by using the `set_work_duration()` method of the `PomodoroTimer` class:

```python
pomodoro_timer.set_work_duration(30)  # Set the duration to 30 minutes
```

### Customizing Break Duration

By default, a short break has a duration of 5 minutes and a long break has a duration of 15 minutes. You can customize these durations by using the `set_short_break_duration()` and `set_long_break_duration()` methods of the `PomodoroTimer` class:

```python
pomodoro_timer.set_short_break_duration(10)  # Set the short break duration to 10 minutes
pomodoro_timer.set_long_break_duration(20)  # Set the long break duration to 20 minutes
```

### Audio Notifications

FocusBlocks provides visual and audio notifications to alert users when a session starts or ends, and when it's time for a break. By default, audio notifications are enabled. You can disable them by using the `disable_audio_notification()` method of the `PomodoroTimer` class:

```python
pomodoro_timer.disable_audio_notification()
```

You can enable audio notifications again by using the `enable_audio_notification()` method:

```python
pomodoro_timer.enable_audio_notification()
```

You can also customize the notification sound by using the `set_notification_sound()` method:

```python
pomodoro_timer.set_notification_sound("notification.wav")
```

Make sure to provide the path to the audio file.

## Task Management

FocusBlocks allows you to create a list of tasks you plan to work on during each focus session.

### Adding a Task

To add a task, use the `add_task()` method of the `TaskManager` class:

```python
task_manager.add_task("Task 1", "Description of Task 1", 2)  # Add a task with a duration of 2 Pomodoros
```

The `add_task()` method takes three arguments: the title of the task, a brief description, and the estimated duration in Pomodoros.

### Removing a Task

To remove a task, use the `remove_task()` method of the `TaskManager` class:

```python
task_manager.remove_task("Task 1")  # Remove the task with the title "Task 1"
```

### Getting the List of Tasks

To get the list of tasks, use the `get_tasks()` method of the `TaskManager` class:

```python
tasks = task_manager.get_tasks()  # Get the list of tasks
for task in tasks:
    print(task["title"], task["description"], task["duration"], task["completed"])
```

### Marking a Task as Complete

To mark a task as complete, use the `complete_task()` method of the `TaskManager` class:

```python
task_manager.complete_task("Task 1")  # Mark the task with the title "Task 1" as complete
```

### Editing a Task

To edit the details of a task, use the `edit_task()` method of the `TaskManager` class:

```python
task_manager.edit_task("Task 1", "New Title", "New Description", 3)  # Edit the task with the title "Task 1"
```

The `edit_task()` method takes four arguments: the title of the task to be edited, the new title, the new description, and the new duration in Pomodoros.

## Website and Application Blocking

FocusBlocks allows you to block access to distracting websites and applications during focus sessions.

### Adding a Website to the Block List

To add a website to the block list, use the `add_blocked_website()` method of the `Blocker` class:

```python
blocker.add_blocked_website("example.com")  # Add "example.com" to the block list
```

### Removing a Website from the Block List

To remove a website from the block list, use the `remove_blocked_website()` method of the `Blocker` class:

```python
blocker.remove_blocked_website("example.com")  # Remove "example.com" from the block list
```

### Adding an Application to the Block List

To add an application to the block list, use the `add_blocked_application()` method of the `Blocker` class:

```python
blocker.add_blocked_application("example.exe")  # Add "example.exe" to the block list
```

### Removing an Application from the Block List

To remove an application from the block list, use the `remove_blocked_application()` method of the `Blocker` class:

```python
blocker.remove_blocked_application("example.exe")  # Remove "example.exe" from the block list
```

### Blocking Websites and Applications

To block websites and applications, use the `block_websites_and_applications()` method of the `Blocker` class:

```python
blocker.block_websites_and_applications()  # Block the websites and applications in the block list
```

### Unblocking Websites and Applications

To unblock websites and applications, use the `unblock_websites_and_applications()` method of the `Blocker` class:

```python
blocker.unblock_websites_and_applications()  # Unblock the websites and applications in the block list
```

## Conclusion

FocusBlocks is a powerful productivity tool that can help you manage your time effectively and stay focused on your tasks. With its Pomodoro timer, task management, and website/application blocking features, you can improve your productivity and achieve your goals. Start using FocusBlocks today and take control of your time!

```

This user manual provides a detailed guide on how to install and use FocusBlocks. It covers the main features of the software, including the Pomodoro timer, task management, and website/application blocking. Users can follow the instructions to get started with FocusBlocks and make the most of its productivity-enhancing features.