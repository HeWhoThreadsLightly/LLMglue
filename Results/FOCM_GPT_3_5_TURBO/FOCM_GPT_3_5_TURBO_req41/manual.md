# File Organizer and Content Manager (FOCM) User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a desktop application designed to help users efficiently organize, search, and manage their local files. This software aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. FOCM provides a unified interface for managing digital content and supports various file types, including documents, images, videos, and more.

This user manual will guide you through the installation process, introduce the main functions of FOCM, and provide instructions on how to use the application effectively.

## Installation

FOCM is developed using Python programming language and requires certain dependencies to be installed. Please follow the steps below to install the necessary environment dependencies:

1. Ensure that Python is installed on your system. You can download Python from the official website: https://www.python.org/downloads/

2. Clone or download the FOCM repository from the GitHub repository: [FOCM GitHub Repository](https://github.com/your-repository-link)

3. Navigate to the downloaded FOCM directory using the command line or terminal.

4. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary dependencies specified in the requirements.txt file.

5. Once the dependencies are installed, you can launch FOCM by running the following command:

   ```
   python main.py
   ```

   This will start the FOCM application.

## Main Functions

FOCM provides a range of features to help you organize, search, and manage your files effectively. The main functions of FOCM are as follows:

### User Interface

FOCM has a user-friendly interface with the following components:

1. Main Window: The central hub of the application featuring a dual-pane layout. One pane displays the directory tree (folders), and the other pane shows the contents of the selected directory.

2. Toolbar: A toolbar at the top of the main window with buttons for common actions such as creating a new folder, deleting a file, refreshing the view, toggling between list/grid view, and a search bar.

3. Status Bar: A status bar at the bottom of the main window displaying information about the selected files/folders and general statistics such as the total number of files and total size.

4. Search and Filter Panel: A dedicated panel accessible from the main window that allows users to enter search criteria, choose filters (file type, date modified, size), and display results in a list or grid format.

5. File Preview Window: A pop-up or sidebar window that provides a quick preview of the selected file. For text documents and images, a preview is shown within the window. For videos and audio files, basic playback controls are provided.

6. File Properties and Metadata Editor: A dialog box that displays detailed information about a selected file/folder, including file size, creation/modification dates. It also allows the user to edit metadata tags.

7. Settings/Preferences Window: A separate window accessible from the main menu that allows users to customize application settings such as theme selection (dark/light), default views, file organization rules, backup settings, and extension/plugin management.

8. Tag Management Interface: A panel or window for creating, editing, and deleting tags. Users can assign tags to files or folders from this interface, providing a flexible way to categorize and locate files quickly.

9. Backup and Synchronization Setup Wizard: A step-by-step wizard that guides users through setting up backup destinations (external drive, cloud storage) and synchronization options, including scheduling automatic backups.

10. Help and Tutorial Section: A dedicated window or section accessible from the main menu that offers a searchable help database, user manual, and interactive tutorials on key features.

### File Organization

FOCM provides powerful file organization features to help you keep your files organized:

1. Automated Organization Rules: FOCM allows users to create customizable rules for automatically organizing files based on file type, date criteria, file name patterns, and file size thresholds. Users can specify the target folder structure for organized files and create new folders based on rule criteria.

2. Manual Tagging and Categorization: Users can assign custom tags to files and folders manually. FOCM offers a tagging interface that suggests existing tags as the user types and allows the creation of new tags. Users can also create custom categories to group files/folders based on project, client, priority, or any other user-defined category.

3. Bulk File Operations: FOCM supports bulk operations to rename, move, copy, or delete multiple files at once based on user selection. Users can also bulk apply tags or move files to a category, with undo functionality to revert changes if needed.

4. Folder and File Management: Users can create, rename, move, and delete files and folders from within the application. FOCM provides a drag-and-drop interface for moving files and folders into different categories or locations. It also includes a feature to detect and resolve duplicate files based on name, size, and optionally content hash.

5. Custom Folder Views and Sorting: FOCM allows users to customize how folders and files are displayed with options for list, grid, and thumbnail views. Users can sort files and folders by name, size, date modified, or custom tags/categories.

6. File Watcher and Auto-Update: FOCM implements a file watcher mechanism that automatically updates file organization based on predefined rules when new files are added to monitored folders. This feature works in real-time or at user-defined intervals, ensuring the organization structure is always up-to-date.

7. Integration with File System: FOCM integrates closely with the operating system's file system to reflect changes made within the app in real-time in the user's file explorer or finder. It supports right-click context menu options in the operating system's file explorer to quickly tag, categorize, or apply predefined organization rules to selected files or folders.

### Search and Filter

FOCM provides advanced search and filter capabilities to help you find files and folders quickly:

1. Advanced Search Functionality: FOCM allows you to search for files and folders using partial or full file names. It also supports content-based search capabilities, allowing you to find files containing specific text, even within documents or metadata for images and videos. Regular expressions (regex) can be used in search queries for complex pattern matching.

2. Custom Search Filters: FOCM offers predefined filters to quickly select files based on common criteria such as file type, size, and modification or creation date. Users can also create, save, and apply custom filter sets based on any combination of file attributes, including custom tags, project names, or specific content.

3. Tag-Based Searching: FOCM integrates a tagging system where users can assign custom tags to files and folders. Users can search for files based on these tags. FOCM supports hierarchical tags to facilitate detailed organization and searching.

4. Search History and Saved Searches: FOCM automatically saves recent searches, allowing you to quickly repeat previous searches.

## Conclusion

FOCM is a powerful desktop application that helps you efficiently organize, search, and manage your local files. With its automated organization, advanced search capabilities, and content management features, FOCM enhances productivity and simplifies file management. By following this user manual, you can make the most of FOCM and effectively manage your digital content.

If you have any further questions or need assistance, please refer to the FOCM Help and Tutorial section or contact our support team.

Happy organizing and managing your files with FOCM!

```