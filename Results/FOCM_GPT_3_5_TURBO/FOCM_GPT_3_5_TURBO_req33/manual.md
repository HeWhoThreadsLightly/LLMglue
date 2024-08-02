# File Organizer and Content Manager User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a desktop application designed to help users efficiently organize, search, and manage their local files. This software aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. It provides a unified interface for managing digital content, supporting various file types, including documents, images, videos, and more.

## Installation

To install the File Organizer and Content Manager, follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

2. Open a command prompt or terminal window.

3. Use the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Once the installation is complete, you can run the application using the following command:

   ```
   python main.py
   ```

## Main Window

The main window of the File Organizer and Content Manager serves as the central hub of the application. It features a dual-pane layout, with one pane for the directory tree (folders) and another for viewing the contents of the selected directory.

### Toolbar

The toolbar at the top of the main window provides buttons for common actions. These actions include creating a new folder, deleting a file, refreshing the view, toggling between list/grid view, and searching for files.

### Status Bar

The status bar at the bottom of the main window displays information about the selected files/folders and general statistics, such as the total number of files and total size.

## Search and Filter Panel

The search and filter panel is a dedicated panel accessible from the main window. It allows users to enter search criteria, choose filters (file type, date modified, size), and display results in a list or grid format. Advanced search options are available for more precise filtering, including full-text search within documents.

## File Preview Window

The file preview window provides a quick preview of the selected file. For text documents and images, the preview is shown within the window. For videos and audio files, basic playback controls are provided.

### Edit Mode

For text files, the file preview window also supports edit mode, enabling users to make quick edits directly within the preview window.

## File Properties and Metadata Editor

The file properties and metadata editor is a dialog box that displays when a user selects "Properties" from the context menu of a file or folder. It shows detailed information about the file, including file size, creation/modification dates, and allows the user to edit metadata tags.

## Settings/Preferences Window

The settings/preferences window is a separate window accessible from the main menu. It allows users to customize application settings, including theme selection (dark/light), default views, file organization rules, backup settings, and extension/plugin management.

## Tag Management Interface

The tag management interface is a panel or window for creating, editing, and deleting tags. Users can also assign tags to files or folders from this interface, providing a flexible way to categorize and locate files quickly.

## Backup and Synchronization Setup Wizard

The backup and synchronization setup wizard is a step-by-step wizard that guides users through setting up backup destinations (external drive, cloud storage) and synchronization options, including scheduling automatic backups.

## Help and Tutorial Section

The help and tutorial section is a dedicated window or section accessible from the main menu. It offers a searchable help database, user manual, and interactive tutorials on key features.

## File Organization

The File Organizer and Content Manager provides various features for file organization.

### Automated Organization Rules

Users can create customizable rules for automatically organizing files based on file type, date criteria, file name patterns, and file size thresholds. Users can specify the target folder structure for organized files, with options to create new folders based on rule criteria.

### Manual Tagging and Categorization

Users can assign custom tags to files and folders manually. The application offers a tagging interface that suggests existing tags as the user types and allows the creation of new tags. Users can also create custom categories to group files/folders based on project, client, priority, or any other user-defined category. Files can be viewed and accessed by tags and categories through a dedicated interface or filter.

### Bulk File Operations

The application supports bulk operations to rename, move, copy, or delete multiple files at once based on user selection. Users can also bulk apply tags or move files to a category, with undo functionality to revert changes if needed.

### Folder and File Management

Users can create, rename, move, and delete files and folders from within the application. The application provides a drag-and-drop interface for moving files and folders into different categories or locations. It also includes a feature to detect and resolve duplicate files based on name, size, and optionally content hash, with options to keep, delete, or merge duplicate files.

### Custom Folder Views and Sorting

Users can customize how folders and files are displayed, including list, grid, and thumbnail views. The application supports sorting files and folders by name, size, date modified, or custom tags/categories.

### File Watcher and Auto-Update

The File Organizer and Content Manager implements a file watcher mechanism that automatically updates file organization based on predefined rules when new files are added to monitored folders. This feature works in real-time or at user-defined intervals, ensuring the organization structure is always up-to-date.

### Integration with File System

The application integrates closely with the operating system's file system to reflect changes made within the app in real-time in the user's file explorer or finder. It also supports right-click context menu options in the operating system’s file explorer to quickly tag, categorize, or apply predefined organization rules to selected files or folders.

## Conclusion

The File Organizer and Content Manager provides a comprehensive set of features for efficiently organizing, searching, and managing local files. With its automated organization rules, manual tagging and categorization, bulk file operations, and integration with the file system, users can easily stay organized and find files quickly. The user manual provided here should guide you through the installation process and help you make the most of the application's features. Enjoy using the File Organizer and Content Manager!