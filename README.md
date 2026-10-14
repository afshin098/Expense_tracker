# Expense Tracker

## Description

Expense Tracker is a command-line application built with Python and PostgreSQL. It allows users to add, view, search, update, and delete expenses. The application stores expense data in a PostgreSQL database.

## Features

- Add new expenses.
- View all expenses in a table.
- Search for an expense by ID.
- Update an expense amount.
- Delete an expense.
- Validate user input.
- Handle database errors.

## Technologies

- Python
- PostgreSQL
- Psycopg 3
- python-dotenv

## Requirements

- Python 3
- PostgreSQL
- Required Python packages: `psycopg[binary]` and `python-dotenv`

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd expense_tracker
```

Replace `<repository-url>` with the URL of your GitHub repository.

### 2. Create a Virtual Environment

```bash
py -m venv .venv
```

Activate the virtual environment on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install "psycopg[binary]" python-dotenv
```

### 4. Configure Environment Variables

Create a `.env` file in the project root directory and add your PostgreSQL connection settings.

```dotenv
DB_HOST=localhost
DB_NAME=expense_tracker
DB_USER=your_username
DB_PASSWORD=your_password
DB_PORT=5432
```

Replace the username and password with your own PostgreSQL credentials.

### 5. Set Up the Database

Create a PostgreSQL database named `expense_tracker`.

Create the required `categories` and `expenses` tables and configure the foreign key relationship between them before running the application.

## Usage

Run the application from the project directory:

```bash
python main.py
```

Use the menu to manage your expenses.

- **Show all expenses:** Display all saved expenses.
- **Find an expense:** Search for an expense by its ID.
- **Add an expense:** Add a new expense with a title, amount, and category.
- **Update an expense:** Change the amount of an existing expense.
- **Delete an expense:** Remove an expense by its ID.
- **Exit:** Close the application.

## Environment Variables

The application uses environment variables to configure the PostgreSQL database connection.

Create a `.env` file in the project root directory with the following variables:

| Variable | Description |
|---|---|
| `DB_HOST` | PostgreSQL server address |
| `DB_NAME` | Database name |
| `DB_USER` | PostgreSQL username |
| `DB_PASSWORD` | PostgreSQL password |
| `DB_PORT` | PostgreSQL server port (default: `5432`) |

Do not commit your `.env` file or expose your database credentials in a public repository.