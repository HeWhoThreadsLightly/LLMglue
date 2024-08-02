# File Organizer and Content Manager (FOCM) User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a desktop application designed to help users efficiently organize, search, and manage their local files. This software aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. FOCM supports various file types, including documents, images, videos, and more, providing a unified interface for managing digital content.

## Installation

To use FOCM, you need to install the following dependencies:

- Python (version 3.7 or higher)
- tkinter (version 8.6)
- Pillow (version 8.3.2)
- pywin32 (version 301)
- python-magic (version 0.4.24)

You can install these dependencies by running the following command:

```
pip install -r requirements.txt
```

## Getting Started

To start using FOCM, follow these steps:

1. Clone the FOCM repository or download the source code.
2. Install the required dependencies as mentioned in the installation section.
3. Open a terminal or command prompt and navigate to the FOCM directory.
4. Run the following command to start the application:

```
python main.py
```

5. The FOCM main window will open, featuring a dual-pane layout with a directory tree on the left and the contents of the selected directory on the right.

## Main Window

The FOCM main window serves as the central hub of the application. It consists of the following components:

- Directory Tree: The left pane displays a directory tree, allowing you to navigate through folders and select a directory.
- Content View: The right pane shows the contents of the selected directory, including files and subfolders.
- Toolbar: The toolbar at the top provides buttons for common actions, such as creating a new folder, deleting a file, refreshing the view, toggling between list/grid view, and a search bar.
- Status Bar: The status bar at the bottom displays information about the selected files/folders and general statistics, such as the total number of files and total size.

## Search and Filter Panel

FOCM provides a dedicated search and filter panel to help you find specific files based on search criteria and filters. The search and filter panel can be accessed from the main window and offers the following features:

- Search Criteria: Enter search keywords to find files matching the specified criteria.
- Filters: Choose filters such as file type, date modified, and size to narrow down the search results.
- Display Format: Choose to display the search results in a list or grid format.

Additionally, FOCM offers advanced search options, including full-text search within documents, allowing for more precise filtering.

## File Preview Window

FOCM provides a file preview window that allows you to quickly preview the selected file. The file preview window can be opened as a pop-up or sidebar window and offers the following features:

- Text Documents and Images: Show a preview of the file within the window.
- Videos and Audio Files: Provide basic playback controls for videos and audio files.

For text files, FOCM also offers an edit mode, enabling users to make quick edits directly within the preview window.

## File Properties and Metadata Editor

FOCM includes a file properties and metadata editor that allows you to view and edit detailed information about a file or folder. To access the file properties and metadata editor, right-click on a file or folder and select "Properties" from the context menu. The file properties and metadata editor display information such as file size, creation/modification dates, and allow you to edit metadata tags.

## Settings/Preferences Window

FOCM provides a separate settings/preferences window accessible from the main menu. This window allows you to customize various application settings, including:

- Theme Selection: Choose between dark and light themes.
- Default Views: Set default views for the directory tree and content view.
- File Organization Rules: Define rules for automated file organization.
- Backup Settings: Configure backup destinations and synchronization options.
- Extension/Plugin Management: Manage extensions and plugins for additional functionality.

## Tag Management Interface

FOCM offers a tag management interface that allows you to create, edit, and delete tags. You can also assign tags to files or folders from this interface, providing a flexible way to categorize and locate files quickly.

## Backup and Synchronization Setup Wizard

FOCM includes a step-by-step backup and synchronization setup wizard. This wizard guides you through the process of setting up backup destinations, such as external drives or cloud storage, and configuring synchronization options, including scheduling automatic backups.

## Conclusion

With the File Organizer and Content Manager (FOCM), you can efficiently organize, search, and manage your local files. Its automated organization, advanced search capabilities, and content management features enhance productivity and simplify file management. Start using FOCM today to experience a unified interface for managing your digital content.