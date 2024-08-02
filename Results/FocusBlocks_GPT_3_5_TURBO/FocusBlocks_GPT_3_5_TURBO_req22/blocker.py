'''
FocusBlocks - Pomodoro Technique with Website and Application Blocking
This file contains the website and application blocking functionality.
'''
import platform
import subprocess
class Blocker:
    def __init__(self):
        self.blocked_websites = []
        self.blocked_applications = []
    def add_blocked_website(self, website):
        """
        Adds a website to the blocked list.
        Args:
            website (str): The website to be blocked.
        Returns:
            None
        """
        self.blocked_websites.append(website)
    def remove_blocked_website(self, website):
        """
        Removes a website from the blocked list.
        Args:
            website (str): The website to be unblocked.
        Returns:
            None
        """
        self.blocked_websites.remove(website)
    def add_blocked_application(self, application):
        """
        Adds an application to the blocked list.
        Args:
            application (str): The application to be blocked.
        Returns:
            None
        """
        self.blocked_applications.append(application)
    def remove_blocked_application(self, application):
        """
        Removes an application from the blocked list.
        Args:
            application (str): The application to be unblocked.
        Returns:
            None
        """
        self.blocked_applications.remove(application)
    def is_website_blocked(self, website):
        """
        Checks if a website is blocked.
        Args:
            website (str): The website to be checked.
        Returns:
            bool: True if the website is blocked, False otherwise.
        """
        return website in self.blocked_websites
    def is_application_blocked(self, application):
        """
        Checks if an application is blocked.
        Args:
            application (str): The application to be checked.
        Returns:
            bool: True if the application is blocked, False otherwise.
        """
        return application in self.blocked_applications
    def block_websites(self):
        """
        Blocks the websites in the blocked list.
        Returns:
            None
        """
        if platform.system() == 'Windows':
            for website in self.blocked_websites:
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'add', 'rule', 'name="FocusBlocks Website Blocker"', 'dir=out', 'action=block', 'remoteip=' + website])
    def unblock_websites(self):
        """
        Unblocks the websites in the blocked list.
        Returns:
            None
        """
        if platform.system() == 'Windows':
            for website in self.blocked_websites:
                subprocess.run(['netsh', 'advfirewall', 'firewall', 'delete', 'rule', 'name="FocusBlocks Website Blocker"', 'dir=out', 'action=block', 'remoteip=' + website])
    def block_applications(self):
        """
        Blocks the applications in the blocked list.
        Returns:
            None
        """
        if platform.system() == 'Windows':
            for application in self.blocked_applications:
                subprocess.run(['taskkill', '/f', '/im', application])
    def unblock_applications(self):
        """
        Unblocks the applications in the blocked list.
        Returns:
            None
        """
        if platform.system() == 'Windows':
            for application in self.blocked_applications:
                subprocess.run(['taskkill', '/f', '/im', application])