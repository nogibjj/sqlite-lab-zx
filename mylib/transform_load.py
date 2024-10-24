"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,
avg_distance_root,ingred_normalization_term,semantic_tree_name,
semantic_tree_node
"""
import sqlite3
import csv
import os

#load the csv file and insert into a new sqlite3 database
def load(dataset="data/Grocery.csv"):  # 修改为相对路径
    """Transforms and Loads data into the local SQLite3 database"""

    print(os.getcwd())

    if not os.path.isfile(dataset):
        print(f"Error: The dataset '{dataset}' does not exist.")
        return None

    payload = csv.reader(open(dataset, newline=''), delimiter=',')
    conn = sqlite3.connect('GroceryDB.db')
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS GroceryDB")
    c.execute("CREATE TABLE GroceryDB (id INT PRIMARY KEY,general_name,"
              "count_products, ingred_FPro, avg_FPro_products," 
              "avg_distance_root, ingred_normalization_term,"
              "semantic_tree_name, semantic_tree_node)")
    
    c.executemany("INSERT INTO GroceryDB VALUES (?,?, ?, ?, ?, ?, ?, ?, ?)", payload)
    conn.commit()
    conn.close()
    return "GroceryDB.db"


