# File Organizer and Content Manager (FOCM) User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a powerful desktop application designed to help users efficiently organize, search, and manage their local files. FOCM aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. It provides a unified interface for managing digital content, supporting various file types, including documents, images, videos, and more.

This user manual will guide you through the installation process, introduce the main features of FOCM, and provide step-by-step instructions on how to use the application effectively.

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
    - Text Size and Font Adjustments
    - Color Blind Mode
    - Magnification and Zoom
    - Feedback and Error Handling

## 1. Installation

To install FOCM, follow these steps:

1. Open a terminal or command prompt.
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

The directory tree pane is located on the left side of the main window. It displays the hierarchical structure of your file system, allowing you to navigate through folders and subfolders. Clicking on a folder will update the content view to show the files within that folder.

### Content View

The content view pane is located on the right side of the main window. It displays the contents of the currently selected directory in the directory tree. You can view files and folders in either list or grid view, depending on your preference.

### Toolbar

The toolbar is located at the top of the main window. It provides quick access to common actions, such as creating a new folder, deleting a file, refreshing the view, toggling between list and grid view, and performing a search. The search bar allows you to enter search criteria and find specific files or folders.

### Status Bar

The status bar is located at the bottom of the main window. It displays information about the selected files and folders, as well as general statistics such as the total number of files and the total size of the selected files.

## 3. Search and Filter Panel

The search and filter panel in FOCM allows you to perform advanced searches and apply filters to narrow down your search results. It can be accessed from the main window by clicking on the search icon or using the keyboard shortcut.

### Basic Search

The basic search functionality allows you to search for files and folders using partial or full file names. Simply enter your search query in the search bar and press Enter. FOCM will display the search results in the content view.

### Advanced Search

FOCM provides advanced search options for more precise filtering. You can perform full-text search within documents, search based on file type, date modified, and size, and even use regular expressions for complex pattern matching.

### Filters

FOCM offers predefined filters to quickly select files based on common criteria such as file type, size, and modification or creation date. You can also create and save custom filters based on any combination of file attributes, including custom tags, project names, or specific content.

## 4. File Preview Window

FOCM provides a file preview window that allows you to quickly preview the selected file without opening it in an external application. The file preview window can be opened as a pop-up or sidebar window, depending on your preference.

### Text Documents and Images

For text documents and images, the file preview window will display a preview of the file within the window itself. You can scroll through the document or image and view its contents without leaving the application.

### Videos and Audio Files

For videos and audio files, the file preview window provides basic playback controls. You can play, pause, stop, and adjust the volume of the media file directly within the preview window.

### Edit Mode for Text Files

FOCM allows you to make quick edits to text files directly within the file preview window. You can enter edit mode, make changes to the file, and save the modifications without opening a separate text editor.

## 5. File Properties and Metadata Editor

FOCM provides a file properties and metadata editor that allows you to view and edit detailed information about a file or folder. You can access the file properties dialog by right-clicking on a file or folder and selecting "Properties" from the context menu.

The file properties dialog displays information such as file size, creation/modification dates, and other metadata tags. You can edit the metadata tags and update the file properties as needed.

## 6. Settings/Preferences Window

FOCM offers a settings/preferences window where you can customize various application settings. You can access the settings window from the main menu.

The settings window allows you to customize the application's theme (dark/light), default views, file organization rules, backup settings, and extension/plugin management. You can tailor FOCM to suit your preferences and workflow.

## 7. Tag Management Interface

FOCM provides a tag management interface that allows you to create, edit, and delete tags. Tags are a flexible way to categorize and locate files quickly. You can assign tags to files or folders from the tag management interface, making it easy to organize and retrieve your files based on specific tags.

The tag management interface suggests existing tags as you type and allows you to create new tags on the fly. You can also create custom categories to group files/folders based on project, client, priority, or any other user-defined category.

## 8. Backup and Synchronization Setup Wizard

FOCM includes a step-by-step backup and synchronization setup wizard that guides you through the process of setting up backup destinations and synchronization options. You can choose to back up your files to external drives or cloud storage services. The wizard allows you to schedule automatic backups and configure synchronization settings according to your needs.

## 9. Help and Tutorial Section

FOCM provides a dedicated help and tutorial section that offers a searchable help database, user manual, and interactive tutorials on key features. You can access the help and tutorial section from the main menu. It provides comprehensive documentation and guidance on how to use FOCM effectively.

## 10. File Organization

FOCM offers powerful file organization features to help you keep your files organized and easily accessible. It supports both automated organization rules and manual tagging and categorization.

### Automated Organization Rules

FOCM allows you to create customizable rules for automatically organizing files. You can define rules based on file type, date criteria, file name patterns, and file size thresholds. You can specify the target folder structure for organized files and even create new folders based on rule criteria, such as date or project name.

### Manual Tagging and Categorization

FOCM allows you to assign custom tags to files and folders manually. You can create tags, assign them to files or folders, and use them to categorize and locate your files quickly. The tagging interface suggests existing tags as you type and allows you to create new tags on the fly. You can also create custom categories to group files/folders based on specific criteria.

### Bulk File Operations

FOCM supports bulk operations to rename, move, copy, or delete multiple files at once. You can select multiple files in the content view and perform these operations with ease. FOCM also provides options for bulk applying tags or moving files to a category. The application includes an undo functionality to revert changes if needed.

### Folder and File Management

FOCM allows you to create, rename, move, and delete files and folders from within the application. You can perform these operations directly in the content view or using the right-click context menu. FOCM also provides a drag-and-drop interface for moving files and folders into different categories or locations.

### Custom Folder Views and Sorting

FOCM allows you to customize how folders and files are displayed in the content view. You can choose between list, grid, or thumbnail views, depending on your preference. FOCM also supports sorting files and folders by name, size, date modified, or custom tags/categories.

### File Watcher and Auto-Update

FOCM implements a file watcher mechanism that automatically updates file organization based on predefined rules when new files are added to monitored folders. This feature ensures that the organization structure is always up-to-date. You can configure the file watcher to work in real-time or at user-defined intervals.

### Integration with File System

FOCM integrates closely with the operating system's file system to reflect changes made within the application in real-time in the user's file explorer or finder. It supports right-click context menu options in the operating system's file explorer, allowing you to quickly tag, categorize, or apply predefined organization rules to selected files or folders.

## 11. Search and Filter

FOCM provides advanced search functionality to help you find files and folders quickly. You can perform searches based on partial or full file names, content-based search within documents or metadata for images and videos, and even use regular expressions for complex pattern matching.

FOCM offers predefined filters to quickly select files based on common criteria such as file type, size, and modification or creation date. You can also create and save custom filter sets based on any combination of file attributes, including custom tags, project names, or specific content.

FOCM supports tag-based searching, allowing you to assign custom tags to files and folders and then search for these tags. It also supports hierarchical tags, which facilitate detailed organization and searching.

FOCM automatically saves recent searches for quick repetition and allows you to save frequently used search queries or filters for quick access. You can export search results to CSV or other formats for external use. Batch operations on search results are also supported, allowing you to apply actions such as move, delete, or tag to multiple files at once.

The right-click context menu in search results provides quick access to common file operations such as open, rename, delete, move, or edit tags. You can preview images, documents, and videos directly in the context menu.

FOCM offers smart suggestions as you type in the search bar, based on your input, historical searches, and commonly accessed files. It suggests tags, filenames, and content snippets as possible search queries, making it easier to find the files you need.

FOCM seamlessly integrates with the file organization system, allowing you to quickly organize search results into folders or tag groups directly from the search interface.

## 12. Additional Features

FOCM includes additional features to enhance your file management experience.

### Content Management

FOCM provides preview capabilities for common file types such as PDF, DOCX, images, and videos. You can view the contents of these files directly within the application, eliminating the need for external applications.

FOCM offers basic editing tools for text files and images. You can perform text formatting and cropping operations directly within the application. For unsupported file types, FOCM integrates with external applications, allowing you to open and edit files using your preferred software.

### Backup and Synchronization

FOCM includes options to back up important files and folders to external drives or cloud storage services. You can configure automatic backups and synchronization settings to ensure that your files are always protected and up-to-date.

### Documentation and Help

FOCM provides comprehensive user documentation and online help resources. The user manual and online documentation offer detailed explanations of FOCM's features and functionality. Interactive tutorials are available to guide you through key features and help you get started quickly.

## 13. Accessibility Features

FOCM includes several accessibility features to ensure that all users can use the application effectively.

### Keyboard Navigation

FOCM supports full functionality via keyboard shortcuts, allowing users who cannot use a mouse to navigate efficiently through the application. Tab navigation is implemented to navigate through all interactive elements in a logical order. Visual indicators are provided to highlight the currently focused element.

### Screen Reader Support

FOCM makes use of alt text to describe images, icons, and other non-textual elements, ensuring compatibility with screen readers. Labels and roles are used for complex elements such as drag-and-drop interfaces or custom controls, ensuring that their purpose and state are conveyed to screen reader users.

### High Contrast Mode

FOCM supports high contrast themes that make text, icons, and other elements more distinguishable for users with low vision. Text readability and visibility of interactive elements against background colors are ensured in high contrast mode.

### Text Size and Font Adjustments

FOCM allows users to adjust the text size without breaking the layout or losing functionality. Support for user-defined system fonts, including those designed for dyslexia, is provided to accommodate users with specific font preferences.

### Color Blind Mode

FOCM implements color schemes that are accessible to users with various types of color blindness. Information conveyed with color is also distinguishable through patterns or shapes, ensuring that users with color blindness can effectively use the application.

### Magnification and Zoom

FOCM ensures that the application's interface and content can be magnified or zoomed in up to 200% without loss of content or functionality. This feature accommodates users with low vision and allows them to view the application's elements clearly.

### Feedback and Error Handling

FOCM provides clear and understandable feedback for actions such as file movement, deletion, or opening errors. Descriptive error messages are displayed, offering guidance on how to resolve issues. The feedback and error messages are accessible via both text and screen readers, ensuring that all users can understand and act upon them.

## Conclusion

The File Organizer and Content Manager (FOCM) is a comprehensive desktop application that offers powerful file organization, search, and management features. With FOCM, you can efficiently organize your files, perform advanced searches, and easily manage your digital content. The application's intuitive interface, customizable settings, and accessibility features make it a valuable tool for enhancing productivity and file management.

We hope this user manual has provided you with a thorough understanding of FOCM's features and how to use them effectively. If you have any further questions or need assistance, please refer to the documentation or reach out to our support team.

Happy file organizing and content management with FOCM!

```