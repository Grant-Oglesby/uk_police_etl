# Import packages for Streamlit app
import streamlit as st
import os
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_congfig(
    page_title='UK Police Stop and Search Data Analysis',
    page_icon=':bar_chart:',
    layout='wide'
)

# Load cleaned data
police_df = pd.read_csv('data/transform/clean_data.csv')

# Streamlit app layout

# Sidebar
st.sidebar.header('Filter Options')
# Sidebar filter variables
gender_filter = st.sidebar.multiselect(
    'Select Gender',
    options=police_df['gender'].unique(),
    default=police_df['gender'].unique()
)

# Header
st.title('UK Police Crime Data Analysis')

# Display pie chart of crime categories
category_counts = police_df['gender'].value_counts().reset_index()
fig = px.pie(category_counts, names='gender', values='count', title='Gender Distribution')
st.plotly_chart(fig)