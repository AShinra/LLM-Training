import streamlit as st


def upload_xlsx_file():
    uploaded_file = st.file_uploader(label='Input XLSX File', type=['xlsx', 'xls'], accept_multiple_files=False, key='uploaded_xlsx')
    return uploaded_file