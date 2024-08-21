'''
The file_preview module of the File Organizer and Content Manager (FOCM) application.
'''
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
class FilePreview:
    def __init__(self, parent):
        self.parent = parent
        self.preview_label = tk.Label(self.parent, text="File Preview")
        self.preview_label.pack(side=tk.TOP, padx=5, pady=5)
    def show_preview(self, file):
        # TODO: Implement showing the preview of the file
        file_extension = file.split(".")[-1]
        if file_extension in ["txt", "md"]:
            self.show_text_preview(file)
        elif file_extension in ["jpg", "jpeg", "png", "gif"]:
            self.show_image_preview(file)
        elif file_extension in ["mp4", "avi", "mov"]:
            self.show_video_preview(file)
        else:
            messagebox.showinfo("Preview Error", "Preview not available for this file type.")
    def show_text_preview(self, file):
        try:
            with open(file, "r") as f:
                content = f.read()
            text_preview = tk.Text(self.parent)
            text_preview.insert(tk.END, content)
            text_preview.pack(side=tk.TOP, padx=5, pady=5)
        except:
            messagebox.showinfo("Preview Error", "Failed to open the file.")
    def show_image_preview(self, file):
        try:
            image_preview = tk.PhotoImage(file=file)
            image_label = tk.Label(self.parent, image=image_preview)
            image_label.image = image_preview
            image_label.pack(side=tk.TOP, padx=5, pady=5)
        except:
            messagebox.showinfo("Preview Error", "Failed to open the image.")
    def show_video_preview(self, file):
        try:
            video_preview = tk.Label(self.parent, text="Video Preview")
            video_preview.pack(side=tk.TOP, padx=5, pady=5)
            # TODO: Add video playback controls
        except:
            messagebox.showinfo("Preview Error", "Failed to open the video.")