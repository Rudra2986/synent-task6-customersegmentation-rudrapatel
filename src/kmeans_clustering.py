"""
K-Means Clustering Model Training Module
Synent Technologies - Data Science Internship (Summer 2026)
Task 6: Customer Segmentation

This module trains the final K-Means model using the selected optimal clusters.
"""

import pandas as pd
from sklearn.cluster import KMeans
import joblib


def train_kmeans(scaled_data: pd.DataFrame, n_clusters: int) -> KMeans:
    """
    Fits a K-Means model on scaled data.
    
    Args:
        scaled_data (pd.DataFrame): Normalized feature matrix.
        n_clusters (int): Number of target clusters.
        
    Returns:
        KMeans: Fitted KMeans object.
    """
    print(f"Training K-Means with {n_clusters} clusters...")
    # TODO: Initialize KMeans, fit model, return model
    return KMeans()


def save_model(model: KMeans, filepath: str):
    """
    Persists trained model using joblib.
    """
    print(f"Saving model artifact to: {filepath}")
    # TODO: joblib.dump(model, filepath)
    pass


if __name__ == "__main__":
    print("Running K-Means Clustering starter script.")
