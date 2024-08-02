# File Organizer and Content Manager (FOCM) User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a powerful desktop application designed to help users efficiently organize, search, and manage their local files. FOCM aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. It provides a unified interface for managing digital content and supports various file types, including documents, images, videos, and more.

This user manual will guide you through the installation process, introduce the main functions of FOCM, and provide step-by-step instructions on how to use the application effectively.

## Table of Contents

1. Installation
2. Main Window
   - Directory Tree
   - Content View
   - Toolbar
   - Status Bar
3. Search and Filter Panel
   - Basic Search
   - Advanced Search
   - Filters
4. File Preview Window
   - Text Documents and Images
   - Videos and Audio Files
   - Edit Mode for Text Files
5. File Properties and Metadata Editor
6. Settings/Preferences Window
7. Tag Management Interface
8. Backup and Synchronization Setup Wizard
9. Help and Tutorial Section
10. File Organization
   - Automated Organization Rules
   - Manual Tagging and Categorization
   - Bulk File Operations
   - Folder and File Management
   - Duplicate File Detection and Resolution
   - Custom Folder Views and Sorting
   - File Watcher and Auto-Update
   - Integration with File System
11. Search and Filter
   - Advanced Search Functionality
   - Custom Search Filters
   - Tag-Based Searching
   - Search History and Saved Searches
   - Search Results Management
   - Contextual Actions
   - Smart Suggestions
   - Integration with File Organization
12. Additional Features
   - Content Management
   - Backup and Synchronization
   - Documentation and Help
13. Accessibility Features
   - Keyboard Navigation
   - Screen Reader Support
   - High Contrast Mode

## 1. Installation

To install FOCM, follow these steps:

1. Open a command prompt or terminal.
2. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

   Note: Make sure you have Python and pip installed on your system.

3. Once the installation is complete, you can launch FOCM by running the following command:

   ```
   python main.py
   ```

   The FOCM application will open, and you can start using it to organize and manage your files.

## 2. Main Window

The main window of FOCM serves as the central hub for file organization and management. It consists of several key components:

### Directory Tree

The directory tree pane displays the folder structure of your local file system. It allows you to navigate through different directories and select folders to view their contents in the content view pane.

### Content View

The content view pane displays the files and folders within the selected directory. You can switch between list and grid view to customize how the files are displayed. The content view also supports sorting by name, size, date modified, and custom tags/categories.

### Toolbar

The toolbar at the top of the main window provides quick access to common actions. It includes buttons for creating new folders, deleting files, refreshing the view, toggling between list/grid view, and a search bar for performing searches.

### Status Bar

The status bar at the bottom of the main window displays information about the selected files/folders and general statistics, such as the total number of files and total size.

## 3. Search and Filter Panel

FOCM provides a dedicated search and filter panel that allows you to search for files and apply filters to narrow down the results. The search and filter panel includes the following features:

### Basic Search

You can enter a search query in the search bar of the toolbar to search for files and folders based on partial or full file names. FOCM will display the search results in the content view.

### Advanced Search

FOCM supports advanced search options for more precise filtering. You can perform full-text search within documents, use regular expressions for complex pattern matching, and apply predefined filters based on file type, size, and modification date.

### Filters

FOCM allows you to choose filters such as file type, date modified, and size to refine your search results. You can display the results in a list or grid format.

## 4. File Preview Window

FOCM provides a file preview window that allows you to quickly preview the selected file. The file preview window supports different file types:

### Text Documents and Images

For text documents and images, FOCM displays a preview within the window. You can also edit text files directly within the preview window.

### Videos and Audio Files

For videos and audio files, FOCM provides basic playback controls within the preview window. You can play, pause, and adjust the volume of the media files.

## 5. File Properties and Metadata Editor

FOCM allows you to view and edit the properties and metadata of files and folders. When you select a file or folder and right-click to open the context menu, you can choose "Properties" to access the file properties and metadata editor. The editor displays detailed information about the file, such as file size, creation/modification dates, and allows you to edit metadata tags.

## 6. Settings/Preferences Window

FOCM provides a separate settings/preferences window that allows you to customize the application settings. In the settings/preferences window, you can choose the theme (dark/light), set default views, configure file organization rules, manage backup settings, and handle extension/plugin management.

## 7. Tag Management Interface

FOCM includes a tag management interface that allows you to create, edit, and delete tags. You can assign tags to files and folders from this interface, providing a flexible way to categorize and locate files quickly. The tag management interface also suggests existing tags as you type and allows the creation of new tags.

## 8. Backup and Synchronization Setup Wizard

FOCM provides a step-by-step wizard that guides you through setting up backup destinations and synchronization options. The wizard helps you choose external drives or cloud storage as backup destinations and configure automatic backup schedules.

## 9. Help and Tutorial Section

FOCM includes a dedicated help and tutorial section that offers a searchable help database, user manual, and interactive tutorials on key features. You can access this section from the main menu to get assistance and learn more about using FOCM effectively.

## 10. File Organization

FOCM offers powerful file organization features to help you manage your files efficiently. These features include:

### Automated Organization Rules

FOCM allows you to create customizable rules for automatically organizing files. You can define rules based on file type, date criteria, file name patterns, and file size thresholds. You can also specify the target folder structure for organized files, including options to create new folders based on rule criteria.

### Manual Tagging and Categorization

FOCM enables manual tagging and categorization of files and folders. You can assign custom tags to files and folders, create custom categories for grouping files/folders, and view/access files by tags and categories through a dedicated interface or filter.

### Bulk File Operations

FOCM supports bulk operations to rename, move, copy, or delete multiple files at once based on user selection. You can also apply tags or move files to a category in bulk. FOCM provides undo functionality to revert changes if needed.

### Folder and File Management

FOCM allows you to create, rename, move, and delete files and folders from within the application. It provides a drag-and-drop interface for easy file and folder management. FOCM also includes a feature to detect and resolve duplicate files based on name, size, and optionally content hash.

### Custom Folder Views and Sorting

FOCM allows you to customize how folders and files are displayed in the content view. You can choose between list, grid, and thumbnail views. FOCM also supports sorting files and folders by name, size, date modified, or custom tags/categories.

### File Watcher and Auto-Update

FOCM implements a file watcher mechanism that automatically updates file organization based on predefined rules when new files are added to monitored folders. This feature works in real-time or at user-defined intervals, ensuring that the organization structure is always up-to-date.

### Integration with File System

FOCM integrates closely with the operating system's file system to reflect changes made within the app in real-time in the user's file explorer or finder. It supports right-click context menu options in the operating system's file explorer for quick tagging, categorization, or application of predefined organization rules to selected files or folders.

## 11. Search and Filter

FOCM provides advanced search and filter capabilities to help you find files and folders quickly. These features include:

### Advanced Search Functionality

FOCM allows you to search for files and folders using partial or full file names. It also supports content-based search capabilities, allowing you to find files containing specific text within documents or metadata for images and videos. You can use regular expressions (regex) in search queries for complex pattern matching.

### Custom Search Filters

FOCM provides predefined filters to quickly select files based on common criteria such as file type, size, and modification or creation date. You can also create, save, and apply custom filter sets based on any combination of file attributes, including custom tags, project names, or specific content.

### Tag-Based Searching

FOCM integrates a tagging system that allows you to assign custom tags to files and folders. You can search for files based on these tags, facilitating detailed organization and searching. FOCM supports hierarchical tags, enabling you to create tag hierarchies for better organization.

### Search History and Saved Searches

FOCM automatically saves recent searches for quick repetition. You can also save frequently used search queries or filters for quick access. This feature helps you streamline your search process and save time.

### Search Results Management

FOCM provides sortable search results based on various criteria such as name, size, date modified, and custom tags. You can export search results to CSV or other formats for external use. Batch operations on search results allow you to apply actions (move, delete, tag) to multiple files at once.

### Contextual Actions

FOCM offers a right-click context menu in search results to provide quick access to common file operations such as open, rename, delete, move, or edit tags. It also provides a preview option directly in the context menu for images, documents, and videos.

### Smart Suggestions

As you type in the search bar, FOCM offers smart suggestions based on your input, historical searches, and commonly accessed files. It suggests tags, filenames, and content snippets as possible search queries, making it easier to find the files you need.

### Integration with File Organization

FOCM seamlessly integrates with the file organization system, allowing you to quickly organize search results into folders or tag groups directly from the search interface. This integration enhances your file management workflow and improves efficiency.

## 12. Additional Features

In addition to file organization and search capabilities, FOCM offers several additional features to enhance your file management experience:

### Content Management

FOCM provides preview capabilities for common file types such as PDF, DOCX, images, and videos. You can view these files directly within the application, making it easier to review and manage your digital content. FOCM also includes basic editing tools for text files and images, such as text formatting and cropping. For unsupported file types, FOCM integrates with external applications for editing.

### Backup and Synchronization

FOCM allows you to back up important files and folders to external drives or cloud storage services. You can configure backup destinations and synchronization options through a setup wizard. FOCM supports automatic backups and ensures that your files are protected and up-to-date.

### Documentation and Help

FOCM provides comprehensive user documentation and help resources. The user manual and online help resources offer detailed information on using FOCM effectively. Additionally, FOCM includes tutorials for first-time users to demonstrate key features and help you get started quickly.

## 13. Accessibility Features

FOCM includes several accessibility features to ensure that all users can access and use the application effectively:

### Keyboard Navigation

FOCM supports full functionality via keyboard shortcuts, allowing users who cannot use a mouse to navigate efficiently through the application. Tab navigation is implemented to navigate through all interactive elements in a logical order. Visual indicators are provided to highlight the currently focused element.

### Screen Reader Support

FOCM makes use of alt text to describe images, icons, and other non-textual elements, ensuring compatibility with screen readers. Labels and roles are used for complex elements such as drag-and-drop interfaces or custom controls to convey their purpose and state to screen reader users.

### High Contrast Mode

FOCM supports high contrast themes that make text, icons, and other elements more distinguishable for users with low vision. This feature enhances the visibility and usability of the application for users with visual impairments.

---

Congratulations! You are now familiar with the main functions and features of the File Organizer and Content Manager (FOCM) application. Use this user manual as a reference to make the most out of FOCM and streamline your file management workflow. Enjoy organizing, searching, and managing your local files with ease!