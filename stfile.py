import streamlit as st
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from generator import GenerateRandomBookList
import pandas as pd

st.title("隨機書本產生器")

uploaded_file = st.file_uploader("選擇檔案")

if uploaded_file is not None:
    print(uploaded_file)
    
    if uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
    elif uploaded_file.name.endswith('.csv'):
        df =  pd.read_csv(uploaded_file)
    else:
        raise ValueError(f"不支援的格式: {uploaded_file.name.endswith}")
    random_books = GenerateRandomBookList(df)
    st.dataframe(random_books, use_container_width=True)

