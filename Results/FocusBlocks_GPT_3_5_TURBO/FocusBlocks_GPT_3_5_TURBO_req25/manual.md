# FocusBlocks User Manual

## Introduction

FocusBlocks is a productivity tool designed to help users manage their time effectively using the Pomodoro technique with a twist. The application acts as a timer and also blocks distracting websites and applications during focus sessions. It includes features for task management, allowing users to allocate specific tasks to each focus session and track their progress over time.

## Installation

To use FocusBlocks, you need to have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

Once Python is installed, you can install FocusBlocks by running the following command in your terminal or command prompt:

```
pip install focusblocks
```

## Getting Started

To start using FocusBlocks, you can import the necessary modules and create instances of the main classes:

```python
from focusblocks import PomodoroTimer, TaskManager, Blocker

pomodoro_timer = PomodoroTimer()
task_manager = TaskManager()
blocker = Blocker()
```

## Pomodoro Timer

The Pomodoro timer is the core feature of FocusBlocks. It allows you to start, pause, and stop focus sessions based on the Pomodoro technique.

### Starting a Focus Session

To start a focus session, use the `start()` method of the `PomodoroTimer` class:

```python
pomodoro_timer.start()
```

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

### Customizing Focus and Break Durations

By default, the focus duration is set to 25 minutes and the short break duration is set to 5 minutes. You can customize these durations using the following methods:

```python
pomodoro_timer.set_work_duration(30)  # Set focus duration to 30 minutes
pomodoro_timer.set_short_break_duration(10)  # Set short break duration to 10 minutes
```

### Audio Notifications

FocusBlocks provides visual and audio notifications to alert users when a session starts or ends, and when it's time for a break. By default, audio notifications are enabled. You can disable them using the following method:

```python
pomodoro_timer.disable_audio_notification()
```

### Task Management

FocusBlocks allows you to create and manage tasks for each focus session.

#### Adding a Task

To add a task, use the `add_task()` method of the `TaskManager` class:

```python
task_manager.add_task("Task 1", "Description of Task 1", 2)  # Add a task with title, description, and duration of 2 Pomodoros
```

#### Removing a Task

To remove a task, use the `remove_task()` method of the `TaskManager` class:

```python
task_manager.remove_task("Task 1")  # Remove the task with the specified title
```

#### Getting the List of Tasks

To get the list of tasks, use the `get_tasks()` method of the `TaskManager` class:

```python
tasks = task_manager.get_tasks()  # Get the list of tasks
for task in tasks:
    print(task["title"], task["description"], task["duration"], task["completed"])  # Print task details
```

#### Completing a Task

To mark a task as complete, use the `complete_task()` method of the `TaskManager` class:

```python
task_manager.complete_task("Task 1")  # Mark the task with the specified title as complete
```

#### Editing a Task

To edit a task, use the `edit_task()` method of the `TaskManager` class:

```python
task_manager.edit_task("Task 1", "New Title", "New Description", 3)  # Edit the task with the specified title and update its details
```

## Distracting Website and Application Blocker

FocusBlocks allows you to block access to distracting websites and applications during focus sessions.

### Adding a Website to the Block List

To add a website to the block list, use the `add_blocked_website()` method of the `Blocker` class:

```python
blocker.add_blocked_website("example.com")  # Add a website to the block list
```

### Removing a Website from the Block List

To remove a website from the block list, use the `remove_blocked_website()` method of the `Blocker` class:

```python
blocker.remove_blocked_website("example.com")  # Remove a website from the block list
```

### Adding an Application to the Block List

To add an application to the block list, use the `add_blocked_application()` method of the `Blocker` class:

```python
blocker.add_blocked_application("example.exe")  # Add an application to the block list
```

### Removing an Application from the Block List

To remove an application from the block list, use the `remove_blocked_application()` method of the `Blocker` class:

```python
blocker.remove_blocked_application("example.exe")  # Remove an application from the block list
```

### Blocking Websites and Applications

To block websites and applications, use the `block_websites_and_applications()` method of the `Blocker` class:

```python
blocker.block_websites_and_applications()  # Block websites and applications in the block list
```

### Unblocking Websites and Applications

To unblock websites and applications, use the `unblock_websites_and_applications()` method of the `Blocker` class:

```python
blocker.unblock_websites_and_applications()  # Unblock websites and applications in the block list
```

## Customization

FocusBlocks provides customization options for focus periods, breaks, notification sounds, and themes.

### Customizing Focus and Break Durations

In addition to the default durations, you can set custom durations for focus periods and breaks using the following methods:

```python
pomodoro_timer.set_work_duration(30)  # Set focus duration to 30 minutes
pomodoro_timer.set_short_break_duration(10)  # Set short break duration to 10 minutes
```

### Customizing Notification Sounds

You can customize the notification sound by providing the path to a sound file using the `set_notification_sound()` method of the `PomodoroTimer` class:

```python
pomodoro_timer.set_notification_sound("path/to/notification.wav")  # Set the notification sound to a custom sound file
```

### Customizing Themes

FocusBlocks currently does not provide built-in theme customization options. However, you can modify the source code or UI elements to customize the appearance of the application according to your preferences.

## Reporting and Analytics

FocusBlocks provides reporting and analytics features to track your productivity.

### Daily, Weekly, and Monthly Reports

You can generate daily, weekly, and monthly reports showing your productivity using the `generate_report()` method of the `TaskManager` class:

```python
task_manager.generate_report("daily")  # Generate a daily report
task_manager.generate_report("weekly")  # Generate a weekly report
task_manager.generate_report("monthly")  # Generate a monthly report
```

### Visual Analytics

FocusBlocks currently does not provide built-in visual analytics features. However, you can export the generated reports to external tools or libraries to create graphs or charts for productivity trend analysis.

## Technical Requirements

FocusBlocks uses local storage or an embedded database to store user data and preferences. No additional setup or configuration is required.

## Additional Features

### Integration with Calendar Applications

FocusBlocks currently does not provide integration with popular calendar applications for task scheduling. However, you can manually synchronize your tasks and schedule with your preferred calendar application.

### Social Features

FocusBlocks currently does not provide social features to set and share productivity challenges with friends or colleagues. However, you can use external communication platforms or tools to collaborate and share productivity challenges.

## Accessibility Requirements

FocusBlocks aims to provide accessibility features to ensure a smooth user experience for all users.

### Keyboard Navigation

FocusBlocks supports full functionality via keyboard shortcuts to ensure efficient navigation for users who cannot use a mouse. The following keyboard shortcuts are available:

- Start focus session: `Ctrl + S`
- Pause focus session: `Ctrl + P`
- Stop focus session: `Ctrl + X`
- Add task: `Ctrl + A`
- Remove task: `Ctrl + R`
- Complete task: `Ctrl + C`
- Edit task: `Ctrl + E`
- Add blocked website: `Ctrl + W`
- Remove blocked website: `Ctrl + Shift + W`
- Add blocked application: `Ctrl + B`
- Remove blocked application: `Ctrl + Shift + B`

### Tab Navigation

FocusBlocks implements tab navigation through all interactive elements in a logical order. Pressing the `Tab` key will navigate through the elements, and pressing `Enter` or `Space` will activate the selected element.

### Visual Indicators

FocusBlocks provides visual indicators for the currently focused element to assist users in navigating the application. The focused element is highlighted or outlined to provide a clear indication of the current focus.

### Screen Reader Support

FocusBlocks makes use of alt text to describe images, icons, and other non-textual elements. It also uses labels and roles for complex elements (like drag-and-drop interfaces or custom controls) to ensure their purpose and state are conveyed to screen reader users.

## Conclusion

FocusBlocks is a powerful productivity tool that combines the Pomodoro technique with website and application blocking, task management, and reporting features. By effectively managing your time and eliminating distractions, you can improve your productivity and achieve your goals. Start using FocusBlocks today and take control of your focus and productivity!