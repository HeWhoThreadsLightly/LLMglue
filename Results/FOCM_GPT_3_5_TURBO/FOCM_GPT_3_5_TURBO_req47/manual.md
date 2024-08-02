# File Organizer and Content Manager User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a desktop application designed to help users efficiently organize, search, and manage their local files. This software aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. It provides a unified interface for managing digital content and supports various file types, including documents, images, videos, and more.

## Installation

To install the File Organizer and Content Manager, follow these steps:

1. Ensure that you have Python installed on your system. You can download Python from the official website: https://www.python.org/downloads/

2. Open a terminal or command prompt and navigate to the directory where you want to install the application.

3. Clone the repository by running the following command:

   ```
   git clone https://github.com/your-username/focm.git
   ```

4. Change into the cloned directory:

   ```
   cd focm
   ```

5. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

6. Once the installation is complete, you can launch the application by running the following command:

   ```
   python main.py
   ```

## Main Window

The main window of the File Organizer and Content Manager serves as the central hub of the application. It features a dual-pane layout, with one pane for the directory tree (folders) and another for viewing the contents of the selected directory.

### Toolbar

At the top of the main window, you will find a toolbar with buttons for common actions. These buttons include:

- **New Folder**: Create a new folder in the selected directory.
- **Delete File**: Delete the selected file.
- **Refresh View**: Refresh the view to reflect any changes in the file system.
- **Toggle View**: Switch between list and grid view for the content pane.
- **Search Bar**: Enter search criteria to perform a search.

### Status Bar

At the bottom of the main window, you will find a status bar that displays information about the selected files/folders and general statistics, such as the total number of files and total size.

## Search and Filter Panel

The File Organizer and Content Manager provides a dedicated panel for searching and filtering files. This panel is accessible from the main window and allows users to enter search criteria, choose filters (file type, date modified, size), and display results in a list or grid format.

### Advanced Search Options

The search and filter panel includes advanced search options for more precise filtering. These options allow users to perform full-text search within documents and use regular expressions for complex pattern matching.

## File Preview Window

When a file is selected in the content pane, the File Organizer and Content Manager provides a file preview window. This window can be a pop-up or a sidebar window and provides a quick preview of the selected file. For text documents and images, the preview is shown within the window. For videos and audio files, basic playback controls are provided.

### Edit Mode

For text files, the file preview window includes an edit mode that allows users to make quick edits directly within the preview window. This feature enables users to modify text files without opening a separate text editor.

## File Properties and Metadata Editor

The File Organizer and Content Manager includes a file properties and metadata editor. This editor is accessible from the context menu of a file or folder and displays detailed information about the selected item, such as file size, creation/modification dates. It also allows users to edit metadata tags associated with the file.

## Settings/Preferences Window

The File Organizer and Content Manager provides a separate window for customizing application settings. This window is accessible from the main menu and allows users to customize various aspects of the application, including theme selection (dark/light), default views, file organization rules, backup settings, and extension/plugin management.

## Tag Management Interface

To facilitate flexible categorization and quick file retrieval, the File Organizer and Content Manager includes a tag management interface. This interface allows users to create, edit, and delete tags. Users can also assign tags to files or folders directly from this interface.

## Backup and Synchronization Setup Wizard

The File Organizer and Content Manager includes a step-by-step wizard that guides users through setting up backup destinations (external drive, cloud storage) and synchronization options. This wizard allows users to schedule automatic backups and ensures that files are always up-to-date.

## Help and Tutorial Section

To assist users in understanding and using the File Organizer and Content Manager effectively, the application provides a dedicated help and tutorial section. This section is accessible from the main menu and offers a searchable help database, user manual, and interactive tutorials on key features.

## File Organization

The File Organizer and Content Manager offers various features to help users organize their files effectively.

### Automated Organization Rules

Users can create customizable rules for automatically organizing files based on file type, date criteria, file name patterns, and file size thresholds. These rules allow users to specify the target folder structure for organized files and create new folders based on rule criteria, such as date or project name.

### Manual Tagging and Categorization

Users can assign custom tags to files and folders manually. The application offers a tagging interface that suggests existing tags as the user types and allows the creation of new tags. Users can also create custom categories to group files/folders based on project, client, priority, or any other user-defined category.

### Bulk File Operations

The File Organizer and Content Manager supports bulk operations for renaming, moving, copying, or deleting multiple files at once. Users can select multiple files and apply actions, such as applying tags or moving files to a category, in bulk. The application also provides an undo functionality to revert changes if needed.

### Folder and File Management

Users can create, rename, move, and delete files and folders directly from within the application. The application provides a drag-and-drop interface for moving files and folders into different categories or locations. It also includes a feature to detect and resolve duplicate files based on name, size, and optionally content hash, with options to keep, delete, or merge duplicate files.

### Custom Folder Views and Sorting

The File Organizer and Content Manager allows users to customize how folders and files are displayed. Users can choose between list, grid, and thumbnail views. The application also supports sorting files and folders by name, size, date modified, or custom tags/categories.

### File Watcher and Auto-Update

The File Organizer and Content Manager implements a file watcher mechanism that automatically updates file organization based on predefined rules when new files are added to monitored folders. This feature works in real-time or at user-defined intervals, ensuring that the organization structure is always up-to-date.

### Integration with File System

The File Organizer and Content Manager integrates closely with the operating system's file system. It reflects changes made within the application in real-time in the user's file explorer or finder. The application also supports right-click context menu options in the operating system's file explorer, allowing users to quickly tag, categorize, or apply predefined organization rules to selected files or folders.

## Search and Filter

The File Organizer and Content Manager provides advanced search functionality to help users find files and folders quickly.

### Advanced Search Functionality

Users can search for files and folders using partial or full file names. The application also supports content-based search capabilities, allowing users to find files containing specific text, even within documents or metadata for images and videos. Advanced search functionality includes support for regular expressions (regex) in search queries for complex pattern matching.

### Custom Search Filters

The application offers predefined filters to quickly select files based on common criteria, such as file type, size, and modification or creation date. Users can also create, save, and apply custom filter sets based on any combination of file attributes, including custom tags, project names, or specific content.

### Tag-Based Searching

The File Organizer and Content Manager integrates a tagging system that allows users to assign custom tags to files and folders. Users can then search for files based on these tags. The application supports hierarchical tags to facilitate detailed organization and searching.

### Search History and Saved Searches

The File Organizer and Content Manager automatically saves recent searches for quick repetition. Users can also save frequently used search queries or filters for quick access. This feature helps users to streamline their search process and save time.

### Search Results Management

Search results in the File Organizer and Content Manager are sortable based on various criteria, such as name, size, date modified, and custom tags. Users can export search results to CSV or other formats for external use. Batch operations on search results allow users to apply actions, such as moving, deleting, or tagging, to multiple files at once. Contextual actions in the search results context menu provide quick access to common file operations, such as open, rename, delete, move, or edit tags. The context menu also includes a preview option for images, documents, and videos.

## Conclusion

The File Organizer and Content Manager is a powerful desktop application that helps users efficiently organize, search, and manage their local files. With its automated organization, advanced search capabilities, and content management features, it enhances productivity and simplifies file management. By following this user manual, you can make the most of the File Organizer and Content Manager and streamline your file organization and search processes.