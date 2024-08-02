# File Organizer and Content Manager (FOCM) User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a desktop application designed to help users efficiently organize, search, and manage their local files. This software aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. FOCM supports various file types, including documents, images, videos, and more, providing a unified interface for managing digital content.

## Installation

To install FOCM, follow these steps:

1. Ensure that you have Python installed on your system. FOCM is developed using Python and requires it to run.

2. Clone the FOCM repository from GitHub or download the source code as a ZIP file.

3. Open a terminal or command prompt and navigate to the directory where you cloned or extracted the FOCM source code.

4. Create a virtual environment for FOCM using the following command:

   ```
   python -m venv focm-env
   ```

5. Activate the virtual environment by running the appropriate command for your operating system:

   - Windows: `focm-env\Scripts\activate`
   - macOS/Linux: `source focm-env/bin/activate`

6. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

7. Once the installation is complete, you can launch FOCM by running the following command:

   ```
   python main.py
   ```

## User Interface

FOCM provides a user-friendly interface to manage your files. Here are the main components of the user interface:

### Main Window

The main window is the central hub of the application. It features a dual-pane layout, with one pane for the directory tree (folders) and another for viewing the contents of the selected directory.

### Toolbar

The toolbar is located at the top of the main window and provides buttons for common actions. These actions include creating a new folder, deleting a file, refreshing the view, toggling between list/grid view, and a search bar.

### Status Bar

The status bar is located at the bottom of the main window and displays information about the selected files/folders and general statistics, such as the total number of files and total size.

### Search and Filter Panel

The search and filter panel is a dedicated panel accessible from the main window. It allows users to enter search criteria, choose filters (file type, date modified, size), and display results in a list or grid format. Advanced search options, including full-text search within documents, are also available.

## Using FOCM

FOCM provides several features to help you efficiently organize, search, and manage your files. Here are some common tasks and how to perform them using FOCM:

### Creating a New Folder

To create a new folder, follow these steps:

1. Click on the "New Folder" button in the toolbar.

2. A dialog box will appear asking for the folder name. Enter the desired name and click "OK".

3. The new folder will be created in the currently selected directory.

### Deleting a File

To delete a file, follow these steps:

1. Select the file you want to delete in the content view pane.

2. Click on the "Delete File" button in the toolbar.

3. A confirmation dialog box will appear asking if you want to delete the file. Click "Yes" to proceed with the deletion.

4. The file will be permanently deleted from your system.

### Refreshing the View

To refresh the view and update the file list, follow these steps:

1. Click on the "Refresh View" button in the toolbar.

2. The content view pane will be updated to reflect any changes in the selected directory.

### Toggling between List/Grid View

FOCM allows you to switch between list and grid view for the content display. To toggle between these views, follow these steps:

1. Click on the "Toggle View" button in the toolbar.

2. The content view pane will switch between list and grid view, depending on the current display mode.

### Performing a Search

FOCM provides powerful search capabilities to help you find files based on specific criteria. To perform a search, follow these steps:

1. Enter your search query in the search bar located in the toolbar.

2. Click on the "Search" button or press Enter.

3. FOCM will display the search results in the content view pane, based on the search criteria.

4. You can further refine your search by using the advanced search options available in the search and filter panel.

## Conclusion

FOCM is a powerful desktop application that helps you efficiently organize, search, and manage your local files. With its automated organization, advanced search capabilities, and content management features, FOCM enhances productivity and simplifies file management. Follow the installation instructions and explore the user interface to start using FOCM and experience its benefits.