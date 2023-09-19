import streamlit as st
import pandas as pd
import plotly_express  as px

st.set_page_config(page_title='Excel Plotter')

st.title('Excel Plotter 📈')
st.subheader('Feed me with Your Excel file')


upload_file = st.file_uploader('Choose a XLSX File', type='xlsx')

if upload_file:
    st.markdown('---')
    df = pd.read_excel(upload_file, engine='openpyxl', header=2)
    st.dataframe(df)

groupby_column = st.selectbox('What would you like to analysis',
('State', 'Department', 'Gender'),
)
