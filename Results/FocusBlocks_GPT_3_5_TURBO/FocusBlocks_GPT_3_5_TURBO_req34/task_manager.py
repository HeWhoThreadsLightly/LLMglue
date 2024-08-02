'''
FocusBlocks - Pomodoro Technique with Website and Application Blocking
This file contains the task management functionality.
'''
class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        """
        Adds a task to the task list.
        Args:
            task (dict): The task to be added.
        Returns:
            None
        """
        self.tasks.append(task)
    def remove_task(self, title):
        """
        Removes a task from the task list.
        Args:
            title (str): The title of the task to be removed.
        Returns:
            None
        """
        for task in self.tasks:
            if task["title"] == title:
                self.tasks.remove(task)
                break
    def get_tasks(self):
        """
        Returns the list of tasks.
        Returns:
            list: The list of tasks.
        """
        return self.tasks
    def complete_task(self, title):
        """
        Marks a task as complete.
        Args:
            title (str): The title of the task to be marked as complete.
        Returns:
            None
        """
        for task in self.tasks:
            if task["title"] == title:
                task["completed"] = True
                break
    def edit_task(self, title, new_title, new_description, new_duration):
        """
        Edits the details of a task.
        Args:
            title (str): The title of the task to be edited.
            new_title (str): The new title of the task.
            new_description (str): The new description of the task.
            new_duration (int): The new duration of the task in Pomodoros.
        Returns:
            None
        """
        for task in self.tasks:
            if task["title"] == title:
                task["title"] = new_title
                task["description"] = new_description
                task["duration"] = new_duration
                break