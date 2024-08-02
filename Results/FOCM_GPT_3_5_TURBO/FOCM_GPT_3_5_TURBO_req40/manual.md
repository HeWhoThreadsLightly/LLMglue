# File Organizer and Content Manager (FOCM) User Manual

## Introduction

Welcome to the user manual for the File Organizer and Content Manager (FOCM) desktop application. FOCM is designed to help you efficiently organize, search, and manage your local files, enhancing productivity and file management through automated organization, advanced search capabilities, and content management features.

This manual will guide you through the installation process, introduce you to the main functions of FOCM, and provide step-by-step instructions on how to use the application effectively.

## Table of Contents

1. Installation
2. Main Window
   - Directory Tree
   - Content View
   - Toolbar
   - Status Bar
3. Search and Filter Panel
   - Basic Search
   - Advanced Search
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
   - Custom Search Filters
   - Tag-Based Searching

## 1. Installation

To install FOCM, follow these steps:

1. Open a terminal or command prompt.
2. Run the following command: `pip install focm`
3. Wait for the installation to complete.

FOCM requires the following dependencies, which will be installed automatically:

- tkinter
- ttk

Once the installation is complete, you can launch FOCM by running the following command: `python main.py`

## 2. Main Window

The main window is the central hub of the FOCM application. It features a dual-pane layout, with one pane for the directory tree (folders) and another for viewing the contents of the selected directory.

### Directory Tree

The directory tree pane displays the file system structure of your local machine. You can navigate through folders by expanding and collapsing the tree nodes. Clicking on a folder will update the content view pane to show the files and subfolders within that folder.

### Content View

The content view pane displays the files and subfolders within the selected directory. You can switch between list and grid view using the toggle view button in the toolbar. The content view supports drag-and-drop functionality for moving files and folders into different categories or locations.

### Toolbar

The toolbar at the top of the main window provides buttons for common actions. These include creating a new folder, deleting a file, refreshing the view, toggling between list and grid view, and performing a search. The search bar allows you to enter search criteria and quickly find files based on file names or other attributes.

### Status Bar

The status bar at the bottom of the main window displays information about the selected files and folders, as well as general statistics such as the total number of files and total size.

## 3. Search and Filter Panel

The search and filter panel is a dedicated panel accessible from the main window. It allows you to enter search criteria, choose filters (file type, date modified, size), and display the results in a list or grid format.

### Basic Search

The basic search functionality allows you to search for files and folders using partial or full file names. Simply enter your search query in the search bar and click the search button. The content view will be updated to show the search results.

### Advanced Search

The advanced search functionality provides more precise filtering options. You can search for files containing specific text within documents or metadata for images and videos. Regular expressions (regex) can also be used for complex pattern matching. Predefined filters are available for common criteria such as file type, size, and modification date. You can also create and save custom filter sets based on any combination of file attributes, including custom tags, project names, or specific content.

## 4. File Preview Window

The file preview window provides a quick preview of the selected file. For text documents and images, the preview is shown within the window. For videos and audio files, basic playback controls are available. Text files can also be edited directly within the preview window.

## 5. File Properties and Metadata Editor

The file properties and metadata editor is a dialog box that displays detailed information about a selected file or folder. It shows file size, creation/modification dates, and allows you to edit metadata tags.

## 6. Settings/Preferences Window

The settings/preferences window is a separate window accessible from the main menu. It allows you to customize application settings, including theme selection (dark/light), default views, file organization rules, backup settings, and extension/plugin management.

## 7. Tag Management Interface

The tag management interface is a panel or window for creating, editing, and deleting tags. You can assign tags to files or folders from this interface, providing a flexible way to categorize and locate files quickly.

## 8. Backup and Synchronization Setup Wizard

The backup and synchronization setup wizard guides you through the process of setting up backup destinations (external drive, cloud storage) and synchronization options. You can schedule automatic backups and choose the files and folders to include.

## 9. Help and Tutorial Section

The help and tutorial section is a dedicated window or section accessible from the main menu. It offers a searchable help database, user manual, and interactive tutorials on key features. You can find answers to common questions and learn how to use the application effectively.

## 10. File Organization

FOCM provides various features for organizing and managing files and folders.

### Automated Organization Rules

You can create customizable rules for automatically organizing files based on file type, date criteria, file name patterns, and file size thresholds. You can specify the target folder structure for organized files and create new folders based on rule criteria such as date or project name.

### Manual Tagging and Categorization

You can assign custom tags to files and folders manually. FOCM offers a tagging interface that suggests existing tags as you type and allows the creation of new tags. You can also create custom categories to group files and folders based on project, client, priority, or any other user-defined category. Files can be viewed and accessed by tags and categories through a dedicated interface or filter.

### Bulk File Operations

FOCM supports bulk operations for renaming, moving, copying, or deleting multiple files at once. You can select multiple files and apply tags or move them to a category in bulk. Undo functionality is available to revert changes if needed.

### Folder and File Management

FOCM allows you to create, rename, move, and delete files and folders from within the application. The drag-and-drop interface makes it easy to move files and folders into different categories or locations. Duplicate files can be detected and resolved based on name, size, and optionally content hash. You can choose to keep, delete, or merge duplicate files.

### Custom Folder Views and Sorting

You can customize how folders and files are displayed in FOCM. List, grid, and thumbnail views are available. Files and folders can be sorted by name, size, date modified, or custom tags/categories.

### File Watcher and Auto-Update

FOCM implements a file watcher mechanism that automatically updates file organization based on predefined rules when new files are added to monitored folders. This feature works in real-time or at user-defined intervals, ensuring that the organization structure is always up-to-date.

### Integration with File System

FOCM integrates closely with the operating system's file system to reflect changes made within the app in real-time in the user's file explorer or finder. Right-click context menu options are available in the operating system's file explorer to quickly tag, categorize, or apply predefined organization rules to selected files or folders.

## 11. Search and Filter

FOCM provides advanced search functionality and custom search filters to help you find files and folders quickly.

### Advanced Search Functionality

You can search for files and folders using partial or full file names. Content-based search capabilities allow you to find files containing specific text, even within documents or metadata for images and videos. Support for regular expressions (regex) is available for complex pattern matching.

### Custom Search Filters

Predefined filters are available to quickly select files based on common criteria such as file type, size, and modification or creation date. You can also create, save, and apply custom filter sets based on any combination of file attributes, including custom tags, project names, or specific content. Integration of a tagging system allows you to assign custom tags to files and folders and then search for these tags. Hierarchical tags are supported to facilitate detailed organization and searching.

## Conclusion

Congratulations! You have completed the user manual for the File Organizer and Content Manager (FOCM) desktop application. You should now have a good understanding of how to install FOCM, navigate the main window, perform searches, preview files, manage file properties, customize settings, organize files and folders, and use the search and filter features effectively.

If you have any further questions or need additional assistance, please refer to the help and tutorial section or contact our support team.

Happy organizing and managing your files with FOCM!