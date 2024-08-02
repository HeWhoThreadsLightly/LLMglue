# Personal Finance Manager User Manual

## Introduction

The Personal Finance Manager is a desktop application designed to help users manage their personal finances. It provides an easy-to-use interface for entering financial transactions, categorizing them, and generating reports to understand spending habits and financial health. This user manual will guide you through the installation process, introduce the main functions of the software, and provide instructions on how to use it effectively.

## Installation

To install the Personal Finance Manager, follow these steps:

1. Ensure that you have Python installed on your computer. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Download the source code of the Personal Finance Manager from the repository: [https://github.com/your-repo](https://github.com/your-repo)

3. Extract the downloaded source code to a directory of your choice.

4. Open a terminal or command prompt and navigate to the directory where you extracted the source code.

5. Create a virtual environment by running the following command:

   ```
   python -m venv venv
   ```

6. Activate the virtual environment:

   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

7. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

8. Once the installation is complete, you can launch the Personal Finance Manager by running the following command:

   ```
   python main.py
   ```

## Main Features

The Personal Finance Manager offers the following main features:

1. Dashboard: Provides a quick overview of your financial status, including total income, expenses for the current month, and a graph showing spending trends over the last six months.

2. Transactions: Allows you to view a list of all transactions, filter transactions by date range, category, or income/expense type, and add new transactions.

3. Reports: Generates reports to understand your spending habits and financial health.

4. Settings: Allows you to customize the application settings.

## Using the Personal Finance Manager

### Dashboard

The Dashboard provides a quick overview of your financial status. It displays the following information:

- Current Balance: Shows your current balance.

- Recent Transactions: Displays a list of your recent transactions.

- Upcoming Bills: Shows a list of your upcoming bills.

### Transactions

The Transactions window allows you to view, filter, and add transactions. Here's how you can use it:

- View Transactions: The Transactions window displays a list of all your transactions. You can use the filters at the top of the window to filter transactions by date range, category, or income/expense type.

- Add Transaction: To add a new transaction, click on the "Add Transaction" button. A form will appear where you can enter the transaction details, including the transaction date, amount, category, payment method, and optional notes. Once you have entered the details, click the "Submit" button to add the transaction.

- Edit/Delete Transaction: To edit or delete a transaction, right-click on the transaction in the list. A context menu will appear with options to edit or delete the transaction.

### Reports

The Reports window allows you to generate reports to understand your spending habits and financial health. Here's how you can use it:

- Generate Report: Click on the "Generate Report" button to generate a report. The report will include information such as total income, total expenses, and total savings.

### Settings

The Settings window allows you to customize the application settings. Currently, there are no customizable settings available.