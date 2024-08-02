# File Organizer and Content Manager User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a powerful desktop application designed to help users efficiently organize, search, and manage their local files. With FOCM, you can enhance your productivity and file management through automated organization, advanced search capabilities, and content management features. FOCM supports various file types, including documents, images, videos, and more, providing a unified interface for managing your digital content.

This user manual will guide you through the installation process, introduce the main functions of FOCM, and provide step-by-step instructions on how to use the application effectively.

## Installation

To install FOCM, please follow these steps:

1. Ensure that you have Python installed on your computer. FOCM requires Python 3.7 or higher.

2. Clone the FOCM repository from GitHub or download the source code as a ZIP file.

3. Open a terminal or command prompt and navigate to the directory where you cloned or extracted the FOCM source code.

4. Create a virtual environment (optional but recommended) by running the following command:

   ```
   python -m venv myenv
   ```

5. Activate the virtual environment by running the appropriate command for your operating system:

   - Windows: `myenv\Scripts\activate`
   - macOS/Linux: `source myenv/bin/activate`

6. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

7. Once the installation is complete, you can launch FOCM by running the following command:

   ```
   python main.py
   ```

   The FOCM application window should now appear on your screen.

## Main Window

The main window of FOCM serves as the central hub for managing your files. It features a dual-pane layout, with one pane for the directory tree (folders) and another for viewing the contents of the selected directory.

### Directory Tree

The directory tree pane displays the hierarchical structure of your files and folders. You can navigate through your file system by expanding and collapsing folders. To select a folder, simply click on it in the directory tree.

### Content View

The content view pane displays the files and folders within the selected directory. You can view the contents of a folder by selecting it in the directory tree. The content view supports different display modes, including list view and grid view, which can be toggled using the toolbar buttons.

### Toolbar

The toolbar at the top of the main window provides quick access to common actions. It includes the following buttons:

- **New Folder**: Click this button to create a new folder within the selected directory.
- **Delete File**: Click this button to delete the selected file.
- **Refresh View**: Click this button to refresh the content view and update the file listing.
- **Toggle View**: Click this button to switch between list view and grid view in the content view.
- **Search Bar**: Enter search criteria in the search bar and click the search button to perform a search.

### Status Bar

The status bar at the bottom of the main window displays information about the selected files and folders, as well as general statistics such as the total number of files and the total size.

## Search and Filter Panel

FOCM provides a dedicated search and filter panel that allows you to refine your file search and apply filters based on various criteria. To access the search and filter panel, click on the search button in the toolbar.

### Basic Search

In the search and filter panel, you can enter search criteria to find files and folders based on partial or full file names. Simply enter your search query and click the search button to perform the search. The search results will be displayed in the content view.

### Advanced Search

FOCM also supports advanced search options for more precise filtering. You can search for files containing specific text within documents or metadata for images and videos. Additionally, you can use regular expressions (regex) in your search queries for complex pattern matching.

### Custom Filters

FOCM allows you to create custom filters to quickly select files based on common criteria such as file type, size, and modification or creation date. You can save and apply custom filter sets based on any combination of file attributes, including custom tags, project names, or specific content.

## File Preview Window

FOCM provides a file preview window that allows you to quickly preview the selected file. For text documents and images, the preview will be displayed within the window. For videos and audio files, basic playback controls will be available.

### Edit Mode

For text files, FOCM allows you to make quick edits directly within the preview window. Simply click on the edit button to enter edit mode and make your changes. Once you're done, click the save button to save your changes.

## File Properties and Metadata Editor

FOCM includes a file properties and metadata editor that allows you to view and edit detailed information about a file or folder. To access the file properties and metadata editor, right-click on a file or folder and select "Properties" from the context menu.

The file properties and metadata editor displays information such as file size, creation/modification dates, and allows you to edit metadata tags. You can modify the metadata tags to categorize your files and make them easier to search and manage.

## Settings/Preferences Window

FOCM provides a separate settings/preferences window that allows you to customize various application settings. To access the settings/preferences window, click on the main menu and select "Settings" or "Preferences".

In the settings/preferences window, you can customize the following:

- Theme selection (dark/light)
- Default views (list/grid view)
- File organization rules
- Backup settings
- Extension/plugin management

## Tag Management Interface

FOCM includes a tag management interface that allows you to create, edit, and delete tags. You can assign tags to files or folders from this interface, providing a flexible way to categorize and locate your files quickly.

In the tag management interface, you can create new tags, edit existing tags, and delete tags that are no longer needed. You can also assign tags to files or folders by selecting them and choosing the appropriate tag from the tag management interface.

## Backup and Synchronization Setup Wizard

FOCM provides a step-by-step wizard that guides you through setting up backup destinations and synchronization options. The wizard allows you to choose external drives or cloud storage services as backup destinations and configure automatic backup schedules.

The backup and synchronization setup wizard ensures that your important files and folders are backed up regularly and synchronized across multiple devices or storage locations.

## Help and Tutorial Section

FOCM includes a dedicated help and tutorial section that provides access to a searchable help database, user manual, and interactive tutorials on key features. To access the help and tutorial section, click on the main menu and select "Help" or "Tutorials".

The help and tutorial section is designed to assist you in using FOCM effectively and getting the most out of its features. It provides comprehensive documentation and step-by-step instructions on various aspects of the application.

## File Organization

FOCM offers powerful file organization features to help you keep your files organized and easily accessible. It supports both automated organization rules and manual tagging and categorization.

### Automated Organization Rules

FOCM allows you to create customizable rules for automatically organizing files based on various criteria. You can define rules based on file type, date criteria, file name patterns, and file size thresholds. You can also specify the target folder structure for organized files, including options to create new folders based on rule criteria such as date or project name.

### Manual Tagging and Categorization

FOCM allows you to assign custom tags to files and folders manually. You can create tags, edit existing tags, and assign tags to files or folders using the tag management interface. FOCM also supports the creation of custom categories, where you can group files and folders based on project, client, priority, or any other user-defined category.

You can view and access files by tags and categories through a dedicated interface or filter, making it easy to locate files based on their assigned tags or categories.

### Bulk File Operations

FOCM supports bulk file operations, allowing you to perform actions such as renaming, moving, copying, or deleting multiple files at once. You can select multiple files or folders and apply bulk operations based on your selection. FOCM also provides undo functionality to revert changes if needed.

### Folder and File Management

FOCM allows you to create, rename, move, and delete files and folders directly within the application. You can perform these operations from the main window or the file properties and metadata editor. FOCM provides a drag-and-drop interface for moving files and folders into different categories or locations.

### Duplicate File Detection and Resolution

FOCM includes a feature to detect and resolve duplicate files based on name, size, and optionally content hash. When duplicate files are detected, FOCM offers options to keep, delete, or merge duplicate files. This helps you eliminate duplicate files and keep your file system organized and clutter-free.

### Custom Folder Views and Sorting

FOCM allows you to customize how folders and files are displayed in the content view. You can choose between list view, grid view, or thumbnail view. FOCM also supports sorting files and folders by name, size, date modified, or custom tags/categories. This allows you to organize and view your files in a way that suits your preferences.

### File Watcher and Auto-Update

FOCM implements a file watcher mechanism that automatically updates file organization based on predefined rules when new files are added to monitored folders. This feature works in real-time or at user-defined intervals, ensuring that the organization structure is always up-to-date. FOCM monitors changes in the file system and applies the necessary organization rules to keep your files organized.

### Integration with File System

FOCM integrates closely with the operating system's file system to reflect changes made within the application in real-time in your file explorer or finder. This means that any changes you make to files or folders in FOCM will be immediately visible in your file explorer or finder. FOCM also supports right-click context menu options in the operating system's file explorer, allowing you to quickly tag, categorize, or apply predefined organization rules to selected files or folders.

## Search and Filter

FOCM provides advanced search functionality to help you find files and folders quickly and efficiently. You can search for files and folders using partial or full file names, and FOCM supports content-based search capabilities that allow you to find files containing specific text, even within documents or metadata for images and videos.

### Advanced Search

FOCM supports advanced search options for more precise filtering. You can use regular expressions (regex) in your search queries for complex pattern matching. This allows you to perform advanced searches based on specific patterns or criteria.

### Custom Search Filters

FOCM provides predefined filters to quickly select files based on common criteria such as file type, size, and modification or creation date. You can also create, save, and apply custom filter sets based on any combination of file attributes, including custom tags, project names, or specific content. This allows you to create custom search filters tailored to your specific needs.

### Tag-Based Searching

FOCM integrates a tagging system that allows you to assign custom tags to files and folders. You can then search for files based on these tags. FOCM supports hierarchical tags, which means you can create tag hierarchies to facilitate detailed organization and searching. For example, you can create tags like "Work/Project1" or "Personal/Photos" to categorize your files and make them easier to find.

### Search History and Saved Searches

FOCM automatically saves recent searches, allowing you to quickly repeat previous searches. You can also save frequently used search queries or filters for quick access. This feature helps you save time and effort by eliminating the need to re-enter search criteria or recreate complex filters.

### Search Results Management

FOCM provides various options for managing search results. You can sort search results based on various criteria such as name, size, date modified, and custom tags. You can also export search results to CSV or other formats for external use. Additionally, FOCM supports batch operations on search results, allowing you to apply actions such as move, delete, or tag to multiple files at once.

### Contextual Actions

FOCM offers contextual actions in the search results interface to provide quick access to common file operations. Right-clicking on a file in the search results will display a context menu with options to open, rename, delete, move, or edit tags. Additionally, FOCM provides a preview option directly in the context menu for images, documents, and videos, allowing you to quickly preview files without opening them.

### Smart Suggestions

FOCM provides smart suggestions as you type in the search bar. These suggestions are based on your input, historical searches, and commonly accessed files. FOCM suggests tags, filenames, and content snippets as possible search queries, making it easier and faster to find the files you need.

### Integration with File Organization

FOCM seamlessly integrates with the file organization system, allowing you to quickly organize search results into folders or tag groups directly from the search interface. This integration ensures that your search results are organized and categorized according to your file organization rules, making it easier to manage and access your files.

## Additional Features

FOCM includes additional features to enhance your content management experience.

### Content Management

FOCM provides preview capabilities for common file types such as PDF, DOCX, images, and videos. You can preview these files directly within the application, eliminating the need to open external applications.

For text files and images, FOCM offers basic editing tools such as text formatting and cropping. You can make quick edits to text files and images without leaving the application.

FOCM also integrates with external applications for editing unsupported file types. If you have a specific application installed for editing a particular file type, FOCM can launch that application to open and edit the file.

### Backup and Synchronization

FOCM includes options to backup important files and folders to external drives or cloud storage services. You can configure backup destinations and synchronization options using the backup and synchronization setup wizard. The wizard guides you through the process of setting up automatic backups and ensures that your files are protected and synchronized across multiple devices or storage locations.

## Conclusion

Congratulations! You have now learned how to install and use the File Organizer and Content Manager (FOCM) application. With FOCM, you can efficiently organize, search, and manage your local files, enhancing your productivity and file management capabilities.

If you have any further questions or need assistance, please refer to the help and tutorial section within the application or consult the documentation provided.

Happy organizing and managing your files with FOCM!

```