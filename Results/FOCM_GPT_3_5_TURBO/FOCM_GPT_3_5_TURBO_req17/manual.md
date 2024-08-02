# File Organizer and Content Manager (FOCM) User Manual

## Introduction

Welcome to the user manual for the File Organizer and Content Manager (FOCM) desktop application. FOCM is designed to help you efficiently organize, search, and manage your local files, enhancing your productivity and file management capabilities. This manual will guide you through the installation process, introduce you to the main functions of the software, and provide instructions on how to use it effectively.

## Table of Contents

1. Installation
2. Main Functions
   - User Interface
   - Directory Tree
   - Content View
   - Toolbar
   - Status Bar
   - Search and Filter Panel
   - File Preview Window
   - File Properties and Metadata Editor
   - Settings/Preferences Window
   - Tag Management Interface
   - Backup and Synchronization Setup Wizard
   - Help and Tutorial Section
   - File Organization Rules
3. Usage Instructions
   - Creating a New Folder
   - Deleting a File
   - Refreshing the View
   - Toggling between List/Grid View
   - Performing a Search
   - Updating the Directory Tree
   - Updating the Content View

## 1. Installation

To install FOCM, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where you have downloaded the FOCM files.
3. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Once the installation is complete, you can launch FOCM by running the following command:

   ```
   python main.py
   ```

   The FOCM application window will open, and you can start using the software.

## 2. Main Functions

### User Interface

The FOCM user interface consists of several components:

- Main Window: The central hub of the application featuring a dual-pane layout. One pane displays the directory tree (folders), and the other pane shows the contents of the selected directory.
- Toolbar: A toolbar at the top with buttons for common actions, such as creating a new folder, deleting a file, refreshing the view, toggling between list/grid view, and a search bar.
- Status Bar: A status bar at the bottom displaying information about the selected files/folders and general statistics, such as the total number of files and total size.

### Directory Tree

The directory tree pane in the main window displays the file system structure. You can navigate through folders by expanding and collapsing the tree nodes. Clicking on a folder will display its contents in the content view pane.

### Content View

The content view pane in the main window shows the contents of the selected directory. Files and folders are displayed in a list or grid format, depending on the view mode. You can switch between list and grid view using the toggle view button in the toolbar.

### Toolbar

The toolbar at the top of the main window provides buttons for common actions:

- New Folder: Clicking this button will create a new folder in the selected directory.
- Delete File: Clicking this button will delete the selected file.
- Refresh View: Clicking this button will refresh the view, updating the directory tree and content view.
- Toggle View: Clicking this button will toggle between list and grid view in the content view.
- Search Bar: Enter search criteria in the search bar and click the search button to perform a search.

### Status Bar

The status bar at the bottom of the main window displays information about the selected files/folders and general statistics. It shows the total number of files and the total size of the selected files/folders.

### Search and Filter Panel

The search and filter panel is a dedicated panel accessible from the main window. It allows you to enter search criteria, choose filters (file type, date modified, size), and display the search results in a list or grid format. Advanced search options, including full-text search within documents, are also available.

### File Preview Window

The file preview window is a pop-up or sidebar window that provides a quick preview of the selected file. For text documents and images, the preview is shown within the window. For videos and audio files, basic playback controls are provided.

### File Properties and Metadata Editor

The file properties and metadata editor is a dialog box that displays detailed information about a selected file/folder. It shows file size, creation/modification dates, and allows you to edit metadata tags.

### Settings/Preferences Window

The settings/preferences window is a separate window accessible from the main menu. It allows you to customize application settings, such as theme selection (dark/light), default views, file organization rules, backup settings, and extension/plugin management.

### Tag Management Interface

The tag management interface is a panel or window for creating, editing, and deleting tags. You can assign tags to files or folders from this interface, providing a flexible way to categorize and locate files quickly.

### Backup and Synchronization Setup Wizard

The backup and synchronization setup wizard is a step-by-step wizard that guides you through setting up backup destinations (external drive, cloud storage) and synchronization options, including scheduling automatic backups.

### Help and Tutorial Section

The help and tutorial section is a dedicated window or section accessible from the main menu. It offers a searchable help database, user manual, and interactive tutorials on key features.

### File Organization Rules

FOCM allows you to create customizable rules for automatically organizing files. These rules can be based on file type, date criteria (creation date, modification date), file name patterns (using wildcards or regular expressions), and file size thresholds.

## 3. Usage Instructions

### Creating a New Folder

To create a new folder in the selected directory, follow these steps:

1. Select the directory in the directory tree where you want to create the new folder.
2. Click the "New Folder" button in the toolbar.
3. Enter the name of the new folder in the dialog box that appears.
4. Click "OK" to create the new folder.

### Deleting a File

To delete a file, follow these steps:

1. Select the file in the content view.
2. Click the "Delete File" button in the toolbar.
3. Confirm the deletion in the dialog box that appears.

### Refreshing the View

To refresh the view and update the directory tree and content view, click the "Refresh View" button in the toolbar.

### Toggling between List/Grid View

To switch between list and grid view in the content view, click the "Toggle View" button in the toolbar.

### Performing a Search

To perform a search, follow these steps:

1. Enter the search criteria in the search bar.
2. Click the search button in the toolbar.
3. The search results will be displayed in the content view.

### Updating the Directory Tree

To update the directory tree with the current file system structure, click the "Refresh View" button in the toolbar.

### Updating the Content View

To update the content view with a specific list of files, pass the list of files to the `update_content_view` method in the code. This can be done programmatically or through user interaction.

## Conclusion

Congratulations! You have completed the user manual for the File Organizer and Content Manager (FOCM) desktop application. You should now have a good understanding of how to install FOCM, navigate its user interface, and use its main functions effectively. If you have any further questions or need assistance, please refer to the documentation or contact our support team. Happy file organizing and content managing!