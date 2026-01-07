# Import packages for Streamlit app
import streamlit as st
import pandas as pd
import plotly.express as px

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
    options=['Bar Chart', 'Pie Chart', 'Line Chart'],
    default='Bar Chart'
)
pie_selected = bool(chart_type == 'Pie Chart')
# Sidebar filter variables
select_pie = st.sidebar.selectbox(
    'Select Pie Chart Variable',
    options=police_df.columns.tolist(),
    visible=pie_selected
)
# Select x axis variable
select_x = st.sidebar.selectbox(
    'Select X-axis Variable',
    options=police_df.columns.tolist(),
    visible=not pie_selected
)
# Select y axis variable
select_y = st.sidebar.selectbox(
    'Select Y-axis Variable',
    options=police_df.columns.tolist(),
    visible=not pie_selected
)
# Dynamic filter to select colour
select_color = st.sidebar.selectbox(
    'Select Colour Variable',
    options=police_df.columns.tolist(),
    visible=not pie_selected
)

# Header
st.title('UK Police Crime Data Analysis')

# Different chart based on sidebar selection
# Filter data based on sidebar selection
if chart_type == 'Bar Chart':
    fig = px.bar(
        police_df,
        title=f'{chart_type} of {select_y} vs {select_x} coloured by {select_color}',
        x=select_x,
        y=select_y,
        color=select_color
    )
elif chart_type == 'Pie Chart':
    fig = px.pie(
        police_df,
        title=f'{chart_type} of {select_y} vs {select_x} coloured by {select_color}',
        names=select_x,
        values=select_y
    )
elif chart_type == 'Line Chart':
    fig = px.line(
        police_df,
        x=select_x,
        y=select_y
    )
st.plotly_chart(fig)
