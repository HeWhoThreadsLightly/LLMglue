# FocusBlocks User Manual

## Introduction

Welcome to FocusBlocks, a productivity tool designed to help you manage your time effectively using the Pomodoro technique with a twist. This application not only acts as a simple timer but also blocks distracting websites and applications during focus sessions. It includes features for task management, allowing you to allocate specific tasks to each focus session and track your progress over time.

## Installation

To use FocusBlocks, you need to have Python installed on your computer. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Once you have Python installed, you can follow these steps to install FocusBlocks:

1. Open a terminal or command prompt.
2. Navigate to the directory where you have downloaded the FocusBlocks files.
3. Run the following command to install the required dependencies:

```
pip install -r requirements.txt
```

## Getting Started

To start using FocusBlocks, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where you have downloaded the FocusBlocks files.
3. Run the following command to start the application:

```
python main.py
```

## Main Functions

### Start a Focus Session

To start a focus session, click on the "Start" button or run the `start_pomodoro()` function in the terminal or command prompt.

During a focus session, the timer will count down the duration of the session (default: 25 minutes). You should focus on your task during this time and avoid distractions.

### Pause a Focus Session

To pause a focus session, click on the "Pause" button or run the `pause_pomodoro()` function in the terminal or command prompt.

Pausing a focus session will temporarily stop the timer. You can resume the session later by clicking on the "Resume" button or running the `start_pomodoro()` function again.

### Stop a Focus Session

To stop a focus session, click on the "Stop" button or run the `stop_pomodoro()` function in the terminal or command prompt.

Stopping a focus session will reset the timer and end the session. You can start a new session by clicking on the "Start" button or running the `start_pomodoro()` function again.

### Customize Session Duration

By default, the focus session duration is set to 25 minutes. If you want to customize the duration, you can modify the `work_duration` variable in the `pomodoro.py` file.

### Customize Break Intervals

By default, the short break duration is set to 5 minutes and the long break duration is set to 15 minutes. If you want to customize these durations, you can modify the `short_break_duration` and `long_break_duration` variables in the `pomodoro.py` file.

### Track Tasks

FocusBlocks includes a task management feature that allows you to allocate specific tasks to each focus session and track your progress over time. To use this feature, you can modify the `TaskManager` class in the `task_manager.py` file.

## Conclusion

Congratulations! You have successfully installed and learned how to use FocusBlocks. This productivity tool will help you manage your time effectively and improve your focus during work or study sessions. Enjoy your productive sessions with FocusBlocks!