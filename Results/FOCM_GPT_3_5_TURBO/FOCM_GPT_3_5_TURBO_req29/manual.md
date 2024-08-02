# File Organizer and Content Manager User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a desktop application designed to help users efficiently organize, search, and manage their local files. This software aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. It provides a unified interface for managing digital content and supports various file types, including documents, images, videos, and more.

## Installation

To install the File Organizer and Content Manager, follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

2. Open a command prompt or terminal and navigate to the directory where you want to install the application.

3. Clone the repository by running the following command:

   ```
   git clone https://github.com/your-username/focm.git
   ```

4. Change into the `focm` directory:

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

The main window of the File Organizer and Content Manager is the central hub of the application. It features a dual-pane layout, with one pane for the directory tree (folders) and another for viewing the contents of the selected directory.

### Toolbar

At the top of the main window, you will find a toolbar with buttons for common actions. These buttons allow you to create a new folder, delete a file, refresh the view, toggle between list/grid view, and perform a search.

### Status Bar

At the bottom of the main window, there is a status bar that displays information about the selected files/folders and general statistics, such as the total number of files and total size.

## Search and Filter Panel

The File Organizer and Content Manager provides a dedicated panel for searching and filtering files. This panel is accessible from the main window and allows you to enter search criteria, choose filters (file type, date modified, size), and display the results in a list or grid format.

### Advanced Search Options

For more precise filtering, the application offers advanced search options. These options include full-text search within documents, allowing you to search for specific keywords or phrases within the content of your files.

## File Preview Window

When you select a file in the File Organizer and Content Manager, a file preview window will appear. This window provides a quick preview of the selected file. For text documents and images, the preview will be shown within the window. For videos and audio files, basic playback controls will be available.

### Edit Mode

For text files, the file preview window also includes an edit mode. This mode allows you to make quick edits directly within the preview window, without the need to open a separate text editor.

## File Properties and Metadata Editor

The File Organizer and Content Manager allows you to view and edit the properties and metadata of files and folders. To access this feature, simply right-click on a file or folder and select "Properties" from the context menu. A dialog box will appear, showing detailed information about the selected item, including file size, creation/modification dates, and metadata tags.

## Settings/Preferences Window

The application provides a separate window for customizing the settings and preferences. You can access this window from the main menu. In the settings/preferences window, you can customize various aspects of the application, such as the theme (dark/light), default views, file organization rules, backup settings, and extension/plugin management.

## Tag Management Interface

The File Organizer and Content Manager includes a panel or window for managing tags. From this interface, you can create, edit, and delete tags. You can also assign tags to files or folders, providing a flexible way to categorize and locate your files quickly.

## Backup and Synchronization Setup Wizard

To help you set up backup destinations and synchronization options, the application provides a step-by-step wizard. This wizard guides you through the process of selecting backup destinations (external drive, cloud storage) and setting up automatic backups. You can also schedule the backups to occur at specific times.

## Help and Tutorial Section

The File Organizer and Content Manager includes a dedicated window or section for accessing help and tutorials. You can access this window from the main menu. In the help and tutorial section, you will find a searchable help database, a user manual, and interactive tutorials on key features of the application.

## File Organization

The File Organizer and Content Manager offers various features for organizing your files.

### Automated Organization Rules

The application allows you to create customizable rules for automatically organizing files. These rules can be based on file type, date criteria (creation date, modification date), file name patterns (using wildcards or regular expressions), and file size thresholds. You can specify the target folder structure for organized files, with options to create new folders based on rule criteria, such as date or project name.

### Manual Tagging and Categorization

You can manually assign custom tags to files and folders in the File Organizer and Content Manager. The application offers a tagging interface that suggests existing tags as you type and allows you to create new tags. You can also create custom categories to group files and folders based on project, client, priority, or any other user-defined category. You can view and access files by tags and categories through a dedicated interface or filter.

### Bulk File Operations

The application supports bulk operations for renaming, moving, copying, or deleting multiple files at once. You can select multiple files and perform these operations with ease. The application also includes options for bulk applying tags or moving files to a category. If you make a mistake, the application provides an undo functionality to revert changes if needed.

### Folder and File Management

The File Organizer and Content Manager allows you to create, rename, move, and delete files and folders from within the application. It provides a drag-and-drop interface for moving files and folders into different categories or locations. The application also includes a feature to detect and resolve duplicate files based on name, size, and optionally content hash. You can choose to keep, delete, or merge duplicate files.

### Custom Folder Views and Sorting

You can customize how folders and files are displayed in the File Organizer and Content Manager. The application offers different views, such as list, grid, and thumbnail views. You can also sort files and folders by name, size, date modified, or custom tags/categories.

## Conclusion

The File Organizer and Content Manager is a powerful tool for efficiently organizing, searching, and managing your local files. With its automated organization, advanced search capabilities, and content management features, it enhances productivity and simplifies file management. Whether you need to organize your personal files or manage a large collection of documents, images, and videos, the File Organizer and Content Manager is here to help. Enjoy the benefits of a unified interface and take control of your digital content.