# FocusBlocks User Manual

## Introduction

FocusBlocks is a productivity tool designed to help users manage their time effectively using the Pomodoro technique with a twist. The application acts as a timer and also blocks distracting websites and applications during focus sessions. It includes features for task management, allowing users to allocate specific tasks to each focus session and track their progress over time.

## Installation

To use FocusBlocks, you need to install the required dependencies. Follow the steps below to install the necessary environment dependencies:

1. Make sure you have Python installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Open a terminal or command prompt and navigate to the directory where you have downloaded the FocusBlocks code.

3. Create a virtual environment (optional but recommended) by running the following command:

   ```
   python -m venv venv
   ```

4. Activate the virtual environment by running the appropriate command for your operating system:

   - Windows:

     ```
     venv\Scripts\activate
     ```

   - macOS/Linux:

     ```
     source venv/bin/activate
     ```

5. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

## Getting Started

Once you have installed the dependencies, you can start using FocusBlocks. Follow the steps below to get started:

1. Open a terminal or command prompt and navigate to the directory where you have downloaded the FocusBlocks code.

2. Activate the virtual environment (if you created one) by running the appropriate command.

3. Run the main.py file using the following command:

   ```
   python main.py
   ```

4. The FocusBlocks application will start running, and you will see the main menu.

## Main Menu

The main menu of FocusBlocks provides options to start, pause, and stop the Pomodoro timer, manage tasks, and customize settings. Use the arrow keys to navigate through the menu and press Enter to select an option.

### Start Pomodoro

Selecting this option will start the Pomodoro timer. You will be prompted to select a task or tasks you intend to work on during the focus session. Once the timer starts, it will run for the specified duration, and you will receive visual and audio notifications when a session starts or ends, and when it's time for a break.

### Pause Pomodoro

Selecting this option will pause the Pomodoro timer. The remaining time will be saved, and you can resume the timer later.

### Stop Pomodoro

Selecting this option will stop the Pomodoro timer. Any progress made during the current session will be lost.

### Manage Tasks

Selecting this option will allow you to create, edit, and delete tasks. You can also mark tasks as complete and review completed tasks at the end of each day or session.

### Customize Settings

Selecting this option will allow you to customize the duration of focus sessions and break intervals. You can also customize notification sounds and themes of the application.

## Task Management

FocusBlocks provides a task management feature that allows you to create, edit, and delete tasks. Each task has a title, a brief description, an estimated duration (number of Pomodoros), and a completion status.

To manage tasks, select the "Manage Tasks" option from the main menu. You will see a list of tasks with options to add, edit, delete, and mark tasks as complete.

### Add Task

Selecting the "Add Task" option will prompt you to enter the title, description, and estimated duration of the task. Once you provide the required information, the task will be added to the task list.

### Edit Task

Selecting the "Edit Task" option will prompt you to select a task from the list. Once you select a task, you can edit its title, description, and estimated duration.

### Delete Task

Selecting the "Delete Task" option will prompt you to select a task from the list. Once you select a task, it will be deleted from the task list.

### Mark Task as Complete

Selecting the "Mark Task as Complete" option will prompt you to select a task from the list. Once you select a task, it will be marked as complete.

### Review Completed Tasks

Selecting the "Review Completed Tasks" option will display a list of completed tasks. You can review the tasks completed during the current day or session.

## Customization

FocusBlocks allows you to customize various aspects of the application, including the duration of focus sessions and break intervals, notification sounds, and themes.

To customize settings, select the "Customize Settings" option from the main menu. You will see options to customize focus session duration, break interval duration, notification sounds, and themes.

### Customize Focus Session Duration

Selecting the "Customize Focus Session Duration" option will prompt you to enter the desired duration for focus sessions. You can set a custom duration in minutes.

### Customize Break Interval Duration

Selecting the "Customize Break Interval Duration" option will prompt you to enter the desired duration for break intervals. You can set a custom duration in minutes.

### Customize Notification Sounds

Selecting the "Customize Notification Sounds" option will allow you to choose a custom notification sound for session start, session end, and break time.

### Customize Themes

Selecting the "Customize Themes" option will allow you to choose a custom theme for the application. You can select from a list of predefined themes or create your own.

## Conclusion

FocusBlocks is a powerful productivity tool that helps you manage your time effectively using the Pomodoro technique. With its features for task management and distraction blocking, you can stay focused and increase your productivity. Use this user manual as a guide to get started with FocusBlocks and make the most out of your work sessions. Happy focusing!

```