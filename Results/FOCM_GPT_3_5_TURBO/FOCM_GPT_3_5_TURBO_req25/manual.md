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

## 1. Installation

To install FOCM, follow these steps:

1. Open a terminal or command prompt.
2. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Once the installation is complete, you can launch FOCM by running the following command:

   ```
   python main.py
   ```

   This will open the main window of FOCM.

## 2. Main Window

The main window is the central hub of FOCM, featuring a dual-pane layout. One pane displays the directory tree (folders), and the other pane displays the contents of the selected directory.

### Directory Tree

The directory tree pane allows you to navigate through your file system and select folders. To expand or collapse a folder, click on the arrow icon next to the folder name. To select a folder, click on its name.

### Content View

The content view pane displays the contents of the selected directory. By default, the content view displays files and folders in a list format. You can switch to a grid view by clicking the "Toggle View" button in the toolbar.

### Toolbar

The toolbar at the top of the main window provides buttons for common actions. These actions include creating a new folder, deleting a file, refreshing the view, toggling between list/grid view, and searching for files.

### Status Bar

The status bar at the bottom of the main window displays information about the selected files/folders and general statistics, such as the total number of files and the total size.

## 3. Search and Filter Panel

The search and filter panel is a dedicated panel accessible from the main window. It allows you to enter search criteria, choose filters (file type, date modified, size), and display the search results in a list or grid format.

### Basic Search

To perform a basic search, follow these steps:

1. Enter your search query in the search bar.
2. Press the "Search" button or hit Enter.
3. The content view will update to display the search results.

### Advanced Search

FOCM also provides advanced search options for more precise filtering. You can perform a full-text search within documents to find specific content within files. To perform an advanced search, follow these steps:

1. Click on the "Advanced Search" button in the search and filter panel.
2. Enter your search query in the search bar.
3. Choose additional filters, such as file type, date modified, and size.
4. Click the "Search" button to perform the search.
5. The content view will update to display the search results.

## 4. File Preview Window

The file preview window provides a quick preview of the selected file. For text documents and images, the preview is displayed within the window. For videos and audio files, basic playback controls are available.

### Text Documents and Images

When you select a text document or an image file, the file preview window will display the content of the file. For text documents, you can also enter edit mode to make quick edits directly within the preview window.

### Videos and Audio Files

When you select a video or audio file, the file preview window will provide basic playback controls. You can play, pause, stop, and adjust the volume of the media file.

## 5. File Properties and Metadata Editor

FOCM allows you to view and edit detailed information about files and folders. To access the file properties and metadata editor, follow these steps:

1. Right-click on a file or folder in the content view.
2. Select "Properties" from the context menu.
3. A dialog box will appear, displaying information such as file size, creation/modification dates, and metadata tags.
4. You can edit the metadata tags in the dialog box.

## 6. Settings/Preferences Window

The settings/preferences window allows you to customize various application settings. To access the settings/preferences window, follow these steps:

1. Click on the "Settings" or "Preferences" option in the main menu.
2. The settings/preferences window will open, displaying options such as theme selection (dark/light), default views, file organization rules, backup settings, and extension/plugin management.
3. Customize the settings according to your preferences.

## 7. Tag Management Interface

FOCM provides a tag management interface for creating, editing, and deleting tags. You can assign tags to files and folders from this interface, providing a flexible way to categorize and locate files quickly.

To access the tag management interface, follow these steps:

1. Click on the "Tag Management" option in the main menu.
2. The tag management interface will open, displaying existing tags and options to create, edit, and delete tags.
3. To assign a tag to a file or folder, select the file or folder in the content view, and choose the desired tag from the tag management interface.

## 8. Backup and Synchronization Setup Wizard

FOCM includes a step-by-step wizard that guides you through setting up backup destinations and synchronization options. This wizard helps you schedule automatic backups and choose external drives or cloud storage for backup.

To access the backup and synchronization setup wizard, follow these steps:

1. Click on the "Backup and Synchronization" option in the main menu.
2. The setup wizard will open, guiding you through the process of setting up backup destinations and synchronization options.
3. Follow the instructions in the wizard to configure your backup and synchronization settings.

## 9. Help and Tutorial Section

FOCM provides a dedicated help and tutorial section accessible from the main menu. This section offers a searchable help database, a user manual, and interactive tutorials on key features.

To access the help and tutorial section, follow these steps:

1. Click on the "Help" or "Tutorial" option in the main menu.
2. The help and tutorial section will open, providing access to the searchable help database, user manual, and interactive tutorials.

## 10. File Organization

FOCM offers powerful file organization features to help you keep your files organized and easily accessible. These features include automated organization rules, manual tagging and categorization, bulk file operations, and folder and file management.

### Automated Organization Rules

FOCM allows you to create customizable rules for automatically organizing files. These rules can be based on file type, date criteria (creation date, modification date), file name patterns (using wildcards or regular expressions), and file size thresholds. You can specify the target folder structure for organized files and create new folders based on rule criteria (e.g., date, project name).

### Manual Tagging and Categorization

FOCM enables you to assign custom tags to files and folders manually. The application offers a tagging interface that suggests existing tags as you type and allows the creation of new tags. You can also create custom categories to group files and folders based on project, client, priority, or any other user-defined category. You can view and access files by tags and categories through a dedicated interface or filter.

### Bulk File Operations

FOCM supports bulk operations to rename, move, copy, or delete multiple files at once based on user selection. You can also bulk apply tags or move files to a category. The application provides an undo functionality to revert changes if needed.

### Folder and File Management

FOCM allows you to create, rename, move, and delete files and folders from within the application. You can perform these actions directly in the content view or through the context menu.

## Conclusion

Congratulations! You have completed the File Organizer and Content Manager (FOCM) user manual. You should now have a good understanding of how to install FOCM, navigate the main window, perform searches, preview files, manage file properties, customize settings, manage tags, set up backups and synchronization, access help and tutorials, and organize your files effectively.

If you have any further questions or need additional assistance, please refer to the documentation or contact our support team.

Happy organizing and managing your files with FOCM!

```