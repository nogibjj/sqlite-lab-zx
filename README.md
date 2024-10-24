# Grocery Database ETL and Query Project
[![CI](https://github.com/nogibjj/sqlite-lab-zx/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/sqlite-lab-zx/actions/workflows/cicd.yml)
## Project Overview

This project implements an ETL (Extract, Transform, Load) process for a grocery dataset and provides functionalities to query the data stored in a SQLite database. The project consists of several modules that handle data extraction from a CSV file, transformation, loading into a database, and querying the database for information.

## Project Structure
```
├── .devcontainer
│ ├── Dockerfile
│ └── devcontainer.json
├── .github
│ └── workflows
│ └── cicd.yml
├── mylib
│ ├── init.py
│ ├── extract.py
│ ├── query.py
│ └── transform_load.py
├── .gitignore
├── Dockerfile
├── GroceryDB.db
├── LICENSE
├── Makefile
├── README.md
├── main.py
├── requirements.txt
├── setup.sh
└── test_main.py
```
- **.devcontainer/**: Contains configuration for development container.
  - **Dockerfile**: Defines the environment setup.
  - **devcontainer.json**: Configuration for VS Code remote development.

- **.github/workflows/**: Contains CI/CD pipeline configurations.
  - **cicd.yml**: Defines the GitHub Actions workflow.

- **mylib/**: Library modules for the project.
  - **extract.py**: Responsible for extracting data from a CSV file.
  - **query.py**: Contains functions to query the database.
  - **transform_load.py**: Handles data transformation and loading into a SQLite database.

- **Makefile**: Contains commands for installation, linting, testing, and deployment.
- **main.py**: The main script that orchestrates the ETL process and querying functionalities.
- **test_main.py**: Contains tests for the database operations.
- **GroceryDB.db**: SQLite database file.
- **requirements.txt**: Lists Python dependencies.
- **setup.sh**: Script for setting up the environment.
- **Dockerfile**: Used for building Docker images.
- **README.md**: Documentation and instructions for the project.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the ETL Process

To run the ETL process and populate the database, execute the following command:

```bash
python main.py
```

This command will:
1. Extract data from the CSV file located at `data/Grocery.csv`.
2. Transform the data and load it into the SQLite database named `GroceryDB.db`.

### Querying the Database

The `main.py` file also includes functionalities to query the database. You can customize the `main()` function in `main.py` to perform various queries like:

- Insert data into the database.
- Read data from the database.
- Update existing records.
- Delete records.

### Running Tests

To ensure that everything is working correctly, you can run the tests using:

```bash
make test
```

This command will execute the tests defined in `test_main.py`.

## Linting

To check for code quality, run the linting tool with:

```bash
make lint
```

This command will use `ruff` for linting the code.
