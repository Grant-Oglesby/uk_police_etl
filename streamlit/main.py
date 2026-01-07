# Import packages for Streamlit app
import streamlit as st
import pandas as pd
from plotly import express as px

# Set page configuration
st.set_page_config(
    page_title='UK Police Stop and Search Data Analysis',
    page_icon=':bar_chart:',
    layout='wide'
)

# Load cleaned data
police_df = pd.read_csv('data/transform/clean_data.csv')

# Streamlit app layout

# Sidebar
st.sidebar.header('Filter Options')
# Chart type selection
chart_type = st.sidebar.selectbox(
    'Select Chart Type',
    options=['Bar Chart', 'Line Chart'],
    index=0
)
# Sidebar filter variables
# Select x axis variable
select_x = st.sidebar.selectbox(
    'Select X-axis Variable',
    options=police_df.columns.tolist(),
    index=0
)
# Select y axis variable
select_y = st.sidebar.selectbox(
    'Select Y-axis Variable',
    options=police_df.columns.tolist(),
    index=1
)
# Dynamic filter to select colour
select_color = st.sidebar.selectbox(
    'Select Colour Variable',
    options=police_df.columns.tolist(),
    index=2
)

# Header
st.title('UK Police Crime Data Analysis')

# Prepare new df to hold selected data outside figures for optimisation
display_df = police_df[[select_x, select_y, select_color]].copy()


# Different chart based on sidebar selection
# Filter data based on sidebar selection
if chart_type == 'Bar Chart':
    fig = px.bar(
        display_df,
        title=f'{chart_type} of {select_y} vs {select_x}',
        x=select_x,
        y=select_y,
        color=select_color
    )
elif chart_type == 'Line Chart':
    fig = px.line(
        display_df,
        title=f'{chart_type} of {select_y} vs {select_x}',
        x=select_x,
        y=select_y
    )
else:
    st.write("Please select a valid chart type.")
st.plotly_chart(fig)
