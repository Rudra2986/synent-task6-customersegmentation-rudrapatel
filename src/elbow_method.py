"""
Elbow Method Evaluation Starter Module
Synent Technologies - Data Science Internship (Summer 2026)
Task 6: Customer Segmentation

This module computes and plots the WCSS curve to determine the optimal number of clusters.
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def calculate_wcss(scaled_data: pd.DataFrame, max_k: int = 10) -> list:
    """
    Computes Within-Cluster Sum of Squares (WCSS) for cluster counts from 1 to max_k.
    
    Args:
        scaled_data (pd.DataFrame): Scaled customer feature matrix.
        max_k (int): Maximum cluster count to evaluate.
        
    Returns:
        list: WCSS scores.
    """
    print(f"Calculating WCSS up to K={max_k}...")
    wcss = []
    # TODO: Loop from 1 to max_k, train KMeans(n_clusters=i, random_state=42), append model.inertia_
    return wcss


def plot_elbow_curve(wcss: list, output_image_path: str):
    """
    Saves WCSS elbow curve visualization.
    """
    print(f"Plotting elbow curve to: {output_image_path}")
    # TODO: plt.plot(range(1, len(wcss) + 1), wcss)
    pass


if __name__ == "__main__":
    print("Running Elbow Method starter script.")
