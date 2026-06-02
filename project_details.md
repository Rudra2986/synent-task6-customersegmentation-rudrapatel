# Synent Technologies - Data Science Internship (Summer 2026)
## Task 6: Customer Segmentation & Behavioral Analysis (Consolidated Project Details)

> **Goal:** This document serves as a complete, self-contained reference detailing the dataset, code architecture, script functions, clustering logic, segment profiles, and environment configuration of the Customer Segmentation project. You can provide this file to any LLM/AI to immediately grant it full context for debugging, explaining, or writing extension features.

---

## 👤 Author Information
- **Name:** Rudra Patel
- **Internship ID:** `SYN/J2/IP806`
- **Email:** `rudrapatel2156@gmail.com`
- **LinkedIn Profile:** [Rudra Patel](https://www.linkedin.com/in/rudrapatel-cs)
- **GitHub Profile:** [Rudra2986](https://www.github.com/Rudra2986)

---

## 📂 Project Directory Structure
```
Task-6-Customer-Segmentation/
│
├── data/
│   ├── raw/                 # Contains raw Mall_Customers.csv
│   │   └── Mall_Customers.csv
│   └── processed/           # Contains cleaned and labeled datasets
│       ├── cleaned_customers.csv
│       └── segmented_customers.csv
│
├── notebooks/
│   └── customer_segmentation.ipynb # Complete step-by-step notebook
│
├── src/                     # Core python pipeline modules
│   ├── data_cleaning.py     # Check for nulls/duplicates & parse headers
│   ├── feature_selection.py # Subsetting target dimensions
│   ├── scaling.py           # Standardize features using StandardScaler
│   ├── elbow_method.py      # Calculate WCSS & plot Elbow curve
│   ├── kmeans_clustering.py # Train model & map cohort labels
│   └── cluster_visualization.py # Generate 2D image and 3D HTML plot
│
├── reports/
│   └── customer_clusters_3d.html # Interactive 3D HTML visualization
│
├── images/                  # Visual assets
│   ├── elbow_method.png     # Line plot showing optimal K point
│   └── customer_clusters_2d.png # Scatter plot showing segments & centroids
│
├── models/                  # Serialized ML assets
│   └── kmeans_model.joblib  # Saved K-Means trained model weights
│
├── requirements.txt         # Project packages list
├── README.md                # General readme overview
└── project_details.md       # [This File] All-in-one AI context file
```

---

## 📊 Dataset Specifications
* **Dataset Name:** `Mall_Customers.csv` (Located under `data/raw/`)
* **Shape:** $200$ rows, $5$ columns.
* **Fields & Data Types:**
  1. `CustomerID`: `int64` (Unique identifier per customer)
  2. `Gender`: `object` (`Male` or `Female` categorical string)
  3. `Age`: `int64` (Age of customer in years)
  4. `Annual Income (k$)`: `int64` (Annual household income in thousands of dollars)
  5. `Spending Score (1-100)`: `int64` (Score assigned by the mall based on purchase frequency/depth)

---

## ⚙️ Dependencies & Virtual Env
The required modules in `requirements.txt` are:
* `pandas` & `numpy` (Data manipulation)
* `matplotlib` & `seaborn` (Static plotting)
* `plotly` (Interactive 3D HTML graphs)
* `scikit-learn` (StandardScaler and KMeans clustering algorithms)
* `joblib` (Model serialization)

---

## 🛠️ Code Modules & Logic Explanations

### 1. `src/data_cleaning.py`
* **Purpose:** Inspects dataset health, nulls, duplicates, and standardizes structure.
* **Key Functions:**
  * `assess_dataset(df: pd.DataFrame) -> dict`: Returns row/col shape, null summaries, and duplicate metrics, printing an analytical summary.
  * `clean_customer_data(df: pd.DataFrame) -> pd.DataFrame`: Removes duplicate records, drops null values, and strips whitespace from headers.
* **Output:** Saves results to `data/processed/cleaned_customers.csv`.

### 2. `src/feature_selection.py`
* **Purpose:** Selects features of interest for spatial distance analysis.
* **Key Function:**
  * `select_clustering_features(df: pd.DataFrame, feature_columns: list) -> pd.DataFrame`: Extracts specific numeric dimensions (e.g. `['Annual Income (k$)', 'Spending Score (1-100)']`).

### 3. `src/scaling.py`
* **Purpose:** Standardizes columns to prevent features with wider ranges from distorting Euclidean distance values.
* **Key Function:**
  * `scale_features(df: pd.DataFrame) -> pd.DataFrame`: Applies `StandardScaler` from scikit-learn. Preserves feature headers inside a pandas DataFrame wrapper.

### 4. `src/elbow_method.py`
* **Purpose:** Solves the optimal number of clusters ($K$) using the Elbow Method.
* **Key Calculations:**
  * Runs K-Means across a cluster range of $K = 1$ to $10$.
  * Calculates WCSS (Within-Cluster Sum of Squares) or Inertia for each $K$.
  * Plots WCSS values vs. $K$ numbers. The point where the rate of decrease drops significantly represents the optimal cluster count.
* **Output:** Saves the line plot as `images/elbow_method.png`.

### 5. `src/kmeans_clustering.py`
* **Purpose:** Fits the K-Means clustering algorithm to the standardized features and labels customers.
* **Key Steps:**
  * Trains a K-Means model (`n_clusters=5`, `init='k-means++'`, `random_state=42`).
  * Serializes the model using `joblib.dump` to `models/kmeans_model.joblib`.
  * Assigns cluster index numbers ($0$ to $4$) back to the unscaled customer dataset.
* **Output:** Exports the labeled customer matrix to `data/processed/segmented_customers.csv`.

### 6. `src/cluster_visualization.py`
* **Purpose:** Visualizes customer segmentations.
* **Key Functions:**
  * `plot_2d_clusters(df: pd.DataFrame, output_dir: str)`: Plots Annual Income vs. Spending Score in a 2D scatter plot using a custom palette. Calculates unscaled coordinates of group centroids and overlays them as large black `X` marks. Saved as `images/customer_clusters_2d.png`.
  * `plot_3d_interactive_clusters(df: pd.DataFrame, reports_dir: str)`: Uses Plotly Express to plot Age vs. Annual Income vs. Spending Score. Color-codes points by segment labels. Saved as `reports/customer_clusters_3d.html`.

---

## 🏆 Customer Cohorts & Insights
Based on clustering ($K=5$), the customers are grouped into 5 strategic cohorts:
1. **Cluster 0: Standard Group** (81 customers): Average income ($40\text{k}$-$70\text{k}$), average spending score ($40$-$60$). Target with standard campaigns.
2. **Cluster 1: Champions** (39 customers): High income ($>70\text{k}$), high spending score ($>60$). Target with premium loyalty rewards.
3. **Cluster 2: Low-Value Cohort** (22 customers): Low income ($<40\text{k}$), low spending score ($<40$). Target with budget-saving discounts.
4. **Cluster 3: Careless Spenders** (35 customers): Low income ($<40\text{k}$), high spending score ($>60$). Target with high-frequency impulse deals.
5. **Cluster 4: Conserving Spenders** (23 customers): High income ($>70\text{k}$), low spending score ($<40$). Target with catalog reminders highlighting product quality.

---

## 🤖 Instructions for AI Prompts
If you want to feed this project to another AI, copy and paste this prompt:

```text
You are an expert Machine Learning Engineer. I am providing you with the project details of my "Customer Segmentation" project (Task 6).

Here is the setup:
- Raw dataset is located in 'data/raw/Mall_Customers.csv'.
- Preprocessed dataset is saved by 'src/data_cleaning.py' to 'data/processed/cleaned_customers.csv'.
- Features of interest are standardized using 'src/scaling.py'.
- Optimal cluster count was determined as K=5 using 'src/elbow_method.py'.
- K-Means is trained by 'src/kmeans_clustering.py', saving the model binary to 'models/kmeans_model.joblib' and outputting 'data/processed/segmented_customers.csv'.
- Cluster plots are generated by 'src/cluster_visualization.py'.

Please read this configuration and assist me with:
1. Writing scripts or extending the model (e.g. comparing K-Means with DBSCAN or Hierarchical clustering).
2. Triage/debugging of machine learning pipeline issues.
3. Refactoring visualization functions.
```
