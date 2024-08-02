# FocusBlocks User Manual

## Introduction

FocusBlocks is a productivity tool designed to help users manage their time effectively using the Pomodoro technique with a twist. The application acts as a timer and also blocks distracting websites and applications during focus sessions. It includes features for task management, allowing users to allocate specific tasks to each focus session and track their progress over time.

This user manual will guide you through the installation process, explain the main functions of the software, and provide instructions on how to use it effectively.

## Installation

To use FocusBlocks, you need to have Python installed on your computer. Follow these steps to install the required dependencies and set up the environment:

1. Open a terminal or command prompt.

2. Navigate to the directory where you have downloaded or cloned the FocusBlocks project.

3. Create a virtual environment (optional but recommended):

   ```shell
   python -m venv venv
   ```

4. Activate the virtual environment:

   - For Windows:

     ```shell
     venv\Scripts\activate
     ```

   - For macOS and Linux:

     ```shell
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

6. You're now ready to use FocusBlocks!

## Main Functions

### Pomodoro Timer

The Pomodoro timer is the core feature of FocusBlocks. It allows you to start, pause, and stop focus sessions based on the Pomodoro technique.

To start a focus session, use the `start_pomodoro()` function:

```python
start_pomodoro()
```

To pause a focus session, use the `pause_pomodoro()` function:

```python
pause_pomodoro()
```

To stop a focus session, use the `stop_pomodoro()` function:

```python
stop_pomodoro()
```

### Customizing Timer Durations

By default, the focus session duration is set to 25 minutes, and the short break duration is set to 5 minutes. You can customize these durations using the following functions:

- `set_work_duration(duration)`: Set the duration of the focus session in minutes.
- `set_short_break_duration(duration)`: Set the duration of the short break in minutes.
- `set_long_break_duration(duration)`: Set the duration of the long break in minutes.

For example, to set the focus session duration to 30 minutes:

```python
set_work_duration(30)
```

### Visual and Audio Notifications

FocusBlocks provides visual and audio notifications to alert you when a session starts or ends, and when it's time for a break. The visual notifications are not implemented in the current version, but you can enable audio notifications using the following function:

```python
enable_audio_notifications()
```

### Task Management

FocusBlocks allows you to create a list of tasks you plan to work on during each focus session. You can add tasks, remove tasks, and get the list of tasks.

To add a task, use the `add_task(task)` function:

```python
add_task("Write user manual")
```

To remove a task, use the `remove_task(task)` function:

```python
remove_task("Write user manual")
```

To get the list of tasks, use the `get_tasks()` function:

```python
tasks = get_tasks()
print(tasks)
```

### Distracting Website and Application Blocker

During focus sessions, FocusBlocks can block access to a user-customizable list of websites and applications that are deemed distracting. You can add websites and applications to the block list, remove them, and block or unblock them.

To add a website to the block list, use the `add_blocked_website(website)` function:

```python
add_blocked_website("facebook.com")
```

To remove a website from the block list, use the `remove_blocked_website(website)` function:

```python
remove_blocked_website("facebook.com")
```

To add an application to the block list, use the `add_blocked_application(application)` function:

```python
add_blocked_application("spotify.exe")
```

To remove an application from the block list, use the `remove_blocked_application(application)` function:

```python
remove_blocked_application("spotify.exe")
```

To block websites and applications, use the `block_websites_and_applications()` function:

```python
block_websites_and_applications()
```

To unblock websites and applications, use the `unblock_websites_and_applications()` function:

```python
unblock_websites_and_applications()
```

## Conclusion

FocusBlocks is a powerful productivity tool that combines the Pomodoro technique with website and application blocking. By following the instructions in this user manual, you can effectively manage your time, stay focused, and increase your productivity.

If you have any questions or encounter any issues while using FocusBlocks, please refer to the documentation or contact our support team for assistance.

Happy focusing!