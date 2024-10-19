"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

food dataset
"""
import requests
import pandas as pd

def extract(url="https://raw.githubusercontent.com/Barabasi-Lab/GroceryDB/main/data/GroceryDB_IgFPro.csv", 
            file_path="data/Grocery.csv"):
    """"Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    df=pd.read_csv(file_path)
    df_sub=df.head(66)
    df_sub.to_csv(file_path, index=False)
    return file_path



