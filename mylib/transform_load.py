import sqlite3
import csv
import os

def load(dataset="/workspaces/sqlite-lab-zx/data/Grocery.csv"):
    """Transforms and Loads data into the local SQLite3 database"""

    # Prints the full working directory and path
    print(os.getcwd())

    # Open the CSV file and create a reader
    with open(dataset, newline='') as csvfile:
        payload = csv.reader(csvfile, delimiter=',')
        
        # Skip the header row
        next(payload)

        # Create a connection to the SQLite database
        conn = sqlite3.connect('GroceryDB.db')
        c = conn.cursor()
        
        # Drop the table if it exists and create a new one
        c.execute("DROP TABLE IF EXISTS GroceryDB")
        c.execute("CREATE TABLE GroceryDB (id INTEGER PRIMARY KEY AUTOINCREMENT, general_name TEXT, "
                  "count_products INTEGER, ingred_FPro TEXT, avg_FPro_products REAL, "
                  "avg_distance_root REAL, ingred_normalization_term TEXT, "
                  "semantic_tree_name TEXT, semantic_tree_node TEXT)")

        # Insert data into the database
        for row in payload:
            try:
                # Convert data types as needed
                general_name = row[0]
                count_products = int(row[1])  # Ensure this is an integer
                ingred_FPro = row[2]
                avg_FPro_products = float(row[3])  # Ensure this is a float
                avg_distance_root = float(row[4])  # Ensure this is a float
                ingred_normalization_term = row[5]
                semantic_tree_name = row[6]
                semantic_tree_node = row[7]

                # Insert into the database
                c.execute("INSERT INTO GroceryDB (general_name, count_products, ingred_FPro, "
                          "avg_FPro_products, avg_distance_root, ingred_normalization_term, "
                          "semantic_tree_name, semantic_tree_node) "
                          "VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
                          (general_name, count_products, ingred_FPro, 
                           avg_FPro_products, avg_distance_root, 
                           ingred_normalization_term, semantic_tree_name, 
                           semantic_tree_node))
            except ValueError as e:
                print(f"Error converting data: {e} - Row: {row}")
                continue  # Skip this row if there's an error

        conn.commit()
        conn.close()
        return "GroceryDB.db"



