# app/main.py

import streamlit as st
import pandas as pd
from utils import generate_dummy_data


# Set Streamlit page configuration
st.set_page_config(
    page_title="Data Insights Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# App title
st.title("📊 Dynamic Data Insights Dashboard")

# Sidebar controls
st.sidebar.header("Dashboard Controls")

# Slider for number of data rows
num_rows = st.sidebar.slider("Select number of rows", 10, 1000, 100)

# Select metric to analyze
metric = st.sidebar.selectbox("Select a metric", ["sales", "profit", "quantity"])

# Select chart type
chart_type = st.sidebar.radio("Chart type", ["Bar Chart", "Line Chart"])

# Simulate or fetch data
df = generate_dummy_data(num_rows)

# Display DataFrame
st.subheader(f"Showing first {num_rows} rows of data")
st.dataframe(df.head())

# Chart rendering based on user choice
st.subheader(f"{chart_type} for {metric.title()}")

if chart_type == "Bar Chart":
    plot_bar_chart(df, metric)
else:
    plot_line_chart(df, metric)

# Optional: Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")

