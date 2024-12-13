import pandas as pd

def all_xlsx():
    df = pd.read_excel('sop.xlsx')
    data = {}
    
    for index, row in df.head().iterrows():
        data[row['key']] = [row['alert'], row['query']]

    return data

def key_xlsx(key: str):
    df = pd.read_excel('sop.xlsx')
    data = {}
    
    for index, row in df.head().iterrows():
        data[row['key']] = [row['alert'], row['query']]

    return data[f'{key}']