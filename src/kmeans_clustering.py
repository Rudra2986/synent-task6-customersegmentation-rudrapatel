"""
K-Means Clustering Training Module
Synent Technologies - Data Science Internship (Summer 2026)
Task 6: Customer Segmentation

This module trains the final K-Means algorithm using the optimal cluster count
and maps the resulting segment labels back to the customer dataset.
It also serializes the trained model using joblib.
"""

import os
import pandas as pd
from sklearn.cluster import KMeans
import joblib

from feature_selection import select_clustering_features
from scaling import scale_features


def train_kmeans(scaled_data: pd.DataFrame, n_clusters: int) -> KMeans:
    """
    Fits K-Means regressor model.
    """
    print(f"  [Action] Fitting K-Means with {n_clusters} clusters...")
    kmeans = KMeans(n_clusters=n_clusters, init='k-means++', random_state=42, n_init=10)
    kmeans.fit(scaled_data)
    return kmeans


def save_model(model: KMeans, filepath: str):
    """
    Saves model binary.
    """
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    joblib.dump(model, filepath)
    print(f"  [Action] Serialized trained model weights to: {filepath}")


def main():
    cleaned_path = "c:/COLLEGE/Synent-Internship-2026/Task-6-Customer-Segmentation/data/processed/cleaned_customers.csv"
    model_dir = "c:/COLLEGE/Synent-Internship-2026/Task-6-Customer-Segmentation/models"
    processed_dir = "c:/COLLEGE/Synent-Internship-2026/Task-6-Customer-Segmentation/data/processed"
    
    model_path = os.path.join(model_dir, "kmeans_model.joblib")
    output_path = os.path.join(processed_dir, "segmented_customers.csv")
    
    if not os.path.exists(cleaned_path):
        print(f"Error: Cleaned dataset not found at {cleaned_path}")
        return
        
    try:
        df = pd.read_csv(cleaned_path)
        
        # Extract features and scale them
        features = select_clustering_features(df, ['Annual Income (k$)', 'Spending Score (1-100)'])
        scaled_features = scale_features(features)
        
        # Optimal cluster selection for Mall Customers is K=5
        n_clusters = 5
        kmeans = train_kmeans(scaled_features, n_clusters)
        
        # Save model
        save_model(kmeans, model_path)
        
        # Map labels back to dataset
        df['Cluster'] = kmeans.labels_
        
        # Save segmented data
        df.to_csv(output_path, index=False)
        print(f"SUCCESS: Segmented customers file saved to: {output_path}")
        print(f"Segment breakdown:\n{df['Cluster'].value_counts().sort_index()}")
        
    except Exception as e:
        print(f"Error in training: {e}")


if __name__ == "__main__":
    main()
