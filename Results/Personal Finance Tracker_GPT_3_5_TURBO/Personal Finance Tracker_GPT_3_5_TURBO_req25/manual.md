# Personal Finance Manager User Manual

## Introduction

Welcome to the Personal Finance Manager! This desktop application is designed to help you manage your personal finances by tracking your income, expenses, and investments. It provides an easy-to-use interface for entering financial transactions, categorizing them, and generating reports to understand your spending habits and financial health.

In this user manual, you will find detailed instructions on how to install the application, navigate through its main windows, and utilize its key features. Let's get started!

## Table of Contents

1. Installation
2. Main Windows and Navigation
   - Dashboard
   - Transactions
   - Reports
   - Settings
3. Dashboard
   - Overview
   - Customization
4. Transactions
   - Viewing Transactions
   - Adding a New Transaction
   - Editing and Deleting Transactions
5. Reports
   - Generating Reports
   - Customizing Reports
   - Exporting Reports
6. Settings
   - Adjusting Application Preferences
   - Data Backup and Restore
7. Login and Security
   - Logging In
   - Encrypting the Database
   - Logging Out
8. Additional Features
   - Data Management
   - Reporting
   - Security
   - Settings and Customization
   - Documentation and Help

## 1. Installation

To install the Personal Finance Manager desktop application, follow these steps:

1. Open a terminal or command prompt on your computer.
2. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

   Note: Make sure you have Python and pip installed on your system.

3. Once the installation is complete, you can launch the application by running the following command:

   ```
   python main.py
   ```

   The Personal Finance Manager window will appear, and you can start using the application.

## 2. Main Windows and Navigation

The Personal Finance Manager application features four main windows: Dashboard, Transactions, Reports, and Settings. These windows can be accessed through the primary navigation menu or toolbar.

### Dashboard

The Dashboard provides a quick overview of your financial status. It displays your total income, expenses for the current month, and a graph showing your spending trends over the last six months. Additionally, you can customize the widgets or cards on the Dashboard to display critical information such as upcoming bills, budget summary, and investment performance.

### Transactions

The Transactions window allows you to view a list of all your financial transactions. You can filter the transactions by date range, category, or income/expense type. You can also add new transactions using a form that includes fields for the transaction date, amount, category (with a dropdown to select from predefined or custom categories), payment method, and optional notes. Each transaction in the list can be edited or deleted using the context menu or buttons.

### Reports

The Reports window offers various reports on your financial data. You can select the report type from a dropdown menu, specify the date range, and filter by categories or income/expense type for more detailed analysis. The reports are visualized through charts and graphs, and you can export them to PDF or image formats for sharing or printing.

### Settings

The Settings window allows you to adjust application preferences such as default currency, date format, application theme (light or dark mode), and notification preferences for reminders about bills and recurring transactions. It also includes options for data backup and restore, including exporting and importing the financial database in CSV format.

## 3. Dashboard

The Dashboard provides a quick overview of your financial status and allows you to customize the widgets or cards displayed on it.

### Overview

The Dashboard displays the following information:

- Current Balance: Shows your current balance in the selected currency.
- Recent Transactions: Displays a list of your most recent transactions.
- Upcoming Bills: Shows a list of your upcoming bills.

### Customization

You can customize the widgets or cards on the Dashboard to display the information that is most relevant to you. To customize the Dashboard:

1. Click on the "Customize" or "Edit" button (if available) on the Dashboard.
2. Rearrange the widgets or cards by dragging and dropping them.
3. Customize the content of each widget or card by selecting the desired options or entering the required information.
4. Click on the "Save" or "Apply" button to save your changes.

## 4. Transactions

The Transactions window allows you to view, add, edit, and delete your financial transactions.

### Viewing Transactions

In the Transactions window, you can view a list of all your financial transactions. You can filter the transactions by date range, category, or income/expense type using the provided filters. The transactions will be displayed in a list format, showing the transaction date, amount, category, payment method, and any optional notes.

### Adding a New Transaction

To add a new transaction:

1. Click on the "Add Transaction" button in the Transactions window.
2. Fill in the required fields in the transaction form, including the transaction date, amount, category, payment method, and optional notes.
3. Click on the "Submit" or "Save" button to add the transaction.

### Editing and Deleting Transactions

To edit a transaction:

1. Select the transaction from the list in the Transactions window.
2. Click on the "Edit" button or right-click on the transaction to access the context menu.
3. Make the necessary changes to the transaction details in the transaction form.
4. Click on the "Submit" or "Save" button to save the changes.

To delete a transaction:

1. Select the transaction from the list in the Transactions window.
2. Click on the "Delete" button or right-click on the transaction to access the context menu.
3. Confirm the deletion when prompted.

## 5. Reports

The Reports window allows you to generate and customize reports on your financial data.

### Generating Reports

To generate a report:

1. Open the Reports window.
2. Select the desired report type from the dropdown menu.
3. Specify the date range for the report.
4. Filter the report by categories or income/expense type if needed.
5. Click on the "Generate Report" button to generate the report.

### Customizing Reports

You can customize the parameters of the reports to suit your needs. The available customization options may vary depending on the report type. Common customization options include selecting the time period, choosing specific categories to include, and filtering by income/expense type.

### Exporting Reports

Once a report is generated, you can export it to PDF or image formats for sharing or printing. To export a report, use the export functionality provided in the Reports window. Select the desired export format and follow the prompts to save the report to your desired location.

## 6. Settings

The Settings window allows you to adjust various application preferences and manage data backup and restore.

### Adjusting Application Preferences

In the Settings window, you can adjust the following application preferences:

- Default Currency: Set the default currency for your financial transactions.
- Date Format: Choose the desired date format for displaying transaction dates.
- Application Theme: Select the preferred theme for the application (light or dark mode).
- Notification Preferences: Customize the notification preferences for reminders about bills and recurring transactions.

### Data Backup and Restore

The Settings window also includes options for data backup and restore. You can export the financial database in CSV format to create backups or transfer your data to another device. You can also import a CSV file to restore your financial data from a backup or another source.

## 7. Login and Security

The Personal Finance Manager provides login and security features to protect your financial data.

### Logging In

Upon launching the application, you will be greeted with a login screen. Enter your password in the provided field to access your financial data. If you are a new user, you may need to create an account and set a password before logging in.

### Encrypting the Database

For data storage, the Personal Finance Manager uses SQLite and encrypts the database with your password when the application is closed. This ensures that your financial data is protected and secure.

### Logging Out

To secure your session when not in use, you can log out of the application. The logout option is accessible from the main navigation or user profile menu. Click on the "Logout" button to log out of the application.

## 8. Additional Features

In addition to the main functionality described above, the Personal Finance Manager offers several additional features to enhance your financial management experience.

### Data Management

The application allows you to add, edit, and delete income and expense transactions. You can categorize transactions into predefined or custom categories, such as groceries, utilities, or salary. The application also provides functionality to import and export financial data in CSV format for backup and data portability.

### Reporting

The software generates visual reports, including charts and graphs, to show spending trends over time, expense breakdown by category, and comparison of income vs. expenses. You can customize the report parameters, such as the time period and categories to include, to gain more insights into your financial data.

### Security

The Personal Finance Manager provides secure storage of your financial data. The database file is encrypted with your password to ensure the confidentiality of your information. User authentication (login) is required to access the financial data, providing an additional layer of security.

### Settings and Customization

You can customize various settings in the application to tailor it to your preferences. Adjust the default currency, date format, and application theme (light or dark mode) to suit your needs. The software also supports notifications for recurring transactions and reminders for upcoming bills, helping you stay on top of your financial commitments.

### Documentation and Help

Comprehensive user documentation is provided with the Personal Finance Manager. The documentation details how to use the application and troubleshoot common issues. If you need further assistance or have any questions, please refer to the documentation or reach out to our support team.

## Conclusion

Congratulations! You have completed the Personal Finance Manager user manual. We hope this guide has provided you with a comprehensive understanding of the application and its features. If you have any further questions or need assistance, please consult the documentation or contact our support team.

Happy financial management!
```