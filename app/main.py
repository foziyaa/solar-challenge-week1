import streamlit as st
import matplotlib.pyplot as plt
from utils import get_combined_data, plot_metric_comparison


st.set_page_config(page_title="Solar Comparison Dashboard", layout="wide")

st.title("☀️ Cross-Country Solar Potential Dashboard")

# Sidebar
metric = st.sidebar.selectbox("Choose metric", ['GHI', 'DNI', 'DHI'])

# Load data
df_all = get_combined_data()

# Show boxplot
st.subheader(f"Boxplot of {metric} by Country")
fig, ax = plt.subplots()
plot_metric_comparison(df_all, metric)
st.pyplot(fig)

# Summary stats
st.subheader("📊 Summary Statistics")
st.dataframe(
    df_all.groupby('Country')[metric].describe()[['mean', '50%', 'std']].rename(columns={'50%': 'median'})
)
