# File Organizer and Content Manager User Manual

## Introduction
The File Organizer and Content Manager (FOCM) is a powerful desktop application designed to help users efficiently organize, search, and manage their local files. With FOCM, you can enhance your productivity and file management through automated organization, advanced search capabilities, and content management features. This user manual will guide you through the installation process, introduce the main functions of the software, and provide instructions on how to use it effectively.

## Installation
To install FOCM, please follow these steps:

1. Ensure that you have Python installed on your computer. FOCM requires Python version 3.7 or higher.

2. Open a terminal or command prompt and navigate to the directory where you want to install FOCM.

3. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Once the installation is complete, you can launch FOCM by running the following command:

   ```
   python main.py
   ```

   The FOCM application window will open, and you can start using the software.

## Main Window
The main window of FOCM serves as the central hub for managing your files. It features a dual-pane layout, with one pane for the directory tree (folders) and another for viewing the contents of the selected directory.

### Toolbar
At the top of the main window, you will find a toolbar with buttons for common actions. These buttons allow you to create new folders, delete files, refresh the view, toggle between list and grid view, and perform searches.

### Status Bar
The status bar at the bottom of the main window displays information about the selected files/folders and general statistics, such as the total number of files and total size.

## Search and Filter Panel
FOCM provides a dedicated panel for searching and filtering files. You can access this panel from the main window. In the search and filter panel, you can enter search criteria, choose filters (file type, date modified, size), and display the results in a list or grid format.

### Advanced Search Options
FOCM offers advanced search options for more precise filtering. You can perform full-text search within documents, allowing you to find files containing specific text. Additionally, FOCM supports regular expressions (regex) in search queries for complex pattern matching.

## File Preview Window
FOCM provides a file preview window that allows you to quickly preview the selected file. For text documents and images, the preview is shown within the window. For videos and audio files, basic playback controls are provided.

### Edit Mode
For text files, FOCM offers an edit mode that enables you to make quick edits directly within the preview window. This feature allows you to modify text files without opening them in a separate editor.

## File Properties and Metadata Editor
FOCM includes a file properties and metadata editor that displays detailed information about a selected file or folder. This dialog box shows file size, creation/modification dates, and allows you to edit metadata tags. To access the file properties and metadata editor, right-click on a file or folder and select "Properties" from the context menu.

## Settings/Preferences Window
FOCM provides a separate settings/preferences window that allows you to customize various application settings. In this window, you can choose the theme (dark/light), set default views, configure file organization rules, manage backups, and handle extensions/plugins.

## Tag Management Interface
FOCM offers a tag management interface that allows you to create, edit, and delete tags. You can assign tags to files or folders from this interface, providing a flexible way to categorize and locate files quickly.

## Backup and Synchronization Setup Wizard
FOCM includes a step-by-step wizard that guides you through setting up backup destinations and synchronization options. This wizard helps you configure automatic backups and schedule them according to your preferences.

## Help and Tutorial Section
FOCM provides a dedicated help and tutorial section that offers a searchable help database, user manual, and interactive tutorials on key features. You can access this section from the main menu.

## File Organization
FOCM offers powerful file organization features to help you keep your files organized and easily accessible.

### Automated Organization Rules
You can create customizable rules for automatically organizing files based on various criteria, such as file type, date criteria (creation date, modification date), file name patterns, and file size thresholds. FOCM allows you to specify the target folder structure for organized files and create new folders based on rule criteria, such as date or project name.

### Manual Tagging and Categorization
FOCM allows you to assign custom tags to files and folders manually. The application offers a tagging interface that suggests existing tags as you type and allows you to create new tags. You can also create custom categories to group files/folders based on project, client, priority, or any other user-defined category. FOCM provides a dedicated interface or filter to view and access files by tags and categories.

### Bulk File Operations
FOCM supports bulk operations to rename, move, copy, or delete multiple files at once based on your selection. You can also bulk apply tags or move files to a category. FOCM includes an undo functionality to revert changes if needed.

### Folder and File Management
FOCM allows you to create, rename, move, and delete files and folders from within the application. The software provides a drag-and-drop interface for easy file and folder management. FOCM also includes a feature to detect and resolve duplicate files based on name, size, and optionally content hash. You can choose to keep, delete, or merge duplicate files.

### Custom Folder Views and Sorting
FOCM allows you to customize how folders and files are displayed. You can choose between list, grid, and thumbnail views. The software supports sorting files and folders by name, size, date modified, or custom tags/categories.

### File Watcher and Auto-Update
FOCM implements a file watcher mechanism that automatically updates file organization based on predefined rules when new files are added to monitored folders. This feature works in real-time or at user-defined intervals, ensuring that the organization structure is always up-to-date.

### Integration with File System
FOCM integrates closely with the operating system's file system to reflect changes made within the application in real-time in the user's file explorer or finder. The software supports right-click context menu options in the operating system's file explorer, allowing you to quickly tag, categorize, or apply predefined organization rules to selected files or folders.

## Search and Filter
FOCM provides advanced search functionality to help you find files and folders quickly.

### Advanced Search
You can search for files and folders using partial or full file names. FOCM also supports content-based search capabilities, allowing you to find files containing specific text, even within documents or metadata for images and videos. The software supports regular expressions (regex) in search queries for complex pattern matching.

### Custom Search Filters
FOCM offers predefined filters to quickly select files based on common criteria, such as file type, size, and modification or creation date. Additionally, you can create, save, and apply custom filter sets based on any combination of file attributes, including custom tags, project names, or specific content.

### Tag-Based Searching
FOCM integrates a tagging system that allows you to assign custom tags to files and folders. You can then search for these tags to quickly locate specific files. The software supports hierarchical tags to facilitate detailed organization and searching.

### Search History and Saved Searches
FOCM automatically saves recent searches for quick repetition. You can also save frequently used search queries or filters for quick access.

### Search Results Management
FOCM provides sortable search results based on various criteria, such as name, size, date modified, and custom tags. You can export search results to CSV or other formats for external use. The software allows batch operations on search results, enabling you to apply actions (move, delete, tag) to multiple files at once. Contextual actions are available in the search results, providing quick access to common file operations like open, rename, delete, move, or edit tags. Preview options are also available directly in the context menu for images, documents, and videos.

### Smart Suggestions
As you type in the search bar, FOCM offers smart suggestions based on your input, historical searches, and commonly accessed files. The software suggests tags, filenames, and content snippets as possible search queries.

### Integration with File Organization
FOCM seamlessly integrates with the file organization system, allowing you to quickly organize search results into folders or tag groups directly from the search interface.

## Conclusion
With the File Organizer and Content Manager (FOCM), you have a powerful tool at your disposal to efficiently organize, search, and manage your local files. This user manual has provided an overview of the main functions and features of FOCM, as well as instructions on how to install and use the software effectively. We hope that FOCM will enhance your productivity and simplify your file management tasks. Enjoy using FOCM!

```