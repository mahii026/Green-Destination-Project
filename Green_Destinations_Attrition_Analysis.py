
# Employee Attrition Analysis at Green Destinations
# Author: Mahii Patel

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("greendestination.csv")

# Display basic information
print("First 5 rows of the dataset:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# Calculate Attrition Rate
print("\nAttrition Count:")
print(df['Attrition'].value_counts())

attrition_rate = df['Attrition'].value_counts(normalize=True) * 100
print("\nAttrition Rate (%):")
print(attrition_rate)

# Attrition vs Age
plt.figure()
sns.boxplot(x='Attrition', y='Age', data=df)
plt.title("Attrition vs Age")
plt.show()

# Attrition vs Years at Company
plt.figure()
sns.boxplot(x='Attrition', y='YearsAtCompany', data=df)
plt.title("Attrition vs Years at Company")
plt.show()

# Attrition vs Monthly Income
plt.figure()
sns.boxplot(x='Attrition', y='MonthlyIncome', data=df)
plt.title("Attrition vs Monthly Income")
plt.show()

print("\nAnalysis Completed Successfully.")
