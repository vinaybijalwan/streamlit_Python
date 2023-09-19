import streamlit as st
import pandas as pd
import altair as alt

# Set up the Streamlit app
st.title("Patanjali Ayurveda Hospital Data Graph")
st.sidebar.title("Options")
filename = st.sidebar.file_uploader("Upload a CSV file", type="csv")
if filename is not None:
    df = pd.read_csv(filename)

    # Let the user choose which columns to count
    column1 = st.sidebar.selectbox("Select the first column to count", df.columns)
    column2 = st.sidebar.selectbox("Select the second column to count", df.columns)

    # Count the values in the two columns and create a DataFrame
    counts = df[[column1, column2]].groupby([column1, column2]).size().reset_index(name="count")

    # Display the counts as a graph
    chart = alt.Chart(counts).mark_bar().encode(
        x=column1,
        y="count",
        color=column2
    ).interactive()
    st.altair_chart(chart, use_container_width=True)


st.write('Total patient' )