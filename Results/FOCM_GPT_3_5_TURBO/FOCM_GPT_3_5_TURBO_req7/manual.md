# File Organizer and Content Manager (FOCM) User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a desktop application designed to help users efficiently organize, search, and manage their local files. This software aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. FOCM supports various file types, including documents, images, videos, and more, providing a unified interface for managing digital content.

## Installation

To use FOCM, you need to install the required dependencies. Follow the steps below to install the necessary environment dependencies:

1. Open a terminal or command prompt.
2. Navigate to the directory where you have downloaded the FOCM application files.
3. Run the following command to install the dependencies:

   ```
   pip install -r requirements.txt
   ```

   This command will install the required dependencies, including `tkinter` and `Pillow`.

## Getting Started

Once you have installed the dependencies, you can start using FOCM. Follow the steps below to get started:

1. Open a terminal or command prompt.
2. Navigate to the directory where you have downloaded the FOCM application files.
3. Run the following command to start the application:

   ```
   python main.py
   ```

   This command will launch the FOCM application.

## Main Window

The main window of FOCM is the central hub of the application. It features a dual-pane layout, with one pane for the directory tree (folders) and another for viewing the contents of the selected directory.

### Toolbar

The main window includes a toolbar at the top with buttons for common actions. The available buttons are:

- **New Folder**: Click this button to create a new folder.
- **Delete File**: Click this button to delete a file.
- **Refresh View**: Click this button to refresh the view.
- **Toggle View**: Click this button to toggle between list and grid view.
- **Search Bar**: Enter search criteria in the search bar and click the search button to perform a search.

### Status Bar

The main window also includes a status bar at the bottom. It displays information about the selected files/folders and general statistics, such as the total number of files and total size.

## Search and Filter Panel

FOCM provides a dedicated panel for searching and filtering files. This panel is accessible from the main window. It allows users to enter search criteria, choose filters (file type, date modified, size), and display results in a list or grid format.

### Advanced Search Options

FOCM also offers advanced search options for more precise filtering. These options include full-text search within documents, allowing users to search for specific content within files.

## File Preview Window

FOCM provides a file preview window that allows users to quickly preview selected files. For text documents and images, the preview is shown within the window. For videos and audio files, basic playback controls are provided.

### Edit Mode

For text files, FOCM offers an edit mode that enables users to make quick edits directly within the preview window. This feature allows for easy modification of text files without the need to open a separate text editor.

## Conclusion

FOCM is a powerful desktop application for organizing, searching, and managing local files. With its automated organization, advanced search capabilities, and content management features, FOCM enhances productivity and simplifies file management. Follow the instructions in this user manual to install and use FOCM effectively.