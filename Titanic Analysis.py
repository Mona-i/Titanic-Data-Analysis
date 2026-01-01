import pandas as pd
# load the csv file
df = pd.read_csv('train.csv')
print(df.head())

print(df.info())  # Data types and missing values
print(df.describe()) # stats like mean age

df['Age'].fillna(df['Age'].mean(), inplace=True)


print(df.duplicated().sum())  # should not be 0

survival_rate = df['Survived'].mean() * 100
print(f"overall survival rate: {survival_rate:.2f}%")

print(df.groupby('Sex')['Survived'].mean())
print(df.groupby('Pclass')['Survived'].mean())

print(df.corr(numeric_only=True)) #Focus on 'Survived' column

import seaborn as sns 
import matplotlib.pyplot as plt

sns.barplot(x='Sex', y='Survived', data=df)
plt.title('Survival Rate By Gender')
plt.show()

sns.histplot(df['Age'], bins=20)
plt.title('Age Distribution')
plt.show()

sns.boxplot(x='Pclass', y='Fare', data=df)
plt.title('fire by Passenger Class')
plt.show()

# 