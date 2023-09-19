import streamlit as st
import pandas as pd

@st.cache
def load_data(file_path):
    return pd.read_csv(file_path)

def main():
    st.title("Filter Data from CSV Example")
    file_path = st.file_uploader("Upload a CSV file", type=["csv"])

    if file_path:
        df = load_data(file_path)
        column_options = df.columns.tolist()
        selected_column = st.selectbox("Select a column to filter by", column_options)
        unique_values = df[selected_column].unique().tolist()
        selected_value = st.selectbox("Select a value to filter by", unique_values)
        filtered_df = df[df[selected_column] == selected_value]
        st.dataframe(filtered_df)

if __name__ == '__main__':
    main()
