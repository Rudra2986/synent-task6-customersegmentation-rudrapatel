"""
Cluster Visualization Starter Module
Synent Technologies - Data Science Internship (Summer 2026)
Task 6: Customer Segmentation

This module handles multi-dimensional plotting of the customer cohorts.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def plot_2d_clusters(df: pd.DataFrame, x_col: str, y_col: str, label_col: str, output_path: str):
    """
    Plots cluster labels on a 2D scatter chart.
    
    Args:
        df (pd.DataFrame): Dataframe with features and cluster labels.
        x_col (str): X axis feature column.
        y_col (str): Y axis feature column.
        label_col (str): Column holding the cluster predictions.
        output_path (str): Filepath to save the plot.
    """
    print(f"Plotting 2D clusters: {x_col} vs {y_col}...")
    # TODO: plt.figure(), sns.scatterplot(), plt.savefig()
    pass


def plot_3d_interactive_clusters(df: pd.DataFrame, x_col: str, y_col: str, z_col: str, label_col: str, output_html_path: str):
    """
    Generates interactive 3D scatter chart of clusters and exports to HTML.
    """
    print(f"Generating 3D interactive plot for: {x_col}, {y_col}, {z_col}...")
    # TODO: px.scatter_3d(), fig.write_html()
    pass


if __name__ == "__main__":
    print("Running Cluster Visualization starter script.")
