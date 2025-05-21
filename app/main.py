# app/main.py

import streamlit as st
import pandas as pd
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
st.set_page_config(
    page_title="Data Insights Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 Dynamic Data Insights Dashboard")
st.sidebar.header("Dashboard Controls")

num_rows = st.sidebar.slider("Select number of rows", 10, 1000, 100)
metric = st.sidebar.selectbox("Select a metric", ["sales", "profit", "quantity"])
chart_type = st.sidebar.radio("Chart type", ["Bar Chart", "Line Chart"])

df = generate_dummy_data(num_rows)

st.subheader(f"Showing first {num_rows} rows of data")
st.dataframe(df.head())

st.subheader(f"{chart_type} for {metric.title()}")

if chart_type == "Bar Chart":
    plot_bar_chart(df, metric)
else:
    plot_line_chart(df, metric)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
