import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_file_path(country):
    """Return the CSV file path for each country."""
    country_paths = {
        "benin": "notebooks/eda/data/eda_clean.csv",
        "sierraleone": "notebooks/sierraleone/data/sierraleone_clean.csv",
        "togo": "notebooks/togo/data/togo_clean.csv"
    }

    if not isinstance(country, str):
        raise TypeError("Country must be a string.")
    
    path = country_paths.get(country.lower())
    if path is None:
        raise ValueError(f"No file path defined for country: {country}")
    
    return path

def get_combined_data():
    """Load and concatenate all country DataFrames, adding a 'Country' column."""
    countries = ['benin', 'sierraleone', 'togo']
    dfs = []

    for country in countries:
        try:
            path = get_file_path(country)
            if not os.path.exists(path):
                raise FileNotFoundError(f"File not found: {path}")
            df = pd.read_csv(path)
            df['Country'] = country.capitalize()
            dfs.append(df)
        except Exception as e:
            print(f"Error loading data for {country}: {e}")
            continue

    if not dfs:
        raise ValueError("No valid data loaded from any country.")
    
    combined_df = pd.concat(dfs, ignore_index=True)
    return combined_df

def plot_metric_comparison(df, metric):
    """
    Create a boxplot of a solar metric grouped by Country.

    Args:
        df (pd.DataFrame): DataFrame with a 'Country' column.
        metric (str): One of 'GHI', 'DNI', or 'DHI'.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame.")
    if 'Country' not in df.columns:
        raise ValueError("DataFrame must contain a 'Country' column.")
    if metric not in df.columns:
        raise ValueError(f"'{metric}' not found in DataFrame.")

    try:
        plt.figure(figsize=(8,6))
        sns.boxplot(x='Country', y=metric, data=df)
        plt.title(f'{metric} Comparison by Country')
        plt.xlabel('Country')
        plt.ylabel(metric)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error creating boxplot for {metric}: {e}")

def summary_stats_table(df, metric):
    """
    Generate a summary stats table with mean, median, and std by country.

    Args:
        df (pd.DataFrame): DataFrame with a 'Country' column.
        metric (str): Metric column to summarize.

    Returns:
        pd.DataFrame: Summary statistics table.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame.")
    if 'Country' not in df.columns:
        raise ValueError("DataFrame must contain a 'Country' column.")
    if metric not in df.columns:
        raise ValueError(f"'{metric}' not found in DataFrame.")

    try:
        stats = df.groupby('Country')[metric].agg(['mean', 'median', 'std'])
        return stats.reset_index()
    except Exception as e:
        print(f"Error generating summary table for {metric}: {e}")
        return pd.DataFrame()
