# File Organizer and Content Manager User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a desktop application designed to help users efficiently organize, search, and manage their local files. This software aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. It provides a unified interface for managing digital content, supporting various file types, including documents, images, videos, and more.

## Installation

To use the File Organizer and Content Manager, follow these steps:

1. Install Python: FOCM is developed using Python programming language. If you don't have Python installed, download and install the latest version from the official Python website (https://www.python.org).

2. Install dependencies: FOCM requires the following dependencies to be installed. Open a command prompt or terminal and run the following command to install the dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Download the FOCM source code: Download the source code of FOCM from the provided link or repository.

4. Run the application: Open a command prompt or terminal, navigate to the directory where you downloaded the source code, and run the following command:

   ```
   python main.py
   ```

   This will start the FOCM application.

## Main Window

The main window of FOCM serves as the central hub of the application. It features a dual-pane layout, with one pane for the directory tree (folders) and another for viewing the contents of the selected directory.

### Toolbar

The toolbar at the top of the main window provides buttons for common actions. The available buttons are:

- Create New Folder: Clicking this button allows you to create a new folder in the selected directory.
- Delete File: Clicking this button allows you to delete the selected file.
- Refresh View: Clicking this button refreshes the view, updating the directory tree and content view.
- Toggle View: Clicking this button toggles between list and grid view in the content view.
- Search Bar: Enter search criteria in the search bar and click the Search button to perform a search.

### Status Bar

The status bar at the bottom of the main window displays information about the selected files/folders and general statistics, such as the total number of files and total size.

## Search and Filter Panel

FOCM provides a dedicated panel accessible from the main window for searching and filtering files. This panel allows you to enter search criteria, choose filters (file type, date modified, size), and display results in a list or grid format.

### Advanced Search Options

FOCM offers advanced search options for more precise filtering. These options include full-text search within documents, allowing you to find files containing specific text.

## File Preview Window

FOCM provides a file preview window that allows you to quickly preview the selected file. For text documents and images, the preview is shown within the window. For videos and audio files, basic playback controls are provided.

### Edit Mode

For text files, FOCM allows you to make quick edits directly within the preview window. Simply enable the edit mode and make the necessary changes.

## File Properties and Metadata Editor

FOCM provides a dialog box that displays detailed information about a selected file or folder. This dialog box shows file size, creation/modification dates, and allows you to edit metadata tags.

## Settings/Preferences Window

FOCM offers a separate window accessible from the main menu for customizing application settings. In this window, you can customize the theme (dark/light), default views, file organization rules, backup settings, and extension/plugin management.

## Tag Management Interface

FOCM provides a panel or window for creating, editing, and deleting tags. You can assign tags to files or folders from this interface, providing a flexible way to categorize and locate files quickly.

## Backup and Synchronization Setup Wizard

FOCM includes a step-by-step wizard that guides you through setting up backup destinations (external drive, cloud storage) and synchronization options, including scheduling automatic backups.

## Help and Tutorial Section

FOCM offers a dedicated window or section accessible from the main menu, providing a searchable help database, user manual, and interactive tutorials on key features.

## File Organization

FOCM provides various features for organizing files and folders.

### Automated Organization Rules

You can create customizable rules for automatically organizing files based on file type, date criteria (creation date, modification date), file name patterns (using wildcards or regular expressions), and file size thresholds. You can specify the target folder structure for organized files, with options to create new folders based on rule criteria (e.g., date, project name).

### Manual Tagging and Categorization

FOCM allows you to assign custom tags to files and folders manually. It offers a tagging interface that suggests existing tags as you type and allows the creation of new tags. You can also create custom categories to group files/folders based on project, client, priority, or any other user-defined category. You can view and access files by tags and categories through a dedicated interface or filter.

### Bulk File Operations

FOCM supports bulk operations to rename, move, copy, or delete multiple files at once based on user selection. You can also bulk apply tags or move files to a category. Undo functionality is provided to revert changes if needed.

### Folder and File Management

FOCM allows you to create, rename, move, and delete files and folders from within the application. It provides a drag-and-drop interface for moving files and folders into different categories or locations. It also includes a feature to detect and resolve duplicate files based on name, size, and optionally content hash, with options to keep, delete, or merge duplicate files.

### Custom Folder Views and Sorting

FOCM allows you to customize how folders and files are displayed, including list, grid, and thumbnail views. It supports sorting files and folders by name, size, date modified, or custom tags/categories.

### File Watcher and Auto-Update

FOCM implements a file watcher mechanism that automatically updates file organization based on predefined rules when new files are added to monitored folders. This feature works in real-time or at user-defined intervals, ensuring the organization structure is always up-to-date.

### Integration with File System

FOCM integrates closely with the operating system's file system to reflect changes made within the app in real-time in the user's file explorer or finder. It supports right-click context menu options in the operating system's file explorer to quickly tag, categorize, or apply predefined organization rules to selected files or folders.

## Search and Filter

FOCM provides advanced search functionality to help you find files and folders.

### Advanced Search

You can search for files and folders using partial or full file names. FOCM also supports content-based search capabilities, allowing you to find files containing specific text, even within documents or metadata for images and videos. It supports regular expressions (regex) in search queries for complex pattern matching.

### Custom Search Filters

FOCM offers predefined filters to quickly select files based on common criteria such as file type, size, and modification or creation date. It also allows you to create, save, and apply custom filter sets based on any combination of file attributes, including custom tags, project names, or specific content.

## Conclusion

The File Organizer and Content Manager (FOCM) provides a comprehensive set of features for efficiently organizing, searching, and managing local files. With its automated organization rules, manual tagging and categorization, bulk file operations, and advanced search capabilities, FOCM enhances productivity and simplifies file management. Whether you need to organize your personal files or manage a large collection of documents, images, and videos, FOCM is the ideal solution. Enjoy using FOCM and stay organized!