"""
Data Cleaning & Preprocessing Module
Synent Technologies - Data Science Internship (Summer 2026)
Task 6: Customer Segmentation

This module performs initial dataset assessment, checks for nulls/duplicates,
standardizes column headings, and saves the cleaned dataset to the processed folder.
"""

import os
import pandas as pd


def assess_dataset(df: pd.DataFrame) -> dict:
    """
    Assesses customer dataset and prints summaries.
    """
    print("=" * 60)
    print("TASK 6: CUSTOMER DATASET ASSESSMENT")
    print("=" * 60)
    
    shape = df.shape
    rows, cols = shape
    print(f"Shape: {rows} rows, {cols} columns")
    print(f"Null Values count:\n{df.isnull().sum()}")
    print(f"Duplicate rows: {df.duplicated().sum()}")
    
    assessment = {
        "rows": rows,
        "columns": cols,
        "nulls": df.isnull().sum().sum(),
        "duplicates": df.duplicated().sum()
    }
    print("=" * 60)
    return assessment


def clean_customer_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans raw customer profiling data.
    """
    cleaned_df = df.copy()
    
    # 1. Drop duplicates
    cleaned_df = cleaned_df.drop_duplicates()
    
    # 2. Check for null values and handle if present (though none are present in this dataset)
    cleaned_df = cleaned_df.dropna()
    
    # 3. Clean column names (strip spaces, resolve special characters)
    cleaned_df.columns = [col.strip() for col in cleaned_df.columns]
    
    return cleaned_df


def main():
    raw_path = "c:/COLLEGE/Synent-Internship-2026/Task-6-Customer-Segmentation/data/raw/Mall_Customers.csv"
    processed_dir = "c:/COLLEGE/Synent-Internship-2026/Task-6-Customer-Segmentation/data/processed"
    output_path = os.path.join(processed_dir, "cleaned_customers.csv")
    
    os.makedirs(processed_dir, exist_ok=True)
    
    if not os.path.exists(raw_path):
        print(f"Error: Raw file not found at {raw_path}")
        return
        
    try:
        df = pd.read_csv(raw_path)
        assess_dataset(df)
        cleaned_df = clean_customer_data(df)
        cleaned_df.to_csv(output_path, index=False)
        print(f"SUCCESS: Cleaned dataset saved to: {output_path}")
        print(f"Final Shape: {cleaned_df.shape}\n")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
