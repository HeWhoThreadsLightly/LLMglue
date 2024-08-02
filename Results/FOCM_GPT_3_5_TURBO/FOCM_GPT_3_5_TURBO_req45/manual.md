# File Organizer and Content Manager User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a desktop application designed to help users efficiently organize, search, and manage their local files. This software aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. It provides a unified interface for managing digital content and supports various file types, including documents, images, videos, and more.

## Installation

To install the File Organizer and Content Manager, follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Open a command prompt or terminal window.

3. Navigate to the directory where you have downloaded or cloned the FOCM project files.

4. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Once the installation is complete, you can launch the application by running the following command:

   ```
   python main.py
   ```

## Main Window

The main window of the File Organizer and Content Manager serves as the central hub of the application. It features a dual-pane layout, with one pane for the directory tree (folders) and another for viewing the contents of the selected directory.

### Toolbar

The toolbar at the top of the main window provides buttons for common actions. These actions include creating a new folder, deleting a file, refreshing the view, toggling between list and grid view, and performing a search.

### Status Bar

The status bar at the bottom of the main window displays information about the selected files/folders and general statistics, such as the total number of files and total size.

## Search and Filter Panel

The File Organizer and Content Manager provides a dedicated panel for searching and filtering files. This panel is accessible from the main window and allows users to enter search criteria, choose filters (file type, date modified, size), and display results in a list or grid format.

### Advanced Search Options

The search and filter panel includes advanced search options for more precise filtering. Users can perform full-text search within documents, enabling them to find files containing specific text.

## File Preview Window

The File Organizer and Content Manager provides a file preview window that allows users to quickly preview the selected file. For text documents and images, the preview is shown within the window. For videos and audio files, basic playback controls are provided.

### Edit Mode

For text files, the file preview window includes an edit mode that enables users to make quick edits directly within the preview window.

## File Properties and Metadata Editor

The File Organizer and Content Manager includes a file properties and metadata editor. This dialog box displays detailed information about a file or folder, including file size, creation/modification dates, and allows the user to edit metadata tags.

## Settings/Preferences Window

The File Organizer and Content Manager provides a separate settings/preferences window that allows users to customize application settings. This includes theme selection (dark/light), default views, file organization rules, backup settings, and extension/plugin management.

## Tag Management Interface

The File Organizer and Content Manager includes a tag management interface. This panel or window allows users to create, edit, and delete tags. Users can also assign tags to files or folders from this interface, providing a flexible way to categorize and locate files quickly.

## Backup and Synchronization Setup Wizard

The File Organizer and Content Manager provides a step-by-step wizard that guides users through setting up backup destinations (external drive, cloud storage) and synchronization options, including scheduling automatic backups.

## Help and Tutorial Section

The File Organizer and Content Manager includes a dedicated help and tutorial section. This window or section is accessible from the main menu and offers a searchable help database, user manual, and interactive tutorials on key features.

## File Organization

The File Organizer and Content Manager offers various features for file organization.

### Automated Organization Rules

Users can create customizable rules for automatically organizing files based on file type, date criteria (creation date, modification date), file name patterns, and file size thresholds. Users can specify the target folder structure for organized files, with options to create new folders based on rule criteria (e.g., date, project name).

### Manual Tagging and Categorization

Users can assign custom tags to files and folders manually. The application offers a tagging interface that suggests existing tags as the user types and allows the creation of new tags. Users can also create custom categories to group files/folders based on project, client, priority, or any other user-defined category. Files can be viewed and accessed by tags and categories through a dedicated interface or filter.

### Bulk File Operations

The File Organizer and Content Manager supports bulk operations to rename, move, copy, or delete multiple files at once based on user selection. Users can also bulk apply tags or move files to a category, with undo functionality to revert changes if needed.

### Folder and File Management

Users can create, rename, move, and delete files and folders from within the application. The application provides a drag-and-drop interface for moving files and folders into different categories or locations. It also includes a feature to detect and resolve duplicate files based on name, size, and optionally content hash. Users can choose to keep, delete, or merge duplicate files.

### Custom Folder Views and Sorting

Users can customize how folders and files are displayed in the File Organizer and Content Manager. They can choose between list, grid, and thumbnail views. The application also supports sorting files and folders by name, size, date modified, or custom tags/categories.

### File Watcher and Auto-Update

The File Organizer and Content Manager implements a file watcher mechanism that automatically updates file organization based on predefined rules when new files are added to monitored folders. This feature works in real-time or at user-defined intervals, ensuring the organization structure is always up-to-date.

### Integration with File System

The File Organizer and Content Manager integrates closely with the operating system's file system. It reflects changes made within the app in real-time in the user's file explorer or finder. It also supports right-click context menu options in the operating system's file explorer to quickly tag, categorize, or apply predefined organization rules to selected files or folders.

## Search and Filter

The File Organizer and Content Manager provides advanced search functionality to help users find files and folders.

### Partial and Full-Text Search

Users can search for files and folders using partial or full file names. The application also supports content-based search capabilities, allowing users to find files containing specific text, even within documents or metadata for images and videos.

### Regular Expressions

The search functionality in the File Organizer and Content Manager supports regular expressions (regex) in search queries for complex pattern matching.

### Custom Search Filters

The application includes predefined filters to quickly select files based on common criteria such as file type, size, and modification or creation date. Users can also create, save, and apply custom filter sets based on any combination of file attributes, including custom tags, project names, or specific content.

### Tag-Based Searching

The File Organizer and Content Manager integrates a tagging system where users can assign custom tags to files and folders. Users can then search for these tags to quickly locate files. The application supports hierarchical tags to facilitate detailed organization and searching.

### Search History and Saved Searches

The File Organizer and Content Manager automatically saves recent searches for quick repetition. Users can also save frequently used search queries or filters for quick access.

### Search Results Management

Search results in the File Organizer and Content Manager are sortable based on various criteria such as name, size, date modified, and custom tags. Users can export search results to CSV or other formats for external use. Batch operations on search results are also supported, allowing users to apply actions (move, delete, tag) to multiple files at once.

## Conclusion

The File Organizer and Content Manager provides a comprehensive set of features for efficient file organization, search, and management. With its automated organization rules, manual tagging and categorization, and advanced search capabilities, users can easily organize and find their files, enhancing productivity and file management.