# File Organizer and Content Manager User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a desktop application designed to help users efficiently organize, search, and manage their local files. This software aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. It provides a unified interface for managing digital content and supports various file types, including documents, images, videos, and more.

## Installation

To install the File Organizer and Content Manager, follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

2. Open a command prompt or terminal window.

3. Navigate to the directory where you have downloaded the FOCM files.

4. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Once the installation is complete, you can launch the FOCM application by running the following command:

   ```
   python main.py
   ```

## Main Window

The main window of the FOCM application is the central hub where you can perform various file management tasks. It features a dual-pane layout, with one pane for the directory tree (folders) and another for viewing the contents of the selected directory.

### Toolbar

At the top of the main window, you will find a toolbar with buttons for common actions. These buttons allow you to create a new folder, delete a file, refresh the view, toggle between list/grid view, and perform a search.

### Status Bar

At the bottom of the main window, there is a status bar that displays information about the selected files/folders and general statistics, such as the total number of files and the total size.

## Search and Filter Panel

The FOCM application provides a dedicated panel for searching and filtering files. This panel is accessible from the main window and allows you to enter search criteria, choose filters (file type, date modified, size), and display the results in a list or grid format.

### Advanced Search Options

The search and filter panel also offers advanced search options for more precise filtering. You can perform a full-text search within documents to find specific content within files.

## File Preview Window

When you select a file in the FOCM application, you can preview its content in a pop-up or sidebar window. For text documents and images, the preview window will display the content within the window. For videos and audio files, basic playback controls will be provided.

### Edit Mode

For text files, the file preview window also supports an edit mode. This allows you to make quick edits directly within the preview window, without the need to open a separate text editor.

## File Properties and Metadata Editor

The FOCM application provides a file properties and metadata editor. When you select a file or folder and right-click to open the context menu, you can choose the "Properties" option. This will open a dialog box that displays detailed information about the file, including its size, creation/modification dates. You can also edit metadata tags for the file.

## Settings/Preferences Window

The FOCM application offers a separate window accessible from the main menu, where you can customize application settings. This includes selecting the theme (dark/light), setting default views, configuring file organization rules, managing backup settings, and handling extension/plugin management.

## Tag Management Interface

To provide a flexible way to categorize and locate files quickly, the FOCM application includes a tag management interface. This interface allows you to create, edit, and delete tags. You can also assign tags to files or folders directly from this interface.

## Backup and Synchronization Setup Wizard

To help you set up backup destinations and synchronization options, the FOCM application provides a step-by-step wizard. This wizard guides you through the process of selecting backup destinations (external drive, cloud storage) and configuring synchronization options, including scheduling automatic backups.

## Help and Tutorial Section

The FOCM application includes a dedicated window or section accessible from the main menu, offering a searchable help database, user manual, and interactive tutorials on key features. This section provides comprehensive guidance on how to use the application effectively and make the most out of its features.

## File Organization

The FOCM application offers both automated organization rules and manual tagging and categorization options to help you organize your files effectively.

### Automated Organization Rules

You can create customizable rules for automatically organizing files based on various criteria, including file type, date criteria (creation date, modification date), file name patterns (using wildcards or regular expressions), and file size thresholds. You can specify the target folder structure for organized files and even create new folders based on rule criteria, such as date or project name.

### Manual Tagging and Categorization

In addition to automated organization rules, the FOCM application allows you to manually assign custom tags to files and folders. The application offers a tagging interface that suggests existing tags as you type and allows you to create new tags. You can also create custom categories to group files/folders based on project, client, priority, or any other user-defined category.

## Conclusion

The File Organizer and Content Manager (FOCM) is a powerful desktop application that helps you efficiently organize, search, and manage your local files. With its automated organization rules, advanced search capabilities, and content management features, the FOCM application enhances productivity and simplifies file management. Whether you need to find specific files, preview their content, edit metadata, or create custom tags and categories, the FOCM application provides a unified interface for all your file management needs.