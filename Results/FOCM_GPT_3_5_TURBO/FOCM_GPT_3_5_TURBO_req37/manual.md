# File Organizer and Content Manager User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a desktop application designed to help users efficiently organize, search, and manage their local files. This software aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. It provides a unified interface for managing digital content, supporting various file types, including documents, images, videos, and more.

## Installation

To install the File Organizer and Content Manager, follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

2. Open a command prompt or terminal window.

3. Navigate to the directory where you have downloaded the FOCM files.

4. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Once the installation is complete, you can launch the FOCM application by running the following command:

   ```
   python main.py
   ```

## Main Window

The main window of the FOCM application serves as the central hub for file organization and management. It features a dual-pane layout, with one pane for the directory tree (folders) and another for viewing the contents of the selected directory.

### Toolbar

The toolbar at the top of the main window provides buttons for common actions. These include creating a new folder, deleting a file, refreshing the view, toggling between list/grid view, and a search bar for performing searches.

### Status Bar

The status bar at the bottom of the main window displays information about the selected files/folders and general statistics, such as the total number of files and total size.

## Search and Filter Panel

The FOCM application includes a dedicated search and filter panel, accessible from the main window. This panel allows users to enter search criteria, choose filters (file type, date modified, size), and display the results in a list or grid format.

### Advanced Search Options

The search and filter panel provides advanced search options for more precise filtering. This includes full-text search within documents, allowing users to find files containing specific text.

## File Preview Window

The FOCM application includes a file preview window that provides a quick preview of the selected file. For text documents and images, the preview is shown within the window. For videos and audio files, basic playback controls are provided.

### Edit Mode

For text files, the file preview window also includes an edit mode, enabling users to make quick edits directly within the preview window.

## File Properties and Metadata Editor

The FOCM application allows users to view and edit detailed information about files and folders through a file properties and metadata editor. This dialog box displays when a user selects "Properties" from the context menu of a file or folder. It shows information such as file size, creation/modification dates, and allows the user to edit metadata tags.

## Settings/Preferences Window

The FOCM application provides a separate settings/preferences window accessible from the main menu. This window allows users to customize application settings, including theme selection (dark/light), default views, file organization rules, backup settings, and extension/plugin management.

## Tag Management Interface

The FOCM application includes a tag management interface for creating, editing, and deleting tags. Users can also assign tags to files or folders from this interface, providing a flexible way to categorize and locate files quickly.

## Backup and Synchronization Setup Wizard

The FOCM application includes a step-by-step wizard that guides users through setting up backup destinations (external drive, cloud storage) and synchronization options, including scheduling automatic backups.

## Help and Tutorial Section

The FOCM application provides a dedicated help and tutorial section accessible from the main menu. This section offers a searchable help database, user manual, and interactive tutorials on key features.

## File Organization

The FOCM application offers both automated and manual file organization features to help users efficiently manage their files.

### Automated Organization Rules

Users can create customizable rules for automatically organizing files based on criteria such as file type, date criteria (creation date, modification date), file name patterns, and file size thresholds. Users can specify the target folder structure for organized files, with options to create new folders based on rule criteria (e.g., date, project name).

### Manual Tagging and Categorization

Users can assign custom tags to files and folders manually. The FOCM application offers a tagging interface that suggests existing tags as the user types and allows the creation of new tags. Users can also create custom categories to group files/folders based on project, client, priority, or any other user-defined category. Files can be viewed and accessed by tags and categories through a dedicated interface or filter.

### Bulk File Operations

The FOCM application supports bulk operations to rename, move, copy, or delete multiple files at once based on user selection. Users can also bulk apply tags or move files to a category, with undo functionality to revert changes if needed.

### Folder and File Management

Users can create, rename, move, and delete files and folders from within the FOCM application. The application provides a drag-and-drop interface for moving files and folders into different categories or locations. It also includes a feature to detect and resolve duplicate files based on name, size, and optionally content hash, with options to keep, delete, or merge duplicate files.

### Custom Folder Views and Sorting

The FOCM application allows users to customize how folders and files are displayed, including list, grid, and thumbnail views. Users can also sort files and folders by name, size, date modified, or custom tags/categories.

### File Watcher and Auto-Update

The FOCM application implements a file watcher mechanism that automatically updates file organization based on predefined rules when new files are added to monitored folders. This feature works in real-time or at user-defined intervals, ensuring the organization structure is always up-to-date.

### Integration with File System

The FOCM application integrates closely with the operating system's file system to reflect changes made within the app in real-time in the user's file explorer or finder. It also supports right-click context menu options in the operating system's file explorer to quickly tag, categorize, or apply predefined organization rules to selected files or folders.

## Search and Filter

The FOCM application provides advanced search functionality to help users find files and folders based on various criteria.

### Partial or Full File Name Search

Users can search for files and folders using partial or full file names.

### Content-Based Search

The FOCM application supports content-based search capabilities, allowing users to find files containing specific text. This includes searching within documents or metadata for images and videos.

### Regular Expressions

The FOCM application supports regular expressions (regex) in search queries for complex pattern matching.

### Custom Search Filters

The FOCM application provides predefined filters to quickly select files based on common criteria such as file type (e.g., documents, images, videos), size (e.g., less than 10MB), and modification or creation date (e.g., last 7 days).

## Conclusion

The File Organizer and Content Manager (FOCM) is a powerful desktop application that helps users efficiently organize, search, and manage their local files. With its automated organization, advanced search capabilities, and content management features, FOCM enhances productivity and simplifies file management. Whether you need to organize files, search for specific content, or customize your file views, FOCM provides a comprehensive solution for all your file management needs.