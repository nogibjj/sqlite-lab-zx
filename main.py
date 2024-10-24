"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import (
    connect_db,
    create_data,
    read_data,
    update_data,
    delete_data,
    query_apple,
    query_average_count
)

def main():
    # Extract the data
    file_path = extract()  # Call the extract function

    # Load the extracted data into the database
    conn = connect_db()
    load(file_path)  # Call the load function

    # Read data
    read_data(conn)

    # Create data (example values, now without id)
    sample_data = ("Apple", 50, "FPro1", 12.5, 0.5, "Norm1", "Tree1", "Node1")
    create_data(conn, sample_data)

    # Query specific data
    query_apple(conn)

    # Query average count_products
    query_average_count(conn)

    # Delete data (optional)
    # delete_data(conn, 1)  # Example: delete the record where id is 1

    conn.close()

if __name__ == "__main__":
    main()

