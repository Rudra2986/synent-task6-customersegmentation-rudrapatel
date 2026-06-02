"""
Data Cleaning Starter Module
Synent Technologies - Data Science Internship (Summer 2026)
Task 6: Customer Segmentation

This module performs initial data loading, null checking, type checks, and duplicate cleaning.
"""

import pandas as pd


def load_raw_data(file_path: str) -> pd.DataFrame:
    """
    Loads raw customer profile data.
    """
    print(f"Loading raw data from: {file_path}")
    # TODO: Implement loading logic
    return pd.DataFrame()


def clean_customer_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans raw customer data by handling null values and dropping duplicates.
    
    Args:
        df (pd.DataFrame): Raw customer data.
        
    Returns:
        pd.DataFrame: Cleaned dataframe.
    """
    print("Checking for nulls and duplicates...")
    # TODO: df.isnull().sum() checks
    # TODO: df.drop_duplicates()
    return df


if __name__ == "__main__":
    print("Running Customer Data Cleaning starter script.")
