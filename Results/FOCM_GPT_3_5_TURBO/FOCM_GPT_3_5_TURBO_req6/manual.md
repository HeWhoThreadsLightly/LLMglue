# File Organizer and Content Manager (FOCM) User Manual

## Introduction

The File Organizer and Content Manager (FOCM) is a desktop application designed to help users efficiently organize, search, and manage their local files. This software aims to enhance productivity and file management through automated organization, advanced search capabilities, and content management features. FOCM supports various file types, including documents, images, videos, and more, providing a unified interface for managing digital content.

## Installation

To use FOCM, you need to install the required dependencies. Follow the steps below to install the necessary environment dependencies:

1. Ensure you have Python installed on your system. FOCM is developed using Python, so you need to have Python installed to run the application.

2. Open a terminal or command prompt and navigate to the directory where you have downloaded the FOCM files.

3. Create a virtual environment (optional but recommended) by running the following command:

   ```
   python -m venv myenv
   ```

   Replace `myenv` with the name you want to give to your virtual environment.

4. Activate the virtual environment by running the appropriate command for your operating system:

   - For Windows:

     ```
     myenv\Scripts\activate
     ```

   - For macOS and Linux:

     ```
     source myenv/bin/activate
     ```

5. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary dependencies, including `tkinter` and `Pillow`.

6. Once the installation is complete, you are ready to use FOCM.

## Getting Started

To start using FOCM, follow the steps below:

1. Open a terminal or command prompt and navigate to the directory where you have downloaded the FOCM files.

2. Activate the virtual environment (if you created one) by running the appropriate command for your operating system (as mentioned in the installation steps).

3. Run the following command to start FOCM:

   ```
   python main.py
   ```

   This will launch the FOCM application.

## Main Window

The main window of FOCM serves as the central hub of the application. It features a dual-pane layout, with one pane for the directory tree (folders) and another for viewing the contents of the selected directory.

### Toolbar

The main window includes a toolbar at the top with buttons for common actions. The available buttons are:

- **New Folder**: Clicking this button will create a new folder in the currently selected directory.

- **Delete File**: Clicking this button will delete the selected file.

- **Refresh View**: Clicking this button will refresh the view of the current directory.

- **Toggle View**: Clicking this button will toggle between list and grid view for the file contents.

- **Search Bar**: The search bar allows you to enter search criteria to filter the displayed files.

### Status Bar

The main window also includes a status bar at the bottom, which displays information about the selected files/folders and general statistics, such as the total number of files and the total size.

## Search and Filter Panel

FOCM provides a dedicated panel for searching and filtering files. This panel is accessible from the main window and allows users to enter search criteria, choose filters (file type, date modified, size), and display results in a list or grid format.

### Advanced Search Options

FOCM offers advanced search options for more precise filtering. This includes full-text search within documents, allowing you to search for specific keywords or phrases within the content of supported file types.

## File Preview Window

FOCM provides a file preview window that allows you to quickly preview the selected file. For text documents and images, the preview will be shown within the window. For videos and audio files, basic playback controls will be provided.

## Conclusion

Congratulations! You are now familiar with the File Organizer and Content Manager (FOCM) application. Use this user manual as a guide to efficiently organize, search, and manage your local files using FOCM. Enjoy enhanced productivity and file management through automated organization, advanced search capabilities, and content management features.