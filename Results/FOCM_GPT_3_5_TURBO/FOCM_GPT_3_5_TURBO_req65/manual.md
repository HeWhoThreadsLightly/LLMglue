# File Organizer and Content Manager User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a desktop application designed to help users efficiently organize, search, and manage their local files. This software aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. It provides a unified interface for managing digital content and supports various file types, including documents, images, videos, and more.

## Installation

To install the File Organizer and Content Manager, follow these steps:

1. Ensure that you have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

2. Download the FOCM source code from the provided link.

3. Open a terminal or command prompt and navigate to the directory where you downloaded the source code.

4. Create a virtual environment for the FOCM application by running the following command:

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

7. Once the dependencies are installed, you can launch the FOCM application by running the following command:

   ```
   python main.py
   ```

## Getting Started

When you launch the FOCM application, you will see the main window with a dual-pane layout. The left pane displays the directory tree, and the right pane displays the contents of the selected directory.

### Main Window

The main window of the FOCM application consists of the following components:

- Directory Tree: This pane displays the directory structure of your local files. You can navigate through the folders by expanding and collapsing the tree nodes.

- Content View: This pane displays the contents of the selected directory. You can view files and folders in either list or grid view.

- Toolbar: The toolbar at the top of the main window contains buttons for common actions, such as creating a new folder, deleting a file, refreshing the view, toggling between list and grid view, and a search bar for performing searches.

- Status Bar: The status bar at the bottom of the main window displays information about the selected files/folders and general statistics, such as the total number of files and total size.

### Creating a New Folder

To create a new folder in the FOCM application, follow these steps:

1. Select the directory where you want to create the new folder in the directory tree.

2. Click the "New Folder" button in the toolbar.

3. Enter the name of the new folder in the dialog box that appears.

4. Click "OK" to create the new folder.

### Deleting a File

To delete a file in the FOCM application, follow these steps:

1. Select the file you want to delete in the content view.

2. Click the "Delete File" button in the toolbar.

3. Confirm the deletion in the dialog box that appears.

### Refreshing the View

To refresh the view in the FOCM application, follow these steps:

1. Click the "Refresh View" button in the toolbar.

### Toggling Between List and Grid View

To toggle between list and grid view in the FOCM application, follow these steps:

1. Click the "Toggle View" button in the toolbar.

### Performing a Search

To perform a search in the FOCM application, follow these steps:

1. Enter the search criteria in the search bar in the toolbar.

2. Press Enter or click the "Search" button.

3. The search results will be displayed in the content view.

## Advanced Features

The FOCM application also includes several advanced features to enhance file organization, search, and content management. These features include:

- Automated Organization Rules: You can create customizable rules for automatically organizing files based on file type, date criteria, file name patterns, and file size thresholds. You can specify the target folder structure for organized files and create new folders based on rule criteria.

- Manual Tagging and Categorization: You can assign custom tags to files and folders manually. The application offers a tagging interface that suggests existing tags and allows the creation of new tags. You can also create custom categories to group files/folders based on project, client, priority, or any other user-defined category.

- Bulk File Operations: The application supports bulk operations to rename, move, copy, or delete multiple files at once. You can also bulk apply tags or move files to a category, with undo functionality to revert changes if needed.

- Folder and File Management: You can create, rename, move, and delete files and folders from within the application. The application provides a drag-and-drop interface for moving files and folders into different categories or locations. It also includes a feature to detect and resolve duplicate files based on name, size, and optionally content hash.

- Custom Folder Views and Sorting: You can customize how folders and files are displayed in the application, including list, grid, and thumbnail views. You can also sort files and folders by name, size, date modified, or custom tags/categories.

- File Watcher and Auto-Update: The application implements a file watcher mechanism that automatically updates file organization based on predefined rules when new files are added to monitored folders. This feature works in real-time or at user-defined intervals to ensure the organization structure is always up-to-date.

- Integration with File System: The application integrates closely with the operating system's file system to reflect changes made within the app in real-time in the user's file explorer or finder. It also supports right-click context menu options in the operating system's file explorer to quickly tag, categorize, or apply predefined organization rules to selected files or folders.

- Advanced Search Functionality: The application provides advanced search capabilities, including partial or full file name search, content-based search within documents or metadata for images and videos, and support for regular expressions in search queries for complex pattern matching. It also includes predefined filters and user-defined filters for quick and customized file selection.

- Tag-Based Searching: The application integrates a tagging system where you can assign custom tags to files and folders and then search for these tags. It supports hierarchical tags to facilitate detailed organization and searching.

- Search History and Saved Searches: The application automatically saves recent searches for quick repetition. You can also save frequently used search queries or filters for quick access.

- Contextual Actions: The application provides a right-click context menu in search results to provide quick access to common file operations like open, rename, delete, move, or edit tags. It also includes a preview option directly in the context menu for images, documents, and videos.

- Smart Suggestions: As you type in the search bar, the application offers smart suggestions based on your input, historical searches, and commonly accessed files. It suggests tags, filenames, and content snippets as possible search queries.

- Integration with File Organization: The application seamlessly integrates with the file organization system, allowing you to quickly organize search results into folders or tag groups directly from the search interface.

## Conclusion

The File Organizer and Content Manager (FOCM) is a powerful desktop application that helps you efficiently organize, search, and manage your local files. With its automated organization, advanced search capabilities, and content management features, FOCM enhances your productivity and simplifies file management. Whether you need to organize files based on rules, manually tag and categorize files, perform advanced searches, or manage your files and folders, FOCM provides a unified interface and a range of features to meet your needs. Enjoy using FOCM and stay organized!