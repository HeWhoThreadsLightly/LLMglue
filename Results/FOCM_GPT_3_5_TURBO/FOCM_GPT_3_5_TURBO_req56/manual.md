# File Organizer and Content Manager User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a desktop application designed to help users efficiently organize, search, and manage their local files. This software aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. It provides a unified interface for managing digital content and supports various file types, including documents, images, videos, and more.

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

At the top of the main window, you will find a toolbar with buttons for common actions. These buttons allow you to create a new folder, delete a file, refresh the view, toggle between list/grid view, and perform a search.

### Status Bar

The bottom of the main window contains a status bar that displays information about the selected files/folders and general statistics, such as the total number of files and total size.

## Search and Filter Panel

The File Organizer and Content Manager provides a dedicated panel for searching and filtering files. This panel is accessible from the main window and allows you to enter search criteria, choose filters (file type, date modified, size), and display the results in a list or grid format.

### Advanced Search Options

The search and filter panel includes advanced search options for more precise filtering. These options allow you to perform a full-text search within documents, enabling you to find files containing specific text.

### File Preview Window

When you select a file in the main window, a file preview window will appear. This window provides a quick preview of the selected file. For text documents and images, the preview will be displayed within the window. For videos and audio files, basic playback controls will be available.

### Edit Mode for Text Files

For text files, the file preview window includes an edit mode. This mode allows you to make quick edits directly within the preview window, saving you time and effort.

### File Properties and Metadata Editor

By selecting "Properties" from the context menu of a file or folder, a dialog box will appear. This dialog box shows detailed information about the file, including file size, creation/modification dates, and allows you to edit metadata tags.

### Settings/Preferences Window

The File Organizer and Content Manager provides a separate window accessible from the main menu. This window allows you to customize application settings, such as theme selection (dark/light), default views, file organization rules, backup settings, and extension/plugin management.

### Tag Management Interface

To provide a flexible way to categorize and locate files quickly, the File Organizer and Content Manager includes a tag management interface. This interface allows you to create, edit, and delete tags. You can also assign tags to files or folders directly from this interface.

### Backup and Synchronization Setup Wizard

To ensure the safety of your files, the File Organizer and Content Manager includes a step-by-step wizard that guides you through setting up backup destinations (external drive, cloud storage) and synchronization options. This wizard includes the ability to schedule automatic backups, providing peace of mind and data protection.

### Help and Tutorial Section

The File Organizer and Content Manager offers a dedicated window or section accessible from the main menu. This section provides a searchable help database, user manual, and interactive tutorials on key features. It is designed to assist you in getting the most out of the application and resolving any questions or issues you may have.

## File Organization

The File Organizer and Content Manager includes powerful file organization features to help you keep your files organized and easily accessible.

### Automated Organization Rules

The application allows you to create customizable rules for automatically organizing files. These rules can be based on file type, date criteria (creation date, modification date), file name patterns (using wildcards or regular expressions), and file size thresholds. You can specify the target folder structure for organized files, with options to create new folders based on rule criteria (e.g., date, project name).

### Manual Tagging and Categorization

In addition to automated organization, the File Organizer and Content Manager allows you to manually assign custom tags to files and folders. The application offers a tagging interface that suggests existing tags as you type and allows the creation of new tags. You can also create custom categories to group files/folders based on project, client, priority, or any other user-defined category. The application provides a dedicated interface or filter to view and access files by tags and categories.

### Bulk File Operations

To save time and effort, the File Organizer and Content Manager supports bulk operations on files. You can rename, move, copy, or delete multiple files at once based on your selection. The application also includes options for bulk applying tags or moving files to a category. If needed, you can use the undo functionality to revert changes.

### Folder and File Management

The File Organizer and Content Manager allows you to create, rename, move, and delete files and folders directly from within the application. It provides a drag-and-drop interface for easy file and folder management, allowing you to move files and folders into different categories or locations effortlessly. The application also includes a feature to detect and resolve duplicate files based on name, size, and optionally content hash. You can choose to keep, delete, or merge duplicate files.

### Custom Folder Views and Sorting

To suit your preferences, the File Organizer and Content Manager allows you to customize how folders and files are displayed. You can choose between list, grid, and thumbnail views. The application supports sorting files and folders by name, size, date modified, or custom tags/categories.

### File Watcher and Auto-Update

The File Organizer and Content Manager includes a file watcher mechanism that automatically updates file organization based on predefined rules when new files are added to monitored folders. This feature works in real-time or at user-defined intervals, ensuring that the organization structure is always up-to-date.

### Integration with File System

The File Organizer and Content Manager integrates closely with the operating system's file system. It reflects changes made within the application in real-time in the user's file explorer or finder. The application also supports right-click context menu options in the operating system's file explorer, allowing you to quickly tag, categorize, or apply predefined organization rules to selected files or folders.

## Search and Filter

The File Organizer and Content Manager provides advanced search functionality to help you find files and folders quickly and efficiently.

### Advanced Search Functionality

The application allows you to search for files and folders using partial or full file names. It also provides content-based search capabilities, enabling you to find files containing specific text, even within documents or metadata for images and videos. The search functionality supports regular expressions (regex) for complex pattern matching.

### Custom Search Filters

The File Organizer and Content Manager includes predefined filters to quickly select files based on common criteria, such as file type (e.g., documents, images, videos), size (e.g., less than 10MB), and modification or creation date (e.g., last 7 days). Additionally, you can create, save, and apply custom filter sets based on any combination of file attributes, including custom tags, project names, or specific content.

### Tag-Based Searching

To facilitate detailed organization and searching, the File Organizer and Content Manager integrates a tagging system. You can assign custom tags to files and folders and then search for these tags. The application supports hierarchical tags, allowing you to create a structured tagging system (e.g., Work/Project1, Personal/Photos).

### Search History and Saved Searches

The File Organizer and Content Manager automatically saves recent searches for quick repetition. You can also save frequently used search queries or filters for quick access, making it easy to perform repetitive searches.

### Search Results Management

The application provides sortable search results based on various criteria, such as name, size, date modified, and custom tags. You can export search results to CSV or other formats for external use. Batch operations on search results are supported, allowing you to apply actions (e.g., move, delete, tag) to multiple files at once. The right-click context menu in search results provides quick access to common file operations, such as open, rename, delete, move, or edit tags. Preview options for images, documents, and videos are also available directly in the context menu.

### Smart Suggestions

To assist you in finding files and performing searches, the File Organizer and Content Manager offers smart suggestions. As you type in the search bar, the system provides suggestions based on your input, historical searches, and commonly accessed files. These suggestions can include tags, filenames, and content snippets.

### Integration with File Organization

The File Organizer and Content Manager seamlessly integrates with the file organization system. This integration allows you to quickly organize search results into folders or tag groups directly from the search interface, streamlining your workflow.

## Additional Features

In addition to the core file organization and search capabilities, the File Organizer and Content Manager includes several additional features to enhance your experience.

### Content Management

The application provides preview capabilities for common file types, such as PDF, DOCX, images, and videos. You can view these files directly within the application, eliminating the need for external viewers. For text files and images, basic editing tools are available, allowing you to perform tasks such as text formatting and cropping. The File Organizer and Content Manager also integrates with external applications for editing unsupported file types, providing a seamless editing experience.

### Backup and Synchronization

To ensure the safety and availability of your files, the File Organizer and Content Manager includes options for backing up important files and folders. You can choose to back up to external drives or cloud storage services, depending on your preferences and requirements.

### Documentation and Help

Comprehensive user manual and online help resources are available to assist you in using the File Organizer and Content Manager effectively. The user manual provides detailed instructions on how to use the various features and functionalities of the application. Additionally, interactive tutorials are available to demonstrate key features and help you get started quickly.

## Conclusion

The File Organizer and Content Manager is a powerful desktop application that simplifies file organization, enhances search capabilities, and provides content management features. With its intuitive interface and comprehensive set of tools, you can efficiently manage your local files, improve productivity, and easily find the information you need. Whether you are a student, professional, or casual user, the File Organizer and Content Manager is designed to meet your file management needs.