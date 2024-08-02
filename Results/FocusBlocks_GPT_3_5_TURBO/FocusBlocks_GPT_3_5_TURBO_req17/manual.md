# FocusBlocks User Manual

## Introduction

FocusBlocks is a productivity tool designed to help users manage their time effectively using the Pomodoro technique with a twist. The application acts as a timer and also blocks distracting websites and applications during focus sessions. It includes features for task management, allowing users to allocate specific tasks to each focus session and track their progress over time.

## Installation

To use FocusBlocks, you need to have Python installed on your computer. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Once you have Python installed, you can install the required dependencies by running the following command in your terminal or command prompt:

```
pip install -r requirements.txt
```

## Getting Started

To start using FocusBlocks, you can run the `main.py` file in your Python environment. This will launch the application and provide you with a command-line interface to interact with the different features.

## Core Features

### Pomodoro Timer

The Pomodoro timer allows you to start, pause, and stop a focus session based on the Pomodoro technique. By default, each focus session is 25 minutes long, followed by a 5-minute short break. After every four focus sessions, there is a 15-minute long break.

To start a focus session, use the command `start_pomodoro`.

To pause a focus session, use the command `pause_pomodoro`.

To stop a focus session, use the command `stop_pomodoro`.

### Distracting Website and Application Blocker

The distracting website and application blocker prevents access to a user-customizable list of websites and applications that are deemed distracting. You can add or remove websites and applications from the block list.

To add a website to the block list, use the command `add_blocked_website <website>`.

To remove a website from the block list, use the command `remove_blocked_website <website>`.

To add an application to the block list, use the command `add_blocked_application <application>`.

To remove an application from the block list, use the command `remove_blocked_application <application>`.

### Task Management

The task management feature allows you to create a list of tasks to work on during each focus session. Each task has a title, a brief description, an estimated duration in Pomodoros, and a completion status.

To add a task, use the command `add_task <title> <description> <duration>`.

To remove a task, use the command `remove_task <title>`.

To mark a task as complete, use the command `complete_task <title>`.

To edit a task, use the command `edit_task <title> <new_title> <new_description> <new_duration>`.

## Additional Features

### Customization

FocusBlocks allows you to customize the durations of focus periods and breaks. You can also customize the list of websites and applications to block during focus sessions.

To set a custom duration for focus periods, use the command `set_work_duration <duration>`.

To set a custom duration for short breaks, use the command `set_short_break_duration <duration>`.

To set a custom duration for long breaks, use the command `set_long_break_duration <duration>`.

### Reporting and Analytics

FocusBlocks provides daily, weekly, and monthly reports showing your productivity. These reports include the number of focus sessions completed, tasks completed, and time spent in focus. Visual analytics in the form of graphs or charts are also available to help you assess productivity trends.

## Conclusion

FocusBlocks is a powerful productivity tool that combines the Pomodoro technique with website and application blocking and task management features. By using FocusBlocks, you can effectively manage your time, stay focused, and track your progress towards your goals.