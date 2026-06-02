"""
Feature Selection Module
Synent Technologies - Data Science Internship (Summer 2026)
Task 6: Customer Segmentation

This module extracts specific customer features (Annual Income and Spending Score)
to be used for K-Means clustering.
"""

import pandas as pd


def select_clustering_features(df: pd.DataFrame, feature_columns: list) -> pd.DataFrame:
    """
    Subsets the dataframe to only include target features for clustering.
    
    Args:
        df (pd.DataFrame): Cleaned customer dataset.
        feature_columns (list): Columns to extract.
        
    Returns:
        pd.DataFrame: Matrix containing only selected features.
    """
    print(f"  [Action] Selecting clustering columns: {feature_columns}")
    return df[feature_columns]


if __name__ == "__main__":
    # Small test loop
    print("Feature Selection module initialized.")
