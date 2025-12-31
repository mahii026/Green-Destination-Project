# Employee Attrition Analysis at Green Destinations
# Author: Mahii Patel

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create output folder
os.makedirs("outputs", exist_ok=True)

# Load dataset
df = pd.read_csv("greendestination.csv")

# Display data info
print(df.head())
print(df.info())

# Attrition rate
attrition_rate = df['Attrition'].value_counts(normalize=True) * 100
print("Attrition Rate (%):")
print(attrition_rate)

# Attrition Count
plt.figure()
sns.countplot(x='Attrition', data=df)
plt.title("Employee Attrition Count")
plt.savefig("outputs/attrition_count.png")
plt.close()

# Attrition vs Age
plt.figure()
sns.boxplot(x='Attrition', y='Age', data=df)
plt.title("Attrition vs Age")
plt.savefig("outputs/attrition_vs_age.png")
plt.close()

# Attrition vs Years at Company
plt.figure()
sns.boxplot(x='Attrition', y='YearsAtCompany', data=df)
plt.title("Attrition vs Years at Company")
plt.savefig("outputs/attrition_vs_years.png")
plt.close()

# Attrition vs Monthly Income
plt.figure()
sns.boxplot(x='Attrition', y='MonthlyIncome', data=df)
plt.title("Attrition vs Monthly Income")
plt.savefig("outputs/attrition_vs_income.png")
plt.close()

print("Analysis completed successfully.")
