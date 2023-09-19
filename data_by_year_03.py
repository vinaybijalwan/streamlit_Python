import streamlit as st
import pandas as pd
import datetime
import altair as alt

## basic set up of Dashboad page
st.set_page_config(
    page_title="Patient Dashboard 2016 - 2022",
    page_icon="✅",
    layout="wide",
)




# Set up the Streamlit app
st.title("Patanjali Ayurveda Hospital Data Graph")



##load dataset
@st.experimental_memo
def load_data():
    data=pd.read_csv(r'pah_2016_2022_with_Y_M_02_01.csv', encoding='latin1', low_memory=False)
    return data

df = load_data()


year_filter = st.sidebar.selectbox("Select a Year", [2016, 2017, 2018, 2019, 2020, 2021, 2022])



##load data 2016
if year_filter == 2016:
    filtered_df = df[df['yyyy'] == year_filter]
    st.write(filtered_df.head(100))
    monthly_patient_count = filtered_df.groupby(['yyyy', 'mm']).size()
    chart_data = pd.DataFrame(monthly_patient_count).reset_index()
    #chart_data['date'] = pd.to_datetime(chart_data[['yyyy', 'mm']].assign(day=1))
    chart = alt.Chart(chart_data).mark_bar().encode(
    x='date:T',
    y='patient_count:Q'
    ).properties(
    width=700,
    height=400
    )
    st.altair_chart(chart, use_container_width=True)





    st.write(monthly_patient_count)

    

##load data 2017
if year_filter == 2017:
    filtered_df = df[df['yyyy'] == year_filter]
    st.write(filtered_df.head(100))
    monthly_patient_count = filtered_df.groupby(['yyyy', 'mm']).size()
    st.write(monthly_patient_count)


##load data 2018
if year_filter == 2018:
    filtered_df = df[df['yyyy'] == year_filter]
    st.write(filtered_df.head(100))
    monthly_patient_count = filtered_df.groupby(['yyyy', 'mm']).size()
    st.write(monthly_patient_count)


##load data 2019
if year_filter == 2019:
    filtered_df = df[df['yyyy'] == year_filter]
    st.write(filtered_df.head(100))
    monthly_patient_count = filtered_df.groupby(['yyyy', 'mm']).size()
    st.write(monthly_patient_count)

##load data 2020
if year_filter == 2020:
    filtered_df = df[df['yyyy'] == year_filter]
    st.write(filtered_df.head(100))
    monthly_patient_count = filtered_df.groupby(['yyyy', 'mm']).size()
    st.write(monthly_patient_count)


##load data 2021
if year_filter == 2021:
    filtered_df = df[df['yyyy'] == year_filter]
    st.write(filtered_df.head(100))
    monthly_patient_count = filtered_df.groupby(['yyyy', 'mm']).size()
    st.write(monthly_patient_count)


#load data 2022

if year_filter == 2022:
    filtered_df = df[df['yyyy'] == year_filter]
    st.write(filtered_df.head(100))
    monthly_patient_count = filtered_df.groupby(['yyyy', 'mm']).size()
    st.write(monthly_patient_count)