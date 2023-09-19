import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("pah_2016_2022_with_Y_M_02.csv")

# Define the filter options
years = data['yyyy'].unique()
months = data['mm'].unique()
dates = data['Visit Date'].unique()

# Create the Streamlit app
st.title("Filter and Plot Data")

# Year filter
year_filter = st.selectbox("Select a year", years)

# Month filter
month_filter = st.selectbox("Select a month", months)

# Date filter
date_filter = st.selectbox("Select a date", dates)

# Filter the data
filtered_data = data[(data['yyyy'] == year_filter) &
                     (data['mm'] == month_filter) &
                     (data['Visit Date'] == date_filter)]

# Plot the data
if not filtered_data.empty:
    st.write("Line chart for filtered data")
    fig, ax = plt.subplots()
    ax.plot(filtered_data['data'])
    st.pyplot(fig)

# Year-wise line chart
st.write("Line chart year-wise")
year_data = data.groupby('yyyy').sum()
fig, ax = plt.subplots()
ax.plot(year_data['data'])
st.pyplot(fig)

# Month-wise line chart
st.write("Line chart month-wise")
month_data = data.groupby(['yyyy', 'mm']).sum().reset_index()
month_data_filtered = month_data[month_data['yyyy'] == year_filter]
fig, ax = plt.subplots()
ax.plot(month_data_filtered['mm'], month_data_filtered['Data'])
st.pyplot(fig)

# Date-wise line chart
st.write("Line chart date-wise")
date_data = data.groupby(['yyyy', 'mm', 'Visit Date']).sum().reset_index()
date_data_filtered = date_data[(date_data['yyyy'] == year_filter) &
                              (date_data['mm'] == month_filter)]
fig, ax = plt.subplots()
ax.plot(date_data_filtered['Date'], date_data_filtered['Data'])
st.pyplot(fig)
