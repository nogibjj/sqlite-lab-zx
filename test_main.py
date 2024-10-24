"""
Test for the database operations in the GroceryDB
"""

import pytest
from mylib.query import connect_db, create_data, read_data, delete_data

@pytest.fixture
def setup_database():
    """Set up the database for testing."""
    # Connect to the test database
    conn = connect_db("test_GroceryDB.db")

    # Create a table for testing
    conn.execute("CREATE TABLE GroceryDB (id INTEGER PRIMARY KEY AUTOINCREMENT, "
                 "general_name TEXT, "
                 "count_products INTEGER, ingred_FPro TEXT, avg_FPro_products REAL, "
                 "avg_distance_root REAL, ingred_normalization_term TEXT, "
                 "semantic_tree_name TEXT, semantic_tree_node TEXT)")

    yield conn  # This allows the test to run with the database

    # Teardown: Drop the table after tests
    conn.execute("DROP TABLE GroceryDB")
    conn.close()


def test_create_and_read_data(setup_database):
    """Test creating and reading data from the database."""
    conn = setup_database

    # Sample data to insert
    sample_data = ("Apple", 50, "FPro1", 12.5, 0.5, "Norm1", "Tree1", "Node1")
    
    # Create data
    create_data(conn, sample_data)

    # Read data
    rows = read_data(conn)

    # Verify that the inserted data is correctly read
    assert len(rows) == 1  # We should have one row
    assert rows[0][1] == "Apple"  # Check general_name
    assert rows[0][2] == 50  # Check count_products


def test_delete_data(setup_database):
    """Test deleting data from the database."""
    conn = setup_database

    # Insert sample data
    sample_data = ("Banana", 30, "FPro2", 10.5, 0.3, "Norm2", "Tree2", "Node2")
    create_data(conn, sample_data)

    # Verify it was inserted
    rows = read_data(conn)
    assert len(rows) == 1  # Should be one row

    # Delete the inserted data
    delete_data(conn, 1)  # Assuming the id is 1

    # Verify that the data is deleted
    rows = read_data(conn)
    assert len(rows) == 0  # Should be no rows left

