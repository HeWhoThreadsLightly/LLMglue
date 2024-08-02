# FocusBlocks User Manual

## Introduction

Welcome to FocusBlocks, a productivity tool designed to help you manage your time effectively using the Pomodoro technique with a twist. This application not only acts as a simple timer but also blocks distracting websites and applications during focus sessions. It includes features for task management, allowing you to allocate specific tasks to each focus session and track your progress over time.

## Installation

To use FocusBlocks, you need to have Python installed on your computer. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Once you have Python installed, you can install FocusBlocks by following these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where you downloaded the FocusBlocks code.
3. Run the following command to install the required dependencies:

```
pip install -r requirements.txt
```

## Getting Started

To start using FocusBlocks, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where you downloaded the FocusBlocks code.
3. Run the following command to start the application:

```
python main.py
```

4. The application will start, and you will see the main menu.

## Main Menu

The main menu of FocusBlocks provides options to start, pause, and stop a focus session, manage tasks, and configure website and application blocking.

### Start a Focus Session

To start a focus session, select the "Start Focus Session" option from the main menu. The Pomodoro timer will start, and you will be notified when the session starts and ends. During the focus session, distracting websites and applications will be blocked.

### Pause a Focus Session

To pause a focus session, select the "Pause Focus Session" option from the main menu. The timer will be paused, and you can resume the session later.

### Stop a Focus Session

To stop a focus session, select the "Stop Focus Session" option from the main menu. The timer will be stopped, and you can start a new session later.

### Manage Tasks

To manage tasks, select the "Manage Tasks" option from the main menu. You can add tasks, remove tasks, and view the list of tasks.

#### Add a Task

To add a task, select the "Add Task" option from the task management menu. Enter the title, description, and estimated duration of the task. The duration is specified in the number of Pomodoros.

#### Remove a Task

To remove a task, select the "Remove Task" option from the task management menu. Choose the task you want to remove from the list.

#### View Tasks

To view the list of tasks, select the "View Tasks" option from the task management menu. The tasks will be displayed with their titles, descriptions, estimated durations, and completion status.

### Configure Website and Application Blocking

To configure website and application blocking, select the "Configure Blocking" option from the main menu. You can add websites and applications to the block list, remove them, and enable or disable the blocking feature.

#### Add a Website to the Block List

To add a website to the block list, select the "Add Website" option from the blocking configuration menu. Enter the URL of the website you want to block.

#### Remove a Website from the Block List

To remove a website from the block list, select the "Remove Website" option from the blocking configuration menu. Choose the website you want to remove from the list.

#### Add an Application to the Block List

To add an application to the block list, select the "Add Application" option from the blocking configuration menu. Enter the name of the application you want to block.

#### Remove an Application from the Block List

To remove an application from the block list, select the "Remove Application" option from the blocking configuration menu. Choose the application you want to remove from the list.

#### Enable or Disable Blocking

To enable or disable the blocking feature, select the "Enable Blocking" or "Disable Blocking" option from the blocking configuration menu.

## Customization

FocusBlocks allows you to customize the duration of focus sessions and break intervals. By default, the focus session duration is set to 25 minutes, short breaks are set to 5 minutes, and long breaks are set to 15 minutes. You can change these settings by following these steps:

1. Open the `pomodoro.py` file in a text editor.
2. Locate the lines that define the duration variables:

```python
self.work_duration = 25 * 60  # 25 minutes in seconds
self.short_break_duration = 5 * 60  # 5 minutes in seconds
self.long_break_duration = 15 * 60  # 15 minutes in seconds
```

3. Modify the values according to your preferences. The duration is specified in seconds.

## Troubleshooting

If you encounter any issues while using FocusBlocks, please try the following troubleshooting steps:

1. Make sure you have installed the required dependencies by running the command `pip install -r requirements.txt`.
2. Check that you have Python installed on your computer. You can verify this by running the command `python --version` in a terminal or command prompt.
3. Ensure that you are running the application from the correct directory. Navigate to the directory where you downloaded the FocusBlocks code before running the command `python main.py`.
4. If you are experiencing issues with website or application blocking, make sure that you have the necessary permissions to modify firewall rules and kill processes on your system.

If the issue persists, please contact our support team for further assistance.

## Conclusion

Congratulations! You have successfully installed and started using FocusBlocks. This productivity tool will help you manage your time effectively using the Pomodoro technique with website and application blocking. Enjoy your focused work sessions and increased productivity!

```

Please note that the user manual provided above is a template and needs to be customized according to the specific features and functionalities of the FocusBlocks application.