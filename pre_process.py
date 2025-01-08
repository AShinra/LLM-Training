import pandas as pd


def get_headers(uploaded_file):

    df = pd.read_excel(uploaded_file)

    headers = df.columns
    
    return headers
