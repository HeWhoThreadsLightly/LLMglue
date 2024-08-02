# File Organizer and Content Manager (FOCM) User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a desktop application designed to help users efficiently organize, search, and manage their local files. This software aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. FOCM supports various file types, including documents, images, videos, and more, providing a unified interface for managing digital content.

## Installation

To use FOCM, you need to install the following dependencies:

- Python (version 3.6 or higher)
- tkinter (version 8.6 or higher)
- ttk (version 8.6 or higher)

You can install the dependencies by running the following command:

```
pip install -r requirements.txt
```

## Getting Started

To start using FOCM, follow these steps:

1. Clone the FOCM repository or download the source code.

2. Install the required dependencies as mentioned in the Installation section.

3. Open a terminal or command prompt and navigate to the FOCM directory.

4. Run the following command to start the application:

   ```
   python main.py
   ```

5. The FOCM application window will open, displaying a dual-pane layout. The left pane shows the directory tree, and the right pane shows the contents of the selected directory.

## Main Window

The main window of FOCM consists of several components:

### Directory Tree

The left pane of the main window displays the directory tree, allowing you to navigate through your local file system. Clicking on a folder in the directory tree will display its contents in the content view pane.

### Content View

The right pane of the main window displays the contents of the selected directory. You can view files and folders in either list or grid view, depending on your preference.

### Toolbar

The toolbar at the top of the main window provides buttons for common actions:

- **New Folder**: Clicking this button will create a new folder in the current directory.
- **Delete File**: Clicking this button will delete the selected file.
- **Refresh View**: Clicking this button will refresh the content view, updating it with any changes made to the file system.
- **Toggle View**: Clicking this button will toggle between list and grid view in the content view.
- **Search Bar**: The search bar allows you to search for files or folders by entering keywords. Pressing the Enter key will perform the search.

### Status Bar

The status bar at the bottom of the main window displays information about the selected files/folders and general statistics, such as the total number of files and the total size of the selected files/folders.

## Functionality

FOCM provides the following functionality:

- **Create New Folder**: You can create a new folder in the current directory by clicking the "New Folder" button in the toolbar.

- **Delete File**: You can delete a selected file by clicking the "Delete File" button in the toolbar.

- **Refresh View**: You can refresh the content view by clicking the "Refresh View" button in the toolbar. This will update the content view with any changes made to the file system.

- **Toggle View**: You can toggle between list and grid view in the content view by clicking the "Toggle View" button in the toolbar.

- **Search**: You can search for files or folders by entering keywords in the search bar and pressing the Enter key. FOCM will perform the search and display the results in the content view.

## Conclusion

FOCM is a powerful desktop application that helps users efficiently organize, search, and manage their local files. With its automated organization, advanced search capabilities, and content management features, FOCM enhances productivity and simplifies file management. Start using FOCM today to experience a unified interface for managing your digital content.