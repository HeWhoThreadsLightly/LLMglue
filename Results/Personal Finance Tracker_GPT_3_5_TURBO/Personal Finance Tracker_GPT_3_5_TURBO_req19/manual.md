# Personal Finance Manager User Manual

## Introduction
The Personal Finance Manager is a desktop application designed to help users manage their personal finances. It provides an easy-to-use interface for tracking income, expenses, and investments, as well as generating reports to understand spending habits and financial health.

## Installation
To install the Personal Finance Manager, follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: https://www.python.org/downloads/

2. Open a command prompt or terminal and navigate to the directory where you want to install the application.

3. Clone the repository by running the following command:
   ```
   git clone https://github.com/your-username/personal-finance-manager.git
   ```

4. Navigate to the project directory:
   ```
   cd personal-finance-manager
   ```

5. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

6. Run the application by executing the `main.py` file:
   ```
   python main.py
   ```

## Main Windows and Navigation
The Personal Finance Manager features four main windows: Dashboard, Transactions, Reports, and Settings. You can switch between these windows using the primary navigation menu or toolbar.

### Dashboard
The Dashboard provides a quick overview of your financial status. It displays the total income, expenses for the current month, and a graph showing spending trends over the last six months. You can customize and rearrange the widgets or cards displaying critical information such as upcoming bills, budget summary, and investment performance.

### Transactions
The Transactions window allows you to view a list of all your transactions. You can filter the transactions by date range, category, or income/expense type. You can add a new transaction by filling out a form that includes fields for the transaction date, amount, category (with a dropdown to select from predefined or custom categories), payment method, and optional notes. Each transaction in the list can be edited or deleted.

### Reports
The Reports window offers various reports on your financial data. You can select the report type from a dropdown menu, specify the date range, and filter by categories or income/expense type for more detailed analysis. The reports are visualized through charts and graphs. You can export the report to PDF or image formats for sharing or printing.

### Settings
The Settings window allows you to adjust application preferences. You can set the default currency, date format, application theme (light or dark mode), and notification preferences for reminders about bills and recurring transactions. The window also includes options for data backup and restore, including exporting and importing the financial database in CSV format.

## Login and Security
Upon launching the application, you will be greeted with a login screen to ensure that your financial data is protected. The login screen includes a password field. The application uses SQLite to store the data, and the database is encrypted with your password when the app is closed. You can also logout from the main navigation or user profile menu to secure your session when not in use.

## Additional Features
In addition to the main requirements, the Personal Finance Manager includes the following additional features:

### Data Management
- You can add, edit, and delete income and expense transactions.
- You can categorize transactions (e.g., groceries, utilities, salary) and create custom categories.
- You have the functionality to import and export financial data in CSV format for backup and data portability.

### Reporting
- The software generates visual reports (charts, graphs) to show spending trends over time, expense breakdown by category, and comparison of income vs. expenses.

## Conclusion
The Personal Finance Manager is a powerful tool for managing your personal finances. With its intuitive interface and comprehensive features, you can easily track your income, expenses, and investments, and gain valuable insights into your financial health. Start using the Personal Finance Manager today and take control of your finances.