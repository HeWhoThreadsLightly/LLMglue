# FocusBlocks User Manual

## Introduction

Welcome to FocusBlocks, a productivity tool designed to help you manage your time effectively using the Pomodoro technique with a twist. This application not only acts as a simple timer but also blocks distracting websites and applications during focus sessions. It includes features for task management, allowing you to allocate specific tasks to each focus session and track your progress over time.

In this user manual, you will find detailed instructions on how to install and use FocusBlocks to boost your productivity.

## Table of Contents

1. Installation
2. Getting Started
3. Pomodoro Timer
4. Task Management
5. Website and Application Blocker
6. Customization
7. Reporting and Analytics
8. Integration with Calendar Applications
9. Social Features
10. Accessibility Features

## 1. Installation

To install FocusBlocks, follow these steps:

1. Open your terminal or command prompt.
2. Navigate to the directory where you want to install FocusBlocks.
3. Run the following command:

```
pip install focusblocks
```

Note: If you prefer using conda, you can use the following command instead:

```
conda install focusblocks -c conda-forge
```

## 2. Getting Started

To start using FocusBlocks, import the necessary modules and create instances of the main classes:

```python
import pygame
from focusblocks import PomodoroTimer, TaskManager, Blocker

# Check if pygame is available for audio notifications
try:
    pygame.mixer.init()
    audio_player = pygame.mixer.music
except ModuleNotFoundError:
    audio_player = None
    print("Audio notification feature is not available. Please install the pygame library.")
except Exception as e:
    audio_player = None
    print(f"Failed to initialize audio player: {e}")

# Create an instance of the PomodoroTimer class
pomodoro_timer = PomodoroTimer(audio_player)

# Create an instance of the TaskManager class
task_manager = TaskManager()

# Create an instance of the Blocker class
blocker = Blocker()
```

## 3. Pomodoro Timer

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

By default, a focus session has a duration of 25 minutes. You can customize the duration using the `set_work_duration()` method of the `PomodoroTimer` class:

```python
pomodoro_timer.set_work_duration(30)  # Set the duration to 30 minutes
```

### Customizing Break Duration

By default, a short break has a duration of 5 minutes and a long break has a duration of 15 minutes. You can customize these durations using the `set_short_break_duration()` and `set_long_break_duration()` methods of the `PomodoroTimer` class:

```python
pomodoro_timer.set_short_break_duration(10)  # Set the short break duration to 10 minutes
pomodoro_timer.set_long_break_duration(20)  # Set the long break duration to 20 minutes
```

### Enabling/Disabling Audio Notifications

By default, audio notifications are enabled. You can disable them using the `disable_audio_notification()` method of the `PomodoroTimer` class:

```python
pomodoro_timer.disable_audio_notification()
```

To enable audio notifications again, use the `enable_audio_notification()` method:

```python
pomodoro_timer.enable_audio_notification()
```

### Setting Notification Sound

You can customize the notification sound by providing the path to an audio file using the `set_notification_sound()` method of the `PomodoroTimer` class:

```python
pomodoro_timer.set_notification_sound("notification.wav")
```

Note: Make sure the audio file is in a supported format (e.g., WAV).

## 4. Task Management

FocusBlocks allows you to manage your tasks and allocate them to each focus session.

### Adding a Task

To add a task, use the `add_task()` method of the `TaskManager` class:

```python
task_manager.add_task("Task 1", "This is the description of Task 1", 2)
```

The `add_task()` method takes three arguments: the title of the task, the description, and the estimated duration in Pomodoros.

### Removing a Task

To remove a task, use the `remove_task()` method of the `TaskManager` class:

```python
task_manager.remove_task("Task 1")
```

### Getting the List of Tasks

To get the list of tasks, use the `get_tasks()` method of the `TaskManager` class:

```python
tasks = task_manager.get_tasks()
for task in tasks:
    print(task["title"])
```

### Marking a Task as Complete

To mark a task as complete, use the `complete_task()` method of the `TaskManager` class:

```python
task_manager.complete_task("Task 1")
```

### Editing a Task

To edit a task, use the `edit_task()` method of the `TaskManager` class:

```python
task_manager.edit_task("Task 1", "New Title", "New Description", 3)
```

The `edit_task()` method takes four arguments: the current title of the task, the new title, the new description, and the new estimated duration in Pomodoros.

## 5. Website and Application Blocker

FocusBlocks can block access to distracting websites and applications during focus sessions.

### Adding a Website to the Block List

To add a website to the block list, use the `add_blocked_website()` method of the `Blocker` class:

```python
blocker.add_blocked_website("example.com")
```

### Removing a Website from the Block List

To remove a website from the block list, use the `remove_blocked_website()` method of the `Blocker` class:

```python
blocker.remove_blocked_website("example.com")
```

### Adding an Application to the Block List

To add an application to the block list, use the `add_blocked_application()` method of the `Blocker` class:

```python
blocker.add_blocked_application("example.exe")
```

### Removing an Application from the Block List

To remove an application from the block list, use the `remove_blocked_application()` method of the `Blocker` class:

```python
blocker.remove_blocked_application("example.exe")
```

### Blocking Websites and Applications

To block websites and applications, use the `block_websites_and_applications()` method of the `Blocker` class:

```python
blocker.block_websites_and_applications()
```

### Unblocking Websites and Applications

To unblock websites and applications, use the `unblock_websites_and_applications()` method of the `Blocker` class:

```python
blocker.unblock_websites_and_applications()
```

## 6. Customization

FocusBlocks provides various customization options to tailor the application to your preferences.

### Customizing Focus Periods and Breaks

You can set custom durations for focus periods and breaks using the `set_work_duration()` method of the `PomodoroTimer` class:

```python
pomodoro_timer.set_work_duration(30)  # Set the focus period duration to 30 minutes
```

### Customizing Blocked Websites and Applications

You can create a list of websites and applications to block during focus sessions using the `add_blocked_website()` and `add_blocked_application()` methods of the `Blocker` class:

```python
blocker.add_blocked_website("example.com")
blocker.add_blocked_application("example.exe")
```

### Customizing Notification Sounds and Themes

FocusBlocks allows you to customize the notification sounds and themes of the application. To set a custom notification sound, use the `set_notification_sound()` method of the `PomodoroTimer` class. To customize the theme, you can modify the source code or use a third-party library to apply custom styles.

## 7. Reporting and Analytics

FocusBlocks provides reporting and analytics features to help you track your productivity.

### Daily, Weekly, and Monthly Reports

You can generate daily, weekly, and monthly reports showing your productivity using the `generate_report()` method of the `TaskManager` class:

```python
task_manager.generate_report("daily")  # Generate a daily report
task_manager.generate_report("weekly")  # Generate a weekly report
task_manager.generate_report("monthly")  # Generate a monthly report
```

The `generate_report()` method takes one argument: the type of report to generate ("daily", "weekly", or "monthly").

### Visual Analytics

FocusBlocks provides visual analytics in the form of graphs or charts to make it easy to assess productivity trends. You can use third-party libraries such as Matplotlib or Plotly to visualize the data from the generated reports.

## 8. Integration with Calendar Applications

FocusBlocks can integrate with popular calendar applications for task scheduling. To enable this feature, you need to provide the necessary credentials and configure the integration with the specific calendar application. The exact steps for integration may vary depending on the calendar application you are using.

## 9. Social Features

FocusBlocks includes social features that allow you to set and share productivity challenges with friends or colleagues. You can create challenges, set goals, and track your progress together.

## 10. Accessibility Features

FocusBlocks is designed with accessibility in mind and includes several features to support users with different accessibility needs.

### Keyboard Navigation

FocusBlocks provides full functionality via keyboard shortcuts to ensure that users who cannot use a mouse can navigate efficiently through the application. You can use the following keyboard shortcuts:

- Start/Pause Focus Session: `Ctrl + S`
- Stop Focus Session: `Ctrl + X`
- Add Task: `Ctrl + A`
- Remove Task: `Ctrl + R`
- Complete Task: `Ctrl + C`
- Edit Task: `Ctrl + E`
- Add Blocked Website: `Ctrl + W`
- Remove Blocked Website: `Ctrl + Shift + W`
- Add Blocked Application: `Ctrl + B`
- Remove Blocked Application: `Ctrl + Shift + B`

### Tab Navigation

FocusBlocks implements tab navigation through all interactive elements in a logical order. You can use the `Tab` key to navigate between elements.

### Visual Indicators for Focused Element

FocusBlocks provides visual indicators for the currently focused element to assist users with visual impairments. The focused element is highlighted or outlined to make it more visible.

### Screen Reader Support

FocusBlocks supports screen readers by providing alt text for images, icons, and other non-textual elements. It also uses labels and roles for complex elements (like drag-and-drop interfaces or custom controls) to ensure their purpose and state are conveyed to screen reader users.

### High Contrast Mode

FocusBlocks supports high contrast themes that make text, icons, and other elements more distinguishable for users with low vision. It ensures that all text is readable and all interactive elements are visible against background colors.

### Text Size and Font Adjustments

FocusBlocks allows users to adjust the text size without breaking the layout or losing functionality. It also supports the use of user-defined system fonts, including those designed for dyslexia.

### Color Blind Mode

FocusBlocks implements color schemes that are accessible to users with various types of color blindness (e.g., deuteranopia, protanopia, tritanopia). It ensures that the application is usable and visually distinguishable for color blind users.

## Conclusion

Congratulations! You have completed the FocusBlocks user manual. With this powerful productivity tool, you can effectively manage your time, stay focused, and achieve your goals. Enjoy your productive journey with FocusBlocks!

```

Please note that the user manual provided above is a sample and may need to be customized based on the specific implementation of FocusBlocks.