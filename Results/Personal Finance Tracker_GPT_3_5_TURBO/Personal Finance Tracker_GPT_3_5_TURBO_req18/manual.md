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
7. Data Backup and Restore
8. Security and Login
9. Additional Features
10. Troubleshooting
11. Frequently Asked Questions
12. Conclusion

## 1. Installation

To install the Personal Finance Manager, follow these steps:

1. Ensure that you have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

2. Open a terminal or command prompt and navigate to the directory where you want to install the application.

3. Run the following command to install the required dependencies:

   ```
   pip install pandas matplotlib
   ```

4. Download the source code of the Personal Finance Manager from the repository: [link to repository]

5. Extract the downloaded zip file to the desired location.

6. Open a terminal or command prompt and navigate to the extracted folder.

7. Run the following command to start the application:

   ```
   python main.py
   ```

8. The Personal Finance Manager application will open, and you can start using it.

## 2. Main Features

The Personal Finance Manager offers the following main features:

- Dashboard: Provides a quick overview of your financial status, including total income, expenses for the current month, and a graph showing spending trends over the last six months.

- Transactions: Allows you to view, add, edit, and delete income and expense transactions. You can also categorize transactions and create custom categories.

- Reports: Offers various reports on financial data, including spending by category, income vs. expenses over time, and monthly comparison charts. Reports can be visualized through charts and graphs and exported to PDF or image formats.

- Settings: Allows you to adjust application preferences such as default currency, date format, application theme (light or dark mode), and notification preferences for reminders about bills and recurring transactions. You can also backup and restore your financial database in CSV format.

- Security and Login: Ensures the protection of your financial data with a login screen that requires a password. The application uses SQLite to store data and encrypts the database with your password when the app is closed. You can also logout to secure your session when not in use.

## 3. Getting Started

When you launch the Personal Finance Manager, you will be greeted with a login screen. Enter your password to access the application.

After logging in, you will see the main window with a primary navigation menu or toolbar. The main windows are:

- Dashboard: Provides an overview of your financial status, including total income, expenses for the current month, and a graph showing spending trends over the last six months.

- Transactions: Allows you to view, add, edit, and delete income and expense transactions. You can also categorize transactions and create custom categories.

- Reports: Offers various reports on financial data, including spending by category, income vs. expenses over time, and monthly comparison charts.

- Settings: Allows you to adjust application preferences, backup and restore your financial database, and manage other settings.

To switch between the main windows, simply click on the corresponding option in the navigation menu or toolbar.

## 4. Managing Transactions

The Transactions window allows you to view, add, edit, and delete income and expense transactions. Here's how you can perform these actions:

### Viewing Transactions

1. Click on the "Transactions" option in the navigation menu or toolbar to open the Transactions window.

2. By default, you will see a list of all transactions. You can use filters to display transactions by date range, category, or income/expense type.

3. To apply filters, enter the desired values in the corresponding filter fields and click the "Apply" button.

### Adding a Transaction

1. In the Transactions window, click the "Add Transaction" button.

2. A form will appear with fields for the transaction date, amount, category, payment method, and optional notes.

3. Enter the transaction details in the form.

4. Click the "Submit" button to add the transaction.

### Editing a Transaction

1. In the Transactions window, select the transaction you want to edit from the list.

2. Click the "Edit Transaction" button.

3. The transaction details will appear in a form.

4. Update the transaction details as desired.

5. Click the "Submit" button to save the changes.

### Deleting a Transaction

1. In the Transactions window, select the transaction you want to delete from the list.

2. Click the "Delete Transaction" button.

3. Confirm the deletion when prompted.

## 5. Generating Reports

The Reports window allows you to generate various reports on your financial data. Here's how you can generate and customize reports:

1. Click on the "Reports" option in the navigation menu or toolbar to open the Reports window.

2. By default, the Reports window will show the "Spending by Category" report.

3. Use the dropdown menu to select the desired report type.

4. Specify the date range and filter options for more detailed analysis.

5. Click the "Generate Report" button to fetch and generate the report.

6. The report will be displayed as a chart or graph, depending on the report type.

7. You can export the report to PDF or image formats for sharing or printing.

## 6. Customizing Settings

The Settings window allows you to customize various application preferences. Here's how you can customize the settings:

1. Click on the "Settings" option in the navigation menu or toolbar to open the Settings window.

2. In the Settings window, you can adjust the following preferences:

   - Default currency: Set the default currency for your transactions.

   - Date format: Choose the desired date format for displaying dates.

   - Application theme: Switch between light and dark mode.

   - Notification preferences: Set preferences for reminders about bills and recurring transactions.

3. Make the desired changes to the settings.

4. Click the "Save Settings" button to apply the changes.

## 7. Data Backup and Restore

The Settings window also allows you to backup and restore your financial database. Here's how you can perform these actions:

### Data Backup

1. In the Settings window, click the "Backup Data" button.

2. Choose a location to save the backup file.

3. Click the "Save" button to create the backup file.

### Data Restore

1. In the Settings window, click the "Restore Data" button.

2. Select the backup file you want to restore.

3. Click the "Restore" button to restore the data from the backup file.

## 8. Security and Login

The Personal Finance Manager ensures the security of your financial data with a login screen and encryption. Here's how you can use the security features:

### Login

1. When you launch the application, you will be greeted with a login screen.

2. Enter your password in the password field.

3. Click the "Login" button to access the application.

### Logout

1. To secure your session when not in use, click on the "Logout" option in the navigation menu or user profile menu.

2. You will be logged out of the application.

### Data Encryption

1. The application uses SQLite to store your financial data.

2. The database is encrypted with your password when the application is closed.

## 9. Additional Features

The Personal Finance Manager offers additional features to enhance your financial management experience. Here are some of these features:

- Categorizing Transactions: You can categorize transactions into predefined or custom categories, such as groceries, utilities, or salary.

- Import and Export: You can import and export financial data in CSV format for backup and data portability.

## 10. Troubleshooting

If you encounter any issues while using the Personal Finance Manager, try the following troubleshooting steps:

1. Make sure you have installed the required dependencies as mentioned in the installation instructions.

2. Check if there are any error messages or notifications displayed in the application. These may provide clues about the issue.

3. Restart the application and try again.

4. If the issue persists, consider reaching out to the support team for assistance.

## 11. Frequently Asked Questions

**Q: Can I use the Personal Finance Manager on multiple devices?**

A: The Personal Finance Manager is a desktop application, and it is designed to be used on a single device. However, you can backup and restore your financial database to transfer data between devices.

**Q: Can I customize the categories for transactions?**

A: Yes, you can create custom categories for transactions in addition to the predefined categories.

**Q: Can I generate reports for a specific time period?**

A: Yes, you can specify the date range for reports to analyze financial data for a specific time period.

**Q: Can I export reports to other formats?**

A: Yes, you can export reports to PDF or image formats for sharing or printing.

## 12. Conclusion

Congratulations! You have completed the Personal Finance Manager user manual. You should now have a good understanding of how to install the software, navigate through its main features, and perform various tasks such as managing transactions, generating reports, customizing settings, and ensuring data security.

If you have any further questions or need assistance, please refer to the troubleshooting section or reach out to the support team for help.

Happy financial management with the Personal Finance Manager!

```