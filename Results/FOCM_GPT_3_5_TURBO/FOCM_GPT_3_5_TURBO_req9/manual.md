# File Organizer and Content Manager (FOCM) User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a desktop application designed to help users efficiently organize, search, and manage their local files. This software aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. FOCM supports various file types, including documents, images, videos, and more, providing a unified interface for managing digital content.

## Installation

To install FOCM, follow these steps:

1. Ensure that you have Python installed on your system. FOCM requires Python version 3.7 or higher.

2. Clone the FOCM repository from GitHub or download the source code as a ZIP file.

3. Open a terminal or command prompt and navigate to the directory where you cloned or extracted the FOCM source code.

4. Create a virtual environment (optional but recommended) by running the following command:

   ```
   python -m venv myenv
   ```

   Replace `myenv` with the desired name for your virtual environment.

5. Activate the virtual environment by running the appropriate command for your operating system:

   - Windows: `myenv\Scripts\activate`
   - macOS/Linux: `source myenv/bin/activate`

6. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

7. Once the installation is complete, you can launch FOCM by running the following command:

   ```
   python main.py
   ```

   The FOCM application window should now appear on your screen.

## User Interface

FOCM provides a user-friendly interface for managing your files. Here are the main components of the user interface:

1. Main Window: The central hub of the application featuring a dual-pane layout. One pane displays the directory tree (folders), and the other pane shows the contents of the selected directory.

2. Toolbar: Located at the top of the main window, the toolbar contains buttons for common actions such as creating a new folder, deleting a file, refreshing the view, toggling between list/grid view, and a search bar.

3. Status Bar: Located at the bottom of the main window, the status bar displays information about the selected files/folders and general statistics, such as the total number of files and total size.

4. Search and Filter Panel: A dedicated panel accessible from the main window, allowing users to enter search criteria, choose filters (file type, date modified, size), and display results in a list or grid format.

5. File Preview Window: A pop-up or sidebar window that provides a quick preview of the selected file. For text documents and images, a preview is shown within the window. For videos and audio files, basic playback controls are provided.

6. File Properties and Metadata Editor: A dialog box that displays when a user selects "Properties" from the context menu of a file/folder. It shows detailed information, including file size, creation/modification dates, and allows the user to edit metadata tags.

7. Settings/Preferences Window: A separate window accessible from the main menu, allowing users to customize application settings. This includes theme selection (dark/light), default views, file organization rules, backup settings, and extension/plugin management.

## Using FOCM

Here are some common tasks you can perform using FOCM:

### Creating a New Folder

To create a new folder, follow these steps:

1. Select the directory where you want to create the new folder in the directory tree pane.

2. Click the "New Folder" button in the toolbar.

3. Enter the name of the new folder in the dialog box that appears.

4. Click "OK" to create the new folder.

### Deleting a File

To delete a file, follow these steps:

1. Select the file you want to delete in the content view pane.

2. Click the "Delete File" button in the toolbar.

3. Confirm the deletion in the dialog box that appears.

### Refreshing the View

To refresh the view and update the directory tree and content view with the latest changes, click the "Refresh View" button in the toolbar.

### Searching for Files

To search for files, follow these steps:

1. Enter your search query in the search bar in the toolbar.

2. Click the "Search" button or press Enter.

3. The search results will be displayed in the content view pane.

### Previewing Files

To preview a file, follow these steps:

1. Select the file you want to preview in the content view pane.

2. A pop-up or sidebar window will appear, showing a preview of the file.

3. For text documents and images, the preview will be displayed within the window. For videos and audio files, basic playback controls will be provided.

### Editing Text Files

To edit a text file directly within the preview window, follow these steps:

1. Preview the text file using the file preview window.

2. Click the "Edit" button in the preview window.

3. Make the desired changes to the text file.

4. Click "Save" to save the changes.

### Viewing File Properties and Editing Metadata

To view file properties and edit metadata, follow these steps:

1. Right-click on the file or folder for which you want to view properties.

2. Select "Properties" from the context menu.

3. A dialog box will appear, displaying detailed information about the file or folder.

4. Edit the metadata tags as desired.

5. Click "OK" to save the changes.

### Customizing Application Settings

To customize application settings, follow these steps:

1. Click the "Settings" or "Preferences" option in the main menu.

2. A separate window will appear, allowing you to customize various settings such as theme selection, default views, file organization rules, backup settings, and extension/plugin management.

3. Make the desired changes to the settings.

4. Click "Save" or "Apply" to apply the changes.

## Conclusion

FOCM is a powerful file organizer and content manager that can help you efficiently manage your local files. With its automated organization, advanced search capabilities, and content management features, FOCM aims to enhance your productivity and simplify file management. Use this user manual as a guide to get started with FOCM and make the most out of its features.

If you have any questions or need further assistance, please refer to the documentation or contact our support team.

Happy organizing and managing your files with FOCM!

```