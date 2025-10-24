import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # for heatmap

# 1. Load CSV file
# Replace with your own file path
df = pd.read_csv("column_row/sample_housing_data.csv")

# 2. Display basic info
print("First 5 rows of data:")
print(df.head())
print("\nSummary statistics:")
print(df.describe())
print("\nColumn names:")
print(df.columns)

# 3. Calculate average of a selected column (example: 'Price')
if "Price" in df.columns:
    avg_price = df["Price"].mean()
    print(f"\nAverage Price: {avg_price:.2f}")

# -----------------------------
# 4. Data Visualization
# -----------------------------

# Bar Chart (Category vs. Average Price)
if "Category" in df.columns and "Price" in df.columns:
    avg_price_by_cat = df.groupby("Category")["Price"].mean()
    avg_price_by_cat.plot(kind="bar", figsize=(8,5), color="skyblue")
    plt.title("Average Price by Category")
    plt.xlabel("Category")
    plt.ylabel("Average Price")
    plt.show()

# Scatter Plot (e.g., Area vs. Price)
if "Area" in df.columns and "Price" in df.columns:
    plt.figure(figsize=(7,5))
    plt.scatter(df["Area"], df["Price"], alpha=0.6, c="green")
    plt.title("Scatter Plot: Area vs Price")
    plt.xlabel("Area (sq ft)")
    plt.ylabel("Price")
    plt.show()

# Heatmap (Correlation between numerical columns)
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
