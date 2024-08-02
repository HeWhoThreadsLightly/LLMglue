# File Organizer and Content Manager User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a desktop application designed to help users efficiently organize, search, and manage their local files. This software aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. It provides a unified interface for managing digital content and supports various file types, including documents, images, videos, and more.

## Installation

To install the File Organizer and Content Manager, follow these steps:

1. Ensure that you have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

2. Open a command prompt or terminal window.

3. Navigate to the directory where you have downloaded the File Organizer and Content Manager files.

4. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Once the installation is complete, you can launch the File Organizer and Content Manager by running the following command:

   ```
   python main.py
   ```

## Main Window

The main window of the File Organizer and Content Manager serves as the central hub of the application. It features a dual-pane layout, with one pane for the directory tree (folders) and another for viewing the contents of the selected directory.

### Toolbar

At the top of the main window, you will find a toolbar with buttons for common actions. These actions include creating a new folder, deleting a file, refreshing the view, toggling between list/grid view, and searching for files.

### Status Bar

At the bottom of the main window, there is a status bar that displays information about the selected files/folders and general statistics, such as the total number of files and total size.

## Search and Filter Panel

The File Organizer and Content Manager provides a dedicated panel for searching and filtering files. This panel is accessible from the main window and allows users to enter search criteria, choose filters (file type, date modified, size), and display results in a list or grid format.

### Advanced Search Options

The search and filter panel offers advanced search options for more precise filtering. This includes full-text search within documents, allowing users to find files containing specific text.

## File Preview Window

When a file is selected in the main window, a file preview window will appear. For text documents and images, the preview will be shown within the window. For videos and audio files, basic playback controls will be provided.

### Edit Mode

For text files, the file preview window also includes an edit mode. This enables users to make quick edits directly within the preview window.

## File Properties and Metadata Editor

The File Organizer and Content Manager allows users to view and edit file properties and metadata. By selecting "Properties" from the context menu of a file or folder, a dialog box will appear. This dialog box shows detailed information about the file, including file size, creation/modification dates, and allows the user to edit metadata tags.

## Settings/Preferences Window

The File Organizer and Content Manager provides a separate window accessible from the main menu for customizing application settings. In this window, users can customize various settings, including theme selection (dark/light), default views, file organization rules, backup settings, and extension/plugin management.

## Tag Management Interface

To facilitate flexible file categorization and quick file location, the File Organizer and Content Manager includes a tag management interface. This interface allows users to create, edit, and delete tags. Users can also assign tags to files or folders directly from this interface.

## Backup and Synchronization Setup Wizard

The File Organizer and Content Manager features a step-by-step wizard that guides users through setting up backup destinations (external drive, cloud storage) and synchronization options. This includes scheduling automatic backups to ensure data safety.

## Help and Tutorial Section

For assistance and guidance on using the File Organizer and Content Manager, a dedicated help and tutorial section is accessible from the main menu. This section offers a searchable help database, user manual, and interactive tutorials on key features.

## File Organization

The File Organizer and Content Manager provides various features for file organization, including automated organization rules, manual tagging and categorization, bulk file operations, folder and file management, and duplicate file detection and resolution.

### Automated Organization Rules

Users can create customizable rules for automatically organizing files based on file type, date criteria, file name patterns, and file size thresholds. Users can specify the target folder structure for organized files, with options to create new folders based on rule criteria.

### Manual Tagging and Categorization

Users can assign custom tags to files and folders manually. The application offers a tagging interface that suggests existing tags as the user types and allows the creation of new tags. Users can also create custom categories to group files/folders based on project, client, priority, or any other user-defined category.

### Bulk File Operations

The File Organizer and Content Manager supports bulk operations for renaming, moving, copying, or deleting multiple files at once. Users can also apply tags or move files to a category in bulk, with undo functionality to revert changes if needed.

### Folder and File Management

Users can create, rename, move, and delete files and folders directly within the application. The application provides a drag-and-drop interface for moving files and folders into different categories or locations.

### Duplicate File Detection and Resolution

The File Organizer and Content Manager includes a feature to detect and resolve duplicate files based on name, size, and optionally content hash. Users can choose to keep, delete, or merge duplicate files.

### Custom Folder Views and Sorting

Users can customize how folders and files are displayed in the File Organizer and Content Manager. This includes options for list, grid, and thumbnail views. The application also supports sorting files and folders by name, size, date modified, or custom tags/categories.

### File Watcher and Auto-Update

The File Organizer and Content Manager implements a file watcher mechanism that automatically updates file organization based on predefined rules when new files are added to monitored folders. This feature works in real-time or at user-defined intervals, ensuring the organization structure is always up-to-date.

### Integration with File System

The File Organizer and Content Manager integrates closely with the operating system's file system. This integration reflects changes made within the app in real-time in the user's file explorer or finder. The application also supports right-click context menu options in the operating system's file explorer for quick tagging, categorization, or application of predefined organization rules to selected files or folders.

## Search and Filter

The File Organizer and Content Manager provides advanced search functionality to help users find files and folders quickly.

### Advanced Search Functionality

Users can search for files and folders using partial or full file names. The application also supports content-based search capabilities, allowing users to find files containing specific text, even within documents or metadata for images and videos. Additionally, the application supports regular expressions (regex) in search queries for complex pattern matching.

### Custom Search Filters

The File Organizer and Content Manager offers predefined filters to quickly select files based on common criteria such as file type, size, and modification or creation date. Users can also create, save, and apply custom filter sets based on any combination of file attributes, including custom tags, project names, or specific content.

### Tag-Based Searching

The File Organizer and Content Manager integrates a tagging system where users can assign custom tags to files and folders. Users can then search for files based on these tags. The application also supports hierarchical tags to facilitate detailed organization and searching.

### Search History and Saved Searches

The File Organizer and Content Manager automatically saves recent searches for quick repetition. Users can also save frequently used search queries or filters for quick access.

### Search Results Management

Search results in the File Organizer and Content Manager are sortable based on various criteria such as name, size, date modified, and custom tags. Users can export search results to CSV or other formats for external use. Additionally, batch operations are available on search results, allowing users to apply actions (e.g., move, delete, tag) to multiple files at once.

### Contextual Actions

The File Organizer and Content Manager provides a right-click context menu in search results for quick access to common file operations such as open, rename, delete, move, or edit tags. The context menu also includes a preview option for images, documents, and videos.

### Smart Suggestions

As users type in the search bar, the File Organizer and Content Manager offers smart suggestions based on their input, historical searches, and commonly accessed files. These suggestions can include tags, filenames, and content snippets as possible search queries.

### Integration with File Organization

The File Organizer and Content Manager seamlessly integrates with the file organization system. This allows users to quickly organize search results into folders or tag groups directly from the search interface.

## Additional Features

The File Organizer and Content Manager includes additional features for content management. This includes preview capabilities for common file types such as PDF, DOCX, images, and videos directly within the application.

## Conclusion

The File Organizer and Content Manager is a powerful desktop application that helps users efficiently organize, search, and manage their local files. With its automated organization, advanced search capabilities, and content management features, users can enhance their productivity and streamline their file management tasks.