"""Query the database"""

import sqlite3


def connect_db(db_name="GroceryDB.db"):
    """Connect to the SQLite3 database and return the connection."""
    conn = sqlite3.connect(db_name)
    return conn


def create_data(conn, data):
    """Insert data into the GroceryDB table."""
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO GroceryDB (id, general_name, count_products, "
        "ingred_FPro, avg_FPro_products, avg_distance_root, "
        "ingred_normalization_term, semantic_tree_name, semantic_tree_node) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
        data
    )
    conn.commit()
    print("Data inserted successfully!")


def read_data(conn):
    """Query the database for all rows of the GroceryDB table and return the top 5."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GroceryDB LIMIT 5")
    rows = cursor.fetchall()
    print("Top 5 rows of the GroceryDB table:")
    for row in rows:
        print(row)
    return rows


def update_data(conn, new_value, item_id):
    """Update the count_products value of a record in GroceryDB."""
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE GroceryDB SET count_products = ? WHERE id = ?", 
        (new_value, item_id)
    )
    conn.commit()
    print(f"Record with ID {item_id} updated successfully!")


def delete_data(conn, item_id):
    """Delete a record from the GroceryDB table."""
    cursor = conn.cursor()
    cursor.execute("DELETE FROM GroceryDB WHERE id = ?", (item_id,))
    conn.commit()
    print(f"Record with ID {item_id} deleted successfully!")


def query_apple(conn):
    """Query the database for rows where general_name is 'Apple'."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GroceryDB WHERE general_name = 'Apple'")
    rows = cursor.fetchall()
    print("Rows where general_name is 'Apple':")
    for row in rows:
        print(row)
    return rows


def query_average_count(conn):
    """Query the database for the average count_products value."""
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(count_products) FROM GroceryDB")
    avg_value = cursor.fetchone()[0]
    print(f"The average count_products is: {avg_value}")
    return avg_value


def main():
    # Example usage of the functions
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
