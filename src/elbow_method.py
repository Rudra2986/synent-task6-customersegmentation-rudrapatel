"""
Elbow Method Evaluation Module
Synent Technologies - Data Science Internship (Summer 2026)
Task 6: Customer Segmentation

This module performs the Elbow Method to evaluate the optimal number of clusters
by running K-Means across a range of K values and plotting the WCSS (Within-Cluster Sum of Squares).
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

from feature_selection import select_clustering_features
from scaling import scale_features


def calculate_wcss(scaled_data: pd.DataFrame, max_k: int = 10) -> list:
    """
    Runs K-Means for K values from 1 to max_k and records inertia.
    """
    print(f"  [Action] Calculating WCSS scores for K range 1 to {max_k}...")
    wcss = []
    for k in range(1, max_k + 1):
        # random_state=42 ensures reproducibility of centroid initialization
        kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42, n_init=10)
        kmeans.fit(scaled_data)
        wcss.append(kmeans.inertia_)
    return wcss


def plot_elbow_curve(wcss: list, output_dir: str):
    """
    Plots the WCSS curve and saves it to output_dir/elbow_method.png.
    """
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "elbow_method.png")
    
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(wcss) + 1), wcss, marker='o', linestyle='--', color='#1E3A8A', linewidth=2)
    plt.title('The Elbow Method for Optimal K Choice', fontsize=14, fontweight='bold')
    plt.xlabel('Number of Clusters (K)', fontsize=12)
    plt.ylabel('WCSS (Inertia)', fontsize=12)
    plt.xticks(range(1, len(wcss) + 1))
    plt.grid(True, linestyle=':', alpha=0.6)
    
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"  [Action] Saved Elbow Method plot to: {output_path}")


def main():
    cleaned_path = "c:/COLLEGE/Synent-Internship-2026/Task-6-Customer-Segmentation/data/processed/cleaned_customers.csv"
    output_dir = "c:/COLLEGE/Synent-Internship-2026/Task-6-Customer-Segmentation/images"
    
    if not os.path.exists(cleaned_path):
        print(f"Error: Cleaned dataset not found at {cleaned_path}")
        return
        
    try:
        df = pd.read_csv(cleaned_path)
        
        # Select target features for clustering
        features = select_clustering_features(df, ['Annual Income (k$)', 'Spending Score (1-100)'])
        
        # Scale features
        scaled_features = scale_features(features)
        
        # Calculate WCSS
        wcss = calculate_wcss(scaled_features)
        
        # Plot elbow curve
        plot_elbow_curve(wcss, output_dir)
        
    except Exception as e:
        print(f"Error in Elbow Method calculation: {e}")


if __name__ == "__main__":
    main()
