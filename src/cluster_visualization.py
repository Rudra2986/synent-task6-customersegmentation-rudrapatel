"""
Cluster Visualization Module
Synent Technologies - Data Science Internship (Summer 2026)
Task 6: Customer Segmentation

This module creates a 2D Matplotlib/Seaborn scatter plot showing customer segments and centroids,
and generates an interactive 3D Plotly scatter plot (Age vs Income vs Spending Score) 
exported as HTML.
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


def load_segmented_data(file_path: str) -> pd.DataFrame:
    """
    Loads the segmented customer dataset.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Segmented customer dataset not found at: {file_path}")
    return pd.read_csv(file_path)


def plot_2d_clusters(df: pd.DataFrame, output_dir: str):
    """
    Creates a 2D scatter plot of Annual Income vs. Spending Score with cluster centroids.
    """
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "customer_clusters_2d.png")
    
    plt.figure(figsize=(12, 8))
    sns.set_theme(style="whitegrid")
    
    # Define custom harmonious color palette for 5 clusters
    colors = ['#1E3A8A', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6']
    
    # Plot customer points
    sns.scatterplot(
        data=df,
        x='Annual Income (k$)',
        y='Spending Score (1-100)',
        hue='Cluster',
        palette=colors,
        s=100,
        alpha=0.8,
        edgecolor='black',
        legend='full'
    )
    
    # Calculate and plot centroids (mean of unscaled coordinates for display)
    centroids = df.groupby('Cluster')[['Annual Income (k$)', 'Spending Score (1-100)']].mean().reset_index()
    
    plt.scatter(
        centroids['Annual Income (k$)'],
        centroids['Spending Score (1-100)'],
        s=300,
        c='black',
        marker='X',
        label='Centroids',
        edgecolor='white',
        linewidth=2
    )
    
    plt.title('Customer Segmentation (K-Means Clusters)', fontsize=16, fontweight='bold', pad=15)
    plt.xlabel('Annual Income (k$)', fontsize=12)
    plt.ylabel('Spending Score (1-100)', fontsize=12)
    plt.legend(title='Customer Groups', loc='upper right')
    plt.grid(True, linestyle=':', alpha=0.6)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"  [Action] Saved 2D cluster scatter plot to: {output_path}")


def plot_3d_interactive_clusters(df: pd.DataFrame, reports_dir: str):
    """
    Generates an interactive 3D scatter plot of Age vs. Income vs. Spending Score.
    """
    os.makedirs(reports_dir, exist_ok=True)
    output_path = os.path.join(reports_dir, "customer_clusters_3d.html")
    
    # Map numeric Cluster to string categories for better legend rendering
    df_plot = df.copy()
    df_plot['Cluster_Label'] = df_plot['Cluster'].map({
        0: 'Standard (Cluster 0)',
        1: 'High Income / High Spender (Cluster 1)',
        2: 'Low Income / Low Spender (Cluster 2)',
        3: 'Low Income / High Spender (Cluster 3)',
        4: 'High Income / Low Spender (Cluster 4)'
    })
    
    fig = px.scatter_3d(
        df_plot,
        x='Age',
        y='Annual Income (k$)',
        z='Spending Score (1-100)',
        color='Cluster_Label',
        title='Interactive 3D Customer Cohort Mapping',
        labels={'Cluster_Label': 'Customer Cohorts'},
        opacity=0.8,
        color_discrete_sequence=['#1E3A8A', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6'],
        hover_data=['CustomerID', 'Gender']
    )
    
    # Set sizing and layout
    fig.update_layout(
        margin=dict(l=0, r=0, b=0, t=50),
        legend=dict(yanchor="top", y=0.95, xanchor="left", x=0.01)
    )
    
    fig.write_html(output_path)
    print(f"  [Action] Saved 3D interactive HTML plot to: {output_path}")


def main():
    segmented_path = "c:/COLLEGE/Synent-Internship-2026/Task-6-Customer-Segmentation/data/processed/segmented_customers.csv"
    images_dir = "c:/COLLEGE/Synent-Internship-2026/Task-6-Customer-Segmentation/images"
    reports_dir = "c:/COLLEGE/Synent-Internship-2026/Task-6-Customer-Segmentation/reports"
    
    try:
        df = load_segmented_data(segmented_path)
        plot_2d_clusters(df, images_dir)
        plot_3d_interactive_clusters(df, reports_dir)
        print("SUCCESS: Customer Segmentation visualizations created.")
    except Exception as e:
        print(f"Error in visualization plotting: {e}")


if __name__ == "__main__":
    main()
