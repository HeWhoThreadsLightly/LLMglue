import tkinter as tk
from pomodoro_timer import PomodoroTimer
from task_manager import TaskManager
from website_blocker import WebsiteBlocker
from customization import Customization
from reporting_analytics import ReportingAnalytics
from accessibility import Accessibility
class FocusBlocksApp:
    def __init__(self):
        self.root = tk.Tk()
        self.pomodoro_timer = PomodoroTimer(self.root)
        self.task_manager = TaskManager(self.root)
        self.website_blocker = WebsiteBlocker(self.root)
        self.customization = Customization(self.root)
        self.reporting_analytics = ReportingAnalytics(self.root)
        self.accessibility = Accessibility(self.root)
    def run(self):
        self.root.mainloop()
if __name__ == "__main__":
    app = FocusBlocksApp()
    app.run()