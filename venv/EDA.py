import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset from the CSV file
file_path = 'var_group1.csv'
df = pd.read_csv(file_path)

# 1. Descriptive Statistics
# Display summary statistics
print("Summary Statistics:")
print(df.describe())

# Display the distribution of numeric variables
print("\nNumeric Distribution:")
print(df.describe(include=np.number))

# Display the distribution of categorical variables
categorical_columns = df.select_dtypes(include='object').columns
if not categorical_columns.empty:
    print("\nCategorical Distribution:")
    print(df[categorical_columns].describe())

# 2. Correlation Analysis and Heatmap
# Calculate correlation matrix
correlation_matrix = df.corr()

# Create a heatmap using seaborn
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, cmap='coolwarm', annot=True, fmt=".2f", linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

# # Additional Visualization: Pair Plot
# sns.pairplot(df, hue='EDUC', vars=['COGFLAGO'])
# plt.title('Pair Plot')
# plt.show()

# Additional Visualization: Distribution of a Numeric Variable: in this case, age
# sns.histplot(df['NACCAGE'], kde=True)
# plt.title('Distribution of Age')
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.show()

# # This is a subset of columns related to cognitive assessments
# selected_columns = [
#     'COGMEM', 'COGORI', 'COGJUDG', 'COGLANG', 'COGVIS', 'COGATTN', 'COGFLUC', 'COGFLAGO',
#     'NACCALZD', 'PROBAD', 'POSSAD', 'NACCCOGF', 'COGMODE', 'NACCTMCI', 'NACCALZP',
# ]
# subset_df = df[selected_columns]
# correlation_matrix = subset_df.corr()
# plt.figure(figsize=(12, 10))
# sns.heatmap(correlation_matrix, cmap='coolwarm', annot=True, fmt=".2f", linewidths=0.5)
# plt.title('Selective Correlation Heatmap (Cognitive Function and Alzheimer\'s Diagnosis)')
# plt.show()

# Scatterplot with regression line
plt.figure(figsize=(10, 6))
sns.regplot(x='EDUC', y='COGMEM', data=df)
plt.title('Scatterplot: Education vs Cognitive Memory')
plt.xlabel('Years of Education')
plt.ylabel('COGMEM')
plt.show()


plt.figure(figsize=(10, 6))
sns.boxplot(x='NACCALZD', y='EDUC', data=df)
plt.title('Boxplot: Alzheimer\'s Diagnosis vs Education')
plt.xlabel('Alzheimer\'s Diagnosis')
plt.ylabel('Years of Education')
plt.show()




# I am working on doing some more advanced regression techniques here. The scatterplot with regression line seemed to be skewed because of some weird outliers 
# so I am going to see if I can mitigate that. 
from sklearn.linear_model import HuberRegressor

#TEST A
# Fit a robust regression model
huber = HuberRegressor()
huber.fit(df[['EDUC']], df['COGMEM'])
# Plot the scatterplot with the robust regression line
plt.figure(figsize=(10, 6))
sns.regplot(x='EDUC', y='COGMEM', data=df, scatter_kws={'s': 10})
plt.plot(df['EDUC'], huber.predict(df[['EDUC']]), color='red', linewidth=2)
plt.title('Scatterplot with Robust Regression: Education vs Cognitive Memory')
plt.xlabel('Years of Education')
plt.ylabel('COGMEM')
plt.show()

#TEST B

# Apply logarithmic transformation to 'EDUC' and 'COGMEM'
df['EDUC_log'] = np.log1p(df['EDUC'])
df['COGMEM_log'] = np.log1p(df['COGMEM'])

# Plot the scatterplot with transformed variables
plt.figure(figsize=(10, 6))
sns.regplot(x='EDUC_log', y='COGMEM_log', data=df, scatter_kws={'s': 10})
plt.title('Scatterplot with Log-transformed Variables: Education vs Cognitive Memory')
plt.xlabel('Log(Years of Education)')
plt.ylabel('Log(COGMEM)')
plt.show()