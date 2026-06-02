"""
Feature Scaling Starter Module
Synent Technologies - Data Science Internship (Summer 2026)
Task 6: Customer Segmentation

This module standardizes numerical features so that K-Means Euclidean distance 
computations are not biased by feature magnitudes.
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler


def scale_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies StandardScaler to scale features.
    
    Args:
        df (pd.DataFrame): Dataframe of selected features.
        
    Returns:
        pd.DataFrame: Scaled data values in a DataFrame.
    """
    print("Applying StandardScaler scaling...")
    # TODO: Initialize StandardScaler, fit_transform features, return scaled DataFrame
    return pd.DataFrame()


if __name__ == "__main__":
    print("Running Scaling starter script.")
