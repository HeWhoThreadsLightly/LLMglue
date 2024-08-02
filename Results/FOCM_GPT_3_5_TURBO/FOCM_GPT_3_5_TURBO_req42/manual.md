# File Organizer and Content Manager User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a desktop application designed to help users efficiently organize, search, and manage their local files. This software aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. It provides a unified interface for managing digital content, supporting various file types, including documents, images, videos, and more.

## Installation

To install the File Organizer and Content Manager, follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

2. Clone or download the FOCM repository from GitHub: [FOCM Repository](https://github.com/your-repository-link)

3. Open a terminal or command prompt and navigate to the FOCM directory.

4. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

5. Once the dependencies are installed, you can launch the application by running the following command:

   ```
   python main.py
   ```

## Main Window

The main window of the File Organizer and Content Manager serves as the central hub of the application. It features a dual-pane layout, with one pane for the directory tree (folders) and another for viewing the contents of the selected directory.

### Toolbar

At the top of the main window, you will find a toolbar with buttons for common actions. The toolbar includes the following buttons:

- **New Folder**: Click this button to create a new folder in the selected directory.
- **Delete File**: Click this button to delete the selected file.
- **Refresh View**: Click this button to refresh the view and update the directory tree and content view.
- **Toggle View**: Click this button to toggle between list and grid view in the content view.
- **Search Bar**: Enter your search query in the search bar and click the search button to perform a search.

### Status Bar

At the bottom of the main window, you will find a status bar that displays information about the selected files/folders and general statistics, such as the total number of files and total size.

## Search and Filter Panel

The File Organizer and Content Manager provides a dedicated search and filter panel, accessible from the main window. This panel allows you to enter search criteria, choose filters (file type, date modified, size), and display the results in a list or grid format.

### Advanced Search Options

The search and filter panel includes advanced search options for more precise filtering. You can perform a full-text search within documents, allowing you to find files containing specific text.

### File Preview Window

When you select a file in the content view, a file preview window will appear. For text documents and images, the preview will be displayed within the window. For videos and audio files, basic playback controls will be provided.

### Edit Mode for Text Files

For text files, you can enter edit mode in the file preview window. This allows you to make quick edits directly within the preview window.

### File Properties and Metadata Editor

To view detailed information about a file or folder, right-click on it and select "Properties" from the context menu. A dialog box will appear, showing information such as file size, creation/modification dates. You can also edit metadata tags in this dialog box.

## Settings/Preferences Window

The File Organizer and Content Manager provides a separate settings/preferences window, accessible from the main menu. In this window, you can customize various application settings, including theme selection (dark/light), default views, file organization rules, backup settings, and extension/plugin management.

## Tag Management Interface

The File Organizer and Content Manager includes a tag management interface. This interface allows you to create, edit, and delete tags. You can also assign tags to files or folders from this interface, providing a flexible way to categorize and locate files quickly.

## Backup and Synchronization Setup Wizard

The File Organizer and Content Manager includes a step-by-step wizard that guides you through setting up backup destinations (external drive, cloud storage) and synchronization options. This wizard allows you to schedule automatic backups and ensure your files are always up-to-date.

## Help and Tutorial Section

The File Organizer and Content Manager provides a dedicated help and tutorial section, accessible from the main menu. In this section, you can access a searchable help database, user manual, and interactive tutorials on key features.

## File Organization

The File Organizer and Content Manager offers various file organization features to help you manage your files effectively.

### Automated Organization Rules

You can create customizable rules for automatically organizing files based on file type, date criteria, file name patterns, and file size thresholds. You can specify the target folder structure for organized files and create new folders based on rule criteria.

### Manual Tagging and Categorization

You can assign custom tags to files and folders manually. The application offers a tagging interface that suggests existing tags as you type and allows the creation of new tags. You can also create custom categories to group files/folders based on project, client, priority, or any other user-defined category.

### Bulk File Operations

The File Organizer and Content Manager supports bulk operations to rename, move, copy, or delete multiple files at once. You can also bulk apply tags or move files to a category. The application provides undo functionality to revert changes if needed.

### Folder and File Management

You can create, rename, move, and delete files and folders from within the application. The application also provides a drag-and-drop interface for moving files and folders into different categories or locations. It includes a feature to detect and resolve duplicate files based on name, size, and optionally content hash.

### Custom Folder Views and Sorting

The File Organizer and Content Manager allows you to customize how folders and files are displayed. You can choose between list, grid, and thumbnail views. It also supports sorting files and folders by name, size, date modified, or custom tags/categories.

### File Watcher and Auto-Update

The File Organizer and Content Manager implements a file watcher mechanism that automatically updates file organization based on predefined rules when new files are added to monitored folders. This feature works in real-time or at user-defined intervals, ensuring the organization structure is always up-to-date.

### Integration with File System

The File Organizer and Content Manager integrates closely with the operating system's file system. It reflects changes made within the app in real-time in the user's file explorer or finder. It also supports right-click context menu options in the operating system's file explorer to quickly tag, categorize, or apply predefined organization rules to selected files or folders.

## Search and Filter

The File Organizer and Content Manager provides advanced search functionality to help you find files and folders quickly.

### Advanced Search Functionality

You can search for files and folders using partial or full file names. The application also supports content-based search capabilities, allowing you to find files containing specific text, even within documents or metadata for images and videos. It also supports regular expressions (regex) in search queries for complex pattern matching.

### Custom Search Filters

The File Organizer and Content Manager offers predefined filters to quickly select files based on common criteria such as file type, size, and modification or creation date. You can also create, save, and apply custom filter sets based on any combination of file attributes, including custom tags, project names, or specific content.

### Tag-Based Searching

The File Organizer and Content Manager integrates a tagging system where you can assign custom tags to files and folders. You can then search for files based on these tags. It also supports hierarchical tags to facilitate detailed organization and searching.

### Search History and Saved Searches

The File Organizer and Content Manager automatically saves recent searches for quick repetition. You can also save frequently used search queries or filters for quick access.

## Conclusion

The File Organizer and Content Manager provides a comprehensive set of features to help you efficiently organize, search, and manage your local files. With its automated organization, advanced search capabilities, and content management features, it aims to enhance your productivity and file management experience. Enjoy using the File Organizer and Content Manager and make the most out of your digital content!