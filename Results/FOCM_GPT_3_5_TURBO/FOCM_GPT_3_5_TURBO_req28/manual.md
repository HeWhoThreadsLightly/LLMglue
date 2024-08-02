# File Organizer and Content Manager (FOCM) User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a powerful desktop application designed to help users efficiently organize, search, and manage their local files. With FOCM, you can enhance your productivity and file management through automated organization, advanced search capabilities, and content management features. FOCM supports various file types, including documents, images, videos, and more, providing a unified interface for managing your digital content.

This user manual will guide you through the installation process, introduce you to the main functions of FOCM, and provide step-by-step instructions on how to use the application effectively.

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

## 1. Installation

To install FOCM, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where you have downloaded the FOCM package.
3. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Once the installation is complete, you can launch FOCM by running the following command:

   ```
   python main.py
   ```

   The FOCM application window will open, and you can start using the software.

## 2. Main Window

The main window of FOCM is the central hub of the application. It features a dual-pane layout, with one pane for the directory tree (folders) and another for viewing the contents of the selected directory.

### Directory Tree

The directory tree pane displays the file system structure of your local machine. You can navigate through folders and subfolders by expanding and collapsing the tree nodes. To select a directory, simply click on it in the tree.

### Content View

The content view pane displays the contents of the selected directory. It provides a visual representation of the files and folders within the selected directory. You can customize the view mode (list, grid, or thumbnail) to suit your preference.

### Toolbar

The toolbar at the top of the main window contains buttons for common actions. These buttons allow you to perform actions such as creating a new folder, deleting a file, refreshing the view, toggling between list/grid view, and searching for files.

### Status Bar

The status bar at the bottom of the main window displays information about the selected files/folders and general statistics, such as the total number of files and the total size of the selected files/folders.

## 3. Search and Filter Panel

FOCM provides a dedicated search and filter panel that allows you to enter search criteria, choose filters (file type, date modified, size), and display the search results in a list or grid format.

### Basic Search

To perform a basic search, follow these steps:

1. Enter your search query in the search bar located in the toolbar.
2. Press the Enter key or click the search button.
3. FOCM will display the search results in the content view pane.

### Advanced Search

FOCM also provides advanced search options for more precise filtering. You can perform a full-text search within documents, allowing you to search for specific keywords or phrases within the content of your files.

To perform an advanced search, follow these steps:

1. Click on the search and filter panel button in the toolbar.
2. In the search and filter panel, enter your search query in the advanced search field.
3. Choose additional filters, such as file type, date modified, or size, to narrow down your search.
4. Click the search button to perform the search.
5. FOCM will display the search results in the content view pane.

## 4. File Preview Window

FOCM provides a file preview window that allows you to quickly preview the selected file. For text documents and images, the preview will be displayed within the window. For videos and audio files, basic playback controls will be available.

### Text Documents and Images

When you select a text document or an image file, FOCM will display a preview of the file within the file preview window. You can view the content of the text document or the image without opening any external applications.

### Videos and Audio Files

When you select a video or an audio file, FOCM will provide basic playback controls within the file preview window. You can play, pause, stop, and adjust the volume of the media file without leaving the application.

### Edit Mode for Text Files

FOCM allows you to make quick edits to text files directly within the file preview window. You can enter edit mode for a text file by clicking the edit button in the file preview window. Once in edit mode, you can modify the content of the text file and save your changes.

## 5. File Properties and Metadata Editor

FOCM provides a file properties and metadata editor that allows you to view detailed information about a file or folder. You can access the file properties and metadata editor by right-clicking on a file or folder and selecting "Properties" from the context menu.

The file properties and metadata editor displays information such as file size, creation/modification dates, and allows you to edit metadata tags associated with the file or folder.

## 6. Settings/Preferences Window

FOCM offers a settings/preferences window that allows you to customize various application settings. You can access the settings/preferences window from the main menu.

In the settings/preferences window, you can customize the application theme (dark/light), default views, file organization rules, backup settings, and extension/plugin management.

## 7. Tag Management Interface

FOCM provides a tag management interface that allows you to create, edit, and delete tags. You can also assign tags to files or folders from this interface, providing a flexible way to categorize and locate files quickly.

The tag management interface suggests existing tags as you type and allows you to create new tags. You can group files/folders based on project, client, priority, or any other user-defined category using custom tags.

## 8. Backup and Synchronization Setup Wizard

FOCM includes a step-by-step wizard that guides you through setting up backup destinations (external drive, cloud storage) and synchronization options. The wizard allows you to schedule automatic backups and ensures that your files are securely backed up and synchronized.

## 9. Help and Tutorial Section

FOCM provides a dedicated help and tutorial section that offers a searchable help database, user manual, and interactive tutorials on key features. You can access the help and tutorial section from the main menu.

The help and tutorial section is designed to assist you in getting the most out of FOCM and provide answers to common questions or issues you may encounter.

## 10. File Organization

FOCM offers powerful file organization features to help you efficiently manage your files and folders.

### Automated Organization Rules

FOCM allows you to create customizable rules for automatically organizing files. These rules can be based on file type, date criteria (creation date, modification date), file name patterns (using wildcards or regular expressions), and file size thresholds.

You can specify the target folder structure for organized files, with options to create new folders based on rule criteria such as date or project name.

### Manual Tagging and Categorization

FOCM allows you to assign custom tags to files and folders manually. The application offers a tagging interface that suggests existing tags as you type and allows the creation of new tags.

You can create custom categories to group files/folders based on project, client, priority, or any other user-defined category. FOCM provides a dedicated interface or filter to view and access files by tags and categories.

### Bulk File Operations

FOCM supports bulk operations to rename, move, copy, or delete multiple files at once based on user selection. You can select multiple files or folders and perform these operations in a single action.

FOCM also includes options for bulk applying tags or moving files to a category. The application provides undo functionality to revert changes if needed.

### Folder and File Management

FOCM allows you to create, rename, move, and delete files and folders from within the application. You can perform these actions directly in the content view pane or using the context menu.

The application provides a drag-and-drop interface for moving files and folders into different categories or locations. You can easily organize your files by simply dragging and dropping them to the desired destination.

### Duplicate File Detection and Resolution

FOCM includes a feature to detect and resolve duplicate files based on name, size, and optionally content hash. The application offers options to keep, delete, or merge duplicate files, allowing you to efficiently manage your file duplicates.

### Custom Folder Views and Sorting

FOCM allows you to customize how folders and files are displayed in the content view pane. You can choose between list, grid, or thumbnail views to suit your preference. Additionally, you can customize the sorting order of files and folders based on various criteria.

Congratulations! You are now familiar with the main functions of the File Organizer and Content Manager (FOCM) application. Use this user manual as a reference to make the most out of FOCM and efficiently manage your local files. If you have any further questions or need assistance, please refer to the help and tutorial section or reach out to our support team.

Happy organizing and managing your files with FOCM!

```