# FocusBlocks User Manual

## Introduction

Welcome to FocusBlocks, a productivity tool designed to help you manage your time effectively using the Pomodoro technique with a twist. This application not only acts as a simple timer but also blocks distracting websites and applications during focus sessions. It includes features for task management, allowing you to allocate specific tasks to each focus session and track your progress over time.

## Table of Contents

1. [Installation](#installation)
2. [Getting Started](#getting-started)
3. [Main Functions](#main-functions)
   - [Pomodoro Timer](#pomodoro-timer)
   - [Website and Application Blocker](#website-and-application-blocker)
   - [Task Management](#task-management)
4. [Customization](#customization)
5. [Reporting and Analytics](#reporting-and-analytics)
6. [Technical Requirements](#technical-requirements)
7. [Additional Features](#additional-features)
8. [Accessibility Requirements](#accessibility-requirements)

## Installation <a name="installation"></a>

To install FocusBlocks, follow these steps:

1. Make sure you have Python installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Open a terminal or command prompt.

3. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Once the installation is complete, you are ready to use FocusBlocks.

## Getting Started <a name="getting-started"></a>

To get started with FocusBlocks, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the directory where the FocusBlocks files are located.

3. Run the following command to start the application:

   ```
   python main.py
   ```

4. The FocusBlocks application will open in your default web browser.

## Main Functions <a name="main-functions"></a>

### Pomodoro Timer <a name="pomodoro-timer"></a>

The Pomodoro timer is the core feature of FocusBlocks. It allows you to start, pause, and stop a focus session based on the Pomodoro technique.

To use the Pomodoro timer, follow these steps:

1. Click on the "Start" button to start a focus session. The default duration for a focus session is 25 minutes.

2. During the focus session, the timer will count down the remaining time. Visual and audio notifications will alert you when the session starts, ends, and when it's time for a break.

3. After the focus session ends, you will be prompted to take a short break. The default duration for a short break is 5 minutes.

4. After the short break, you can start another focus session by clicking on the "Start" button again.

5. After every four focus sessions, you will be prompted to take a longer break. The default duration for a long break is 15 minutes.

### Website and Application Blocker <a name="website-and-application-blocker"></a>

The website and application blocker feature allows you to block access to distracting websites and applications during focus sessions.

To use the website and application blocker, follow these steps:

1. Click on the "Blocker" tab in the FocusBlocks application.

2. In the "Blocked Websites" section, you can add or remove websites from the block list. Enter the URL of the website you want to block and click on the "Add" button. To remove a website from the block list, click on the "Remove" button next to the website.

3. In the "Blocked Applications" section, you can add or remove applications from the block list. Enter the name of the application you want to block and click on the "Add" button. To remove an application from the block list, click on the "Remove" button next to the application.

4. During a focus session, the blocked websites and applications will be inaccessible. The blocking feature is robust enough to prevent easy bypasses, such as using a different browser or renaming the application's executable file.

### Task Management <a name="task-management"></a>

The task management feature allows you to create a list of tasks you plan to work on during each focus session.

To use the task management feature, follow these steps:

1. Click on the "Tasks" tab in the FocusBlocks application.

2. In the "Add Task" section, enter the title, description, and estimated duration (in Pomodoros) of the task you want to add. Click on the "Add" button to add the task to the list.

3. The list of tasks will be displayed in the "Task List" section. Each task will have a title, a brief description, an estimated duration, and a completion status.

4. To mark a task as complete, click on the "Complete" button next to the task.

5. To edit a task, click on the "Edit" button next to the task. You can change the title, description, and estimated duration of the task.

6. To remove a task from the list, click on the "Remove" button next to the task.

## Customization <a name="customization"></a>

FocusBlocks provides customization options to tailor the application to your preferences.

To customize FocusBlocks, follow these steps:

1. Click on the "Settings" tab in the FocusBlocks application.

2. In the "Focus Duration" section, you can set a custom duration for focus sessions. Enter the desired duration (in minutes) and click on the "Save" button.

3. In the "Break Duration" section, you can set custom durations for short breaks and long breaks. Enter the desired durations (in minutes) and click on the "Save" button.

4. In the "Notification Sounds" section, you can customize the notification sounds of the application. Click on the "Browse" button to select a sound file for each notification event (start, end, break). Click on the "Save" button to save the changes.

5. In the "Themes" section, you can choose from a selection of pre-defined themes for the application. Click on the desired theme to apply it.

## Reporting and Analytics <a name="reporting-and-analytics"></a>

FocusBlocks provides reporting and analytics features to help you assess your productivity.

To access the reporting and analytics features, follow these steps:

1. Click on the "Reports" tab in the FocusBlocks application.

2. In the "Daily Report" section, you can view a summary of your productivity for the current day. The report includes the number of focus sessions completed, tasks completed, and time spent in focus.

3. In the "Weekly Report" section, you can view a summary of your productivity for the current week. The report includes the number of focus sessions completed, tasks completed, and time spent in focus for each day of the week.

4. In the "Monthly Report" section, you can view a summary of your productivity for the current month. The report includes the number of focus sessions completed, tasks completed, and time spent in focus for each day of the month.

5. The reports are presented in the form of graphs or charts to make it easy to assess productivity trends.

## Technical Requirements <a name="technical-requirements"></a>

FocusBlocks has the following technical requirements:

- Local storage or an embedded database is used to store user data and preferences.

## Additional Features <a name="additional-features"></a>

FocusBlocks includes additional features to enhance your productivity experience.

To access the additional features, follow these steps:

1. Click on the "Calendar" tab in the FocusBlocks application.

2. In the "Task Scheduling" section, you can integrate FocusBlocks with popular calendar applications to schedule tasks. Click on the "Connect" button to connect your calendar application with FocusBlocks.

3. In the "Productivity Challenges" section, you can set and share productivity challenges with friends or colleagues. Click on the "Create Challenge" button to create a new challenge. Enter the details of the challenge and click on the "Save" button.

## Accessibility Requirements <a name="accessibility-requirements"></a>

FocusBlocks is designed with accessibility in mind to ensure that all users can efficiently navigate and use the application.

The accessibility requirements of FocusBlocks include:

- Full functionality is accessible via keyboard shortcuts to ensure that users who cannot use a mouse can navigate efficiently through the application.

- Tab navigation is implemented through all interactive elements in a logical order.

- Visual indicators are provided for the currently focused element.

- Alt text is used to describe images, icons, and other non-textual elements for screen reader support.

- Labels and roles are used for complex elements (like drag-and-drop interfaces or custom controls) to ensure their purpose and state are conveyed to screen reader users.

- Support for high contrast themes that make text, icons, and other elements more distinguishable for users with low vision.

- All text is readable and all interactive elements are visible against background colors in high contrast mode.

- Text size can be adjusted without breaking the layout or losing functionality.

- Support for user-defined system fonts, including those designed for dyslexia.

- Color schemes that are accessible to users with various types of color blindness (e.g., deuteranopia, protanopia, tritanopia).

- Information conveyed with color is also distinguishable through patterns or shapes.

- The application's interface and content can be magnified or zoomed in up to 200% without loss of content or functionality, to accommodate users with low vision.

- Clear and understandable feedback is provided for actions, such as file moved, deleted, or cannot be opened.

## Conclusion

Congratulations! You have completed the FocusBlocks user manual. You are now ready to use FocusBlocks to manage your time effectively and improve your productivity. Enjoy your focused work sessions and achieve your goals with FocusBlocks!