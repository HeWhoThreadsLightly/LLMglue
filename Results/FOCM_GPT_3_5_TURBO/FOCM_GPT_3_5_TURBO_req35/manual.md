# File Organizer and Content Manager User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a desktop application designed to help users efficiently organize, search, and manage their local files. This software aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. It provides a unified interface for managing digital content, supporting various file types, including documents, images, videos, and more.

## Installation

To install the File Organizer and Content Manager, follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

2. Open a terminal or command prompt and navigate to the directory where you want to install the application.

3. Clone the repository by running the following command:

   ```
   git clone https://github.com/your-username/focm.git
   ```

   Replace `your-username` with your GitHub username.

4. Navigate to the `focm` directory:

   ```
   cd focm
   ```

5. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary packages for running the application.

## Getting Started

To start using the File Organizer and Content Manager, follow these steps:

1. Open a terminal or command prompt and navigate to the `focm` directory.

2. Run the following command to start the application:

   ```
   python main.py
   ```

   This will launch the File Organizer and Content Manager.

3. The main window of the application will appear, featuring a dual-pane layout. The left pane displays the directory tree, and the right pane shows the contents of the selected directory.

4. Use the toolbar at the top of the main window to perform common actions, such as creating a new folder, deleting a file, refreshing the view, toggling between list/grid view, and searching for files.

5. Use the status bar at the bottom of the main window to view information about the selected files/folders and general statistics, such as the total number of files and total size.

## Features

### Directory Tree

The directory tree pane in the main window allows you to navigate through the file system. It displays the folder structure and allows you to select directories.

### Content View

The content view pane in the main window shows the contents of the selected directory. It displays files and folders in a list or grid format, depending on the selected view.

### Toolbar

The toolbar at the top of the main window provides buttons for common actions. You can use these buttons to create a new folder, delete a file, refresh the view, toggle between list/grid view, and search for files.

### Status Bar

The status bar at the bottom of the main window displays information about the selected files/folders and general statistics. It shows the total number of files and total size.

### Search and Filter Panel

The search and filter panel, accessible from the main window, allows you to enter search criteria, choose filters (file type, date modified, size), and display results in a list or grid format. It also provides advanced search options for more precise filtering, including full-text search within documents.

### File Preview Window

The file preview window, a pop-up or sidebar window, provides a quick preview of the selected file. For text documents and images, it shows a preview within the window. For videos and audio files, it provides basic playback controls. It also supports edit mode for text files, enabling you to make quick edits directly within the preview window.

### File Properties and Metadata Editor

The file properties and metadata editor, accessible from the context menu of a file/folder, displays detailed information about the selected file. It shows file size, creation/modification dates, and allows you to edit metadata tags.

### Settings/Preferences Window

The settings/preferences window, accessible from the main menu, allows you to customize application settings. You can choose the theme (dark/light), set default views, configure file organization rules, manage backup settings, and handle extension/plugin management.

### Tag Management Interface

The tag management interface, a panel or window, allows you to create, edit, and delete tags. You can assign tags to files or folders from this interface, providing a flexible way to categorize and locate files quickly.

### Backup and Synchronization Setup Wizard

The backup and synchronization setup wizard guides you through setting up backup destinations (external drive, cloud storage) and synchronization options. It includes scheduling automatic backups to ensure data safety.

### Help and Tutorial Section

The help and tutorial section, accessible from the main menu, offers a searchable help database, user manual, and interactive tutorials on key features. It provides assistance and guidance for using the File Organizer and Content Manager effectively.

### File Organization

The File Organizer and Content Manager supports automated organization rules. You can create customizable rules based on file type, date criteria, file name patterns, and file size thresholds. You can specify the target folder structure for organized files and create new folders based on rule criteria.

You can also manually tag and categorize files and folders. The application offers a tagging interface that suggests existing tags as you type and allows the creation of new tags. It supports creating custom categories for grouping files/folders based on project, client, priority, or any other user-defined category. You can view and access files by tags and categories through a dedicated interface or filter.

The application supports bulk file operations, such as renaming, moving, copying, or deleting multiple files at once. You can also bulk apply tags or move files to a category. The application provides undo functionality to revert changes if needed.

### Folder and File Management

The File Organizer and Content Manager allows you to create, rename, move, and delete files and folders from within the application. It provides a drag-and-drop interface for moving files and folders into different categories or locations. It includes a feature to detect and resolve duplicate files based on name, size, and optionally content hash. You can choose to keep, delete, or merge duplicate files.

### Custom Folder Views and Sorting

The File Organizer and Content Manager allows you to customize how folders and files are displayed. You can choose between list, grid, and thumbnail views. It supports sorting files and folders by name, size, date modified, or custom tags/categories.

### File Watcher and Auto-Update

The File Organizer and Content Manager implements a file watcher mechanism that automatically updates file organization based on predefined rules when new files are added to monitored folders. This feature works in real-time or at user-defined intervals, ensuring the organization structure is always up-to-date.

### Integration with File System

The File Organizer and Content Manager integrates closely with the operating system's file system. It reflects changes made within the app in real-time in the user's file explorer or finder. It supports right-click context menu options in the operating system's file explorer to quickly tag, categorize, or apply predefined organization rules to selected files or folders.

### Advanced Search Functionality

The File Organizer and Content Manager provides advanced search functionality. You can search for files and folders using partial or full file names. It also supports content-based search capabilities, allowing you to find files containing specific text, even within documents or metadata for images and videos.

## Conclusion

The File Organizer and Content Manager is a powerful tool for organizing, searching, and managing local files. With its automated organization, advanced search capabilities, and content management features, it enhances productivity and simplifies file management. By following this user manual, you can make the most of the application and efficiently manage your digital content.