# File Organizer and Content Manager User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a desktop application designed to help users efficiently organize, search, and manage their local files. This software aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. It provides a unified interface for managing digital content, supporting various file types, including documents, images, videos, and more.

## Installation

To use the File Organizer and Content Manager, you need to follow these steps:

1. Install Python: FOCM is developed using Python programming language. You can download and install Python from the official website: https://www.python.org/downloads/

2. Install dependencies: FOCM requires the following dependencies to be installed. You can install them using the provided `requirements.txt` file.

   ```
   pip install -r requirements.txt
   ```

3. Download the FOCM source code: You can download the source code from the provided repository: [FOCM Repository](https://github.com/your-repository)

4. Run the application: Open a terminal or command prompt, navigate to the downloaded source code directory, and run the following command:

   ```
   python main.py
   ```

   This will start the FOCM application.

## Main Window

The main window of the FOCM application serves as the central hub for file organization and content management. It features a dual-pane layout, with one pane for the directory tree (folders) and another for viewing the contents of the selected directory.

### Toolbar

The toolbar at the top of the main window provides buttons for common actions. These actions include creating a new folder, deleting a file, refreshing the view, toggling between list and grid view, and a search bar for performing searches.

### Status Bar

The status bar at the bottom of the main window displays information about the selected files/folders and general statistics, such as the total number of files and total size.

## Search and Filter Panel

FOCM provides a dedicated panel accessible from the main window for entering search criteria, choosing filters (file type, date modified, size), and displaying results in a list or grid format. The search and filter panel also includes advanced search options for more precise filtering, including full-text search within documents.

## File Preview Window

FOCM provides a file preview window that can be accessed as a pop-up or sidebar window. The file preview window allows users to quickly preview the selected file. For text documents and images, the preview is shown within the window. For videos and audio files, basic playback controls are provided.

The file preview window also includes an edit mode for text files, enabling users to make quick edits directly within the preview window.

## File Properties and Metadata Editor

FOCM includes a file properties and metadata editor that can be accessed by selecting "Properties" from the context menu of a file or folder. The file properties and metadata editor displays detailed information about the file, including file size, creation/modification dates, and allows the user to edit metadata tags.

## Settings/Preferences Window

FOCM provides a separate settings/preferences window accessible from the main menu. This window allows users to customize application settings, including theme selection (dark/light), default views, file organization rules, backup settings, and extension/plugin management.

## Tag Management Interface

FOCM includes a tag management interface that allows users to create, edit, and delete tags. Users can also assign tags to files or folders from this interface, providing a flexible way to categorize and locate files quickly.

## Backup and Synchronization Setup Wizard

FOCM provides a step-by-step wizard that guides users through setting up backup destinations (external drive, cloud storage) and synchronization options, including scheduling automatic backups.

## Help and Tutorial Section

FOCM includes a dedicated window or section accessible from the main menu, offering a searchable help database, user manual, and interactive tutorials on key features. This section provides comprehensive guidance on how to use the application effectively.

## File Organization

FOCM offers various file organization features to help users efficiently manage their files.

### Automated Organization Rules

FOCM allows users to create customizable rules for automatically organizing files. These rules can be based on file type, date criteria (creation date, modification date), file name patterns (using wildcards or regular expressions), and file size thresholds. Users can specify the target folder structure for organized files, with options to create new folders based on rule criteria, such as date or project name.

### Manual Tagging and Categorization

FOCM allows users to assign custom tags to files and folders manually. The application offers a tagging interface that suggests existing tags as the user types and allows the creation of new tags. Users can also create custom categories to group files/folders based on project, client, priority, or any other user-defined category. Files can be viewed and accessed by tags and categories through a dedicated interface or filter.

### Bulk File Operations

FOCM supports bulk operations to rename, move, copy, or delete multiple files at once based on user selection. It includes options for bulk applying tags or moving files to a category, with undo functionality to revert changes if needed.

### Folder and File Management

FOCM allows users to create, rename, move, and delete files and folders from within the application. It provides a drag-and-drop interface for moving files and folders into different categories or locations. The application also includes a feature to detect and resolve duplicate files based on name, size, and optionally content hash, with options to keep, delete, or merge duplicate files.

### Custom Folder Views and Sorting

FOCM allows users to customize how folders and files are displayed, including list, grid, and thumbnail views. It supports sorting files and folders by name, size, date modified, or custom tags/categories.

### File Watcher and Auto-Update

FOCM implements a file watcher mechanism that automatically updates file organization based on predefined rules when new files are added to monitored folders. This feature works in real-time or at user-defined intervals, ensuring the organization structure is always up-to-date.

### Integration with File System

FOCM integrates closely with the operating system's file system to reflect changes made within the app in real-time in the user's file explorer or finder. It supports right-click context menu options in the operating system's file explorer to quickly tag, categorize, or apply predefined organization rules to selected files or folders.

## Search and Filter

FOCM provides advanced search functionality to help users find files and folders efficiently.

### Advanced Search Functionality

FOCM allows users to search for files and folders using partial or full file names. It also supports content-based search capabilities that enable users to find files containing specific text, even within documents or metadata for images and videos. The application supports regular expressions (regex) in search queries for complex pattern matching.

### Custom Search Filters

FOCM offers predefined filters to quickly select files based on common criteria, such as file type, size, and modification or creation date. Users can also create, save, and apply custom filter sets based on any combination of file attributes, including custom tags, project names, or specific content.

### Tag-Based Searching

FOCM integrates a tagging system where users can assign custom tags to files and folders. Users can then search for files based on these tags. The application supports hierarchical tags to facilitate detailed organization and searching.

### Search History and Saved Searches

FOCM automatically saves recent searches for quick repetition. Users can also save frequently used search queries or filters for quick access.

### Search Results Management

FOCM provides sortable search results based on various criteria, such as name, size, date modified, and custom tags. Users can export search results to CSV or other formats for external use. Batch operations on search results are also supported, allowing users to apply actions (move, delete, tag) to multiple files at once.

### Contextual Actions

FOCM offers a right-click context menu in search results to provide quick access to common file operations, such as open, rename, delete, move, or edit tags. It also includes a preview option directly in the context menu for images, documents, and videos.

### Smart Suggestions

As users type in the search bar, FOCM offers smart suggestions based on their input, historical searches, and commonly accessed files. This feature helps users find files more efficiently.

## Conclusion

The File Organizer and Content Manager (FOCM) provides a comprehensive set of features to help users efficiently organize, search, and manage their local files. With its automated organization rules, manual tagging and categorization, file management capabilities, and advanced search functionality, FOCM aims to enhance productivity and simplify file management tasks. By following this user manual, you can make the most out of the FOCM application and effectively manage your digital content.