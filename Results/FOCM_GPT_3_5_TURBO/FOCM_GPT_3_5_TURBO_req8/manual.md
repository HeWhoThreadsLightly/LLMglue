# File Organizer and Content Manager (FOCM) User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a desktop application designed to help users efficiently organize, search, and manage their local files. This software aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. FOCM supports various file types, including documents, images, videos, and more, providing a unified interface for managing digital content.

## Installation

To install FOCM, follow these steps:

1. Ensure that you have Python installed on your system. FOCM is developed using Python, so it requires a Python environment to run.

2. Clone or download the FOCM repository from [GitHub](https://github.com/your-repository-link).

3. Open a terminal or command prompt and navigate to the FOCM directory.

4. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary packages, including tkinter and Pillow.

5. Once the dependencies are installed, you can run FOCM by executing the following command:

   ```
   python main.py
   ```

   This will launch the FOCM application.

## User Interface

FOCM provides a user-friendly interface with several key components:

### Main Window

The main window is the central hub of the application. It features a dual-pane layout, with one pane for the directory tree (folders) and another for viewing the contents of the selected directory. The directory tree allows you to navigate through your file system, while the content view displays the files and folders within the selected directory.

### Toolbar

The toolbar, located at the top of the main window, provides buttons for common actions. These actions include creating a new folder, deleting a file, refreshing the view, toggling between list/grid view, and searching for files. The search bar allows you to enter search criteria and perform searches within the application.

### Status Bar

The status bar, located at the bottom of the main window, displays information about the selected files/folders and general statistics. It shows the total number of files and the total size of the selected files/folders.

### Search and Filter Panel

The search and filter panel is a dedicated panel accessible from the main window. It allows you to enter search criteria, choose filters (file type, date modified, size), and display the search results in a list or grid format. Advanced search options are available for more precise filtering, including full-text search within documents.

### File Preview Window

The file preview window is a pop-up or sidebar window that provides a quick preview of the selected file. For text documents and images, it shows a preview within the window. For videos and audio files, it provides basic playback controls. The file preview window also supports edit mode for text files, enabling users to make quick edits directly within the preview window.

### File Properties and Metadata Editor

The file properties and metadata editor is a dialog box that displays when a user selects "Properties" from the context menu of a file/folder. It shows detailed information about the file, including file size, creation/modification dates, and allows the user to edit metadata tags.

## Usage

FOCM provides a range of features to help you efficiently organize, search, and manage your local files. Here are some key actions you can perform:

### Creating a New Folder

To create a new folder, follow these steps:

1. Select the directory in which you want to create the new folder in the directory tree pane.

2. Click the "New Folder" button in the toolbar.

3. Enter the name of the new folder in the dialog box that appears.

4. Click "OK" to create the new folder.

### Deleting a File

To delete a file, follow these steps:

1. Select the file you want to delete in the content view pane.

2. Click the "Delete File" button in the toolbar.

3. Confirm the deletion in the dialog box that appears.

### Refreshing the View

To refresh the view, follow these steps:

1. Click the "Refresh View" button in the toolbar.

2. The directory tree and content view will be updated to reflect the current file system structure.

### Toggling Between List/Grid View

To toggle between list and grid view, follow these steps:

1. Click the "Toggle View" button in the toolbar.

2. The content view will switch between list and grid view, depending on the current view.

### Searching for Files

To search for files, follow these steps:

1. Enter your search criteria in the search bar in the toolbar.

2. Click the "Search" button in the toolbar.

3. The search results will be displayed in the content view pane.

### Editing Text Files

To edit a text file, follow these steps:

1. Select the text file you want to edit in the content view pane.

2. Open the file preview window by double-clicking the file or selecting "Preview" from the context menu.

3. Click the "Edit" button in the file preview window.

4. Make your edits in the text editor that appears.

5. Click "Save" to save your changes.

### Viewing File Properties and Editing Metadata

To view file properties and edit metadata, follow these steps:

1. Right-click on the file or folder for which you want to view properties.

2. Select "Properties" from the context menu.

3. The file properties and metadata editor will appear, displaying detailed information about the file.

4. Edit the metadata tags as desired.

5. Click "OK" to save the changes.

## Conclusion

FOCM is a powerful desktop application that helps you efficiently organize, search, and manage your local files. With its automated organization, advanced search capabilities, and content management features, FOCM enhances productivity and simplifies file management. Use this user manual as a guide to make the most of FOCM and streamline your file management workflow.

If you have any further questions or need assistance, please refer to the documentation or contact our support team.

Happy organizing and managing your files with FOCM!

```