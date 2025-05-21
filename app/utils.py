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
    return country_paths.get(country)

def get_combined_data():
    """Load and concatenate all country dataframes, adding a 'Country' column."""
    dfs = []
    for country in ['benin', 'sierraleone', 'togo']:
        path = get_file_path(country)
        if path is None:
            raise ValueError(f"No path defined for country: {country}")
        df = pd.read_csv(path)
        df['Country'] = country.capitalize()
        dfs.append(df)
    combined_df = pd.concat(dfs, ignore_index=True)
    return combined_df

def plot_metric_comparison(df, metric):
    """
    Create a boxplot of a solar metric grouped by Country.
    
    Args:
        df (pd.DataFrame): Combined dataframe with a 'Country' column.
        metric (str): One of 'GHI', 'DNI', or 'DHI'.
    """
    plt.figure(figsize=(8,6))
    sns.boxplot(x='Country', y=metric, data=df)
    plt.title(f'{metric} Comparison by Country')
    plt.xlabel('Country')
    plt.ylabel(metric)
    plt.tight_layout()

def summary_stats_table(df, metric):
    """
    Generate a summary stats table with mean, median, and std by country.
    
    Args:
        df (pd.DataFrame): Combined dataframe with a 'Country' column.
        metric (str): One of 'GHI', 'DNI', or 'DHI'.
        
    Returns:
        pd.DataFrame: Summary stats table.
    """
    stats = df.groupby('Country')[metric].agg(['mean', 'median', 'std'])
    return stats.reset_index()
