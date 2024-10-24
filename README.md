## SQLite Lab
[![CI](https://github.com/nogibjj/sqlite-lab-zx/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/sqlite-lab-zx/actions/workflows/cicd.yml)

# Grocery Database ETL and Query Project

## Project Overview

This project implements an ETL (Extract, Transform, Load) process for a grocery dataset and provides functionalities to query the data stored in a SQLite database. The project consists of several modules that handle data extraction from a CSV file, transformation, loading into a database, and querying the database for information.

## Project Structure

.
├── Makefile
├── main.py
├── mylib
│   ├── __init__.py
│   ├── extract.py
│   ├── query.py
│   └── transform_load.py
└── test_main.py
```

- **Makefile**: Contains commands for linting and testing the project.
- **main.py**: The main script that orchestrates the ETL process and querying functionalities.
- **mylib/**: Contains the main modules for extracting, transforming, loading, and querying data.
  - **extract.py**: Responsible for extracting data from a CSV file.
  - **transform_load.py**: Handles the transformation of the data and loading it into a SQLite database.
  - **query.py**: Contains functions to query the database.
- **test_main.py**: Contains tests for the database operations.

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

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments

- Thank you to all contributors and libraries that made this project possible.
```

Feel free to modify any sections to better fit your project's specifics or add additional information as needed!
