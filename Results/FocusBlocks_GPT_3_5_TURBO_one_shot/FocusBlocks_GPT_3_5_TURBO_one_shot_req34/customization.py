import tkinter as tk
from tkinter import simpledialog
class Customization:
    def __init__(self, root):
        self.root = root
        self.customize_duration_button = tk.Button(self.root, text="Customize Duration", command=self.customize_duration)
        self.customize_block_list_button = tk.Button(self.root, text="Customize Block List", command=self.customize_block_list)
        self.customize_notification_button = tk.Button(self.root, text="Customize Notification", command=self.customize_notification)
    def customize_duration(self):
        duration = simpledialog.askinteger("Customize Duration", "Enter duration in minutes:")
        if duration:
            # Update the duration settings
            pass
    def customize_block_list(self):
        block_list_window = tk.Toplevel(self.root)
        block_list_window.title("Block List")
        block_list_label = tk.Label(block_list_window, text="Blocked Websites and Applications")
        block_list_label.pack()
        block_list = tk.Listbox(block_list_window)
        block_list.pack()
        add_button = tk.Button(block_list_window, text="Add", command=lambda: self.add_to_block_list(block_list))
        add_button.pack()
        remove_button = tk.Button(block_list_window, text="Remove", command=lambda: self.remove_from_block_list(block_list))
        remove_button.pack()
    def add_to_block_list(self, block_list):
        website = simpledialog.askstring("Add Website", "Enter website URL:")
        if website:
            block_list.insert(tk.END, website)
    def remove_from_block_list(self, block_list):
        selected_website = block_list.curselection()
        if selected_website:
            block_list.delete(selected_website)
    def customize_notification(self):
        notification_window = tk.Toplevel(self.root)
        notification_window.title("Notification Customization")
        notification_label = tk.Label(notification_window, text="Notification Settings")
        notification_label.pack()
        # Add customization options for notification sounds
        sound_label = tk.Label(notification_window, text="Notification Sound:")
        sound_label.pack()
        sound_options = ["Sound 1", "Sound 2", "Sound 3"]  # Example sound options
        sound_variable = tk.StringVar(notification_window)
        sound_variable.set(sound_options[0])  # Set default sound option
        sound_dropdown = tk.OptionMenu(notification_window, sound_variable, *sound_options)
        sound_dropdown.pack()
        # Add customization options for notification themes
        theme_label = tk.Label(notification_window, text="Notification Theme:")
        theme_label.pack()
        theme_options = ["Theme 1", "Theme 2", "Theme 3"]  # Example theme options
        theme_variable = tk.StringVar(notification_window)
        theme_variable.set(theme_options[0])  # Set default theme option
        theme_dropdown = tk.OptionMenu(notification_window, theme_variable, *theme_options)
        theme_dropdown.pack()
        # Update the notification settings based on user selections
        def update_settings():
            selected_sound = sound_variable.get()
            selected_theme = theme_variable.get()
            # Update the notification settings with the selected sound and theme
            # ...
            notification_window.destroy()
        # Add a button to apply the selected settings
        apply_button = tk.Button(notification_window, text="Apply", command=update_settings)
        apply_button.pack()