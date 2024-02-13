import pandas as pd

# Load your dataset from the large CSV file
file_path = 'venv/URDC.csv'
df = pd.read_csv(file_path)

# List of columns to keep (replace these with the actual column names you want to keep)
selected_columns = ['NACCID','NACCVNUM','EDUC', 'NACCAGEB', 'NACCAGE','DECIN','DECCLIN','COGMEM','COGORI','COGJUDG',
                    'COGLANG','COGVIS','COGATTN','COGFLUC','COGFLAGO', 'COGOTHR', 'NACCCOGF', 'COGMODE', 'NACCTMCI', 'NACCALZD', 'NACCALZP',
                    'PROBAD', 'PROBADIF','POSSAD','POSSADIF','NACCNORM','NACCIDEM','NACCMCII']

# Create a new DataFrame with only the selected columns
df_subset = df[selected_columns]

# Save the subset DataFrame to a new CSV file
output_file_path = 'var_group1.csv'
df_subset.to_csv(output_file_path, index=False)

# Display the first few rows of the new DataFrame
print("Subset DataFrame:")
print(df_subset.head())
