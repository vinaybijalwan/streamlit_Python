import streamlit as st
import pandas as pd
import altair as alt

# Load the CSV file
df = pd.read_csv("pah_2016_2022_with_Y_M_02_01.csv")

# Convert date column to datetime type
df['Visit Date'] = pd.to_datetime(df['Visit Date'])

# Create a year filter slider
year_filter = st.slider("Select a year", min_value=df['Visit Date'].min().year, max_value=df['Visit Date'].max().year)

# Filter the data by year
df_filtered = df[df['Visit Date'].dt.year == year_filter]

# Group the data by year and month and count the number of records
df_monthly = df_filtered.groupby([df_filtered['Visit Date'].dt.year, df_filtered['Visit Date'].dt.month]).count()
df_monthly.reset_index(inplace=True)
df_monthly.rename(columns={'date': 'count'}, inplace=True)

# Create an Altair chart for the monthly counts
chart = alt.Chart(df_monthly).mark_bar().encode(
    x=alt.X('date(month):O', title='Month'),
    y=alt.Y('count:Q', title='Count'),
    color=alt.Color('date(year):N', title='Year')
).properties(
    width=600,
    height=400,
    title=f"Patient records by month in {year_filter}"
)

# Show the chart
st.altair_chart(chart)
