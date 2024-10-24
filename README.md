## SQLite Lab
[![CI](https://github.com/nogibjj/sqlite-lab-zx/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/sqlite-lab-zx/actions/workflows/cicd.yml)

This project showcases a data pipeline using SQLite, focusing on data loading, transformation, querying, and CRUD (Create, Read, Update, Delete) operations. It integrates Continuous Integration and Continuous Deployment (CI/CD) pipelines to automate database tasks with each repository update. Additionally, it supports command line execution of SQL queries with optional output for data analysis.

## Features

- Import data into an SQLite database.
- Clean and transform data.
- Execute SQL queries for analysis.
- Perform CRUD operations.
- Automated CI/CD integration.

## Usage

### Running the Pipeline

1. Clone the repository.
2. Navigate to the project directory.
3. Run the pipeline using `main.py`, optionally with the `--query` flag.

### Executing Queries

You can run SQL queries using the `--query` flag followed by your SQL statement to display results.

## CI/CD

The project automatically performs the following actions on each push:

1. Data loading into SQLite.
2. Data transformation.
3. SQL query execution.
4. Output logging in `output.txt`.
