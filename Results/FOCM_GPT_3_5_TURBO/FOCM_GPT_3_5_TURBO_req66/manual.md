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

## User Interface

### Main Window
The main window is the central hub of the application. It features a dual-pane layout, with one pane for the directory tree (folders) and another for viewing the contents of the selected directory. The main window also includes a toolbar at the top with buttons for common actions, a search bar, and a status bar at the bottom displaying information about the selected files/folders and general statistics.

### Search and Filter Panel
The search and filter panel is a dedicated panel accessible from the main window. It allows users to enter search criteria, choose filters (file type, date modified, size), and display results in a list or grid format. The search and filter panel also provides advanced search options for more precise filtering, including full-text search within documents.

### File Preview Window
The file preview window is a pop-up or sidebar window that provides a quick preview of the selected file. For text documents and images, it shows a preview within the window. For videos and audio files, it provides basic playback controls. The file preview window also includes an edit mode for text files, enabling users to make quick edits directly within the preview window.

### File Properties and Metadata Editor
The file properties and metadata editor is a dialog box that displays when a user selects "Properties" from the context menu of a file/folder. It shows detailed information including file size, creation/modification dates, and allows the user to edit metadata tags.

### Settings/Preferences Window
The settings/preferences window is a separate window accessible from the main menu. It allows users to customize application settings, including theme selection (dark/light), default views, file organization rules, backup settings, and extension/plugin management.

### Tag Management Interface
The tag management interface is a panel or window for creating, editing, and deleting tags. Users can also assign tags to files or folders from this interface, providing a flexible way to categorize and locate files quickly.

### Backup and Synchronization Setup Wizard
The backup and synchronization setup wizard is a step-by-step wizard that guides users through setting up backup destinations (external drive, cloud storage) and synchronization options, including scheduling automatic backups.

### Help and Tutorial Section
The help and tutorial section is a dedicated window or section accessible from the main menu. It offers a searchable help database, user manual, and interactive tutorials on key features.

## Features

### Automated Organization Rules
The File Organizer and Content Manager allows users to create customizable rules for automatically organizing files. These rules can be based on file type, date criteria (creation date, modification date), file name patterns (using wildcards or regular expressions), and file size thresholds. Users can specify the target folder structure for organized files, with options to create new folders based on rule criteria (e.g., date, project name).

### Manual Tagging and Categorization
Users can assign custom tags to files and folders manually. The application offers a tagging interface that suggests existing tags as the user types and allows the creation of new tags. It also supports creating custom categories where users can group files/folders based on project, client, priority, or any other user-defined category. Users can view and access files by tags and categories through a dedicated interface or filter.

### Bulk File Operations
The application supports bulk operations to rename, move, copy, or delete multiple files at once based on user selection. It includes options for bulk applying tags or moving files to a category, with undo functionality to revert changes if needed.

### Folder and File Management
Users can create, rename, move, and delete files and folders from within the application. The application provides a drag-and-drop interface for moving files and folders into different categories or locations. It also includes a feature to detect and resolve duplicate files based on name, size, and optionally content hash, with options to keep, delete, or merge duplicate files.

### Custom Folder Views and Sorting
Users can customize how folders and files are displayed, including list, grid, and thumbnail views. The application supports sorting files and folders by name, size, date modified, or custom tags/categories.

### File Watcher and Auto-Update
The File Organizer and Content Manager implements a file watcher mechanism that automatically updates file organization based on predefined rules when new files are added to monitored folders. This feature works in real-time or at user-defined intervals, ensuring the organization structure is always up-to-date.

### Integration with File System
The application integrates closely with the operating system's file system to reflect changes made within the app in real-time in the user's file explorer or finder. It supports right-click context menu options in the operating system’s file explorer to quickly tag, categorize, or apply predefined organization rules to selected files or folders.

### Advanced Search Functionality
The application provides advanced search functionality, including the ability to search for files and folders using partial or full file names. It also supports content-based search capabilities that allow users to find files containing specific text, even within documents or metadata for images and videos. Users can use regular expressions (regex) in search queries for complex pattern matching.

### Custom Search Filters
The application offers predefined filters to quickly select files based on common criteria such as file type, size, and modification or creation date. It also allows users to create, save, and apply custom filter sets based on any combination of file attributes, including custom tags, project names, or specific content. Users can perform tag-based searching by assigning custom tags to files and folders and then searching for these tags. The application supports hierarchical tags to facilitate detailed organization and searching.

### Search History and Saved Searches
The application automatically saves recent searches for quick repetition. Users can also save frequently used search queries or filters for quick access.

### Search Results Management
Search results are sortable based on various criteria such as name, size, date modified, and custom tags. Users can export search results to CSV or other formats for external use. Batch operations on search results are supported, allowing users to apply actions (move, delete, tag) to multiple files at once. Contextual actions are available in the search results, providing quick access to common file operations like open, rename, delete, move, or edit tags. Preview options for images, documents, and videos are also available directly in the context menu.

### Smart Suggestions
As users type in the search bar, the system offers smart suggestions based on their input, historical searches, and commonly accessed files. Suggestions include tags, filenames, and content snippets as possible search queries.

### Integration with File Organization
The application seamlessly integrates with the file organization system, allowing users to quickly organize search results into folders or tag groups directly from the search interface.

### Content Management
The File Organizer and Content Manager provides preview capabilities for common file types such as PDF, DOCX, images, and videos directly within the application. Basic editing tools for text files and images, such as text formatting and cropping, are also available. Integration with external applications for editing unsupported file types is supported.

### Backup and Synchronization
The application offers options to backup important files and folders to external drives or cloud storage services. Users can set up backup destinations and synchronization options, including scheduling automatic backups.

### Documentation and Help
Comprehensive user manual and online help resources are available for reference. A tutorial for first-time users is provided to demonstrate key features.

## Accessibility Features

### Keyboard Navigation
The File Organizer and Content Manager ensures that full functionality is accessible via keyboard shortcuts to accommodate users who cannot use a mouse. Tab navigation is implemented through all interactive elements in a logical order. Visual indicators are provided for the currently focused element.

### Screen Reader Support
The application makes use of alt text to describe images, icons, and other non-textual elements. Labels and roles are used for complex elements (like drag-and-drop interfaces or custom controls) to ensure their purpose and state are conveyed to screen reader users.

### High Contrast Mode
The File Organizer and Content Manager supports high contrast themes that make text, icons, and other elements more distinguishable for users with low vision. All text is readable, and all interactive elements are visible against background colors.

### Text Size and Font Adjustments
Users can adjust the text size without breaking the layout or losing functionality. The application supports the use of user-defined system fonts, including those designed for dyslexia.

### Color Blind Mode
Color schemes that are accessible to users with various types of color blindness (e.g., deuteranopia, protanopia, tritanopia) are implemented.

## Conclusion
The File Organizer and Content Manager is a powerful desktop application that helps users efficiently organize, search, and manage their local files. With its automated organization, advanced search capabilities, and content management features, it enhances productivity and simplifies file management tasks. Whether you need to organize files based on specific criteria, perform advanced searches, or manage file properties and metadata, the File Organizer and Content Manager has you covered. Enjoy the benefits of a unified interface for managing your digital content and take control of your file organization today!