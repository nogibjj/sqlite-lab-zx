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
    # Extract
    print("Extracting data...")
    extract()

    # Transform and load
    print("Transforming data...")
    load()

    # Query operations
    print("Querying data...")
    
    conn = connect_db()

    # Create data (example values)
    sample_data = (1, "Apple", 50, "FPro1", 12.5, 0.5, "Norm1", "Tree1", "Node1")
    create_data(conn, sample_data)

    # Read data
    read_data(conn)

    # Update data
    update_data(conn, 100, 1)  # Example: update the count_products to 100 where id is 1

    # Query specific data
    query_apple(conn)

    # Query average count_products
    query_average_count(conn)

    # Delete data
    delete_data(conn, 1)  # Example: delete the record where id is 1

    conn.close()

if __name__ == "__main__":
    main()
