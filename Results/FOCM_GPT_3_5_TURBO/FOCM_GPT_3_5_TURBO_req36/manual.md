# File Organizer and Content Manager (FOCM) User Manual

## Introduction

Welcome to the user manual for the File Organizer and Content Manager (FOCM) desktop application. FOCM is designed to help you efficiently organize, search, and manage your local files, enhancing your productivity and file management capabilities. This manual will guide you through the installation process, introduce you to the main functions of the software, and provide instructions on how to use it effectively.

## Table of Contents

1. Installation
2. Main Window
   - Directory Tree
   - Content View
   - Toolbar
   - Status Bar
3. Search and Filter Panel
4. File Preview Window
5. File Properties and Metadata Editor
6. Settings/Preferences Window
7. Tag Management Interface
8. Backup and Synchronization Setup Wizard
9. Help and Tutorial Section
10. File Organization
    - Automated Organization Rules
    - Manual Tagging and Categorization
    - Bulk File Operations
    - Folder and File Management
    - Custom Folder Views and Sorting
    - File Watcher and Auto-Update
    - Integration with File System
11. Search and Filter
    - Advanced Search Functionality

## 1. Installation

To install FOCM, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where you have downloaded the FOCM source code.
3. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Once the dependencies are installed, you can run the FOCM application by executing the following command:

   ```
   python main.py
   ```

   The FOCM main window will open, and you can start using the application.

## 2. Main Window

The FOCM main window is the central hub of the application. It features a dual-pane layout, with one pane for the directory tree (folders) and another for viewing the contents of the selected directory.

### Directory Tree

The directory tree pane displays the file system structure of your local machine. It allows you to navigate through folders and select directories to view their contents in the content view pane.

### Content View

The content view pane displays the files and folders within the selected directory. You can interact with the files and folders directly from this pane, such as creating new folders, deleting files, and performing various file operations.

### Toolbar

The toolbar at the top of the main window provides buttons for common actions. These actions include creating a new folder, deleting a file, refreshing the view, toggling between list/grid view, and performing a search.

### Status Bar

The status bar at the bottom of the main window displays information about the selected files/folders and general statistics, such as the total number of files and total size.

## 3. Search and Filter Panel

The search and filter panel is a dedicated panel accessible from the main window. It allows you to enter search criteria, choose filters (file type, date modified, size), and display the search results in a list or grid format.

### Advanced Search Options

The search and filter panel provides advanced search options for more precise filtering. You can perform a full-text search within documents, enabling you to find files containing specific text. Additionally, the panel supports regular expressions (regex) in search queries for complex pattern matching.

## 4. File Preview Window

The file preview window is a pop-up or sidebar window that provides a quick preview of the selected file. For text documents and images, the preview is shown within the window. For videos and audio files, basic playback controls are provided.

### Edit Mode for Text Files

The file preview window also supports an edit mode for text files. This enables you to make quick edits directly within the preview window, saving you time and effort.

## 5. File Properties and Metadata Editor

The file properties and metadata editor is a dialog box that displays when you select "Properties" from the context menu of a file or folder. It shows detailed information about the file, including file size, creation/modification dates, and allows you to edit metadata tags.

## 6. Settings/Preferences Window

The settings/preferences window is a separate window accessible from the main menu. It allows you to customize various application settings, including theme selection (dark/light), default views, file organization rules, backup settings, and extension/plugin management.

## 7. Tag Management Interface

The tag management interface is a panel or window for creating, editing, and deleting tags. You can assign tags to files or folders from this interface, providing a flexible way to categorize and locate files quickly. The interface suggests existing tags as you type and allows you to create new tags.

## 8. Backup and Synchronization Setup Wizard

The backup and synchronization setup wizard is a step-by-step wizard that guides you through setting up backup destinations (external drive, cloud storage) and synchronization options. It includes scheduling automatic backups to ensure your files are always protected.

## 9. Help and Tutorial Section

The help and tutorial section is a dedicated window or section accessible from the main menu. It offers a searchable help database, user manual, and interactive tutorials on key features. This section provides comprehensive guidance on using the FOCM application effectively.

## 10. File Organization

FOCM provides powerful file organization features to help you manage your files efficiently.

### Automated Organization Rules

You can create customizable rules for automatically organizing files based on file type, date criteria, file name patterns, and file size thresholds. FOCM allows you to specify the target folder structure for organized files, with options to create new folders based on rule criteria, such as date or project name.

### Manual Tagging and Categorization

FOCM supports manual tagging and categorization of files and folders. You can assign custom tags to files and folders manually, providing a flexible way to categorize and locate files quickly. The application offers a tagging interface that suggests existing tags as you type and allows you to create new tags. You can also create custom categories to group files/folders based on project, client, priority, or any other user-defined category.

### Bulk File Operations

FOCM supports bulk operations to rename, move, copy, or delete multiple files at once based on user selection. You can also bulk apply tags or move files to a category. The application provides undo functionality to revert changes if needed.

### Folder and File Management

FOCM allows you to create, rename, move, and delete files and folders from within the application. It provides a drag-and-drop interface for moving files and folders into different categories or locations. The application also includes a feature to detect and resolve duplicate files based on name, size, and optionally content hash. You can choose to keep, delete, or merge duplicate files.

### Custom Folder Views and Sorting

FOCM allows you to customize how folders and files are displayed. You can choose between list, grid, or thumbnail views. The application supports sorting files and folders by name, size, date modified, or custom tags/categories.

### File Watcher and Auto-Update

FOCM implements a file watcher mechanism that automatically updates file organization based on predefined rules when new files are added to monitored folders. This feature works in real-time or at user-defined intervals, ensuring that the organization structure is always up-to-date.

### Integration with File System

FOCM integrates closely with the operating system's file system. It reflects changes made within the app in real-time in the user's file explorer or finder. The application also supports right-click context menu options in the operating system's file explorer, allowing you to quickly tag, categorize, or apply predefined organization rules to selected files or folders.

## 11. Search and Filter

FOCM provides advanced search functionality to help you find files and folders quickly.

### Advanced Search Functionality

You can search for files and folders using partial or full file names. FOCM also supports content-based search capabilities, allowing you to find files containing specific text, even within documents or metadata for images and videos. The application supports regular expressions (regex) in search queries for complex pattern matching.

---

Congratulations! You are now familiar with the main functions of the File Organizer and Content Manager (FOCM) desktop application. Use this manual as a reference to make the most out of FOCM and enhance your file management capabilities. If you have any further questions or need assistance, please refer to the help and tutorial section or contact our support team. Happy organizing!