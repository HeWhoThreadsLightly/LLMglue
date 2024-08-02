# File Organizer and Content Manager User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a desktop application designed to help users efficiently organize, search, and manage their local files. This software aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. It provides a unified interface for managing digital content, supporting various file types including documents, images, videos, and more.

## Installation

To install the File Organizer and Content Manager, follow these steps:

1. Ensure that you have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

2. Open a command prompt or terminal window.

3. Navigate to the directory where you have downloaded the FOCM files.

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

At the top of the main window, you will find a toolbar with buttons for common actions. These include:

- Create New Folder: Click this button to create a new folder in the selected directory.
- Delete File: Click this button to delete the selected file.
- Refresh View: Click this button to refresh the view and update the directory tree and content view.
- Toggle View: Click this button to toggle between list and grid view in the content view.
- Search Bar: Enter search criteria in the search bar and click the Search button to perform a search.

### Status Bar

At the bottom of the main window, you will find a status bar that displays information about the selected files/folders and general statistics, such as the total number of files and total size.

## Search and Filter Panel

The File Organizer and Content Manager provides a dedicated panel for searching and filtering files. This panel is accessible from the main window.

### Basic Search

In the search and filter panel, you can enter search criteria to find files that match specific attributes. You can choose filters such as file type, date modified, and size. The search results can be displayed in a list or grid format.

### Advanced Search

The application also offers advanced search options for more precise filtering. This includes full-text search within documents, allowing you to find files that contain specific text.

## File Preview Window

When you select a file in the content view, you can open a file preview window. This window provides a quick preview of the selected file. For text documents and images, the preview is shown within the window. For videos and audio files, basic playback controls are provided.

### Edit Mode

For text files, you can enter edit mode within the file preview window. This enables you to make quick edits directly within the preview window, saving you time and effort.

## File Properties and Metadata Editor

The File Organizer and Content Manager allows you to view and edit detailed information about files and folders. When you select a file or folder and right-click, you can choose the "Properties" option from the context menu. This will open a dialog box that displays information such as file size, creation/modification dates, and metadata tags. You can edit the metadata tags to further organize your files.

## Settings/Preferences Window

The application provides a separate window accessible from the main menu for customizing application settings. In this window, you can choose the theme (dark/light), default views, file organization rules, backup settings, and manage extensions/plugins.

## Tag Management Interface

To provide a flexible way to categorize and locate files quickly, the File Organizer and Content Manager offers a tag management interface. This interface allows you to create, edit, and delete tags. You can also assign tags to files or folders directly from this interface.

## Backup and Synchronization Setup Wizard

To ensure the safety of your files, the application includes a step-by-step wizard for setting up backup destinations and synchronization options. You can choose external drives or cloud storage as backup destinations and schedule automatic backups.

## Help and Tutorial Section

The File Organizer and Content Manager provides a dedicated window or section accessible from the main menu for accessing help and tutorials. This includes a searchable help database, user manual, and interactive tutorials on key features. If you have any questions or need assistance, this section will provide the necessary guidance.

## File Organization

The File Organizer and Content Manager offers various features for organizing files.

### Automated Organization Rules

You can create customizable rules for automatically organizing files based on criteria such as file type, date modified, file name patterns, and file size thresholds. These rules allow you to specify the target folder structure for organized files, with options to create new folders based on rule criteria.

### Manual Tagging and Categorization

You can manually assign custom tags to files and folders. The application offers a tagging interface that suggests existing tags as you type and allows the creation of new tags. You can also create custom categories to group files/folders based on project, client, priority, or any other user-defined category. The application provides a dedicated interface or filter to view and access files by tags and categories.

### Bulk File Operations

The application supports bulk operations to rename, move, copy, or delete multiple files at once based on user selection. You can also apply tags or move files to a category in bulk. The application includes an undo functionality to revert changes if needed.

### Folder and File Management

You can create, rename, move, and delete files and folders directly from within the application. The application provides a drag-and-drop interface for easy file and folder management. It also includes a feature to detect and resolve duplicate files based on name, size, and optionally content hash. You can choose to keep, delete, or merge duplicate files.

### Custom Folder Views and Sorting

The File Organizer and Content Manager allows you to customize how folders and files are displayed. You can choose between list, grid, and thumbnail views. The application also supports sorting files and folders by name, size, date modified, or custom tags/categories.

### File Watcher and Auto-Update

To keep your file organization up-to-date, the application implements a file watcher mechanism. This mechanism automatically updates file organization based on predefined rules when new files are added to monitored folders. You can configure the file watcher to work in real-time or at user-defined intervals.

### Integration with File System

The application integrates closely with the operating system's file system. This ensures that changes made within the application are reflected in real-time in the user's file explorer or finder. The application also supports right-click context menu options in the operating system's file explorer. This allows you to quickly tag, categorize, or apply predefined organization rules to selected files or folders.

## Search and Filter

The File Organizer and Content Manager provides advanced search functionality to help you find files and folders quickly.

### Basic Search

You can search for files and folders using partial or full file names. The application allows you to enter search queries and displays the matching results.

### Content-Based Search

The application supports content-based search capabilities. This means you can find files that contain specific text, even within documents or metadata for images and videos.

### Regular Expressions

For complex pattern matching, the application supports regular expressions (regex) in search queries. This allows you to perform advanced searches based on complex patterns.

### Custom Search Filters

The application offers predefined filters to quickly select files based on common criteria such as file type, size, and modification or creation date. Additionally, you can create, save, and apply custom filter sets based on any combination of file attributes, including custom tags, project names, or specific content.

### Tag-Based Searching

To facilitate detailed organization and searching, the application integrates a tagging system. You can assign custom tags to files and folders and then search for these tags. The application supports hierarchical tags, allowing you to create a structured hierarchy for better organization and searching.

### Search History and Saved Searches

The application automatically saves recent searches for quick repetition. You can also save frequently used search queries or filters for quick access.

### Search Results Management

The search results are displayed in a sortable manner based on various criteria such as name, size, date modified, and custom tags. You can export search results to CSV or other formats for external use. Batch operations are supported, allowing you to apply actions (move, delete, tag) to multiple files at once.

### Contextual Actions

The application provides a right-click context menu in the search results. This menu offers quick access to common file operations such as open, rename, delete, move, or edit tags. Additionally, a preview option is available directly in the context menu for images, documents, and videos.

### Smart Suggestions

As you type in the search bar, the application offers smart suggestions based on your input, historical searches, and commonly accessed files. These suggestions can include tags, filenames, and content snippets, making it easier to find what you're looking for.

## Conclusion

The File Organizer and Content Manager is a powerful desktop application that helps you efficiently organize, search, and manage your local files. With its automated organization, advanced search capabilities, and content management features, you can enhance your productivity and streamline your file management tasks. Whether you need to find specific files, organize them based on custom rules, or perform bulk operations, the File Organizer and Content Manager has you covered. Enjoy a seamless file management experience with this comprehensive software.