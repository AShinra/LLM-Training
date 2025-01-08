import pandas as pd
import streamlit as st


def get_headers(uploaded_file):

    df = pd.read_excel(uploaded_file)
    df.reset_index(drop=True, inplace=True)
    st.dataframe(df)

    headers = df.columns
    
    return headers
