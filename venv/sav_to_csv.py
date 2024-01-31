import pandas as pd
import pyreadstat  # This library helps in reading SPSS .sav files


input_sav_file = 'C:\\Users\\Andrew\\Downloads\\hickspatrick01122024.sav'
df, metadata = pyreadstat.read_sav(input_sav_file)

output_csv_file = 'venv\\URDC.csv'

# Save the data to CSV
df.to_csv(output_csv_file, index=False)

print(f"Conversion complete. CSV file saved at: {output_csv_file}")