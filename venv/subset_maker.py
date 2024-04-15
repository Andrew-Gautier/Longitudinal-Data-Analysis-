import pandas as pd

# Load your dataset from the large CSV file
file_path = 'venv/URDC.csv'
df = pd.read_csv(file_path)

# List of columns to keep
selected_columns = ['NACCID', 'NACCVNUM', 'EDUC', 'NACCAGEB', 'NACCAGE', 'DECIN', 'DECCLIN', 'COGMEM', 'COGORI', 'COGJUDG',
                    'COGLANG', 'COGVIS', 'COGATTN', 'COGFLUC', 'COGFLAGO', 'COGOTHR', 'NACCCOGF', 'COGMODE', 'NACCTMCI',
                    'NACCALZD', 'NACCALZP', 'PROBAD', 'PROBADIF', 'POSSAD', 'POSSADIF', 'NACCNORM', 'NACCIDEM', 'NACCMCII']

# Create a new DataFrame with only the selected columns
df_subset = df[selected_columns]

unknown_values = {
    'EDUC': [99],
    'NACCAGEB': [],
    'NACCAGE': [],
    'DECIN': [8, 9],
    'DECCLIN': [],
    'COGMEM': [9],
    'COGORI': [9],
    'COGJUDG': [9],
    'COGLANG': [9],
    'COGVIS': [9],
    'COGATTN': [9],
    'COGFLUC': [9, -4],
    'COGFLAGO': [888, 999, -4],
    'COGOTHR': [9],
    'NACCCOGF': [99],
    'COGMODE': [99],
    'NACCTMCI': [8],
    'NACCALZD': [],
    'NACCALZP': [7, 8],
    'PROBAD': [-4],
    'PROBADIF': [-4],
    'POSSAD': [-4],
    'POSSADIF': [-4]
}

# Display unique values counts before filtering
print("Unique values counts before filtering:")
for column in df_subset.columns:
    print(df_subset[column].value_counts(dropna=False))

# Remove rows with unknown or not applicable values
for column, values in unknown_values.items():
    df_subset = df_subset[~df_subset[column].isin(values)]

# Display unique values counts after filtering
print("\nUnique values counts after filtering:")
for column in df_subset.columns:
    print(df_subset[column].value_counts(dropna=False))
# Save the subset DataFrame to a new CSV file
output_file_path = 'var_group2.csv'
df_subset.to_csv(output_file_path, index=False)

# Display the first few rows of the new DataFrame
print("\nSubset DataFrame:")
print(df_subset.head())
