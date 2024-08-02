# FocusBlocks User Manual

## Introduction

FocusBlocks is a productivity tool designed to help users manage their time effectively using the Pomodoro technique with a twist. The application acts as a timer and also blocks distracting websites and applications during focus sessions. It includes features for task management, allowing users to allocate specific tasks to each focus session and track their progress over time.

## Installation

To use FocusBlocks, you need to have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

Once Python is installed, you can install the required dependencies by running the following command in your terminal or command prompt:

```
pip install -r requirements.txt
```

## Getting Started

To start using FocusBlocks, you can run the `main.py` file in your Python environment. This will launch the application and provide you with a command-line interface to interact with the different features.

## Features

### Pomodoro Timer

The Pomodoro timer is the core feature of FocusBlocks. It allows you to start, pause, and stop focus sessions based on the Pomodoro technique.

To start a focus session, use the `start_pomodoro()` command. This will start a 25-minute focus session by default.

To pause a focus session, use the `pause_pomodoro()` command.

To stop a focus session, use the `stop_pomodoro()` command.

You can customize the duration of focus sessions and break intervals by using the following commands:

- `set_work_duration(duration)`: Set the duration of focus sessions in minutes.
- `set_short_break_duration(duration)`: Set the duration of short breaks in minutes.
- `set_long_break_duration(duration)`: Set the duration of long breaks in minutes.

### Distracting Website and Application Blocker

The distracting website and application blocker feature allows you to block access to a user-customizable list of websites and applications during focus sessions.

To add a website to the block list, use the `add_blocked_website(website)` command.

To remove a website from the block list, use the `remove_blocked_website(website)` command.

To add an application to the block list, use the `add_blocked_application(application)` command.

To remove an application from the block list, use the `remove_blocked_application(application)` command.

You can block websites and applications by using the `block_websites_and_applications()` command. To unblock them, use the `unblock_websites_and_applications()` command.

### Task Management

The task management feature allows you to create a list of tasks you plan to work on during each focus session.

To add a task, use the `add_task(title, description, duration)` command. The duration should be specified in the number of Pomodoros.

To remove a task, use the `remove_task(title)` command.

To get the list of tasks, use the `get_tasks()` command.

To mark a task as complete, use the `complete_task(title)` command.

To edit a task, use the `edit_task(title, new_title, new_description, new_duration)` command.

### Integration with Focus Session

The integration with focus session feature allows you to integrate task selection and time tracking with the Pomodoro timer.

Before starting a focus session, you will be prompted to select a task or tasks you intend to work on during that session.

The application will track the time spent on each task and automatically suggest breaks based on the Pomodoro schedule.

Optionally, you can skip or end the focus session early. In this case, the app will ask if the task was completed or needs to be rescheduled.

### Customization

FocusBlocks provides customization options for focus periods, breaks, notification sounds, and themes.

To set custom durations for focus periods and breaks, use the `set_work_duration(duration)`, `set_short_break_duration(duration)`, and `set_long_break_duration(duration)` commands.

To customize notification sounds, you can replace the `notification.wav` file in the project directory with your own sound file.

To customize the theme of the application, you can modify the code in the `main.py` file.

### Reporting and Analytics

FocusBlocks provides daily, weekly, and monthly reports showing your productivity. These reports include the number of focus sessions completed, tasks completed, and time spent in focus.

Visual analytics in the form of graphs or charts are also available to make it easy to assess productivity trends.

### Technical Requirements

FocusBlocks uses local storage or an embedded database to store user data and preferences. No external database setup is required.

### Additional Features

FocusBlocks offers additional features such as integration with popular calendar applications for task scheduling and a social feature to allow users to set and share productivity challenges with friends or colleagues.

### Accessibility Requirements

FocusBlocks supports keyboard navigation to ensure that users who cannot use a mouse can navigate efficiently through the application. Full functionality is accessible via keyboard shortcuts.

## Conclusion

FocusBlocks is a powerful productivity tool that combines the Pomodoro technique with website and application blocking and task management features. By using FocusBlocks, you can effectively manage your time, stay focused, and improve your productivity.