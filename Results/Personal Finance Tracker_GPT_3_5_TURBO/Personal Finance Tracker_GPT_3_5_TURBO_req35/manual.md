# Personal Finance Manager User Manual

## Introduction

The Personal Finance Manager is a desktop application designed to help users manage their personal finances. It provides a user-friendly interface for tracking income, expenses, and investments, as well as generating reports to understand spending habits and financial health.

This user manual will guide you through the installation process, explain the main features of the application, and provide instructions on how to use each feature effectively.

## Table of Contents

1. Installation
2. Main Features
   - Dashboard
   - Transactions
   - Reports
   - Settings
3. How to Use
   - Dashboard
   - Transactions
   - Reports
   - Settings
4. Troubleshooting
5. Frequently Asked Questions
6. Conclusion

## 1. Installation

To install the Personal Finance Manager application, follow these steps:

1. Ensure that you have Python installed on your computer. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Open a command prompt or terminal window.

3. Use the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Download the application code from the repository: [https://github.com/your-repository](https://github.com/your-repository)

5. Extract the downloaded code to a folder on your computer.

6. Open a command prompt or terminal window and navigate to the extracted code folder.

7. Run the following command to start the application:

   ```
   python main.py
   ```

8. The Personal Finance Manager application should now open on your desktop.

## 2. Main Features

The Personal Finance Manager application consists of four main features:

- Dashboard: Provides a quick overview of your financial status, including total income, expenses for the current month, and a graph showing spending trends over the last six months.

- Transactions: Allows you to view, add, edit, and delete income and expense transactions. You can also categorize transactions and import/export financial data in CSV format.

- Reports: Offers various reports on financial data, including spending by category, income vs. expenses over time, and monthly comparison charts. Reports can be customized based on date range and categories.

- Settings: Allows you to adjust application preferences such as default currency, date format, application theme (light or dark mode), and notification preferences for reminders about bills and recurring transactions. You can also backup and restore data in CSV format.

## 3. How to Use

### 3.1 Dashboard

The Dashboard provides a quick overview of your financial status. It displays the following information:

- Current Balance: Shows the current balance of your accounts.

- Recent Transactions: Displays a list of your most recent transactions.

- Upcoming Bills: Shows a list of upcoming bills and their due dates.

To navigate to the Dashboard, click on the "Dashboard" option in the main navigation menu or toolbar.

### 3.2 Transactions

The Transactions feature allows you to manage your income and expense transactions. Here's how to use it:

#### 3.2.1 View Transactions

To view all your transactions, follow these steps:

1. Click on the "Transactions" option in the main navigation menu or toolbar.

2. The Transactions window will open, displaying a list of all your transactions.

3. Use the filters at the top of the window to filter transactions by date range, category, or income/expense type.

#### 3.2.2 Add a Transaction

To add a new transaction, follow these steps:

1. Open the Transactions window.

2. Click on the "Add Transaction" button.

3. Fill in the transaction details in the form, including the transaction date, amount, category, payment method, and optional notes.

4. Click the "Submit" button to add the transaction.

#### 3.2.3 Edit a Transaction

To edit an existing transaction, follow these steps:

1. Open the Transactions window.

2. Select the transaction you want to edit from the list.

3. Click on the "Edit Transaction" button.

4. Update the transaction details in the form.

5. Click the "Submit" button to save the changes.

#### 3.2.4 Delete a Transaction

To delete a transaction, follow these steps:

1. Open the Transactions window.

2. Select the transaction you want to delete from the list.

3. Click on the "Delete Transaction" button.

4. Confirm the deletion when prompted.

### 3.3 Reports

The Reports feature allows you to generate various reports on your financial data. Here's how to use it:

#### 3.3.1 Generate a Report

To generate a report, follow these steps:

1. Click on the "Reports" option in the main navigation menu or toolbar.

2. The Reports window will open.

3. Select the report type from the dropdown menu.

4. Specify the date range and filter options for more detailed analysis.

5. Click the "Generate Report" button.

6. The report will be displayed as charts and graphs.

#### 3.3.2 Export a Report

To export a report, follow these steps:

1. Generate the desired report using the steps mentioned above.

2. Click on the "Export" button.

3. Select the export format (PDF or image).

4. Choose the destination folder and provide a file name.

5. Click the "Save" button to export the report.

### 3.4 Settings

The Settings feature allows you to customize the application according to your preferences. Here's how to use it:

#### 3.4.1 Adjust Application Preferences

To adjust application preferences, follow these steps:

1. Click on the "Settings" option in the main navigation menu or toolbar.

2. The Settings window will open.

3. Customize the default currency, date format, and application theme (light or dark mode).

4. Set notification preferences for reminders about bills and recurring transactions.

5. Click the "Save Settings" button to apply the changes.

#### 3.4.2 Backup and Restore Data

To backup or restore your data, follow these steps:

1. Open the Settings window.

2. Click on the "Backup Data" or "Restore Data" button.

3. Choose the destination folder for backup or the backup file for restore.

4. Click the "Backup" or "Restore" button to complete the process.

## 4. Troubleshooting

If you encounter any issues while using the Personal Finance Manager application, try the following troubleshooting steps:

1. Make sure you have installed all the required dependencies as mentioned in the installation instructions.

2. Check if your Python version is compatible with the application. The recommended version is Python 3.7 or higher.

3. Verify that you have entered the transaction details correctly when adding or editing transactions.

4. If you are experiencing issues with data backup or restore, ensure that you have sufficient disk space and proper file permissions.

If the issue persists, please refer to the Frequently Asked Questions section or contact our support team for further assistance.

## 5. Frequently Asked Questions

**Q: Can I use the Personal Finance Manager application on multiple devices?**

A: Yes, you can install the application on multiple devices and sync the data using the import/export functionality.

**Q: Can I import my existing financial data into the application?**

A: Yes, you can import financial data in CSV format using the import functionality in the Transactions window.

**Q: Can I customize the categories for income and expenses?**

A: Yes, you can create custom categories for income and expenses in the Transactions window.

**Q: How secure is my financial data in the application?**

A: The application uses SQLite to store financial data, and the database is encrypted with your password when the app is closed. It also requires user authentication (login) to access the financial data.

**Q: Can I generate reports for a specific time period or category?**

A: Yes, you can customize the report parameters such as time period and categories to include in the Reports window.

## 6. Conclusion

Congratulations! You have successfully installed and learned how to use the Personal Finance Manager application. With its intuitive interface and powerful features, you can now effectively manage your personal finances, track income and expenses, and generate insightful reports to improve your financial health.

If you have any further questions or need assistance, please refer to the documentation or contact our support team. Happy financial management!

```