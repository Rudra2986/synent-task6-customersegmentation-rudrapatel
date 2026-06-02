# Project Plan: Customer Segmentation
> **Synent Technologies - Data Science Internship (Summer 2026)**
> **Task 6: Intermediate Level**

---

## 🎯 Objectives
The main objective of this task is to perform customer segmentation on the Mall Customer Dataset.

Key targets:
1. Conduct data exploration to understand demographic patterns (Age, Gender, Income).
2. Clean data and apply normalization/scaling to features.
3. Identify optimal clusters using the Elbow Method and Silhouette Analysis.
4. Build a K-Means clustering model.
5. Create visual representations of the clusters in 2D and 3D.
6. Provide business insights/profiles for each customer group.

---

## 🔄 Expected Workflow
The project will follow a structured data science pipeline:
```
[1. Project Setup] ➔ [2. Data Cleaning] ➔ [3. Feature Selection & Scaling]
                                                       │
[6. Showcase & Submission] 🡨 [5. Interpretation] 🡨 [4. Elbow & K-Means Model]
```

1. **Project Setup (Current State):** Creating task structures, python environments, and planning documentation.
2. **Data Cleaning:** Handle null entries, drop duplicates, encode categorical fields (like Gender) if required.
3. **Feature Selection & Scaling:** Select attributes like Annual Income and Spending Score. Normalize feature ranges using scaling algorithms to avoid scale imbalance issues.
4. **Elbow Method & K-Means Modeling:** Calculate WCSS values for several clusters and plot the curve. Fit the K-Means algorithm using the optimal cluster count.
5. **Cluster Visualization & Interpretation:** Plot scatter plots and summarize clusters (e.g., "High Income, High Spending", "Low Income, Low Spending").
6. **Showcase & Submission:** Finalize documentation, capture results, and record video walkthrough.

---

## 📦 Deliverables
The final submission must include:
1. **GitHub Repository:** Publicly accessible, following naming format: `synent-task6-customersegmentation-rudrapatel`.
2. **Data Folders:** Structured as `data/raw/` and `data/processed/` (cleaned customer data with cluster labels).
3. **Jupyter Notebooks:** Complete execution workflow documenting model choices.
4. **Python Scripts:** Clean code files in `src/` directory.
5. **Visualizations:** High-resolution charts under the `images/` directory.
6. **Video Demonstration:** A 1 to 3-minute video walk-through demonstrating execution, code architecture, and cluster findings.

---

## 🖥️ GitHub Submission Requirements
* **Repository Name:** `synent-task6-customersegmentation-rudrapatel`
* **Privacy:** Public repositories only.
* **Documentation:** The `README.md` must be thoroughly written, capturing problem statements, datasets, results, and environment installation instructions.
* **Version Control:** Regular, logical commits describing the stages of development.

---

## 🎥 Video Demonstration Requirements
* **Duration:** 1 to 3 minutes.
* **Voiceover:** Preferred (explain clear audio, screen sharing, and code walk-through).
* **Key Components to Cover:**
  - Introduction of yourself (your name).
  - High-level overview of the problem statement and dataset.
  - Explain the purpose of Scaling/Standardization.
  - Explain the Elbow Method curve and how you chose K.
  - Show the 2D/3D cluster visual plots.
  - Explain what each cluster represents in business terms.

---

## 📈 Expected Outputs
Upon project completion, the following output targets should be realized:
- **Cleaned Data with Cluster Labels:** Saved in `data/processed/mall_customers_segmented.csv`.
- **WCSS Elbow Curve:** Visual line plot saved in `images/elbow_method.png`.
- **2D Scatter Plot:** Cluster groupings saved in `images/customer_segments_2d.png`.
- **3D Interactive Plot:** Segment groupings saved in HTML format in `reports/` or `images/customer_segments_3d.html`.
- **Marketing Strategy Profiles:** A markdown or PDF report inside the `reports/` directory describing campaigns tailored to each customer tier.
