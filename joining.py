import os
import pandas as pd

directory = r'C:\Users\ACER\geemap101\generated individual Sentinel5p data'

dataframes = []

for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)
        df = pd.read_csv(file_path)
        dataframes.append(df)

merged_df = pd.concat(dataframes, ignore_index=True)

output_file = os.path.join(directory, 'merged_file.csv')
merged_df.to_csv(output_file, index=False)

print(f'Merged CSV saved to {output_file}')
