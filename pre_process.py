import pandas as pd
import streamlit as st


def get_headers(uploaded_file):

    df = pd.read_excel(uploaded_file)
    df.reset_index(drop=True, inplace=True)

    headers = df.columns
    
    return df, headers
