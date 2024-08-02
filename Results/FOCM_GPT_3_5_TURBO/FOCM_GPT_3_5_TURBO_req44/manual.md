# File Organizer and Content Manager User Manual

## Introduction
The File Organizer and Content Manager (FOCM) is a desktop application designed to help users efficiently organize, search, and manage their local files. This software aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. It provides a unified interface for managing digital content and supports various file types, including documents, images, videos, and more.

## Installation
To install the File Organizer and Content Manager, follow these steps:

1. Ensure that you have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

2. Open a command prompt or terminal window.

3. Navigate to the directory where you have downloaded the FOCM files.

4. Run the following command to install the required dependencies:
```
pip install -r requirements.txt
```

## Getting Started
To start using the File Organizer and Content Manager, follow these steps:

1. Open a command prompt or terminal window.

2. Navigate to the directory where you have downloaded the FOCM files.

3. Run the following command to start the application:
```
python main.py
```

4. The File Organizer and Content Manager main window will open, featuring a dual-pane layout. The left pane displays the directory tree, and the right pane displays the contents of the selected directory.

## Main Window
The main window of the File Organizer and Content Manager serves as the central hub for file organization and management. It consists of several components:

### Directory Tree
The left pane of the main window displays the directory tree, allowing you to navigate through your file system. Clicking on a directory will update the content view to display the contents of that directory.

### Content View
The right pane of the main window displays the contents of the selected directory. You can view files and folders in either list or grid view, depending on your preference. The content view supports sorting by name, size, date modified, and custom tags/categories.

### Toolbar
The toolbar at the top of the main window provides buttons for common actions. These actions include creating a new folder, deleting a file, refreshing the view, toggling between list/grid view, and searching for files.

### Status Bar
The status bar at the bottom of the main window displays information about the selected files/folders and general statistics, such as the total number of files and total size.

## File Organization
The File Organizer and Content Manager offers various features for organizing files:

### Automated Organization Rules
You can create customizable rules for automatically organizing files based on file type, date criteria, file name patterns, and file size thresholds. These rules allow you to specify the target folder structure for organized files, with options to create new folders based on rule criteria, such as date or project name.

### Manual Tagging and Categorization
You can assign custom tags to files and folders manually. The application offers a tagging interface that suggests existing tags as you type and allows the creation of new tags. You can also create custom categories to group files/folders based on project, client, priority, or any other user-defined category. Files can be viewed and accessed by tags and categories through a dedicated interface or filter.

### Bulk File Operations
The application supports bulk operations to rename, move, copy, or delete multiple files at once based on user selection. You can also bulk apply tags or move files to a category. The application provides undo functionality to revert changes if needed.

### Folder and File Management
You can create, rename, move, and delete files and folders from within the application. The application also provides a drag-and-drop interface for moving files and folders into different categories or locations. Additionally, the application can detect and resolve duplicate files based on name, size, and optionally content hash. You can choose to keep, delete, or merge duplicate files.

### Custom Folder Views and Sorting
You can customize how folders and files are displayed in the content view. The application supports list, grid, and thumbnail views. You can also sort files and folders by name, size, date modified, or custom tags/categories.

### File Watcher and Auto-Update
The application implements a file watcher mechanism that automatically updates file organization based on predefined rules when new files are added to monitored folders. This feature works in real-time or at user-defined intervals, ensuring that the organization structure is always up-to-date.

### Integration with File System
The application integrates closely with the operating system's file system to reflect changes made within the app in real-time in the user's file explorer or finder. It also supports right-click context menu options in the operating system's file explorer to quickly tag, categorize, or apply predefined organization rules to selected files or folders.

## Search and Filtering
The File Organizer and Content Manager provides advanced search functionality to help you find files and folders:

### Basic Search
You can search for files and folders using partial or full file names. The search results will be displayed in the content view.

### Content-Based Search
The application supports content-based search capabilities, allowing you to find files containing specific text. This includes searching within documents or metadata for images and videos.

### Regular Expressions
You can use regular expressions (regex) in search queries for complex pattern matching.

### Custom Search Filters
The application provides predefined filters to quickly select files based on common criteria, such as file type, size, and modification or creation date. You can also create, save, and apply custom filter sets based on any combination of file attributes, including custom tags, project names, or specific content.

### Tag-Based Searching
The application integrates a tagging system where you can assign custom tags to files and folders. You can then search for files based on these tags. The tagging system supports hierarchical tags to facilitate detailed organization and searching.

### Search History and Saved Searches
The application automatically saves recent searches for quick repetition. You can also save frequently used search queries or filters for quick access.

### Search Results Management
The search results can be sorted based on various criteria, such as name, size, date modified, and custom tags. You can also export search results to CSV or other formats for external use.

## Settings and Preferences
The File Organizer and Content Manager allows you to customize application settings through the Settings/Preferences window. This window can be accessed from the main menu and provides options for theme selection (dark/light), default views, file organization rules, backup settings, and extension/plugin management.

## Help and Tutorials
The File Organizer and Content Manager includes a dedicated Help and Tutorial section. This section can be accessed from the main menu and offers a searchable help database, user manual, and interactive tutorials on key features.

## Conclusion
The File Organizer and Content Manager provides a comprehensive set of features for efficient file organization, search, and management. With its automated organization rules, manual tagging and categorization, bulk file operations, and advanced search capabilities, it offers a powerful solution for managing digital content. Whether you need to organize your files, find specific documents, or customize your file views, the File Organizer and Content Manager has you covered. Enjoy enhanced productivity and file management with this powerful desktop application.