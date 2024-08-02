# FocusBlocks User Manual

## Introduction

FocusBlocks is a productivity tool designed to help users manage their time effectively using the Pomodoro technique. It not only acts as a simple timer but also blocks distracting websites and applications during focus sessions. The application includes features for task management, allowing users to allocate specific tasks to each focus session and track their progress over time.

This user manual will guide you through the installation process, explain the main functions of the software, and provide instructions on how to use it effectively.

## Installation

To use FocusBlocks, you need to have Python installed on your computer. Follow these steps to install the necessary dependencies and set up the environment:

1. Open a terminal or command prompt.
2. Navigate to the directory where you want to install FocusBlocks.
3. Run the following command to install the required packages:

```
pip install -r requirements.txt
```

4. Once the installation is complete, you can start using FocusBlocks.

## Main Functions

### Pomodoro Timer

The Pomodoro timer is the core feature of FocusBlocks. It allows you to start, pause, and stop focus sessions based on the Pomodoro technique. Here's how you can use the Pomodoro timer:

1. Open a terminal or command prompt.
2. Navigate to the directory where FocusBlocks is installed.
3. Run the following command to start the Pomodoro timer:

```
python main.py start
```

4. The timer will start with the default settings of 25 minutes for focus sessions and 5 minutes for short breaks.
5. You will receive visual and audio notifications when a session starts or ends, and when it's time for a break.
6. To pause the timer, press the "Pause" button or run the following command:

```
python main.py pause
```

7. To stop the timer, press the "Stop" button or run the following command:

```
python main.py stop
```

### Task Management

FocusBlocks also includes task management features to help you stay organized during focus sessions. Here's how you can use the task management functionality:

1. Open a terminal or command prompt.
2. Navigate to the directory where FocusBlocks is installed.
3. Run the following command to add a task:

```
python main.py add_task "Task Title" "Task Description" 2
```

4. Replace "Task Title" with the title of your task, "Task Description" with a brief description, and 2 with the estimated duration of the task in Pomodoros.
5. To remove a task, run the following command:

```
python main.py remove_task "Task Title"
```

6. Replace "Task Title" with the title of the task you want to remove.
7. To view the list of tasks, run the following command:

```
python main.py get_tasks
```

8. To mark a task as complete, run the following command:

```
python main.py complete_task "Task Title"
```

9. Replace "Task Title" with the title of the task you want to mark as complete.
10. To edit a task, run the following command:

```
python main.py edit_task "Task Title" "New Task Title" "New Task Description" 3
```

11. Replace "Task Title" with the title of the task you want to edit, "New Task Title" with the new title, "New Task Description" with the new description, and 3 with the new estimated duration of the task in Pomodoros.

### Website and Application Blocker

FocusBlocks can block access to distracting websites and applications during focus sessions. Here's how you can use the website and application blocking functionality:

1. Open a terminal or command prompt.
2. Navigate to the directory where FocusBlocks is installed.
3. Run the following command to add a website to the block list:

```
python main.py add_blocked_website "example.com"
```

4. Replace "example.com" with the website you want to block.
5. To remove a website from the block list, run the following command:

```
python main.py remove_blocked_website "example.com"
```

6. Replace "example.com" with the website you want to unblock.
7. To add an application to the block list, run the following command:

```
python main.py add_blocked_application "example.exe"
```

8. Replace "example.exe" with the application you want to block.
9. To remove an application from the block list, run the following command:

```
python main.py remove_blocked_application "example.exe"
```

10. Replace "example.exe" with the application you want to unblock.
11. To block websites and applications, run the following command:

```
python main.py block_websites_and_applications
```

12. To unblock websites and applications, run the following command:

```
python main.py unblock_websites_and_applications
```

## Conclusion

FocusBlocks is a powerful productivity tool that can help you manage your time effectively and stay focused on your tasks. By using the Pomodoro timer, task management features, and website and application blocker, you can improve your productivity and achieve your goals more efficiently.

If you have any questions or need further assistance, please refer to the documentation or contact our support team. Happy focusing!

```