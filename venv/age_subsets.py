import pandas as pd
from datetime import datetime
import numpy as np



def agebinner(csv_file, age_increment, desired_range):
    # Read CSV file into a DataFrame
    df = pd.read_csv(csv_file, low_memory=False)
    
    # Calculate age for each patient
    current_year = datetime.now().year
    current_month = datetime.now().month
    df['Age'] = current_year - df['BIRTHYR'] - (current_month < df['BIRTHMO']).astype(int)
    
    # Round down the ages to ensure they are whole numbers
    df['Age'] = np.floor(df['Age'])
    
    # Bin ages according to the user-defined increment
    bins = range(0, int(df['Age'].max()) + age_increment, age_increment)
    labels = [f"{start}-{end-1}" for start, end in zip(bins, bins[1:])]
    df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
    
    # Filter DataFrame for the desired age range
    result_df = df[df['Age_Group'].isin(desired_range)]
    
    # Extract patient IDs from the result DataFrame
    patient_ids = result_df['NACCID'].tolist()
    
    return patient_ids


# Example usage:
csv_file_path = 'venv\\URDC.csv'  # Replace with your CSV file path
age_increment = 5
desired_age_range = ['60-64', '65-69', '70-74', '75-79', '80-84', '85-89'] 

result_patient_ids = agebinner(csv_file_path, age_increment, desired_age_range)

print("Patient IDs in the desired age range:", len(result_patient_ids))

# Convert the list of IDs to a set to remove any duplicates
unique_patient_ids = set(result_patient_ids)

# Check if all IDs are unique
if len(result_patient_ids) == len(unique_patient_ids):
    print("All patient IDs are unique.")
else:
    print("Some patient IDs are not unique.")