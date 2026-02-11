import pandas as pd
# Extract function to read CSV file
def extract(file_path):
     print(f"Extracting data from {file_path}...")
     df = pd.read_csv(file_path)
     print("Data extracted successfully.")
     return df
   