# File Organizer and Content Manager (FOCM) User Manual

## Introduction

Welcome to the user manual for the File Organizer and Content Manager (FOCM) desktop application. FOCM is designed to help you efficiently organize, search, and manage your local files, enhancing productivity and file management through automated organization, advanced search capabilities, and content management features.

This manual will guide you through the installation process, provide an overview of the main functions of FOCM, and explain how to use the application effectively.

## Table of Contents

1. Installation
2. Main Functions
   - User Interface
   - File Organization
   - Search and Filter
   - Content Management
3. Usage Guide
   - Organizing Files
   - Searching and Filtering
   - Managing Content
4. Troubleshooting
5. Frequently Asked Questions (FAQs)
6. Contact Support

## 1. Installation

To install FOCM, follow these steps:

1. Ensure that you have Python installed on your computer. FOCM is developed using Python and requires it to run.

2. Clone or download the FOCM repository from [GitHub](https://github.com/your-repo-link).

3. Open a terminal or command prompt and navigate to the downloaded FOCM directory.

4. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary packages for FOCM to run.

5. Once the installation is complete, you can launch FOCM by running the following command:

   ```
   python main.py
   ```

   The FOCM application window should now appear on your screen.

## 2. Main Functions

### User Interface

FOCM features a user-friendly interface with the following components:

- Main Window: The central hub of the application, featuring a dual-pane layout. One pane displays the directory tree (folders), and the other pane shows the contents of the selected directory.

- Toolbar: A top toolbar with buttons for common actions such as creating a new folder, deleting a file, refreshing the view, toggling between list/grid view, and a search bar.

- Status Bar: A bottom status bar that displays information about the selected files/folders and general statistics such as the total number of files and total size.

- Search and Filter Panel: A dedicated panel accessible from the main window, allowing users to enter search criteria, choose filters (file type, date modified, size), and display results in a list or grid format.

- File Preview Window: A pop-up or sidebar window that provides a quick preview of the selected file. For text documents and images, a preview is shown within the window. For videos and audio files, basic playback controls are provided.

- File Properties and Metadata Editor: A dialog box that displays detailed information about a selected file/folder, including file size, creation/modification dates, and allows the user to edit metadata tags.

- Settings/Preferences Window: A separate window accessible from the main menu, allowing users to customize application settings such as theme selection (dark/light), default views, file organization rules, backup settings, and extension/plugin management.

- Tag Management Interface: A panel or window for creating, editing, and deleting tags. Users can assign tags to files or folders from this interface, providing a flexible way to categorize and locate files quickly.

- Backup and Synchronization Setup Wizard: A step-by-step wizard that guides users through setting up backup destinations (external drive, cloud storage) and synchronization options, including scheduling automatic backups.

- Help and Tutorial Section: A dedicated window or section accessible from the main menu, offering a searchable help database, user manual, and interactive tutorials on key features.

### File Organization

FOCM provides powerful file organization features to help you keep your files structured and easily accessible. The application supports both automated organization rules and manual tagging and categorization.

- Automated Organization Rules: Users can create customizable rules based on file type, date criteria, file name patterns, and file size thresholds. FOCM allows users to specify the target folder structure for organized files, with options to create new folders based on rule criteria such as date or project name.

- Manual Tagging and Categorization: Users can assign custom tags to files and folders manually. FOCM offers a tagging interface that suggests existing tags as the user types and allows the creation of new tags. It also supports creating custom categories to group files/folders based on project, client, priority, or any other user-defined category.

- Bulk File Operations: FOCM supports bulk operations to rename, move, copy, or delete multiple files at once based on user selection. Users can also bulk apply tags or move files to a category, with undo functionality to revert changes if needed.

- Folder and File Management: Users can create, rename, move, and delete files and folders from within the application. FOCM provides a drag-and-drop interface for moving files and folders into different categories or locations. It also includes a feature to detect and resolve duplicate files based on name, size, and optionally content hash, with options to keep, delete, or merge duplicate files.

- Custom Folder Views and Sorting: FOCM allows users to customize how folders and files are displayed, including list, grid, and thumbnail views. It supports sorting files and folders by name, size, date modified, or custom tags/categories.

- File Watcher and Auto-Update: FOCM implements a file watcher mechanism that automatically updates file organization based on predefined rules when new files are added to monitored folders. This feature works in real-time or at user-defined intervals, ensuring the organization structure is always up-to-date.

- Integration with File System: FOCM integrates closely with the operating system's file system to reflect changes made within the app in real-time in the user's file explorer or finder. It supports right-click context menu options in the operating system's file explorer to quickly tag, categorize, or apply predefined organization rules to selected files or folders.

### Search and Filter

FOCM provides advanced search functionality to help you quickly find files and folders based on various criteria.

- Advanced Search Functionality: FOCM allows you to search for files and folders using partial or full file names. It also supports content-based search capabilities, allowing you to find files containing specific text, even within documents or metadata for images and videos. The application supports regular expressions (regex) in search queries for complex pattern matching.

- Custom Search Filters: FOCM offers predefined filters to quickly select files based on common criteria such as file type, size, and modification or creation date. It also allows users to create, save, and apply custom filter sets based on any combination of file attributes, including custom tags, project names, or specific content.

- Tag-Based Searching: FOCM integrates a tagging system where users can assign custom tags to files and folders. You can search for files based on these tags, including support for hierarchical tags to facilitate detailed organization and searching.

- Search History and Saved Searches: FOCM automatically saves recent searches for quick repetition. You can also save frequently used search queries or filters for quick access.

- Search Results Management: FOCM provides sortable search results based on various criteria such as name, size, date modified, and custom tags. You can export search results to CSV or other formats for external use. Batch operations on search results allow you to apply actions (e.g., move, delete, tag) to multiple files at once. Contextual actions in the search results context menu provide quick access to common file operations like open, rename, delete, move, or edit tags. Preview options are also available directly in the context menu for images, documents, and videos.

- Smart Suggestions: FOCM offers smart suggestions as you type in the search bar, based on your input, historical searches, and commonly accessed files. It suggests tags, filenames, and content snippets as possible search queries.

- Integration with File Organization: FOCM seamlessly integrates with the file organization system, allowing you to quickly organize search results into folders or tag groups directly from the search interface.

### Content Management

FOCM includes content management features to help you preview and edit various file types.

- Preview Capabilities: FOCM provides preview capabilities for common file types such as PDF, DOCX, images, and videos. You can preview these files directly within the application.

- Basic Editing Tools: FOCM offers basic editing tools for text files and images, including text formatting and cropping.

## 3. Usage Guide

### Organizing Files

To organize your files effectively using FOCM, follow these steps:

1. Use the directory tree pane in the main window to navigate to the desired folder.

2. Create a new folder by clicking the "New Folder" button in the toolbar. Enter the name of the new folder when prompted.

3. Delete a file by selecting it in the content view pane and clicking the "Delete File" button in the toolbar. Confirm the deletion when prompted.

4. Refresh the view by clicking the "Refresh View" button in the toolbar. This updates the directory tree and content view with the latest changes.

5. Toggle between list and grid view by clicking the "Toggle View" button in the toolbar. Choose the view that suits your preference.

6. Use the search and filter panel to enter search criteria, choose filters, and display results in a list or grid format. You can perform advanced searches, including full-text search within documents.

7. Preview a file by selecting it in the content view pane. A pop-up or sidebar window will appear, providing a quick preview of the selected file. For text documents and images, the preview is shown within the window. For videos and audio files, basic playback controls are provided.

8. Edit a text file by selecting it in the content view pane and clicking the "Edit" button in the file preview window. Make your changes directly within the preview window.

9. View and edit file properties and metadata by right-clicking on a file or folder and selecting "Properties" from the context menu. A dialog box will appear, displaying detailed information about the selected file/folder. You can edit metadata tags in this dialog box.

### Searching and Filtering

To search for files and folders effectively using FOCM, follow these steps:

1. Enter a search query in the search bar located in the toolbar. You can search using partial or full file names.

2. Use the search and filter panel to refine your search by choosing filters such as file type, date modified, and size. You can display the search results in a list or grid format.

3. Perform advanced searches by using content-based search capabilities. FOCM allows you to find files containing specific text, even within documents or metadata for images and videos. You can also use regular expressions (regex) in search queries for complex pattern matching.

4. Use predefined filters to quickly select files based on common criteria such as file type, size, and modification or creation date. You can also create, save, and apply custom filter sets based on any combination of file attributes, including custom tags, project names, or specific content.

5. Search for files based on tags by using the tag-based searching feature. FOCM integrates a tagging system where you can assign custom tags to files and folders. You can search for files based on these tags, including support for hierarchical tags.

6. Access search history and saved searches for quick repetition. FOCM automatically saves recent searches, and you can save frequently used search queries or filters for quick access.

7. Manage search results by sorting them based on various criteria such as name, size, date modified, and custom tags. You can export search results to CSV or other formats for external use. Perform batch operations on search results, allowing you to apply actions (e.g., move, delete, tag) to multiple files at once. Use the contextual actions in the search results context menu for quick access to common file operations. Preview options are also available directly in the context menu for images, documents, and videos.

8. Take advantage of smart suggestions as you type in the search bar. FOCM offers smart suggestions based on your input, historical searches, and commonly accessed files. It suggests tags, filenames, and content snippets as possible search queries.

### Managing Content

To manage your content effectively using FOCM, follow these steps:

1. Preview files by selecting them in the content view pane. FOCM provides preview capabilities for common file types such as PDF, DOCX, images, and videos. You can preview these files directly within the application.

2. Edit text files by selecting them in the content view pane and clicking the "Edit" button in the file preview window. Make your changes directly within the preview window. FOCM offers basic editing tools for text files, including text formatting.

## 4. Troubleshooting

If you encounter any issues while using FOCM, please try the following troubleshooting steps:

1. Ensure that you have installed all the required dependencies as mentioned in the installation section of this manual. Check that you have installed Python and the necessary packages using the provided `requirements.txt` file.

2. Make sure that you are running the latest version of FOCM. Check for any available updates on the FOCM repository on GitHub.

3. If you experience any errors or unexpected behavior, try restarting the application. Close the FOCM window and relaunch it to see if the issue persists.

4. If the issue persists, please refer to the FAQs section of this manual or contact our support team for assistance.

## 5. Frequently Asked Questions (FAQs)

**Q: Can I customize the appearance of FOCM?**

A: Yes, FOCM allows you to customize the application settings, including theme selection (dark/light). You can access the settings/preferences window from the main menu.

**Q: Can I schedule automatic backups with FOCM?**

A: Yes, FOCM provides a backup and synchronization setup wizard that guides you through setting up backup destinations (external drive, cloud storage) and synchronization options, including scheduling automatic backups.

**Q: Can I access help and tutorials on using FOCM?**

A: Yes, FOCM offers a dedicated help and tutorial section accessible from the main menu. It provides a searchable help database, user manual, and interactive tutorials on key features.

For more FAQs, please visit our [FAQs page](https://focm.com/faqs).

## 6. Contact Support

If you need further assistance or have any questions or feedback regarding FOCM, please contact our support team:

- Email: support@focm.com
- Phone: +1 123-456-7890
- Live Chat: Visit our website [www.focm.com](https://www.focm.com) and click on the live chat icon in the bottom right corner.

Our support team is available to help you with any issues or inquiries you may have.

Thank you for choosing the File Organizer and Content Manager (FOCM) application. We hope it enhances your productivity and file management experience.

Happy organizing!

```