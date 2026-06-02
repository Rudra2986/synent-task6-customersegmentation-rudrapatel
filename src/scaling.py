"""
Feature Scaling Module
Synent Technologies - Data Science Internship (Summer 2026)
Task 6: Customer Segmentation

This module standardizes numerical features using StandardScaler.
Standardization ensures features are on the same scale, preventing columns
with larger absolute ranges from dominating the distance metrics in K-Means.
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler


def scale_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardizes selected features using standard scaling.
    
    Args:
        df (pd.DataFrame): Input dataframe of numerical columns.
        
    Returns:
        pd.DataFrame: Scaled values in a pandas DataFrame with original columns.
    """
    print("  [Action] Scaling features using StandardScaler...")
    scaler = StandardScaler()
    scaled_array = scaler.fit_transform(df)
    
    # Return as DataFrame to preserve column names for ease of tracking
    scaled_df = pd.DataFrame(scaled_array, columns=df.columns)
    return scaled_df


if __name__ == "__main__":
    print("Scaling module initialized.")
