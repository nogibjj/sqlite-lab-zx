import os
import requests
import pandas as pd

def extract(
    url="https://raw.githubusercontent.com/Barabasi-Lab/GroceryDB/main/data/"
        "GroceryDB_IgFPro.csv", 
    file_path="data/Grocery.csv"
):

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # 下载数据
    with requests.get(url) as r:
        with open(file_path, 'wb') as f:
            f.write(r.content)
    
    # 检查文件是否成功创建
    if os.path.isfile(file_path):
        print(f"File successfully created at: {file_path}")
    else:
        print(f"Failed to create file at: {file_path}")

    df = pd.read_csv(file_path)
    df_sub = df.head(66)
    df_sub.to_csv(file_path, index=False)
    return file_path
