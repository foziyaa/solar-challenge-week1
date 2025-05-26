# app/main.py

import streamlit as st
import pandas as pd
<<<<<<< HEAD
from app.utils import generate_dummy_data, plot_bar_chart, plot_line_chart

# Set Streamlit page configuration
=======
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Simulate dummy data function
# -----------------------------
def generate_dummy_data(n):
    np.random.seed(0)
    data = {
        "date": pd.date_range(start="2023-01-01", periods=n),
        "sales": np.random.randint(100, 1000, size=n),
        "profit": np.random.randint(10, 500, size=n),
        "quantity": np.random.randint(1, 100, size=n)
    }
    return pd.DataFrame(data)

# -----------------------------
# Plotting functions
# -----------------------------
def plot_bar_chart(df, metric):
    st.bar_chart(df.set_index("date")[metric])

def plot_line_chart(df, metric):
    st.line_chart(df.set_index("date")[metric])

# -----------------------------
# Streamlit App Setup
# -----------------------------
>>>>>>> 6bb3b2c3ce964c6d979b364a53b527dd1bf3bb9d
st.set_page_config(
    page_title="Data Insights Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

<<<<<<< HEAD
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
=======
st.title("📊 Dynamic Data Insights Dashboard")
st.sidebar.header("Dashboard Controls")

num_rows = st.sidebar.slider("Select number of rows", 10, 1000, 100)
metric = st.sidebar.selectbox("Select a metric", ["sales", "profit", "quantity"])
chart_type = st.sidebar.radio("Chart type", ["Bar Chart", "Line Chart"])

df = generate_dummy_data(num_rows)

st.subheader(f"Showing first {num_rows} rows of data")
st.dataframe(df.head())

>>>>>>> 6bb3b2c3ce964c6d979b364a53b527dd1bf3bb9d
st.subheader(f"{chart_type} for {metric.title()}")

if chart_type == "Bar Chart":
    plot_bar_chart(df, metric)
else:
    plot_line_chart(df, metric)

<<<<<<< HEAD
# Optional: Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")

=======
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
>>>>>>> 6bb3b2c3ce964c6d979b364a53b527dd1bf3bb9d
