# Personal Finance Manager User Manual

## Introduction

The Personal Finance Manager is a desktop application designed to help users manage their personal finances. It provides a user-friendly interface for tracking income, expenses, and investments, as well as generating reports to understand spending habits and financial health.

This user manual will guide you through the installation process, introduce the main functions of the software, and provide step-by-step instructions on how to use it effectively.

## Table of Contents

1. Installation
2. Main Features
3. Getting Started
4. Managing Transactions
5. Generating Reports
6. Customizing Settings
7. Security and Data Management

## 1. Installation

To install the Personal Finance Manager, follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

2. Open a command prompt or terminal window.

3. Navigate to the directory where you have saved the Personal Finance Manager files.

4. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

5. Once the installation is complete, you can launch the application by running the following command:

   ```
   python main.py
   ```

   The Personal Finance Manager window should now appear on your screen.

## 2. Main Features

The Personal Finance Manager offers the following main features:

- Dashboard: Provides a quick overview of your financial status, including total income, expenses for the current month, and a graph showing spending trends over the last six months.

- Transactions: Allows you to view, add, edit, and delete income and expense transactions. You can also categorize transactions and create custom categories.

- Reports: Offers various reports on financial data, including spending by category, income vs. expenses over time, and monthly comparison charts. Reports can be customized based on date range and categories.

- Settings: Allows you to adjust application preferences such as default currency, date format, application theme (light or dark mode), and notification preferences for reminders about bills and recurring transactions. You can also backup and restore your financial database in CSV format.

## 3. Getting Started

When you launch the Personal Finance Manager, you will be greeted with a login screen. Enter your password to access your financial data. If you are a new user, click on the "Sign Up" button to create a new account.

Once logged in, you will see the main navigation menu or toolbar at the top of the application window. The main windows are:

- Dashboard: Provides an overview of your financial status.
- Transactions: Allows you to manage your income and expense transactions.
- Reports: Generates reports to analyze your financial data.
- Settings: Customizes application preferences and manages data backup.

## 4. Managing Transactions

The Transactions window allows you to view, add, edit, and delete income and expense transactions. Here's how you can perform these actions:

### Viewing Transactions

1. Click on the "Transactions" button in the main navigation menu.

2. The Transactions window will open, displaying a list of all your transactions.

3. Use the filters at the top of the window to display transactions based on date range, category, or income/expense type.

### Adding a Transaction

1. In the Transactions window, click on the "Add Transaction" button.

2. A form will appear where you can enter the transaction details, including the transaction date, amount, category (select from predefined or custom categories), payment method, and optional notes.

3. Fill in the required fields and click the "Submit" button to add the transaction.

### Editing a Transaction

1. In the Transactions window, select the transaction you want to edit from the list.

2. Right-click on the transaction or use the edit button to open the edit form.

3. Update the transaction details as needed and click the "Submit" button to save the changes.

### Deleting a Transaction

1. In the Transactions window, select the transaction you want to delete from the list.

2. Right-click on the transaction or use the delete button to remove the transaction.

3. Confirm the deletion when prompted.

## 5. Generating Reports

The Reports window allows you to generate various reports on your financial data. Here's how you can generate and customize reports:

1. Click on the "Reports" button in the main navigation menu.

2. The Reports window will open, displaying the default report type "Spending by Category".

3. Use the dropdown menus to select the report type, date range, and filter by categories or income/expense type for more detailed analysis.

4. Click the "Generate Report" button to fetch the necessary data and generate the report.

5. The report will be displayed as a chart or graph, depending on the report type. You can export the report to PDF or image formats for sharing or printing.

## 6. Customizing Settings

The Settings window allows you to customize various application preferences and manage data backup. Here's how you can customize your settings:

1. Click on the "Settings" button in the main navigation menu.

2. The Settings window will open, displaying options for default currency, date format, application theme (light or dark mode), and notification preferences.

3. Adjust the settings according to your preferences.

4. To backup or restore your financial database, use the options provided in the Settings window. You can export and import the database in CSV format.

5. Click the "Save Settings" button to apply the changes.

## 7. Security and Data Management

The Personal Finance Manager ensures the security of your financial data and provides options for data management. Here's how it ensures security and offers data management features:

- Login and Security: Upon launching the application, you will be greeted with a login screen to protect your financial data. Enter your password to access the application.

- Data Storage: The application uses SQLite to store your financial data. The database is encrypted with your password when the app is closed, ensuring the security of your data.

- Logout: To secure your session when not in use, click on the "Logout" option in the main navigation or user profile menu.

- Data Backup and Restore: The Settings window provides options for data backup and restore. You can export and import the financial database in CSV format, allowing you to backup your data and ensure data portability.

## Conclusion

Congratulations! You have now learned how to install and use the Personal Finance Manager. With its user-friendly interface and powerful features, you can effectively manage your personal finances, track income and expenses, generate insightful reports, and customize settings according to your preferences.

If you have any further questions or need assistance, please refer to the documentation or contact our support team. Happy financial management!
```