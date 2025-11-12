# eda_benin.py
# Task 2: Data Cleaning & Exploratory Analysis (Benin)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
import os

# ensure plots directory exists
plots_dir = "../plots"
os.makedirs(plots_dir, exist_ok=True)

# 1️⃣ Load dataset
# Update the path if needed
df = pd.read_csv("../data/clean/benin_clean.csv")

# 2️⃣ Basic info & summary statistics
print("Dataset Info:\n")
print(df.info())

print("\nSummary Statistics:\n")
print(df.describe())

print("\nMedian Values:\n")
# only compute medians for numeric columns
print(df.median(numeric_only=True))

print("\nVariance:\n")
# only compute variance for numeric columns
print(df.var(numeric_only=True))

# 3️⃣ Check missing values
print("\nMissing Values:\n")
print(df.isna().sum())

# 4️⃣ Handle missing values (median imputation)
numeric_cols = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'Tamb', 'RH', 'WS', 
                'WSgust', 'WSstdev', 'WD', 'WDstdev', 'BP', 'Cleaning', 
                'Precipitation', 'TModA', 'TModB']

for col in numeric_cols:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].median())

print("\nMissing Values After Imputation:\n")
print(df.isna().sum())

# 5️⃣ Outlier detection & handling using Z-score (GHI, DNI, DHI)
outlier_cols = ['GHI', 'DNI', 'DHI']
z_scores = df[outlier_cols].apply(zscore)

# Identify outliers
outliers = (z_scores.abs() > 3)
print("\nNumber of Outliers:\n")
print(outliers.sum())

# Replace outliers with median
for col in outlier_cols:
    df[col] = df[col].mask(outliers[col], df[col].median())

# 6️⃣ Visualizations
# Boxplot for GHI, DNI, DHI
plt.figure(figsize=(12,6))
sns.boxplot(data=df[outlier_cols])
plt.title("Boxplot of GHI, DNI, DHI")
plt.ylabel("Value")
plt.savefig(os.path.join(plots_dir, "boxplot_GHI_DNI_DHI.png"))
plt.show()

# Histogram for GHI
plt.figure(figsize=(10,5))
sns.histplot(df['GHI'], bins=50, kde=True, color='orange')
plt.title("Histogram of GHI")
plt.xlabel("GHI")
plt.ylabel("Frequency")
plt.savefig(os.path.join(plots_dir, "histogram_GHI.png"))
plt.show()

# Correlation heatmap (use numeric columns only)
plt.figure(figsize=(12,10))
numeric_df = df.select_dtypes(include='number')
if numeric_df.shape[1] == 0:
    print("No numeric columns available for correlation heatmap.")
else:
    sns.heatmap(numeric_df.corr(), annot=True, fmt=".2f", cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.savefig(os.path.join(plots_dir, "correlation_heatmap.png"))
    plt.show()

# 7️⃣ Export the final cleaned dataset
df.to_csv("../data/clean/benin_clean_final.csv", index=False)
print("Final cleaned dataset saved as 'benin_clean_final.csv'.")
