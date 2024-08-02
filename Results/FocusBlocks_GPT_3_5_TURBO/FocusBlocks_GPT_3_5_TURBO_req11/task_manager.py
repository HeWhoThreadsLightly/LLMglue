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
            task (str): The task to be added.
        Returns:
            None
        """
        self.tasks.append(task)
    def remove_task(self, task):
        """
        Removes a task from the task list.
        Args:
            task (str): The task to be removed.
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