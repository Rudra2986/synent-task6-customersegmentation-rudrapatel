"""
Feature Selection Starter Module
Synent Technologies - Data Science Internship (Summer 2026)
Task 6: Customer Segmentation

This module handles feature extraction and mapping for clustering algorithms.
"""

import pandas as pd


def select_clustering_features(df: pd.DataFrame, feature_columns: list) -> pd.DataFrame:
    """
    Filters the dataset to only include variables required for the K-Means algorithm.
    
    Args:
        df (pd.DataFrame): Cleaned customer dataset.
        feature_columns (list): List of column names to keep for clustering.
        
    Returns:
        pd.DataFrame: Feature matrix.
    """
    print(f"Selecting features for clustering: {feature_columns}")
    # TODO: Implement feature selection logic
    return pd.DataFrame()


if __name__ == "__main__":
    print("Running Feature Selection starter script.")
