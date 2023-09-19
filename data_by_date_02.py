#Date:17-02-2023
import streamlit as st
import datetime as dt
import pandas as pd

# Read the CSV file
df = pd.read_csv(r'Jan_2023.csv', encoding='latin1', low_memory=False)

month = ('January', 'February', 'March',
         'April', 'May', 'June',
         'July', 'August', 'September', 
         'October', 'November', 'December')



# Convert date string to datetime and put it in DateTime column.
df['Date'] = pd.to_datetime(df['Visit Date'])

# Create MonthNumber column based from DateTime column.
df["MonthNumber"] = df["Date"].dt.month
#st.dataframe(df)
# Add streamlit selectbox.
sel_month = st.sidebar.selectbox(label="selection the month", options=month)


# Get the month index based from selected month.
# We add 1 since index starts at 0 but our january starts at 1.
month_index = month.index(sel_month) + 1

# Execute query.
st.write('#### Query result')
dfSelection = df.query(
    "MonthNumber == @month_index"
)

# Show data frame with filters applied.
#st.table(dfSelection)
st.dataframe(dfSelection)