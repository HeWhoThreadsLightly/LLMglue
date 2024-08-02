# File Organizer and Content Manager User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a desktop application designed to help users efficiently organize, search, and manage their local files. This software aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. It provides a unified interface for managing digital content and supports various file types, including documents, images, videos, and more.

## Installation

To install the File Organizer and Content Manager, follow these steps:

1. Ensure that you have Python installed on your computer. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Clone or download the FOCM repository from GitHub: [https://github.com/your-repo/focm](https://github.com/your-repo/focm)

3. Open a terminal or command prompt and navigate to the downloaded repository folder.

4. Create a virtual environment (optional but recommended) by running the following command:

   ```
   python -m venv env
   ```

5. Activate the virtual environment by running the appropriate command for your operating system:

   - Windows:

     ```
     env\Scripts\activate
     ```

   - macOS/Linux:

     ```
     source env/bin/activate
     ```

6. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

7. Run the application by executing the following command:

   ```
   python main.py
   ```

## Main Window

The main window of the File Organizer and Content Manager serves as the central hub of the application. It features a dual-pane layout, with one pane for the directory tree (folders) and another for viewing the contents of the selected directory.

### Toolbar

At the top of the main window, you will find a toolbar with buttons for common actions. These buttons allow you to perform the following actions:

- Create a new folder
- Delete a file
- Refresh the view
- Toggle between list/grid view
- Search for files

### Status Bar

At the bottom of the main window, there is a status bar that displays information about the selected files/folders and general statistics, such as the total number of files and total size.

## Search and Filter Panel

The File Organizer and Content Manager provides a dedicated panel for searching and filtering files. This panel is accessible from the main window and allows you to enter search criteria, choose filters (file type, date modified, size), and display results in a list or grid format.

### Advanced Search Options

The search and filter panel also offers advanced search options for more precise filtering. You can perform full-text search within documents, allowing you to find files containing specific text.

### File Preview Window

When you select a file, the File Organizer and Content Manager provides a file preview window. For text documents and images, the preview is shown within the window. For videos and audio files, basic playback controls are available.

### Edit Mode for Text Files

For text files, the file preview window also includes an edit mode. This allows you to make quick edits directly within the preview window.

### File Properties and Metadata Editor

By selecting "Properties" from the context menu of a file or folder, you can access a dialog box that displays detailed information about the file, including file size, creation/modification dates. You can also edit metadata tags for the file.

### Settings/Preferences Window

The File Organizer and Content Manager provides a separate window accessible from the main menu for customizing application settings. In this window, you can select the theme (dark/light), default views, file organization rules, backup settings, and manage extensions/plugins.

### Tag Management Interface

To categorize and locate files quickly, the File Organizer and Content Manager offers a tag management interface. This interface allows you to create, edit, and delete tags. You can also assign tags to files or folders from this interface.

### Backup and Synchronization Setup Wizard

To set up backup destinations and synchronization options, including scheduling automatic backups, the File Organizer and Content Manager provides a step-by-step wizard. This wizard guides you through the process.

### Help and Tutorial Section

The File Organizer and Content Manager includes a dedicated window or section accessible from the main menu. This section offers a searchable help database, user manual, and interactive tutorials on key features.

## File Organization

The File Organizer and Content Manager provides various features for file organization.

### Automated Organization Rules

You can create customizable rules for automatically organizing files based on file type, date criteria (creation date, modification date), file name patterns, and file size thresholds. You can specify the target folder structure for organized files and create new folders based on rule criteria.

### Manual Tagging and Categorization

You can assign custom tags to files and folders manually. The application offers a tagging interface that suggests existing tags as you type and allows the creation of new tags. You can also create custom categories to group files/folders based on project, client, priority, or any other user-defined category.

### Bulk File Operations

The File Organizer and Content Manager supports bulk operations for renaming, moving, copying, or deleting multiple files at once. You can also bulk apply tags or move files to a category. The application provides undo functionality to revert changes if needed.

### Folder and File Management

You can create, rename, move, and delete files and folders from within the application. The application also provides a drag-and-drop interface for moving files and folders into different categories or locations. Additionally, the application can detect and resolve duplicate files based on name, size, and optionally content hash.

### Custom Folder Views and Sorting

The File Organizer and Content Manager allows you to customize how folders and files are displayed. You can choose between list, grid, and thumbnail views. You can also sort files and folders by name, size, date modified, or custom tags/categories.

### File Watcher and Auto-Update

The File Organizer and Content Manager implements a file watcher mechanism that automatically updates file organization based on predefined rules when new files are added to monitored folders. This feature works in real-time or at user-defined intervals, ensuring the organization structure is always up-to-date.

### Integration with File System

The File Organizer and Content Manager integrates closely with the operating system's file system. It reflects changes made within the app in real-time in the user's file explorer or finder. It also supports right-click context menu options in the operating system's file explorer to quickly tag, categorize, or apply predefined organization rules to selected files or folders.

## Search and Filter

The File Organizer and Content Manager provides advanced search functionality to help you find files and folders quickly.

### Advanced Search Functionality

You can search for files and folders using partial or full file names. The application also supports content-based search capabilities, allowing you to find files containing specific text, even within documents or metadata for images and videos. Additionally, you can use regular expressions (regex) in search queries for complex pattern matching.

### Custom Search Filters

The application offers predefined filters to quickly select files based on common criteria such as file type, size, and modification or creation date. You can also create, save, and apply custom filter sets based on any combination of file attributes, including custom tags, project names, or specific content.

### Tag-Based Searching

The File Organizer and Content Manager integrates a tagging system. You can assign custom tags to files and folders and then search for these tags. The application supports hierarchical tags to facilitate detailed organization and searching.

### Search History and Saved Searches

The File Organizer and Content Manager automatically saves recent searches for quick repetition. You can also save frequently used search queries or filters for quick access.

### Search Results Management

Search results in the File Organizer and Content Manager are sortable based on various criteria such as name, size, date modified, and custom tags. You can export search results to CSV or other formats for external use. Batch operations on search results are also supported, allowing you to apply actions (move, delete, tag) to multiple files at once.

### Contextual Actions

The application provides a right-click context menu in search results for quick access to common file operations like open, rename, delete, move, or edit tags. Additionally, a preview option is available directly in the context menu for images, documents, and videos.

### Smart Suggestions

As you type in the search bar, the File Organizer and Content Manager offers smart suggestions based on your input, historical searches, and commonly accessed files. It suggests tags, filenames, and content snippets as possible search queries.

### Integration with File Organization

The File Organizer and Content Manager seamlessly integrates with the file organization system. You can quickly organize search results into folders or tag groups directly from the search interface.

## Additional Features

In addition to the core functionality, the File Organizer and Content Manager offers the following additional features:

### Content Management

The application provides preview capabilities for common file types such as PDF, DOCX, images, and videos. For text files and images, basic editing tools are available, including text formatting and cropping. For unsupported file types, integration with external applications is provided for editing.

### Backup and Synchronization

The File Organizer and Content Manager allows you to backup important files and folders to external drives or cloud storage services. You can set up backup destinations and synchronization options, including scheduling automatic backups.

### Documentation and Help

Comprehensive user manual and online help resources are available for reference. Additionally, a tutorial for first-time users is provided to demonstrate key features.

## Accessibility

The File Organizer and Content Manager includes several accessibility features to ensure a smooth user experience for all users.

### Keyboard Navigation

Full functionality is accessible via keyboard shortcuts, allowing users who cannot use a mouse to navigate efficiently through the application. Tab navigation is implemented through all interactive elements in a logical order. Visual indicators are provided for the currently focused element.

### Screen Reader Support

The application makes use of alt text to describe images, icons, and other non-textual elements. Labels and roles are used for complex elements (like drag-and-drop interfaces or custom controls) to ensure their purpose and state are conveyed to screen reader users.

### High Contrast Mode

The File Organizer and Content Manager supports high contrast themes that make text, icons, and other elements more distinguishable for users with low vision. All text is readable, and all interactive elements are visible against background colors.

## Conclusion

The File Organizer and Content Manager is a powerful desktop application that helps users efficiently organize, search, and manage their local files. With its automated organization, advanced search capabilities, and content management features, it enhances productivity and simplifies file management. Whether you need to find specific files, categorize them with tags, or perform bulk operations, the File Organizer and Content Manager has you covered. Enjoy a seamless file management experience with this comprehensive and user-friendly application.

```