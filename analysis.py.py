import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("clean_superstore_dataset.csv")

# Convert date
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Basic checks
print(df.head())
print(df.columns)
print(df.info())

# Missing values
print(df.isnull().sum())

# Basic Analysis
print(df["Sales"].sum())
print(df["Profit"].sum())

# Region Analysis
grouped = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print(grouped)

# Category Analysis
print(df.groupby("Category")["Sales"].sum().sort_values(ascending=False))
print(df.groupby("Category")["Profit"].sum().sort_values(ascending=False))

# Product Analysis
print(df.groupby("Product_Name")["Sales"].sum().sort_values(ascending=False).head(10))

# Loss making products (based on profit)
print(df.groupby("Product_Name")["Profit"].sum().sort_values().head(10))

# Time Analysis
print(df.groupby(df["Order_Date"].dt.month)["Sales"].sum())
print(df.groupby(df["Order_Date"].dt.year)["Sales"].sum())

# Graphs

# 1. Sales by Region
df.groupby("Region")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Region")
plt.show()

# 2. Sales by Category
df.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Category")
plt.show()

# 3. Profit by Category
df.groupby("Category")["Profit"].sum().plot(kind="bar")
plt.title("Profit by Category")
plt.show()

# 4. Top 10 Products
df.groupby("Product_Name")["Sales"].sum().sort_values(ascending=False).head(10).plot(kind="bar")
plt.title("Top 10 Products")
plt.show()

# 5. Loss Making Products
df.groupby("Product_Name")["Profit"].sum().sort_values().head(10).plot(kind="bar")
plt.title("Loss Making Products")
plt.show()