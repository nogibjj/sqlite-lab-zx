import os
import requests
import pandas as pd

def extract(
    url="https://raw.githubusercontent.com/Barabasi-Lab/GroceryDB/main/data/"
        "GroceryDB_IgFPro.csv", 
    file_path="data/Grocery.csv"
):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    
    if os.path.isfile(file_path):
        print(f"File successfully created at: {file_path}")
    else:
        print(f"Failed to create file at: {file_path}")

    df = pd.read_csv(file_path)

    if 'some_column' in df.columns:
        def convert_to_int(value):
            try:
                return int(value)
            except (ValueError, TypeError):
                return None 

        df['some_column'] = df['some_column'].apply(convert_to_int)

    df_sub = df.head(66)
    df_sub.to_csv(file_path, index=False)

    return file_path
