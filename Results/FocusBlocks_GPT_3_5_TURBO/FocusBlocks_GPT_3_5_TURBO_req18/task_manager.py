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
    def remove_task(self, task):
        """
        Removes a task from the task list.
        Args:
            task (dict): The task to be removed.
        Returns:
            None
        """
        self.tasks.remove(task)
    def get_tasks(self):
        """
        Returns the list of tasks.
        Returns:
            list: The list of tasks.
        """
        return self.tasks
    def complete_task(self, task):
        """
        Marks a task as complete.
        Args:
            task (dict): The task to be marked as complete.
        Returns:
            None
        """
        for t in self.tasks:
            if t["title"] == task:
                t["completed"] = True
                break
    def edit_task(self, task, new_title, new_description, new_duration):
        """
        Edits the details of a task.
        Args:
            task (dict): The task to be edited.
            new_title (str): The new title of the task.
            new_description (str): The new description of the task.
            new_duration (int): The new duration of the task in Pomodoros.
        Returns:
            None
        """
        for t in self.tasks:
            if t["title"] == task:
                t["title"] = new_title
                t["description"] = new_description
                t["duration"] = new_duration
                break